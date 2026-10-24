# NOTES: Interpretation Act 2005 (Ireland), Act No. 23 of 2005

Row `legalese-sonnet-5.5`: one Sonnet 5.5 agent working alone from the brief in `BRIEF.md`, 2026-10-21.
Status: `draft`.
No domain expert has read this against the statute.

Sections 1 and 2 were written BEFORE any L4, so the expected answers in section 2 are the reading of the text and not a copy of what the code printed.
Section 2 is unchanged since then.
Where a later section disagrees with an earlier one, the later section says so out loud (see 2.3).

## 0. Reading guide

- The one thing most readers want: section 6 (the answers to the worked cases) and section 5 (the forks that decide them).
- The headline: **the Act has no rule for most of what the brief asks.**
  It counts days from a day (s 18(h)) and it fixes commencement (ss 15 to 17); it says what a "month", a "year" and a "week" are (Schedule Part 1).
  It has no corresponding-date rule, no rule for a period counted "after" an event, no rule that moves a last day off a day of rest or a holiday, and no moment of day for an Act that says nothing about its commencement.
  Where the text is silent the module REFUSES with a named reason; it never returns a plausible default.
- The alternative answers that other systems give (clamping to the end of a short month, rolling over, moving off a rest day) are in `ie-month-year-readings.l4`, which the Act's own module never calls, so that section 5 can show by running them what each would answer.
  They are NOT the Act's answers.

## 1. Source, target and caveats

- Source: `No.-23-of-2005.txt`, a plain-text rendering made by a converter script from the English print view of the Act as enacted on the electronic Irish Statute Book (sha256 `0108a07dd3db98b0058eacee0baabc34ce41823a52c57d2b52ae94b1bb7893d4`, checked).
  It is NOT the official text, it carries no mark-up, and nothing here is "verified against the official text".
  `srcrefs.py check --strict` compares quotations in the modules with that file, not with any official text.
- The file opens with an unofficial-text notice, a source line, a statement that the Statute Book's legislation directory lists no amendment, repeal or substitution of any section of the Act, and the Oireachtas copyright notice.
  That statement is why the enacted text is treated as the current text (fork F37).
  It is a statement in the file, not something this run re-checked.
- The copyright notice is copied mechanically into the header of every module that quotes the text, and into `SOURCE-LICENSE.md`.
- The file puts each section's marginal note in front of the section number ("Commencement. 16.—(1) ...").
  By s 18(g) a marginal note is not part of the enactment, so the notes are headings and carry no rule.
- The file's front matter, after the arrangement of sections, prints a table headed "Acts Referred to".
  It sits before the Act's own text (which begins at "INTERPRETATION ACT 2005", line 77) and belongs to no section.
  The Schedule's own Part 2 (defined words) is at the end of the file.
- Quotations in the modules are `-- src:N | text` lines produced mechanically by `srcrefs.py quote` from the raw file.
  Each quote run was generated from the line numbers of the `@ref` that follows it, so a run is exactly what its `@ref` cites.
  `_work/` (the generator) was deleted at the end; the standing proof is `srcrefs.py check --strict`, which `check.sh` runs when `SRC_RAW` is set.
- Target compiler: **`unstable`**.
  The brief requires `@lang en`, `REFUSE` and `YMD`, which `main` rejects (`writing-l4-rules/references/dialects.md`), so the encoding cannot be read by `main`, and `check.sh` runs with `L4_TARGET=unstable` as its default, which skips the comparison with a main build.
- `L4_BIN` is `/Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-9afd0288/bin/l4`, sha256 `2d912dd2a61ba36b3fb8c1e02dcbd445ba1143c3b8ecb931462c01050cd607d7` (checked against the brief); `l4 --version` prints `dev`.
  `JL4_LIBRARY_PATH` was unset throughout.
- `@lang en` draws a Hint from the linter on every module ("A module that declares nothing is English; this line can go.").
  The brief requires the line, so the Hint is known and left in; `check.sh` counts errors and assertion lines, and a Hint is neither.
- Method.
  Expected values were written from the text before the code (section 2) and never edited to match a result.
  Each test mechanism was shown to catch a wrong value by a positive control (a wrong `EQUALS`, a wrong `BECAUSE` text, a wrong enum constructor, `NOT` of a true thing and an unexpected refusal each fail to be satisfied); `tests-red-control.l4` keeps eight such wrong expectations permanently, so the gate is seen to catch them on every run.

## 2. Expected answers, decided from the text before any code

Counting follows s 18(h): "Where a period of time is expressed to begin on or be reckoned from a particular day, that day shall be deemed to be included in the period and, where a period of time is expressed to end on or be reckoned to a particular day, that day shall be deemed to be included in the period".
The Schedule (Part 1) defines "month" as "a calendar month", "year, when used without qualification" as "a period of 12 months beginning on the 1st day of January in any year", "week" as "the period between midnight on any Saturday and midnight on the following Saturday", and "midnight" as "in relation to a particular day, the point of time at which the day ends".
The Act has no corresponding-date rule, no rule for a period "after" an event, and no rule moving a last day off a day of rest or a holiday.

### 2.1 Periods

| period | counted from | expected on the text | why |
| --- | --- | --- | --- |
| thirty days | 2026-01-01 | last day **2026-01-30** | s 18(h): 2026-01-01 is day 1, so day 30 is 2026-01-30. |
| three years | 2025-07-16 | **no answer (refuse)** | Schedule Pt 1 "year" is a period of 12 months beginning 1 January; 2025-07-16 is not 1 January; the text has no rule for a period of years that begins elsewhere. |
| five years | 2025-01-15 | **no answer (refuse)** | as above |
| five years | 2025-09-01 | **no answer (refuse)** | as above: 1 September is the first day of a month but not of a year |
| two years | 2024-02-28 | **no answer (refuse)** | as above |
| one year | 2024-02-29 | **no answer (refuse)** | as above; the text has no rule for 29 February |
| one month | 2025-01-31 | **no answer (refuse)** | Schedule Pt 1 "month" is a calendar month; 2025-01-31 is not the first of a month; the text has no rule for a month that lacks the start day's number |

Every case in this table except the first is a prediction that the module refuses.
A test that makes one of them answer is a finding about the reading, not a thing to bless.

### 2.2 Commencement

| case | expected on the text | why |
| --- | --- | --- |
| an Act passed (Bill signed by the President) on 2026-03-10, nothing said about commencement | comes into operation **on 2026-03-10**; the text names **no moment** within that day | s 15(1) (passing is the day of signature; "published" is not a date the Act uses), s 16(1) ("on the date of its passing", with no "at the end of the day before") |
| an Act expressed to come into operation on a day to be fixed later; the day is fixed as 2026-06-01 | comes into operation **at the end of 2026-05-31** (the midnight ending that day), so the whole of 2026-06-01 is in operation | s 16(2); Schedule Pt 1 "midnight" |
| a statutory instrument made on 2026-03-10, nothing said about commencement | comes into operation **at the end of 2026-03-09**, so the whole of 2026-03-10 is in operation | s 16(3) (the one people get backwards: it is the day before the day of making) |

The step from "at the end of D-1" to "the whole of D is in operation" assumes that days tile the timeline with no gap, so that the end of one day and the start of the next are the same point.
The Act does not say "start of D"; it says "end of the day before".
`ie-interpretation-time.l4` therefore stores the moment as `the end of D-1` and derives "in operation throughout D" from it under that stated assumption.

### 2.3 One change made after section 2 was written

Section 2 was not changed.
One assertion written AFTER it was changed, and the change is disclosed here because the brief says a failing assertion is a finding and an expected value is never edited to match the code.

`the first day on which the enactment is in operation throughout`, asked of an Act passed on 2026-03-10 that says nothing about commencement, first returned 2026-03-11 (the day after the passing) and its test expected 2026-03-11.
Re-reading the module against the text showed that the neighbouring function `the enactment ... is in operation throughout` REFUSES for 2026-03-10 itself, because s 16(1) names no moment within that day, and so 2026-03-11 was an upper bound and not an answer: if the Act comes into operation at the start of 2026-03-10 then 2026-03-10 is the first such day, and the text does not exclude that.
The function and its test now refuse, with the same message as its neighbour.
This was found by reading, not by a failing assertion, and it moves the module toward the text, away from what the code had computed.
Nothing in the pre-registered table in 2.2 depends on it: the table's answer for that case was "on 2026-03-10; the text names no moment", which is what the module says.

## 3. Scope: what is encoded and what is not

### 3.1 Encoded, by module

| module | what it answers |
| --- | --- |
| `ie-interpretation-time.l4` (imports only `prelude` and `daydate`) | s 18(h): the last day of a period of N days, weeks, calendar months, years, working days or week-days; whether a day falls within a period; the number of days in a period. Days of rest, recess and holiday as an INPUT. Ss 15 and 16 with the Schedule's "midnight" and "commencement": the day, and the moment within the day, from which an Act, a Saorstat Eireann statute or a statutory instrument is in operation. The Schedule's time words: week, week-day, month, year, financial year, local financial year, working day, public holiday. This Act's own commencement (s 1(2)). |
| `ie-general.l4` | s 2(1) "Act", "enactment", "statutory instrument", "repeal"; s 4 (contrary intention); ss 5 to 9, 11 to 14(1). |
| `ie-operation-and-construction.l4` | s 17; s 18(b), (d), (e), (f), (g); s 20(1); s 21(2); the Schedule's "full age". |
| `ie-powers-and-service.l4` | s 22(3); s 25 (service by post, deemed time of service). |
| `ie-repeal.l4` | s 2(2); s 3(1) and (2); s 26; s 27. |
| `ie-month-year-readings.l4` | NOT the Act. The alternative readings of section 5 (B, B-inclusive, C, D, R), labelled and never called by the Act's modules. |

The brief's six required topics, each with where the answer is or why there is none:

1. When an enactment comes into force or binds, where it does not say: **answered for the day, and for the moment under s 16(2) to (4); no moment under s 16(1).**
2. How a period of days, weeks, months or years is counted: **days from a day: answered; weeks, months and years that begin where the Schedule's unit begins: answered; everything else, and every period "after" an event: the Act has no rule, so REFUSE.**
3. What happens when the last day falls on a rest day, recess or holiday: **the Act has no rule; REFUSE (the roll-forward is reading R, not the Act's).**
4. Deemed service: **s 25 only; the time of delivery is an input.**
5. What a repeal does: **ss 2(2), 3, 26, 27, encoded; the judgments the Act leaves to the reader are inputs.**
6. The meanings of "day", "week", "month", "year" and other time words: **the Schedule defines week, week-day, month, year, financial year, local financial year, midnight, commencement, working day and public holiday; it does not define "day" (the Act is silent; fork F9).**

### 3.2 Not encoded, and why

- **A calendar of holidays.** "Public holiday" is defined by reference to the Organisation of Working Time Act 1997 (Schedule Part 2), which is not in this text.
  Rest days and public holidays are therefore a caller-supplied function from a date to a boolean in every function that needs one.
- **Clock times.** Section 18(i) sends a time expressed by reference to an hour to the Standard Time (Amendment) Act 1971, which is not in this text.
  `the clock time of a specified hour in an enactment` is a named refusal.
- **How a person attains an age.** The Act has no anniversary rule; the day of attaining 18 and the day of marrying are inputs.
- **Judgments the Act leaves to the reader** ("obscure or ambiguous", "absurd", "plain intention", "materially affect", "changed in intent or become unclear or absurd", "consistently with the new enactment", "same idea", "of a continuing nature") are inputs; the encoding does not decide them.
- **The inert provisions** listed in section 4 (ss 1(1), 10, 14(2), 14(3), 15(2), 18(a), 18(c), 18(j), 19, 20(2), 22(1), 22(2), 23, 24, the Schedule's lexical definitions, the long title).
- **The Irish-language text.** Not deposited; which text prevails is a fork (F34), not decided.
- **No other Act, and no case law.**
  Every answer is from the text of this Act; the brief forbids importing an answer from another jurisdiction's law or from general knowledge of how Irish law is applied.

### 3.3 Reading a result

Most functions answer "does this section give X here?".
`FALSE` means the section does not give X; it does not mean the section forbids X.
A refusal means the text, read as it stands, does not answer; the message says what is missing.

## 4. Coverage table

One row per section and subsection, per Schedule part and per Schedule entry, plus rows for the front matter and for the six items of the brief on which the Act has no rule.
Dispositions: `encoded`; `inert` (with the reason); `repealed or blank` (none: the text shows no repealed, blank or reserved provision, and the directory statement in the file lists no amendment); `not applicable` (front matter, formula, tables that are not provisions); `silent` (a row for an item of the brief on which the Act has no provision; it is the brief's "the Act is silent on this", and is counted apart from the dispositions of enacted text).

**Counts: 114 rows: encoded 68, inert 38, repealed or blank 0, not applicable 4, silent 4.**
The rows are finer than one per section, because a section with several subsections or paragraphs of different dispositions has a row for each; every section 1 to 27 has at least one row.
The first six rows are front matter and headings, then come the sections and the Schedule, then the "Acts Referred to" table, and the last four rows are the silences.

| # | Provision | Disposition | Where, or why |
| --- | --- | --- | --- |
| 1 | Front matter: unofficial-text notice, source line, copyright notice, 'Number 23 of 2005', title | not applicable | The first four lines of the file are an unofficial-text notice, a source line, a statement about the Statute Book directory and the Oireachtas copyright notice; 'Number 23 of 2005' and the title follow. They are the file's own front matter and state no rule. The copyright notice is copied mechanically into the header of every module that quotes the text and into SOURCE-LICENSE.md. |
| 2 | ARRANGEMENT OF SECTIONS (table of section numbers and marginal notes) | not applicable | A table of contents: it repeats the marginal notes and Part headings, which by s 18(g) are not part of the enactment. It states no rule and nothing is executed from it. |
| 3 | Long title ('AN ACT RESPECTING THE INTERPRETATION AND APPLICATION OF ACTS AND OF STATUTORY INSTRUMENTS ... AND PROVIDING FOR THE REPEAL OF CERTAIN ENACTMENTS') | inert | States the Act's purpose and subject-matter. It confers no right and imposes no duty, and no function's result would change if it were deleted. Its only possible use is as an aid to construing the Act under ss 5 and 7, which is a judgment the encoding takes as an input (`what section 5 directs about`). |
| 4 | Date line '[17th October, 2005]' | encoded | Taken as the date of the passing of this Act: s 15(2) says the Clerk endorses the date of the passing immediately after the long title and that the date is part of the Act, and this line sits there. Used in `the facts about this Act` (ie-interpretation-time.l4) and tested in tests-commencement.l4 and tests-operation.l4. |
| 5 | Enacting formula 'BE IT ENACTED BY THE OIREACHTAS AS FOLLOWS' | not applicable | Words of enactment; they give the Act its force and state no rule that a function could apply. |
| 6 | Part headings, section headings, marginal notes | inert | By s 18(g) not part of the enactment; the file puts each marginal note in front of its section number (for example 'Commencement. 16.'). The encoding gives them no force. `the matter is taken to be part of the enactment` (ie-operation-and-construction.l4) encodes s 18(g) itself. |
| 7 | s 1(1) short title | inert | A citation name for the Act. Nothing is computed from it; s 14(1)(a) (citing an Act by its short title) is encoded separately in ie-general.l4. |
| 8 | s 1(2) commencement of this Act: '1 January 2006' | encoded | `the facts about this Act` (ie-interpretation-time.l4) with s 16(2): in operation at the end of 31 December 2005. Tested: tests-commencement.l4, tests-operation.l4 (s 21(2)), tests-repeal.l4 (s 3(1)). |
| 9 | s 2(1) 'Act' (an Act of the Oireachtas; a Saorstat Eireann statute that continued in force) | encoded | `is an Act` (ie-general.l4); `Kind of enactment` (ie-interpretation-time.l4). |
| 10 | s 2(1) 'enactment' | encoded | `is an enactment` (ie-general.l4). |
| 11 | s 2(1) 'repeal' (includes revoke, rescind, abrogate or cancel) | encoded | `the word is a repeal within the Act` (ie-general.l4); the list is open ('includes'), so a word outside it refuses. |
| 12 | s 2(1) 'statutory instrument' (and 'made') | encoded | `is a statutory instrument` (ie-general.l4). The extended meaning of 'made' (made, issued, granted or otherwise created) is why the SI date input is called 'the day of its passing or making' and is a supplied fact. |
| 13 | s 2(2) an enactment replaced, expired, lapsed or ceased to have effect is deemed repealed | encoded | `for the purposes of this Act the enactment is deemed to have been repealed` (ie-repeal.l4). |
| 14 | s 3(1)(a) to (d) the Acts repealed (Interpretation Acts 1889, 1923, 1937; Interpretation (Amendment) Act 1993) | encoded | `section 3(1) lists the Act`; `section 3(1) has repealed the Act by the end of` (ie-repeal.l4), composed with s 1(2) and s 16(2): repealed from the end of 31 December 2005. |
| 15 | s 3(2)(a) saving of a meaning assigned by a repealed Act | encoded | `the repeal does not affect the meaning assigned` (ie-repeal.l4); the two 'would be changed in intent or become unclear or absurd' limbs are inputs. |
| 16 | s 3(2)(b) saving of another matter provided for by a repealed Act | encoded | `the repeal does not affect the matter provided for` (ie-repeal.l4); excludes a matter to which (a) relates, on the text's own words. |
| 17 | s 4(1) contrary intention | encoded | `a provision of this Act applies to an enactment` (ie-general.l4). Elsewhere the modules assume that no contrary intention appears, and say so in their headers; `the definition or interpretation provision is read as applicable` (ie-operation-and-construction.l4) is the s 20(1) twin. |
| 18 | s 4(2) provisions relating to other Acts also apply to this Act | encoded | `a provision of this Act that relates to other Acts applies also to this Act` (ie-general.l4). |
| 19 | s 5(1) construing a provision of an Act that is obscure, ambiguous or absurd | encoded | `what section 5 directs about` (ie-general.l4); a penal or other sanction takes the provision out; whose intention (the Oireachtas, the parliament concerned) follows the kind of Act. |
| 20 | s 5(2) the same for a statutory instrument | encoded | Same function; the maker of the instrument. |
| 21 | s 6 construing provisions in changing circumstances | encoded | `a court may make allowance for the change in construing the provision` (ie-general.l4); 'since' is not settled for a change on the very day, so that case refuses. |
| 22 | s 7(1) matters accompanying the signed text, notwithstanding s 18(g) | encoded | `section 7(1) lets a court make use of the matter notwithstanding section 18(g)` (ie-general.l4). |
| 23 | s 7(2) presumption that a copy is a copy of the enrolled text | encoded | `it is presumed that the copy is a copy of the text to which section 7(1) relates` (ie-general.l4). |
| 24 | s 8 summary proceedings where provisions are read together as one | encoded | `section 8 lets the specified person bring summary proceedings for the offence` (ie-general.l4). |
| 25 | s 9(1) a reference to a Part, Chapter, section, Schedule or other division | encoded | `a reference to a division is read as a reference to a division of` (ie-general.l4): the enactment in which the reference occurs. |
| 26 | s 9(2) a reference to a subsection, paragraph, ... or other division | encoded | Same function: the provision in which the reference occurs. 'Other division, by whatever name called' is in both lists, so a division with another name refuses. |
| 27 | s 10 enactment always speaking | inert | States that an enactment continues to have effect and may be applied from time to time as occasion requires. No input varies the answer: a function for it would return the same value for every enactment and every day, and the effect of an enactment on a given day is already computed by the commencement and repeal functions. |
| 28 | s 11 examples | encoded | `the effect of an example under the heading` (ie-general.l4). The heading words 'Sampla' and 'Samplai' (the text has an accented i) are spelt in ASCII in the identifiers. |
| 29 | s 12 deviation from form | encoded | `section 12 saves the form used` (ie-general.l4); 'or' is read literally (fork F19). |
| 30 | s 13 judicial notice | encoded | `it is a public document that shall be judicially noticed` (ie-general.l4); an Act is covered, and the section says nothing about a statutory instrument, so that case refuses. |
| 31 | s 14(1)(a) to (c) citing an Act | encoded | `section 14(1) lets an Act be cited` (ie-general.l4); whether the Act was passed before the 1922 Act, whether there was more than one session, and whether citing by number and year is 'appropriate' are inputs. |
| 32 | s 14(2) a citation is read as a citation of the enactment as amended | inert | Applies to every citation whatever the date of the amendment ('before, on or after' the citing provision came into operation), so no condition varies; a function would return TRUE for every input. It is a rule about what a citation refers to, not about when or whether anything happens. |
| 33 | s 14(3) commas around a year in a citation may be omitted | inert | A typographic permission about punctuation in citations; nothing in it is computed from facts. |
| 34 | s 15(1) date of passing of an Act of the Oireachtas | encoded | `the date of the passing of an Act of the Oireachtas signed on` (ie-interpretation-time.l4): the day the Bill is signed by the President. Defined only for an Act of the Oireachtas, so a Saorstat Eireann statute that is silent on commencement refuses (fork F16). |
| 35 | s 15(2) Clerk of the Dail endorses the date; the date is part of the Act | inert | A duty on an officer, with a deeming that the endorsed date is part of the Act. The deeming is relied on (the date line is read as this Act's date of passing) but nothing about the duty can be computed. |
| 36 | s 16(1) every provision of an Act comes into operation on the date of its passing | encoded | `section 16(1) commencement`, `the commencement of an Act` (ie-interpretation-time.l4). A day, with no moment: asking for the moment refuses. |
| 37 | s 16(2) an Act expressed to come into operation on a particular day: at the end of the day before | encoded | `section 16(2) commencement` (ie-interpretation-time.l4); a day 'to be fixed' is a particular day once fixed, and refuses before. |
| 38 | s 16(3) every provision of an SI comes into operation at the end of the day before the day it is made | encoded | `section 16(3) commencement`, `the commencement of a statutory instrument` (ie-interpretation-time.l4). |
| 39 | s 16(4) an SI expressed to come into operation on a particular day | encoded | `section 16(4) commencement` (ie-interpretation-time.l4). |
| 40 | s 17(a) day to be fixed or ascertained: the instrument or act fixing it may be made after the passing | encoded | `the instrument, act or thing that fixes the day may be made or done on` (ie-operation-and-construction.l4). |
| 41 | s 17(b) a power necessary or expedient for full force on commencement may be exercised after the passing | encoded | `the power to make a statutory instrument or do an act or thing may be exercised on` (ie-operation-and-construction.l4). |
| 42 | s 18(a) singular and plural | inert | A canon: a word importing the singular is also read as importing the plural and the reverse. It turns on no fact the encoding could hold, and a function for it would take a word and return the same word. |
| 43 | s 18(b)(i) masculine includes feminine | encoded | `a word importing the` ... (ie-operation-and-construction.l4): TRUE for every enactment and date. |
| 44 | s 18(b)(ii) feminine includes masculine in an Act passed on or after 22 December 1993 and an SI made after that date | encoded | Same function; 'on or after' for an Act and 'after' for an SI are applied as written (fork F21). |
| 45 | s 18(c) 'person' includes a body corporate and an unincorporated body | inert | A widening of the word 'person' with no condition: a function would be TRUE for every kind of body named. Nothing to test but a constant. |
| 46 | s 18(d)(i), (ii) 'child' includes an adopted child | encoded | `a reference to a child of the person includes the adopted child` (ie-operation-and-construction.l4); the passing of the Adoption Act 1976 is an input because the text gives only its year. |
| 47 | s 18(e) distance measured in a straight line on a horizontal plane | encoded | `the distance between` ... (ie-operation-and-construction.l4), by the horizontal projection; the height is ignored. |
| 48 | s 18(f) a series described by its first and last includes both | encoded | `the number ... is a member of the series from` ..., `the number of members of the series from` ... (ie-operation-and-construction.l4). |
| 49 | s 18(g)(i), (ii) marginal notes, shoulder notes, headings and cross-lines | encoded | `the matter is taken to be part of the enactment`, `the matter may be construed or judicially noticed in construing the enactment` (ie-operation-and-construction.l4), subject to s 7. |
| 50 | s 18(h) periods of time | encoded | `the last day of a period of` ... (ie-interpretation-time.l4): days; weeks, calendar months and years only from the start of the unit; `falls within the period`; named refusals for the rest. See forks F1 to F8. |
| 51 | s 18(i) time by reference to an hour | encoded | `the clock time of a specified hour in an enactment` (ie-interpretation-time.l4) refuses: the Standard Time (Amendment) Act 1971 is not in this text. Encoded as a named refusal. |
| 52 | s 18(j) offences by corporations | inert | 'A reference to a person in relation to an offence includes a body corporate': a widening with no varying condition, the same shape as s 18(c). |
| 53 | s 19 a word in an SI has the meaning it has in the enabling enactment | inert | The two meanings are strings the encoding would copy from one place to another; no condition or computation. Whether the contrary intention (s 4(1)) displaces it is the input already modelled in `a provision of this Act applies to an enactment`. |
| 54 | s 20(1) interpretation provisions apply unless a contrary intention appears | encoded | `the definition or interpretation provision is read as applicable` (ie-operation-and-construction.l4). |
| 55 | s 20(2) other parts of speech and grammatical forms | inert | A canon about grammatical forms of a defined word; nothing to compute from facts. |
| 56 | s 21(1) words in Part 1 of the Schedule have the meanings assigned | encoded | Encoded for the time words (see the Schedule rows below); the remaining Part 1 entries are lexical and are inert, row by row. |
| 57 | s 21(2) words in Part 2 of the Schedule apply to an enactment that comes into operation after this Act commences | encoded | `the enactment comes into operation after the commencement of this Act`, `Part 2 of the Schedule applies to the enactment` (ie-operation-and-construction.l4). |
| 58 | s 22(1) a power may be exercised from time to time | inert | A continuing-effect rule with no condition; same shape as s 10. |
| 59 | s 22(2) a power given to an office holder is exercisable by the holder for the time being | inert | A substitution of holder for office; there is no computation, only a naming rule. |
| 60 | s 22(3) a power to make an SI includes the power to repeal, amend and (where required) replace it | encoded | `a power to make a statutory instrument is read as including the power` (ie-powers-and-service.l4). |
| 61 | s 23(1) a duty shall be performed from time to time as occasion requires | inert | Same shape as s 22(1). |
| 62 | s 23(2) a duty on an office holder is performed by the holder for the time being | inert | Same shape as s 22(2). |
| 63 | s 24 rules of court for a new or varied jurisdiction | inert | Confers a power on whichever authority makes the rules of the court; whether a court's jurisdiction has been conferred, extended or varied is a legal conclusion the encoding would take as an input and return unchanged. |
| 64 | s 25 service by post | encoded | `service by post may be effected under section 25`, `the time at which service is deemed to have been effected`, `the date in UTC on which service is deemed to have been effected` (ie-powers-and-service.l4). |
| 65 | s 26(1) repeal and substitution | encoded | `the repealed enactment is in force throughout` (ie-repeal.l4). |
| 66 | s 26(2)(a) a person appointed continues to act | encoded | `a person appointed under the former enactment continues to act on` (ie-repeal.l4). |
| 67 | s 26(2)(b) continuing securities; things prepared or used | encoded | `the security remains in force`, `the data, books, papers, forms and things may continue to be used` (ie-repeal.l4). |
| 68 | s 26(2)(c) proceedings may be continued, subject to s 27(1) | encoded | `the proceedings may be continued under the new enactment` (ie-repeal.l4); how s 27(1) limits it is not stated, so it is an input (fork F26). |
| 69 | s 26(2)(d) an SI under a repealed and re-enacted provision | encoded | `what paragraph (d) does to the instrument` (ie-repeal.l4), with `the enactment comes into operation after the commencement of this Act` (ie-operation-and-construction.l4). |
| 70 | s 26(2)(e) the same idea in a different form of words | encoded | `the idea in the new enactment is not taken to be different merely because a different form of words is used` (ie-repeal.l4). |
| 71 | s 26(2)(f) a reference to the former enactment | encoded | `how a reference in any other enactment to the former enactment is read` (ie-repeal.l4). |
| 72 | s 27(1)(a) a repeal does not revive what was not in force or not existing | encoded | `what section 27(1)(a) says of a thing that` (ie-repeal.l4). |
| 73 | s 27(1)(b) previous operation and things duly done or suffered | encoded | `the repeal does not affect a thing done or suffered on` (ie-repeal.l4). |
| 74 | s 27(1)(c) rights, privileges, obligations and liabilities | encoded | `the repeal does not affect a right, privilege, obligation or liability acquired, accrued or incurred on` (ie-repeal.l4). |
| 75 | s 27(1)(d) penalties, forfeitures and punishments for an offence before the repeal | encoded | `the repeal does not affect a penalty, forfeiture or punishment for an offence or contravention committed on` (ie-repeal.l4). |
| 76 | s 27(1)(e) legal proceedings pending at the repeal | encoded | `the repeal does not prejudice or affect the legal proceedings` (ie-repeal.l4). |
| 77 | s 27(2) proceedings and penalties as if the enactment had not been repealed | encoded | `the proceedings may be instituted, continued or enforced, and the penalty imposed and carried out, as if the enactment had not been repealed` (ie-repeal.l4). |
| 78 | SCHEDULE heading and 'Section 21.' | inert | A heading and a cross-reference to s 21; no rule. |
| 79 | Sch Pt 1 'commencement' | encoded | `the commencement of the enactment, as the Schedule defines the word` (ie-interpretation-time.l4): the time at which the enactment comes into operation, so a moment, which refuses where only a day is known. |
| 80 | Sch Pt 1 'financial year' (exchequer) | encoded | `the exchequer financial year containing` (ie-interpretation-time.l4): coextensive with a calendar year. |
| 81 | Sch Pt 1 'local financial year' | encoded | `the local financial year containing` (ie-interpretation-time.l4). |
| 82 | Sch Pt 1 'midnight' | encoded | `Midnight` (ie-interpretation-time.l4): the point of time at which a named day ends; the module's moments are stored as the end of a day. |
| 83 | Sch Pt 1 'month' (a calendar month) | encoded | `the calendar month containing`, `the last day of a period of` ... `calendar months` ... (ie-interpretation-time.l4); read as a named month of the calendar (fork F4). |
| 84 | Sch Pt 1 'week' (Saturday midnight to the next Saturday midnight) | encoded | `the week containing`, `is the first day of a week` (ie-interpretation-time.l4); a week runs Sunday to Saturday on the 'midnight' definition (fork F6). |
| 85 | Sch Pt 1 'week-day' (a day which is not a Sunday) | encoded | `is a week-day` (ie-interpretation-time.l4): Monday to Saturday. NOT daydate's `is weekday`, which is Monday to Friday (fork F7). |
| 86 | Sch Pt 1 'year' (12 months beginning on 1 January) | encoded | `the year containing`, `the last day of a period of` ... `years` ... (ie-interpretation-time.l4). |
| 87 | Sch Pt 1 'affidavit' | inert | Includes a declaration in the case of a person allowed by law to declare instead of swearing. A lexical entry: whether a given person is so allowed is a legal conclusion not in the text, so a function would restate its input. |
| 88 | Sch Pt 1 'British statute' | inert | Defines a name for an Act of a former Parliament. Used only to read other enactments; no rule. |
| 89 | Sch Pt 1 'Circuit Court', 'District Court', 'High Court', 'Supreme Court' | inert | Each means the court as established and for the time being maintained by law (the High and Supreme Courts under Article 34 of the Constitution). Names for institutions; nothing is computed from them. |
| 90 | Sch Pt 1 'Constitution' | inert | The Constitution of Ireland enacted on 1 July 1937, as amended. A name; the date is not used by any rule in the text encoded here. |
| 91 | Sch Pt 1 'Dail Eireann', 'Seanad Eireann', 'Oireachtas' | inert | Names for the Houses and the National Parliament by reference to Article 15 of the Constitution. |
| 92 | Sch Pt 1 'Government', 'Minister of the Government', 'President' | inert | Names for the Government (Article 28), a member of it in charge of a Department, and the President including a Commission lawfully exercising the powers. |
| 93 | Sch Pt 1 'Great Britain' | inert | Does not include the Channel Islands or the Isle of Man. A geographic exclusion; nothing is computed. |
| 94 | Sch Pt 1 'land' | inert | A wide inclusive definition (tenements, hereditaments, houses and buildings, land covered by water, estates and interests). Nothing to compute: whether a thing is land is a classification the caller makes. |
| 95 | Sch Pt 1 'oath', 'swear' | inert | Include affirmation, declaration and the like for a person allowed by law to affirm or declare. Lexical; whether the person is so allowed is not in the text. |
| 96 | Sch Pt 1 'ordnance map' | inert | A map made under the Survey (Ireland) Acts 1825 to 1870. A name. |
| 97 | Sch Pt 1 'pre-union Irish statute' | inert | An Act of a Parliament sitting in Ireland before 1 January 1801. A name, with a date no rule uses. |
| 98 | Sch Pt 1 'rateable valuation' | inert | The valuation under the Valuation Act 2001. A name for a figure from another Act. |
| 99 | Sch Pt 1 'rules of court' | inert | Rules made by the authority with power to make rules for the court concerned; the same authority as in s 24. |
| 100 | Sch Pt 1 'Saorstat Eireann statute' | inert | An Act of the Oireachtas of Saorstat Eireann. The module's kind `a statute of Saorstat Eireann continued in force` is s 2(1)(b)'s class; this entry is a name for the wider class, and no rule turns on the difference. |
| 101 | Sch Pt 1 'statutory declaration' | inert | A declaration made under the Statutory Declarations Act 1938. A name. |
| 102 | Sch Pt 1 'writing' | inert | Includes printing, typewriting, lithography, photography and other modes, and information kept in a non-legible form capable of being reproduced legibly. A wide definition with no condition to compute. |
| 103 | Sch Pt 2 'Companies Acts', 'Social Welfare Acts' | inert | Names for groups of Acts; apply only under s 21(2), which is encoded. |
| 104 | Sch Pt 2 'full age' | encoded | `the day on which the person attains full age`, `the person is of full age at the end of`, `the person is of full age throughout` (ie-operation-and-construction.l4); the days of attaining 18 and of marrying are inputs. |
| 105 | Sch Pt 2 'functions' | inert | Includes powers and duties, and references to performing them. A wide definition; nothing to compute. |
| 106 | Sch Pt 2 'Member State' | inert | Where the context so admits, a Member State of the European Communities or the Union. A name. |
| 107 | Sch Pt 2 'Minister of State' | inert | A person appointed under section 1 of the Ministers and Secretaries (Amendment) (No. 2) Act 1977. A name. |
| 108 | Sch Pt 2 'public holiday' | encoded | Determined under the Organisation of Working Time Act 1997, which is not in this text, so the holidays are an INPUT (a function from a date to a boolean) wherever they matter: `is a working day` and the working-day period function (ie-interpretation-time.l4). |
| 109 | Sch Pt 2 'working day' | encoded | `is a working day`, `the last day of a period of` ... `working days` ... (ie-interpretation-time.l4): a day that is not a Saturday, a Sunday or a public holiday. |
| 110 | 'Acts Referred to' table (printed under the Schedule heading in the arrangement) | not applicable | A table in the file's front matter, before the Act's own text begins at 'INTERPRETATION ACT 2005' (line 77); it lists the Acts the text names, with year and number, and belongs to no section. It gives only the YEAR and number of the Adoption Act 1976 and of the 1922 Act, which is why the comparisons with those two Acts are supplied as inputs and not computed. |
| 111 | The meaning of 'day' (the brief's item 6) | silent | The Act is silent on this: there is no definition of 'day'. The encoding takes a day to be a calendar date of daydate that runs from one midnight to the next (fork F9). |
| 112 | A rule that moves the last day of a period off a day of rest, recess or holiday, or a day an office is closed (the brief's item 3) | silent | The Act is silent on this. The whole text was read for one, section by section and in the Schedule, and none moves a last day: the nearest provisions are s 18(h), which says only that the first and last days are included, and the Schedule's 'week-day', 'working day' and 'public holiday', which define kinds of day and move nothing. The function returns the last day when it is an ordinary day and refuses when it is a rest day; the roll-forward is a labelled alternative reading outside the Act's module (fork F8). |
| 113 | A rule for a period 'after' an event, or a corresponding-date rule for months and years (the brief's item 2) | silent | The Act is silent on this: s 18(h) speaks of a period that begins on or is reckoned from a day, and one that ends on or is reckoned to a day, and 'after' appears nowhere in it. The functions refuse (forks F2, F5). |
| 114 | A moment within the day for s 16(1), and a rule for deemed notice other than service by post | silent | The Act is silent on both. For s 16(1) the day is answered and the moment refuses. The only deeming of service is s 25 (forks F11, F29). |

## 5. Fork register

Each row: the question; the readings seen; the one taken; the text that licenses it; where it is encoded and tested.
A reading marked "(not the Act's)" is in `ie-month-year-readings.l4` or is stated here only; the Act's own modules do not use it.

### 5.1 Periods and rest days

| id | question | readings seen | reading taken | text and where tested |
| --- | --- | --- | --- | --- |
| F1 | Does a period "from" a day count that day? | (a) yes; (b) no, the period starts the next day | **(a)** | s 18(h): "Where a period of time is expressed to begin on or be reckoned from a particular day, that day shall be deemed to be included in the period". N days from D end on D + N - 1: 30 days from 2026-01-01 end on 2026-01-30. `tests-periods.l4`, `tests-worked-cases.l4`. |
| F2 | Does a period counted "after" an event count the event's day, and when does it end? | (a) as F1; (b) the event's day is left out, so one more day; (c) the text is silent | **(c): REFUSE** | s 18(h) speaks only of a period "expressed to begin on or be reckoned from" a day and one "expressed to end on or be reckoned to" a day. No provision counts a period "after" an event: where "after" occurs (for example ss 17, 18(d), 18(i), 21(2), 26(2)(d)) it compares dates or hours and starts no period. `how it is counted = after an event` refuses with "section 18(h) says nothing about a period counted after an event". |
| F3 | Is the last day inside the period? | inside; outside | **inside** | The Nth day counting the first as day 1 is the last day and is inside; the next day is outside. For a period "expressed to end on or be reckoned to" a day, s 18(h) includes that day (`falls within the period beginning on ... and ending on`). Boundary dates on both sides are asserted for every unit in `tests-periods.l4`. |
| F4 | What are a "month" and a "year"? | (a) calendar units; (b) fixed lengths (30 days, 365 days) | **(a)** | Schedule Pt 1: "month" means a calendar month; "year", when used without qualification, means a period of 12 months beginning on the 1st day of January in any year; "financial year" (exchequer) and "local financial year" are periods coextensive with a calendar year. So N calendar months beginning on the first of a month end on the last day of the Nth month (1 month from 2025-02-01 ends 2025-02-28; 1 month from 2024-02-01 ends 2024-02-29; 2 months from 2025-01-01 end 2025-02-28), and N years beginning on 1 January end on 31 December of the Nth year. |
| F5 | A period of months or years that begins elsewhere than the first day of the unit: a start on the 31st, on 29 February, in a month lacking the start day's number, or simply mid-month or mid-year | **A** refuse; **B** corresponding date, clamped to the end of a short month (`add months`, `add years`); **B-inclusive** the day before that date, since s 18(h) includes the first day; **C** corresponding date, rolled over into the next month | **A: REFUSE** | The Schedule defines the unit but nothing says what a month or a year that begins part-way ends on; the Act has no corresponding-date rule. `daydate`'s `add months` clamps and `Date` rolls, but those are library conveniences, not text. Refusal messages: "the Act has no rule for a period of calendar months that does not begin on the first day of a month" and "... of years that does not begin on 1 January". What B, B-inclusive and C would answer for the brief's cases is in section 6.1 (`tests-readings.l4`). |
| F6 | What is a "week", and what is N weeks from a day? | (a) Sunday to Saturday, and N weeks only from a Sunday; (b) seven days from any day (reading D, not the Act's) | **(a); from any other day REFUSE** | Schedule Pt 1: "week" means the period between midnight on any Saturday and midnight on the following Saturday; "midnight", in relation to a particular day, is the point of time at which the day ends. So a week runs from the end of a Saturday to the end of the next Saturday, that is Sunday to Saturday. 1 week from Sunday 2026-01-04 ends Saturday 2026-01-10; from any other day: "the Act has no rule for a period of weeks that does not begin on a Sunday". Reading D (1 week from 2026-01-01 ends 2026-01-07) is in `ie-month-year-readings.l4`. |
| F7 | Naming hazard: "week-day" against `daydate`'s `is weekday` | the Act's "week-day" is Monday to Saturday; `daydate`'s `is weekday` is Monday to Friday | **both kept, never mixed** | Schedule Pt 1: "week-day" means a day which is not a Sunday. `is a week-day` in `ie-interpretation-time.l4` is the Act's word. "Working day" (Schedule Pt 2: a day which is not a Saturday, Sunday or public holiday) is `daydate`'s `is weekday` AND NOT a public holiday, and is Monday to Friday. A caller who writes `is weekday` for the Act's "week-day" gets Saturday wrong. |
| F8 | Does anything move a last day that falls on a day of rest, recess or holiday; does it reach months and years or only days; what of several in a row? | (a) no rule: refuse; (b) roll forward to the next day that is not one (reading R, not the Act's); (c) roll forward for days only | **(a): REFUSE** | The whole text was read for a rule and none was found. The nearest provisions are s 18(h) (first and last days are included), the Schedule's "week-day", "working day" and "public holiday" (which define kinds of day and move nothing), and s 25 (service by post, which is about time of delivery). `the last day of a period, allowing for days of rest, recess or holiday` returns the last day when it is an ordinary day and refuses when it is a rest day, including two or more in a row and a rest day reached after a period in months. Reading R, which does roll forward over a run of rest days, is in the readings module and tested. The brief's question whether a roll-forward reaches months and years does not arise on the text, because there is no roll-forward for any unit. `tests-rest-days-and-words.l4`. |
| F9 | What is a "day", and do days tile with no gap? | the Act does not define "day"; (a) a calendar date, midnight to midnight; (b) something else | **(a), with the end of D-1 the same point as the start of D** | Not stated in the text. Schedule Pt 1 "midnight" is "the point of time at which the day ends", which gives the day an end; that the end of one day is the start of the next is an assumption, stated in the module header. It is what lets "comes into operation at the end of the day before" (s 16(2)) mean "in operation throughout the day". `daydate`'s DATE is the calendar date. |

### 5.2 Commencement

| id | question | readings seen | reading taken | text and where tested |
| --- | --- | --- | --- | --- |
| F10 | The brief asks when an enactment "binds". The Act never uses the word. | "binds" = "comes into operation"; or something later | **same** | ss 1(2), 15, 16, 17 say "comes into operation"; the Schedule says "commencement" means "the time at which the enactment comes into operation". Whether an enactment that is in operation binds a given person from that moment is outside the text. |
| F11 | An Act that says nothing: from what moment on the date of its passing? | start of the day; end of the day; the moment of signature; none | **none named: the day is answered, the moment REFUSES** | s 16(1): "every provision of an Act comes into operation on the date of its passing"; contrast s 16(2), which says "at the end of the day before". So `the moment at which the enactment comes into operation` refuses with "section 16(1) names no moment within the date of passing"; `is in operation at the end of` that day is TRUE (it has come into operation on that day); `is in operation throughout` that day, and `the first day on which ... throughout`, refuse; the day before is not in operation and the day after is. See 2.3. |
| F12 | An Act expressed to come into operation on a particular day, named or to be fixed later | the day fixed is a particular day once fixed; before it is fixed there is no day | **s 16(2): at the end of the day before; REFUSE until the day is fixed** | s 16(2) covers a day "named in the Act or ... to be fixed or ascertained in a particular manner". Day fixed as 2026-06-01: moment is the end of 2026-05-31, so the whole of 2026-06-01 is in operation and 2026-05-31 is not. |
| F13 | A statutory instrument that says nothing | s 16(3) as written | **the end of the day before the day it is made** | s 16(3). An instrument made on 2026-03-10 is in operation from the end of 2026-03-09, so the whole of 2026-03-10 is. The day it is made is a supplied fact (the "made" of s 2(1) is wide). |
| F14 | A statutory instrument expressed to commence on a particular day, before or after the making | s 16(4) as written | **the end of the day before the particular day**, even when that day precedes the making | s 16(4) says "whether the day is before or after the date of the making". |
| F15 | "Passed or published" (the brief) | the date of passing; the date of publication | **the day the Bill is signed by the President, supplied as an input** | s 15(1). The Act has no rule keyed to publication, so publication has no effect on this text. The worked case uses 2026-03-10 as the day of signature. |
| F16 | A Saorstat Eireann statute that is silent on commencement | treat its enactment date as the date of passing; or the text is silent | **REFUSE** | s 15(1) defines "the date of the passing" only "of an Act of the Oireachtas"; s 2(1) "Act" also includes a pre-1937 statute, for which s 16(1)'s "date of its passing" has no definition in the Act. |
| F17 | Section 4(1): contrary intention | a flag on every function; or a precondition stated once | **once** | s 4(1). `a provision of this Act applies to an enactment` takes the three places a contrary intention can appear (this Act, the enactment itself, the Act under which it is made) and is the only function that does; the time module's header states the precondition and its functions assume no contrary intention appears. `tests-general.l4`. |

### 5.3 General and construction rules

| id | question | readings seen | reading taken | text and where tested |
| --- | --- | --- | --- | --- |
| F18 | s 2(1) "repeal includes revoke, rescind, abrogate or cancel": a closed or an open list? | closed; open | **open** | "includes". A word outside the five refuses ("`some other word`"). |
| F19 | s 12: "does not materially affect the substance of the form or is not misleading in content or effect": either, or both? | either (literal "or"); both | **either** | The text says "or". The two readings differ only for a form that is misleading but does not affect substance, or the reverse. `section 12 saves the form used`; `tests-general.l4`; red-control test 7 expects the wrong answer for a form that satisfies neither. |
| F20 | s 14(1)(c): when is the session cited? | regnal year and chapter always, session as well when there were several; or the session is optional | **regnal year and chapter only where there was one session; with the session where there was more than one** | "by its regnal year and chapter number and, where there was more than one parliamentary session in the same regnal year, by reference to the session concerned". |
| F21 | s 18(b)(ii): which dates? | as written; or the same boundary for both | **as written**: an Act passed on or after 22 December 1993; an instrument made after that date | An instrument made on 22 December 1993 itself is not within it (red-control test 4). |
| F22 | s 18(d)(ii): "a child to whom subparagraph (i) relates" | a child adopted under the Adoption Acts 1952 to 1998 and the enactments read with them; or only such a child within an Act that also satisfies (i)'s own date test | **a child adopted under those Acts, for an Act passed on or after 14 January 1988** | The Acts Referred to table gives the Adoption Act 1976 only as "1976, No. 29", so the comparison with that Act in (i) is supplied as an input (`the Act was passed after the passing of the Adoption Act 1976`); for (ii) the encoding relies on the date of passing alone, since an Act passed on or after 14 January 1988 was passed after an Act of 1976. |
| F23 | s 21(2): "comes into operation after the commencement of this Act": is the same moment "after"? | no; yes | **no (strict)** | This Act comes into operation at the end of 31 December 2005 (s 1(2) with s 16(2)). An enactment expressed to come into operation on 1 January 2006 does so at that same moment, so Part 2 of the Schedule does not apply to it; one that comes into operation later does. An enactment under s 16(1) passed on 1 January 2006 names no moment and REFUSES. Red-control test 8. |
| F24 | Schedule Pt 2 "full age": when is 18 attained; "or sooner marries" | the Act has no anniversary rule | **both days are inputs; full age is the earlier** | "the time when the person attains the age of 18 years or sooner marries, or any time after either event". No time of day, so "throughout" the day of the event refuses. |
| F25 | s 26(1): until when does the repealed enactment continue? | up to and including the day the substituted provisions commence; up to the moment | **in force throughout every day that ends at or before the moment they come into operation** | "continues in force until the substituted provisions come into operation". With the moment the end of D-1 (s 16(2)), the repealed enactment is in force throughout D-1 and not throughout D. |
| F26 | s 26(2)(c): "subject to section 27(1)" | how s 27(1) limits the continuation is not stated | **an input** (`section 27(1) prevents the continuation`) | The text names the limit and does not define it. |
| F27 | s 6: "since the date of the passing ... or the making": a change on that very day | since; not since | **REFUSE** | The Act fixes no time of day for the passing or the making, so a change on the same day cannot be placed before or after. Other days answer. |
| F28 | s 17: "at any time after the passing": the same day | after; not after | **REFUSE** | Same reason as F27. |
| F29 | s 25: time of deemed service | time zone; "unless the contrary is proved" | **the time of delivery is an input (a DATETIME); the date is read in UTC; if the contrary is proved, REFUSE** | The Act names no time zone (s 18(i) sends a time by hour to an Act not in the text), so the function's name says "in UTC". Once the contrary is proved the Act says only that the deeming is displaced, not what time applies. A letter not posted as the section describes also refuses. |
| F30 | ss 7(1) and 13 for a statutory instrument | no rule; or a rule | **s 7(1): FALSE (it is a rule about an Act); s 13: REFUSE** | s 7(1) speaks of "a provision of an Act", so it gives a court no leave for an instrument. s 13 says "An Act is a public document and shall be judicially noticed" and is silent on an instrument, so whether an instrument is judicially noticed is not answered. |
| F31 | s 3(1): when are the four Acts repealed? | on enactment; on commencement | **with this Act: from the end of 31 December 2005** | s 3(1) is a provision of this Act, so it comes into operation when this Act does (s 1(2) with s 16(2)). |
| F32 | s 18(e): distance | straight line in space; its projection on the horizontal plane | **the horizontal projection; height is ignored** | "measured in a straight line on a horizontal plane". |
| F33 | s 3(2)(a), (b): "(i) in the absence of ..., or (ii) by the application ...": one limb or both | either; both | **either** | The limbs are joined by "or". |
| F38 | s 18(i): a time by reference to an hour | any hour is that hour on the clock | **REFUSE** | "that time shall be determined by reference to the Standard Time (Amendment) Act 1971", which is not in the text. |

### 5.4 The text, the language and the build

| id | question | reading taken | text and where |
| --- | --- | --- | --- |
| F34 | Which language text has authority? | **not decided.** This is an encoding of the English text only. | The English text of the Act says nothing on it. The subject-level note in `../../SOURCE-LICENSE.md` records, for another Act, that Article 25.4 of the Constitution makes the Irish text prevail where both are enrolled and conflict; that is not in this Act, was not used, and this Act's signed language was not checked. |
| F35 | Accented letters in identifiers | transliterated to ASCII (`Saorstat Eireann`, `Sampla`, `Samplai`) | The brief requires ASCII filenames, and the identifiers follow. The quoted text keeps its accents. |
| F36 | Target compiler | `unstable` | Section 1. |
| F37 | Is the enacted text the current text? | **yes, on the file's own statement** | The file says the directory lists no amendment. It was not re-checked. |

### 5.5 Looked at and not forked

Read for ambiguity and left alone, because no reading changes an answer: s 1(2) (a date), s 2(2) (a closed list of five conditions), s 9 (two lists with an open "other division, by whatever name called", encoded as an open case that refuses), s 11 (four named headings), s 15(2) (a duty on an officer), s 18(f) (a series including its first and last; a last before the first refuses), s 22(3), s 26(2)(a), (b), (d), (e), (f), s 27(1)(a) to (e) and (2).
"No ambiguity" is a claim about what was read, not about the Act.

## 6. Answer table for the worked cases

Every answer is on the text of the Act alone, and each was run: `tests-worked-cases.l4` asks all of them through the record interface, `tests-periods.l4` and `tests-commencement.l4` ask them through the plain functions.

### 6.1 Periods

"The Act's answer" is what `ie-interpretation-time.l4` returns.
The three right-hand columns are what the labelled alternative readings of F5 would return (`ie-month-year-readings.l4`, `tests-readings.l4`); **they are not the Act's.**
"Day before" is reading B-inclusive: the day before the corresponding date, because s 18(h) includes the first day.

| period | counted from | the Act's answer | section | B: corresponding date, clamped | B-inclusive: day before it | C: corresponding date, rolled over |
| --- | --- | --- | --- | --- | --- | --- |
| three years | 2025-07-16 | **REFUSE**: "the Act has no rule for a period of years that does not begin on 1 January" | Sch Pt 1 "year"; s 18(h); F4, F5 | 2028-07-16 | 2028-07-15 | 2028-07-16 |
| five years | 2025-01-15 | **REFUSE** (same) | same | 2030-01-15 | 2030-01-14 | 2030-01-15 |
| five years | 2025-09-01 | **REFUSE** (same): 1 September begins a month, not a year | same | 2030-09-01 | 2030-08-31 | 2030-09-01 |
| thirty days | 2026-01-01 | **2026-01-30** (2026-01-01 is day 1; 2026-01-30 is inside, 2026-01-31 outside) | s 18(h); F1, F3 | not asked | not asked | not asked |
| two years | 2024-02-28 | **REFUSE** (same): the text has no rule for a year that begins part-way | same | 2026-02-28 | 2026-02-27 | 2026-02-28 |
| one year | 2024-02-29 | **REFUSE** (same): the text has no rule for 29 February | same | 2025-02-28 | 2025-02-27 | 2025-03-01 |
| one month | 2025-01-31 | **REFUSE**: "the Act has no rule for a period of calendar months that does not begin on the first day of a month": the text has no rule for a month that lacks the start day's number | Sch Pt 1 "month"; s 18(h); F4, F5 | 2025-02-28 | 2025-02-27 | 2025-03-03 |

The same six periods counted "after" an event all refuse: "section 18(h) says nothing about a period counted after an event" (F2).
One week from a Thursday refuses (F6): reading D would give 2026-01-07 for one week from Thursday 2026-01-01.

Periods the Act does answer, besides thirty days from 2026-01-01 (all asserted in `tests-periods.l4`):
one calendar month from 2025-02-01 ends 2025-02-28, from 2024-02-01 ends 2024-02-29; two months from 2025-01-01 end 2025-02-28; thirteen months from 2025-01-01 end 2026-01-31; one week from Sunday 2026-01-04 ends Saturday 2026-01-10; N years from 1 January end on 31 December of the Nth year.
A period of one day ends on its first day; a period of 0, of a fraction, or negative refuses ("a period must be a whole number of units, at least one").

### 6.2 Commencement

| case | day | moment | in operation at the end of / throughout | sections |
| --- | --- | --- | --- | --- |
| an Act passed on 2026-03-10 (Bill signed that day) and silent | **2026-03-10** | **none named: REFUSE** ("section 16(1) names no moment within the date of passing") | at the end of 2026-03-10 yes; throughout 2026-03-10 REFUSE; throughout 2026-03-11 yes; at the end of 2026-03-09 no | ss 15(1), 16(1); F10, F11, F15 |
| an Act that comes into operation on a day to be fixed later; the day is fixed as 2026-06-01 | **2026-06-01** | **the end of 2026-05-31** | at the end of 2026-05-31 yes; throughout 2026-05-31 no; throughout 2026-06-01 yes (first day throughout: 2026-06-01) | s 16(2); Sch Pt 1 "midnight"; F9, F12 |
| a statutory instrument made on 2026-03-10 and silent | **2026-03-10** (the day it is made) | **the end of 2026-03-09** | throughout 2026-03-10 yes; throughout 2026-03-09 no (first day throughout: 2026-03-10) | s 16(3); F13 |

Before the day is fixed, an Act "expressed to come into operation on a day not yet fixed" refuses ("the particular day on which the enactment is to come into operation has not been fixed or ascertained").
For the Act itself: 1 January 2006 under s 1(2) is the end of 31 December 2005 under s 16(2).

### 6.3 Other answers worth seeing

| question | answer | section |
| --- | --- | --- |
| last day of a period is a Sunday (one month from 2025-08-01 ends 2025-08-31) | **REFUSE**: "the Act has no rule for a last day that falls on a day of rest, recess or holiday; another enactment or rules of court may have one"; the same for Saturday and Sunday in a row, and for a supplied holiday | s 18(h); F8 |
| 2 working days from Thursday 2026-01-01, with 2026-01-01 and 2026-01-05 supplied as public holidays | 2026-01-06 | Sch Pt 2 "working day"; s 18(h) |
| 6 week-days from Monday 2026-01-05; 7 week-days | 2026-01-10 (Saturday counts); 2026-01-12 (Sunday does not) | Sch Pt 1 "week-day"; F7 |
| does Part 2 of the Schedule apply to an instrument expressed to commence on 2026-01-01 | yes; on 2006-01-01: **no**, the same moment is not "after" | s 21(2); F23 |
| a word importing the feminine, in an instrument made on 1993-12-22 | **not** read as masculine too; made 1993-12-23: read as masculine too | s 18(b)(ii); F21 |
| service by post, properly addressed and posted, delivery in the ordinary course expected 2026-03-10T23:59:59Z, contrary not proved | deemed effected at 2026-03-10T23:59:59Z, so the date in UTC is 2026-03-10; at 2026-03-11T00:00:00Z it is 2026-03-11; if the contrary is proved: **REFUSE** | s 25; F29 |
| section 3(1): is the Interpretation Act 1937 repealed by the end of 2005-12-31 | yes; by the end of 2005-12-30 no | ss 3(1), 1(2), 16(2); F31 |

## 7. What `check.sh` prints

Run from this directory, after `_work/` and `_probes/` were removed:

```
L4=/Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-9afd0288/bin/l4 \
SRC_RAW=<INPUTS_DIR>/No.-23-of-2005.txt ./check.sh
```

`SRC_RAW` is the raw text; without it the source-quote gate prints that it was NOT RUN and nothing else changes.
`L4_TARGET` defaults to `unstable` in this row's `check.sh`.

```
check.sh: the target is unstable, so the main check was skipped.
module                                    errors satisfied  failed  refused  expected
ie-general.l4                                  0         0       0        0         0
ie-interpretation-time.l4                      0         0       0        0         0
ie-month-year-readings.l4                      0         0       0        0         0
ie-operation-and-construction.l4               0         0       0        0         0
ie-powers-and-service.l4                       0         0       0        0         0
ie-repeal.l4                                   0         0       0        0         0
tests-commencement.l4                          0        57       0        0         0
tests-general.l4                               0       102       0        0         0
tests-operation.l4                             0       112       0        0         0
tests-periods.l4                               0        96       0        0         0
tests-powers-service.l4                        0        31       0        0         0
tests-readings.l4                              0        59       0        0         0
tests-red-control.l4                           8         0       8        0         8
tests-repeal.l4                                0       105       0        0         0
tests-rest-days-and-words.l4                   0        57       0        0         0
tests-worked-cases.l4                          0        26       0        0         0
TOTAL (16 modules)                             8       645       8        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
srcrefs check: 261 src: lines, 132 runs, 172 locators, 0 problems
(exit status 0)
```

How to read it:

- The six `ie-*.l4` modules have no assertions of their own; they type-check with 0 errors.
- Eight failures are expected and are all in `tests-red-control.l4`, whose eight assertions are deliberately wrong (the file header says which wrong reading each guards against).
  `check.sh` counts them in its `expected` column and `encoding.json` records them under `expected_red`; the gate fails if the file produces more or fewer than eight.
- Every other test file has 0 failed, 0 refused and 0 errors.
  A refused assertion makes the run red: a refusal is expected only inside `#ASSERT REFUSED ... BECAUSE ...`, which is satisfied when the stated reason matches.
- Counts are the lines after `Message:`, one per assertion on this binary.
- `srcrefs check --strict` verifies that every quotation is a slice of the raw text and that every `@ref` locator matches the quote run above it.

## 8. Open questions for a domain expert

1. **Periods in months and years from a day that is not the first of the unit.**
   The Schedule defines "month" and "year" and s 18(h) says the first day is included, but there is no corresponding-date rule.
   Is the answer for "one month from 2025-01-31" or "one year from 2024-02-29" in another enactment, in rules of court, or in a general principle the Act presupposes?
   Which of B, B-inclusive and C would a court apply (F5)?
2. **Periods "after" an event.**
   Does s 18(h) govern a period counted "after" an event, and if so is the event's day left out (F2)?
3. **Rest days.**
   Is there a rule, outside this Act, that moves a last day off a day on which an office is closed, and does it reach months and years (F8)?
4. **The moment of commencement under s 16(1).**
   Is there a settled moment on the date of passing, or is the point left open (F11)?
5. **"Week" from a day that is not a Sunday.**
   Is a period of N weeks from any day 7N days (reading D), or is the Schedule's definition limiting (F6)?
6. **Which language text prevails for this Act** (F34).
7. **Section 12's "or"** (F19), **s 18(d)(ii)'s "a child to whom subparagraph (i) relates"** (F22), and **how s 27(1) limits s 26(2)(c)** (F26).
8. **The Standard Time (Amendment) Act 1971**: does it supply the answer that ss 18(i) and 25 leave open, including the time zone in which a deemed time of service falls (F29, F38)?
9. **Public holidays** under the Organisation of Working Time Act 1997: a caller-supplied calendar is the only possibility on this text.
10. **Whether the Act's rule on "day" is simply the ordinary one**, so that the tiling assumption of F9 is harmless.
