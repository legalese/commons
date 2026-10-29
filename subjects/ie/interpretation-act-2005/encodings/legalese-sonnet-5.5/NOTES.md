# NOTES: Interpretation Act 2005 (Ireland), Act No. 23 of 2005

Row `legalese-sonnet-5.5`: one Sonnet 5.5 agent working alone in each pass.
Pass 1 (2026-10-21) wrote the first draft from the brief kept here as `BRIEF-pass1.md`.
Pass 2 (2026-10-29) is the completion pass to "whole", from a second brief that is not in this folder.
Status: `draft`.
No domain expert has read this against the statute.
The deposited text is the enacted text of the Act, not a revision, and it is a plain-text rendering made by a converter script, not the official text (section 1).

Section 2 was written BEFORE any L4 (in pass 1), so the expected answers in it are the reading of the text and not a copy of what the code printed.
Section 2 is unchanged since then.
The re-disposition audit (after section 3) was written BEFORE any new L4 in pass 2; sections 0, 1, 3, 4, 5.5, 5.6, 7, 8 and 9 onward were written or refreshed after the new modules landed.
Where a later section disagrees with an earlier one, the later section says so out loud (see 2.3).

## 0. Reading guide

- The one thing most readers want: section 6 (the answers to the worked cases) and section 5 (the forks that decide them).
- The headline: **the Act has no rule for most of what the brief asks.**
  It counts days from a day (s 18(h)) and it fixes commencement (ss 15 to 17); it says what a "month", a "year" and a "week" are (Schedule Part 1).
  It has no corresponding-date rule, no rule for a period counted "after" an event, no rule that moves a last day off a day of rest or a holiday, and no moment of day for an Act that says nothing about its commencement.
  Where the text is silent the module REFUSES with a named reason; it never returns a plausible default.
- The alternative answers that other systems give (clamping to the end of a short month, rolling over, moving off a rest day) are in `ie-month-year-readings.l4`, which the Act's own module never calls, so that section 5 can show by running them what each would answer.
  They are NOT the Act's answers.
- State of the work (pass 2, 2026-10-29): every one of the 256 units of the text has its own row in section 4.
  111 are `encoded`, 64 are `fork` (a reading was chosen and section 5 names it), 80 are `inert` for reason 1 (not operative), 1 is `inert` for reason 2 (machinery: the short title), and 0 are repealed or blank.
  No row is `out-of-scope` or `deferred`.
- Where to start as a reviewer: section 5.6 (the ten forks found in pass 2, F39 to F48, each pinned by a test), section 9 (the places where the text does not answer), section 10 (numbered findings), and `## Jural relations`.

## 1. Source, target and caveats

- Source: `No.-23-of-2005.txt`, a plain-text rendering made by a converter script from the English print view of the Act as enacted on the electronic Irish Statute Book (sha256 `0108a07dd3db98b0058eacee0baabc34ce41823a52c57d2b52ae94b1bb7893d4`, checked).
  It is NOT the official text, it carries no mark-up, and nothing here is "verified against the official text".
  `srcrefs.py check --strict` compares quotations in the modules with that file, not with any official text.
- The file opens with an unofficial-text notice, a source line, a statement that the Statute Book's legislation directory lists no amendment, repeal or substitution of any section of the Act, and the Oireachtas copyright notice.
  The deposited text is the enacted text, not a revision: the brief for this pass says so, and the file's own statement (line 2) is that the Statute Book's legislation directory, read 2026-10-21, lists no amendment, repeal or substitution of any section of the Act and lists only later provisions that apply it, restrict its application or save it (`../../registers/source-bundle/No.-23-of-2005.meta.json` records the same).
  Neither statement was re-checked in this run (fork F37).
- The copyright notice is copied mechanically into the header of every module that quotes the text, and into `SOURCE-LICENSE.md`.
- The file puts each section's marginal note in front of the section number ("Commencement. 16.—(1) ...").
  By s 18(g) a marginal note is not part of the enactment, so the notes are headings and carry no rule.
- The file's front matter, after the arrangement of sections, prints a table headed "Acts Referred to".
  It sits before the Act's own text (which begins at "INTERPRETATION ACT 2005", line 77) and belongs to no section.
  The Schedule's own Part 2 (defined words) is at the end of the file.
- Quotations in the modules are `-- src:N | text` lines produced mechanically by `srcrefs.py quote` from the raw file.
  Each quote run was generated from the line numbers of the `@ref` that follows it, so a run is exactly what its `@ref` cites.
  The scripts that counted the units and generated the Schedule modules and their tests are not part of this folder; the standing proof of the quotations is `srcrefs.py check --strict`, which `check.sh` runs when `SRC_RAW` is set.
- Target compiler: **`unstable`**.
  The brief requires `@lang en`, `REFUSE` and `YMD`, which `main` rejects (`writing-l4-rules/references/dialects.md`), so the encoding cannot be read by `main`, and `check.sh` runs with `L4_TARGET=unstable` as its default, which skips the comparison with a main build.
- `L4_BIN` is the unstable prerelease binary recorded in `encoding.json` (`l4 --version` prints `unstable-20261028-5e95b5a (unstable, 5e95b5a, 2026-10-28)`, sha256 `0f0f1b86d37164af242ca2b6c03aa31ddeedef752bd10474f1459b78cf539e9d`), checked against the brief's sha256 on 2026-10-29.
  Pass 1 ran on a binary that printed `dev`; the 16 pass-1 modules print the same numbers on both (645 satisfied, 8 failed and expected, 0 refused).
  `JL4_LIBRARY_PATH` was unset throughout.
- `@lang en` draws a Hint from the linter on every module ("A module that declares nothing is English; this line can go.").
  The brief requires the line, so the Hint is known and left in; `check.sh` counts errors and assertion lines, and a Hint is neither.
  A census of `l4 run` over all 26 files on 2026-10-29 found 90 Hints in total, every one that message, no Warning, and no Error except the eight in `tests-red-control.l4`.
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
| `ie-interpretation-time.l4` (imports only `prelude` and `daydate`) | s 18(h): the last day of a period of N days, weeks, calendar months, years, working days or week-days; whether a day falls within a period; the number of days in a period. Days of rest, recess and holiday as an INPUT. Ss 15(1) and 16 with the Schedule's "midnight" and "commencement": the day, and the moment within the day, from which an Act, a Saorstat Eireann statute or a statutory instrument is in operation. The Schedule's time words: week, week-day, month, year, financial year, local financial year, working day, public holiday. This Act's own commencement (s 1(2)). |
| `ie-general.l4` | s 2(1) "Act", "enactment", "statutory instrument", "repeal"; s 4 (contrary intention); ss 5 to 9, 11 to 14(1). |
| `ie-operation-and-construction.l4` | s 17; s 18(b), (d), (e), (f), (g); s 20(1); s 21(2); the Schedule's "full age". |
| `ie-powers-and-service.l4` | s 22(3); s 25 (service by post, deemed time of service). |
| `ie-repeal.l4` | s 2(2); s 3(1) and (2); s 26; s 27. |
| `ie-month-year-readings.l4` | NOT the Act. The alternative readings of section 5 (B, B-inclusive, C, D, R), labelled and never called by the Act's modules. |
| `ie-schedule-definitions.l4` (pass 2) | The Schedule as a table: 32 Part 1 and 8 Part 2 defined words, each with what the entry says it means, includes or does not include, the case or context it is limited to, the things it names, and what it points at; the appliers for "includes" and "does not include" entries; the entries with a condition to apply (President, Minister of the Government, Constitution, pre-union Irish statute, Companies Acts, Social Welfare Acts, Member State); s 21(1) and s 21(2) as the glue that gives a word its Schedule meaning in an enactment. |
| `ie-words-and-meaning.l4` (pass 2) | The lead-in of s 18; s 18(a) singular and plural; s 18(c) person; s 18(j) offences by corporations; s 18(i) a time expressed by reference to an hour, with the 1971 Act's offset as an input; s 19 a word in a statutory instrument; s 20(2) other parts of speech. |
| `ie-powers-duties-continuing.l4` (pass 2) | s 10; s 22(1); s 23(1); s 22(2) and s 23(2) (the holder for the time being of an office); s 24 (rules of court for a jurisdiction an enactment confers, extends or varies). |
| `ie-citation-and-text.l4` (pass 2) | s 7(1)(a), (b), (c) told apart (the coarse rule stays in `ie-general.l4` and is called); s 14(2); s 14(3); s 15(2). |
| `ie-acts-referred-to.l4` (pass 2) | The "Acts Referred to" table, 18 rows, as a lookup. |

The brief's six required topics, each with where the answer is or why there is none:

1. When an enactment comes into force or binds, where it does not say: **answered for the day, and for the moment under s 16(2) to (4); no moment under s 16(1).**
2. How a period of days, weeks, months or years is counted: **days from a day: answered; weeks, months and years that begin where the Schedule's unit begins: answered; everything else, and every period "after" an event: the Act has no rule, so REFUSE.**
3. What happens when the last day falls on a rest day, recess or holiday: **the Act has no rule; REFUSE (the roll-forward is reading R, not the Act's).**
4. Deemed service: **s 25 only; the time of delivery is an input.**
5. What a repeal does: **ss 2(2), 3, 26, 27, encoded; the judgments the Act leaves to the reader are inputs.**
6. The meanings of "day", "week", "month", "year" and other time words: **the Schedule defines week, week-day, month, year, financial year, local financial year, midnight, commencement, working day and public holiday; it does not define "day" (the Act is silent; fork F9).**

### 3.2 What is asked as an input, and what is left out

No provision of the English text is left unencoded: the only `inert` rows are the 80 of reason 1 (title, long title, enacting words, date of enactment, headings and marginal notes, arrangement of sections, the Schedule's heading and cross-reference) and the one of reason 2 (the short title, s 1(1)).
What the encoding takes from the caller, because the text does not supply it:

- **A calendar of holidays.** "Public holiday" is defined by reference to the Organisation of Working Time Act 1997 (Schedule Part 2), which is not in this text.
  Rest days and public holidays are a caller-supplied function from a date to a boolean in every function that needs one.
- **The standard time of a day.** Section 18(i) sends a time expressed by reference to an hour to the Standard Time (Amendment) Act 1971, which is not in this text.
  `the moment in UTC of a time expressed by reference to a specified hour` takes the offset from UTC that Act fixes for the day as an input.
  `the clock time of a specified hour in an enactment` stays as the named refusal for a caller who supplies none.
- **How a person attains an age.** The Act has no anniversary rule; the day of attaining 18 and the day of marrying are inputs.
- **Facts that other enactments fix.**
  That a court is "as established and for the time being maintained by law" is a fact the caller supplies.
  For an entry that points at another enactment (Articles 15, 28 and 34 of the Constitution, the Valuation Act 2001, the Statutory Declarations Act 1938, the Survey (Ireland) Acts 1825 to 1870) the table records the pointer and not the content of the other enactment.
  The "context" in which "Member State" is read, and the day on which a person holds an office, are inputs too.
- **Judgments the Act leaves to the reader** ("obscure or ambiguous", "absurd", "plain intention", "materially affect", "changed in intent or become unclear or absurd", "consistently with the new enactment", "same idea", "of a continuing nature", "as occasion requires") are inputs; the encoding does not decide them.
- **The Irish-language text.** Not deposited; which text prevails is a fork (F34), not decided.
  It is a caveat about the source, not a provision, so it has no row in section 4.
- **No other Act, and no case law.**
  Every answer is from the text of this Act; the brief forbids importing an answer from another jurisdiction's law or from general knowledge of how Irish law is applied.

### 3.3 Reading a result

Most functions answer "does this section give X here?".
`FALSE` means the section does not give X; it does not mean the section forbids X.
A refusal means the text, read as it stands, does not answer; the message says what is missing.

## Re-disposition audit

Written on 2026-10-29 BEFORE any new L4 was written, and kept current as modules landed (the last update is recorded at the end of this section).
It applies the brief's rule that `inert` is allowed for three reasons only: (1) not operative; (2) machinery; (3) shown repealed or blank.
Pass 1 used reasons the brief now lists as NOT reasons ("addresses an official", "an interpretive canon", "refers to another Act not among the sources", "no input from which an answer would differ").

### Counts of the text's units

Counted from `No.-23-of-2005.txt` by a script that reads the file (sha256 `0108a07d...`) and counts one unit per heading, section, subsection, paragraph, subparagraph, defined-term entry and table row.
The script is `_work/units.py`; it was deleted with `_work/` at the end of the run, and its output is reproduced here.

| kind of unit | count |
| --- | --- |
| file header (converter notice, lines 1 to 4) | 1 |
| title block ('Number 23 of 2005' and the title), front and body | 2 |
| arrangement of sections: one entry per section | 27 |
| arrangement of sections: one entry per Part heading | 6 |
| arrangement of sections: the Schedule heading | 1 |
| arrangement of sections: the three Schedule entries (Part 1, Part 2, 'Acts Referred to') | 3 |
| 'Acts Referred to' table rows | 18 |
| long title | 1 |
| date of enactment ('[17th October, 2005]') | 1 |
| enacting formula | 1 |
| Part headings in the body | 6 |
| section headings (marginal notes) | 27 |
| subsections | 36 |
| sections with no subsections (the section is the unit) | 11 |
| s 2(1) definitions ('Act', 'enactment', 'repeal', 'statutory instrument') | 4 |
| paragraphs | 49 |
| subparagraphs | 16 |
| the two effect paragraphs (i), (ii) of s 11 | 2 |
| Schedule heading, Schedule cross-reference ('Section 21 .'), the two Schedule Part headings | 4 |
| Schedule Part 1 entries (defined terms) | 32 |
| Schedule Part 2 entries (defined terms) | 8 |
| **total units** | **256** |

Independent line-level checks, which do not use the script's state machine: 27 lines carry a section number (`N.—`); 20 lines begin `(n)` and 16 section lines open with `(1)`, which is the 36 subsections; 66 lines begin `(x)` with a letter or roman numeral, plus the one `(2) (a)` line of s 3(2)(a), which is the 67 paragraph-level units (49 paragraphs, 16 subparagraphs, 2 effect paragraphs); 44 lines begin with a curly quote, which is the 4 + 32 + 8 defined terms.

### Pass 1's table against the 256 units

- Pass 1's table had **114 rows**: 110 for text and 4 `silent` rows (the brief's questions on which the Act has no rule, which are not units of the text).
- 84 of the 110 text rows covered exactly one unit.
  26 rows covered more than one: together **167 units shared a row** with another unit (the 37 arrangement entries in one row, the 18 'Acts Referred to' rows in one, the 39 headings in one, s 3(1)(a) to (d), s 5(1)(a) to (b)(ii), s 7(1)(a) to (c), s 8, s 11, s 14(1)(a) to (c), s 14(3)(a) and (b), s 18(d)(i) and (ii), s 18(g)(i) and (ii), s 26(2)(d)(i) and (ii), the four courts, three bodies, three officers, 'oath' with 'swear', 'Companies Acts' with 'Social Welfare Acts').
- **5 units were named in no row:** the lead-in lines of s 2(1) ("In this Act"), s 17, s 18, s 26(2) and s 27(1).
  Verdicts: the s 2(1) lead-in is `inert`, reason 1 (it introduces the four definitions and states no rule of its own; each definition has its own row).
  The lead-ins of s 17, s 26(2) and s 27(1) are operative (they state the condition under which paragraphs (a) to (f) apply) and are `encoded` by the functions that already take that condition as a fact (`section 17 applies`, the `reenacted` and `the enactment has been repealed` facts of ie-repeal.l4).
  The lead-in of s 18 ("The following provisions apply to the construction of an enactment") is operative and moves to `encoded`: `the section 18 rules apply to the construction of the enactment` (ie-words-and-meaning.l4) applies s 4(1).
- **The new table has one row per unit (256 rows)**, so no row stands for more than one unit and none is left out.

### Dispositions pass 1 used that the brief does not allow

- `not applicable` (4 rows): rows 1, 2 and 5 are `inert`, reason 1 (the file header and titles, the arrangement of sections, the enacting formula); row 110 ('Acts Referred to') moves to `encoded`: the 18 rows are a table of citations and become a lookup with a test per row.
- `silent` (4 rows, 111 to 114): not text units.
  They leave the coverage table; what they said is kept under "What the text does not answer" below and in the forks they cite (F2, F5, F8, F9, F11, F29).
- 21 pass-1 rows were labelled `encoded` while also carrying a fork-register entry. In this brief a unit about which the register holds a fork is `fork`, pointing at the register entry and at the rule that encodes the chosen reading. The new table does that.

### Verdict on every pass-1 row that was not `encoded`

The 38 pass-1 `inert` rows, then the 4 `not applicable` rows and the 4 `silent` rows.
"Moves" means the unit is encoded in this pass, in the module named in the last column.

| pass-1 row | provision | pass-1 reason, in short | verdict | new module |
| --- | --- | --- | --- | --- |
| 3 | long title | purpose clause | keeps `inert`, reason 1 (long title) | none |
| 6 | Part headings, section headings, marginal notes | not part of the enactment (s 18(g)) | keeps `inert`, reason 1 (headings); the rule that they are not part of the enactment is encoded as s 18(g) | none |
| 7 | s 1(1) short title | a citation name | keeps `inert`, reason 2 (short title) | none |
| 27 | s 10 enactment always speaking | "no input varies the answer" (not a reason) | **moves to encoded** | ie-powers-duties-continuing.l4 |
| 32 | s 14(2) citation read as citation of the amended enactment | "TRUE for every input" (not a reason) | **moves** | ie-citation-and-text.l4 |
| 33 | s 14(3) commas around a year | "typographic" (not a reason) | **moves**, and a fork is found: F39 | ie-citation-and-text.l4 |
| 35 | s 15(2) Clerk endorses the date of the passing | "addresses an official" (not a reason) | **moves**: what it means for a person is that the endorsed date is part of the Act | ie-citation-and-text.l4 |
| 42 | s 18(a) singular and plural | "interpretive canon" (not a reason) | **moves** | ie-words-and-meaning.l4 |
| 45 | s 18(c) 'person' | "a widening with no varying condition" (not a reason) | **moves**, fork F42 (the list of kinds) | ie-words-and-meaning.l4 |
| 52 | s 18(j) offences by corporations | same shape as s 18(c) | **moves** | ie-words-and-meaning.l4 |
| 53 | s 19 word in a statutory instrument | "no condition or computation" (not a reason) | **moves** | ie-words-and-meaning.l4 |
| 55 | s 20(2) other parts of speech | "nothing to compute" (not a reason) | **moves** | ie-words-and-meaning.l4 |
| 58 | s 22(1) a power may be exercised from time to time | same shape as s 10 | **moves** | ie-powers-duties-continuing.l4 |
| 59 | s 22(2) a power given to an office holder | "a naming rule" (not a reason) | **moves**, fork F44 (two holders, a vacancy) | ie-powers-duties-continuing.l4 |
| 61 | s 23(1) a duty from time to time | same shape as s 10 | **moves** | ie-powers-duties-continuing.l4 |
| 62 | s 23(2) a duty on an office holder | as row 59 | **moves** | ie-powers-duties-continuing.l4 |
| 63 | s 24 rules of court | "a legal conclusion taken as an input" (not a reason) | **moves**: what it means for a person is which authority may regulate the procedure of the new jurisdiction | ie-powers-duties-continuing.l4 |
| 78 | Schedule heading and 'Section 21 .' | heading and cross-reference | keeps `inert`, reason 1 | none |
| 87 | Sch Pt 1 'affidavit' | "lexical" (not a reason) | **moves** | ie-schedule-definitions.l4 |
| 88 | 'British statute' | "a name" (not a reason) | **moves** | ie-schedule-definitions.l4 |
| 89 | 'Circuit Court', 'District Court', 'High Court', 'Supreme Court' | "names for institutions" (not a reason) | **move**, one table row each | ie-schedule-definitions.l4 |
| 90 | 'Constitution' | "a name" | **moves** | ie-schedule-definitions.l4 |
| 91 | 'Dáil Éireann', 'Seanad Éireann', 'Oireachtas' | "names for the Houses" | **move**, one row each | ie-schedule-definitions.l4 |
| 92 | 'Government', 'Minister of the Government', 'President' | "names" | **move**, fork F40 for 'President' | ie-schedule-definitions.l4 |
| 93 | 'Great Britain' | "a geographic exclusion; nothing is computed" | **moves** | ie-schedule-definitions.l4 |
| 94 | 'land' | "a classification the caller makes" (not a reason) | **moves** (the named members are the content) | ie-schedule-definitions.l4 |
| 95 | 'oath', 'swear' | "lexical" | **move** | ie-schedule-definitions.l4 |
| 96 | 'ordnance map' | "a name" | **moves** | ie-schedule-definitions.l4 |
| 97 | 'pre-union Irish statute' | "a name, with a date no rule uses" (the date is a boundary and is testable) | **moves**, fork F41 (1 January 1801) | ie-schedule-definitions.l4 |
| 98 | 'rateable valuation' | "a name for a figure from another Act" (a borrowed fact is asked as an input) | **moves** | ie-schedule-definitions.l4 |
| 99 | 'rules of court' | "the same authority as in s 24" | **moves** | ie-schedule-definitions.l4 |
| 100 | 'Saorstát Éireann statute' | "no rule turns on the difference" | **moves** | ie-schedule-definitions.l4 |
| 101 | 'statutory declaration' | "a name" | **moves** | ie-schedule-definitions.l4 |
| 102 | 'writing' | "a wide definition with no condition" | **moves** (the named modes are the content) | ie-schedule-definitions.l4 |
| 103 | Sch Pt 2 'Companies Acts', 'Social Welfare Acts' | "names for groups of Acts" | **move**, one row each | ie-schedule-definitions.l4 |
| 105 | 'functions' | "a wide definition" | **moves** | ie-schedule-definitions.l4 |
| 106 | 'Member State' | "a name" | **moves**; the context is an input | ie-schedule-definitions.l4 |
| 107 | 'Minister of State' | "a name" | **moves** | ie-schedule-definitions.l4 |
| 1 | file header and titles | `not applicable` | `inert`, reason 1 | none |
| 2 | arrangement of sections | `not applicable` | `inert`, reason 1 (a table of contents repeating marginal notes and headings) | none |
| 5 | enacting formula | `not applicable` | `inert`, reason 1 | none |
| 110 | 'Acts Referred to' table | `not applicable` | **moves to encoded**: 18 rows, a lookup with a test per row | ie-acts-referred-to.l4 |
| 111 to 114 | the four `silent` rows | questions of the brief, not text | leave the table; kept under "What the text does not answer" | none |

Also re-derived, because the brief says a borrowed fact is asked as an input and not refused:

| pass-1 row | provision | pass-1 treatment | verdict | new module |
| --- | --- | --- | --- | --- |
| 51 | s 18(i) time by reference to an hour | a bare refusal (`the clock time of a specified hour in an enactment`) | the old refusal stays (it is the answer when no offset is supplied); **a new function takes the borrowed fact** (the offset of the standard time the Standard Time (Amendment) Act 1971 fixes) as an input | ie-words-and-meaning.l4 |
| 22 | s 7(1)(a), (b), (c) | one coarse function that does not tell the three paragraphs apart | the three paragraphs are separate units and separate rules in the new module; the old function is kept and called | ie-citation-and-text.l4 |

### Totals after this pass

The coverage table in section 4 has 256 rows, one per unit.
Of the 38 pass-1 `inert` rows, 34 moved (to `encoded` or `fork`) and 4 kept `inert` (the long title; the headings and marginal notes; the short title, s 1(1), reason 2; the Schedule heading and cross-reference); the 4 `not applicable` rows became 3 `inert` (reason 1) and 1 `encoded`.
Dispositions of the 256 units: `encoded` 111, `fork` 64, `inert` reason 1 80, `inert` reason 2 1, `inert` reason 3 0, repealed or blank 0.
The table was generated from a disposition list that stops with an error if any unit has no disposition or any disposition names no unit, so no row is missing and none is invented.

### Last update

2026-10-29, after the five new modules and their five test files landed and `check.sh` was green (26 modules, 1284 satisfied, 8 failed and expected, 0 refused); after the two edits that fixed the includes lookup (finding 13, F48) the same run gives 1304 satisfied after the first edit, 1312 after the second and 1322 after the third.
Each "moves" in the verdict table above was carried out in the module named in its last column.

## 4. Coverage table

One row per unit of the text (256 rows): one per heading, section, subsection, paragraph, subparagraph, defined-term entry and table row, as counted in the audit above.
The unit label is the first words of the unit; the line is the line of `No.-23-of-2005.txt` where it begins.
Dispositions:

- `encoded`: a function or table in the module named in the last column, with tests in the file named there.
- `fork`: encoded, and the text admits another reading; the fork register (section 5) names the readings, the one taken and the text that licenses it, and the last column names the rule that carries the choice and the test that pins it.
- `inert`, with one of three reasons: 1 not operative (title, long title, enacting words, headings, date of enactment); 2 machinery (the Act's own short title); 3 text shown repealed or blank.
- `repealed or blank`: none. The text shows no repealed, blank or reserved provision, and the file's statement lists no amendment.

**Counts: 256 rows: encoded 111, fork 64, inert reason 1 80, inert reason 2 1, inert reason 3 0, repealed or blank 0.**
Every section 1 to 27 has a row for its heading and a row for each subsection and paragraph the text numbers.
Rows for the front matter come first, then the arrangement of sections, the "Acts Referred to" table, the body in order, and the Schedule.
The "where" column cites only function names and constants that exist in the named module and, for the tests, in the named test file (checked by script on 2026-10-29: 0 names missing).
A constant for a Schedule entry is reached in the tests through the lookup `the Part N entry for`, not by its own name.

| # | Unit | Line | Disposition | Where, or why |
| --- | --- | --- | --- | --- |
| 1 | HDR: converter notice, source line, language line, copyright (lines 1-4) | 1 | inert 1 | The converter's notice, source line, language line and copyright notice (lines 1 to 4) are not part of the Act. The copyright notice is copied mechanically into the header of every module that quotes the text and into SOURCE-LICENSE.md. |
| 2 | TITLE-F: Number 23 of 2005 / INTERPRETATION ACT 2005 (front) | 6 | inert 1 | The number and title of the Act: not operative. |
| 3 | Arrangement: PART1: PART 1 Preliminary and General | 11 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 4 | Arrangement: s1: 1. / Short title and commencement. | 14 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 5 | Arrangement: s2: 2. / Interpretation. | 15 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 6 | Arrangement: s3: 3. / Repeals and savings. | 16 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 7 | Arrangement: s4: 4. / Application. | 17 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 8 | Arrangement: PART2: PART 2 Miscellaneous Rules | 18 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 9 | Arrangement: s5: 5. / Construing ambiguous or obscure provisions, etc. | 20 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 10 | Arrangement: s6: 6. / Construing provisions in changing circumstances. | 21 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 11 | Arrangement: s7: 7. / Supplemental provision to sections 5 and 6. | 22 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 12 | Arrangement: s8: 8. / Reading provisions together as one and summary proceedings for ... | 23 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 13 | Arrangement: s9: 9. / References in enactments to Parts, etc. | 24 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 14 | Arrangement: s10: 10. / Enactment always speaking. | 25 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 15 | Arrangement: s11: 11. / References in enactments to examples. | 26 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 16 | Arrangement: s12: 12. / Deviation from form. | 27 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 17 | Arrangement: PART3: PART 3 Citation and Operation of Enactments | 28 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 18 | Arrangement: s13: 13. / Judicial notice. | 30 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 19 | Arrangement: s14: 14. / Citation and references to amended enactments. | 31 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 20 | Arrangement: s15: 15. / Date of passing of Acts of Oireachtas. | 32 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 21 | Arrangement: s16: 16. / Commencement. | 33 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 22 | Arrangement: s17: 17. / Exercise of statutory powers before commencement of Act. | 34 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 23 | Arrangement: PART4: PART 4 Meaning and Construction of Words and Expressions | 35 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 24 | Arrangement: s18: 18. / General rules of construction. | 37 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 25 | Arrangement: s19: 19. / Construction of statutory instruments. | 38 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 26 | Arrangement: s20: 20. / Interpretation provisions. | 39 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 27 | Arrangement: s21: 21. / Interpretation of words and expressions in Schedule. | 40 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 28 | Arrangement: PART5: PART 5 Powers and Duties | 41 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 29 | Arrangement: s22: 22. / Powers under enactments. | 43 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 30 | Arrangement: s23: 23. / Duties under enactments. | 44 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 31 | Arrangement: s24: 24. / Rules of court. | 45 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 32 | Arrangement: s25: 25. / Service by post. | 46 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 33 | Arrangement: PART6: PART 6 Amendment of Enactments, Etc. | 47 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 34 | Arrangement: s26: 26. / Repeals and substitutions. | 49 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 35 | Arrangement: s27: 27. / Effect of repeal of enactment. | 50 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 36 | Arrangement: SCHEDULE: SCHEDULE Interpretation of Particular Words and Expressions | 51 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 37 | Arrangement: SCH-PT1: PART 1 (of the Schedule) | 53 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 38 | Arrangement: SCH-PT2: PART 2 (of the Schedule) | 54 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 39 | Arrangement: SCH-ACTS: Acts Referred to | 55 | inert 1 | An entry in the arrangement of sections: a table of contents that repeats a marginal note or a Part heading, which by s 18(g) is not part of the enactment (s 18(g) is encoded: ie-operation-and-construction.l4 `the matter is taken to be part of the enactment`). |
| 40 | 'Acts Referred to' row 1: Adoption Act 1976 / 1976, No. 29 | 56 | encoded | The constant for this row and `the row of Acts Referred to for` (ie-acts-referred-to.l4). Test: tests-acts-referred-to.l4. |
| 41 | 'Acts Referred to' row 2: Adoption Acts 1952 to 1998 | 57 | encoded | The constant for this row and `the row of Acts Referred to for` (ie-acts-referred-to.l4). Test: tests-acts-referred-to.l4. |
| 42 | 'Acts Referred to' row 3: An Act for the Union of Great Britain and Ireland / 40 Geo. 3. c. 38 | 58 | encoded | The constant for this row and `the row of Acts Referred to for` (ie-acts-referred-to.l4). Test: tests-acts-referred-to.l4. |
| 43 | 'Acts Referred to' row 4: Companies Acts 1963 to 2001 | 59 | encoded | The constant for this row and `the row of Acts Referred to for` (ie-acts-referred-to.l4). Test: tests-acts-referred-to.l4. |
| 44 | 'Acts Referred to' row 5: Constitution of the Irish Free State (Saorstát Eireann) Act 1922 / ... | 60 | encoded | The constant for this row and `the row of Acts Referred to for` (ie-acts-referred-to.l4). Test: tests-acts-referred-to.l4. |
| 45 | 'Acts Referred to' row 6: Interpretation Act 1889 / 52 & 53 Vict. c. 63 | 61 | encoded | The constant for this row and `the row of Acts Referred to for` (ie-acts-referred-to.l4). Test: tests-acts-referred-to.l4. |
| 46 | 'Acts Referred to' row 7: Interpretation Act 1923 / 1923, No. 63 | 62 | encoded | The constant for this row and `the row of Acts Referred to for` (ie-acts-referred-to.l4). Test: tests-acts-referred-to.l4. |
| 47 | 'Acts Referred to' row 8: Interpretation Act 1937 / 1937, No. 38 | 63 | encoded | The constant for this row and `the row of Acts Referred to for` (ie-acts-referred-to.l4). Test: tests-acts-referred-to.l4. |
| 48 | 'Acts Referred to' row 9: Interpretation (Amendment) Act 1993 / 1993, No. 35 | 64 | encoded | The constant for this row and `the row of Acts Referred to for` (ie-acts-referred-to.l4). Test: tests-acts-referred-to.l4. |
| 49 | 'Acts Referred to' row 10: Ministers and Secretaries (Amendment) (No. 2) Act 1977 / 1977, No. 28 | 65 | encoded | The constant for this row and `the row of Acts Referred to for` (ie-acts-referred-to.l4). Test: tests-acts-referred-to.l4. |
| 50 | 'Acts Referred to' row 11: Organisation of Working Time Act 1997 / 1997, No. 20 | 66 | encoded | The constant for this row and `the row of Acts Referred to for` (ie-acts-referred-to.l4). Test: tests-acts-referred-to.l4. |
| 51 | 'Acts Referred to' row 12: Social Welfare Acts | 67 | encoded | The constant for this row and `the row of Acts Referred to for` (ie-acts-referred-to.l4). Test: tests-acts-referred-to.l4. |
| 52 | 'Acts Referred to' row 13: Social Welfare (Consolidation) Act 1993 / 1993, No. 27 | 68 | encoded | The constant for this row and `the row of Acts Referred to for` (ie-acts-referred-to.l4). Test: tests-acts-referred-to.l4. |
| 53 | 'Acts Referred to' row 14: Standard Time (Amendment) Act 1971 / 1971, No. 17 | 69 | encoded | The constant for this row and `the row of Acts Referred to for` (ie-acts-referred-to.l4). Test: tests-acts-referred-to.l4. |
| 54 | 'Acts Referred to' row 15: Status of Children Act 1987 / 1987, No. 26 | 70 | encoded | The constant for this row and `the row of Acts Referred to for` (ie-acts-referred-to.l4). Test: tests-acts-referred-to.l4. |
| 55 | 'Acts Referred to' row 16: Statutory Declarations Act 1938 / 1938, No. 37 | 71 | encoded | The constant for this row and `the row of Acts Referred to for` (ie-acts-referred-to.l4). Test: tests-acts-referred-to.l4. |
| 56 | 'Acts Referred to' row 17: Survey (Ireland) Acts 1825 to 1870 | 72 | encoded | The constant for this row and `the row of Acts Referred to for` (ie-acts-referred-to.l4). Test: tests-acts-referred-to.l4. |
| 57 | 'Acts Referred to' row 18: Valuation Act 2001 / 2001, No. 13 | 73 | encoded | The constant for this row and `the row of Acts Referred to for` (ie-acts-referred-to.l4). Test: tests-acts-referred-to.l4. |
| 58 | TITLE-B: Number 23 of 2005 / INTERPRETATION ACT 2005 (body) | 75 | inert 1 | The number and title of the Act: not operative. |
| 59 | LONGTITLE: AN ACT RESPECTING THE INTERPRETATION AND APPLICATION OF ACTS AND OF ... | 79 | inert 1 | The long title states the Act's purpose and creates no rule. |
| 60 | DATELINE: [17th October, 2005] | 80 | encoded | `the facts about this Act` (ie-interpretation-time.l4): the date of the passing of this Act, 17 October 2005, as s 15(2) places it after the long title. Tests: tests-commencement.l4, tests-operation.l4. |
| 61 | ENACTING: BE IT ENACTED BY THE OIREACHTAS AS FOLLOWS: | 81 | inert 1 | The enacting words. |
| 62 | PART1: PART 1 Preliminary and General | 82 | inert 1 | A Part heading: not part of the enactment (s 18(g)). |
| 63 | s 1 heading: Short title and commencement | 83 | inert 1 | A marginal note: not part of the enactment (s 18(g)). |
| 64 | s 1(1): (1) This Act may be cited as the Interpretation Act 2005. | 83 | inert 2 | Machinery: the short title. (Citing an Act by its short title, s 14(1)(a), is encoded separately.) |
| 65 | s 1(2): (2) This Act comes into operation on 1 January 2006. | 84 | encoded | `the facts about this Act` (ie-interpretation-time.l4) with s 16(2): in operation at the end of 31 December 2005. Tests: tests-commencement.l4, tests-operation.l4, tests-repeal.l4. |
| 66 | s 2 heading: Interpretation | 85 | inert 1 | A marginal note: not part of the enactment (s 18(g)). |
| 67 | s 2(1): (1) In this Act— | 85 | inert 1 | The lead-in 'In this Act' introduces the four definitions below; each definition has its own row. |
| 68 | s 2(1)"Act": “Act” means— | 86 | encoded | `is an Act` (ie-general.l4). Test: tests-general.l4. |
| 69 | s 2(1)(a): (a) an Act of the Oireachtas, and | 87 | encoded | `is an Act` (ie-general.l4). Test: tests-general.l4. |
| 70 | s 2(1)(b): (b) a statute which was in force in Saorstát Éireann immediately ... | 88 | encoded | `is an Act` (ie-general.l4). Test: tests-general.l4. |
| 71 | s 2(1)"enactment": “enactment” means an Act or a statutory instrument or any portion of ... | 89 | encoded | `is an enactment` (ie-general.l4). Test: tests-general.l4. |
| 72 | s 2(1)"repeal": “repeal” includes revoke, rescind, abrogate or cancel; | 90 | fork | F18 (open list). `the word is a repeal within the Act` (ie-general.l4); a word outside the five refuses. Test: tests-general.l4, tests-red-control.l4. |
| 73 | s 2(1)"statutory instrument": “statutory instrument” means an order, regulation, rule, bye-law, ... | 91 | encoded | `is a statutory instrument` (ie-general.l4). Test: tests-general.l4. |
| 74 | s 2(2): (2) For the purposes of this Act, an enactment which has been ... | 92 | encoded | `for the purposes of this Act the enactment is deemed to have been repealed` (ie-repeal.l4). Test: tests-repeal.l4. |
| 75 | s 3 heading: Repeals and savings | 93 | inert 1 | A marginal note: not part of the enactment (s 18(g)). |
| 76 | s 3(1): (1) The following Acts are repealed: | 93 | fork | F31 (when the four Acts are repealed). `section 3(1) lists the Act`, `section 3(1) has repealed the Act by the end of` (ie-repeal.l4). Test: tests-repeal.l4. |
| 77 | s 3(1)(a): (a) the Interpretation Act 1889; | 94 | fork | F31 (when the four Acts are repealed). `section 3(1) lists the Act`, `section 3(1) has repealed the Act by the end of` (ie-repeal.l4). Test: tests-repeal.l4. |
| 78 | s 3(1)(b): (b) the Interpretation Act 1923 ; | 95 | fork | F31 (when the four Acts are repealed). `section 3(1) lists the Act`, `section 3(1) has repealed the Act by the end of` (ie-repeal.l4). Test: tests-repeal.l4. |
| 79 | s 3(1)(c): (c) the Interpretation Act 1937 ; | 96 | fork | F31 (when the four Acts are repealed). `section 3(1) lists the Act`, `section 3(1) has repealed the Act by the end of` (ie-repeal.l4). Test: tests-repeal.l4. |
| 80 | s 3(1)(d): (d) the Interpretation (Amendment) Act 1993 . | 97 | fork | F31 (when the four Acts are repealed). `section 3(1) lists the Act`, `section 3(1) has repealed the Act by the end of` (ie-repeal.l4). Test: tests-repeal.l4. |
| 81 | s 3(2): (2) (a) The repeal by this Act of an Act which assigns a meaning to a ... | 98 | fork | F33 (one limb or both). `the repeal does not affect the meaning assigned` (ie-repeal.l4). Test: tests-repeal.l4. |
| 82 | s 3(2)(a): (a) The repeal by this Act of an Act which assigns a meaning to a ... | 98 | fork | F33 (one limb or both). `the repeal does not affect the meaning assigned` (ie-repeal.l4). Test: tests-repeal.l4. |
| 83 | s 3(2)(a)(i): (i) in the absence of that meaning in this Act, or | 99 | fork | F33 (one limb or both). `the repeal does not affect the meaning assigned` (ie-repeal.l4). Test: tests-repeal.l4. |
| 84 | s 3(2)(a)(ii): (ii) by the application to the other enactment of the meaning ... | 100 | fork | F33 (one limb or both). `the repeal does not affect the meaning assigned` (ie-repeal.l4). Test: tests-repeal.l4. |
| 85 | s 3(2)(b): (b) The repeal by this Act of an Act which provides for any matter ... | 102 | fork | F33 (one limb or both). `the repeal does not affect the matter provided for` (ie-repeal.l4). Test: tests-repeal.l4. |
| 86 | s 3(2)(b)(i): (i) in the absence of that matter being provided for in this Act, or | 103 | fork | F33 (one limb or both). `the repeal does not affect the matter provided for` (ie-repeal.l4). Test: tests-repeal.l4. |
| 87 | s 3(2)(b)(ii): (ii) by the application to the other enactment of a matter provided ... | 104 | fork | F33 (one limb or both). `the repeal does not affect the matter provided for` (ie-repeal.l4). Test: tests-repeal.l4. |
| 88 | s 4 heading: Application | 106 | inert 1 | A marginal note: not part of the enactment (s 18(g)). |
| 89 | s 4(1): (1) A provision of this Act applies to an enactment except in so far ... | 106 | fork | F17 (stated once, as a precondition). `a provision of this Act applies to an enactment` (ie-general.l4). Test: tests-general.l4. |
| 90 | s 4(2): (2) The provisions of this Act which relate to other Acts also apply ... | 107 | encoded | `a provision of this Act that relates to other Acts applies also to this Act` (ie-general.l4). Test: tests-general.l4. |
| 91 | PART2: PART 2 Miscellaneous Rules | 108 | inert 1 | A Part heading: not part of the enactment (s 18(g)). |
| 92 | s 5 heading: Construing ambiguous or obscure provisions, etc | 109 | inert 1 | A marginal note: not part of the enactment (s 18(g)). |
| 93 | s 5(1): (1) In construing a provision of any Act (other than a provision that ... | 109 | encoded | `what section 5 directs about` (ie-general.l4); whose intention follows the kind of Act (limbs (i), (ii)) or the maker (s 5(2)); a penal or other sanction takes the provision out. Test: tests-general.l4. |
| 94 | s 5(1)(a): (a) that is obscure or ambiguous, or | 110 | encoded | `what section 5 directs about` (ie-general.l4); whose intention follows the kind of Act (limbs (i), (ii)) or the maker (s 5(2)); a penal or other sanction takes the provision out. Test: tests-general.l4. |
| 95 | s 5(1)(b): (b) that on a literal interpretation would be absurd or would fail to ... | 111 | encoded | `what section 5 directs about` (ie-general.l4); whose intention follows the kind of Act (limbs (i), (ii)) or the maker (s 5(2)); a penal or other sanction takes the provision out. Test: tests-general.l4. |
| 96 | s 5(1)(b)(i): (i) in the case of an Act to which paragraph (a) of the definition of ... | 112 | encoded | `what section 5 directs about` (ie-general.l4); whose intention follows the kind of Act (limbs (i), (ii)) or the maker (s 5(2)); a penal or other sanction takes the provision out. Test: tests-general.l4. |
| 97 | s 5(1)(b)(ii): (ii) in the case of an Act to which paragraph (b) of that definition ... | 113 | encoded | `what section 5 directs about` (ie-general.l4); whose intention follows the kind of Act (limbs (i), (ii)) or the maker (s 5(2)); a penal or other sanction takes the provision out. Test: tests-general.l4. |
| 98 | s 5(2): (2) In construing a provision of a statutory instrument (other than a ... | 115 | encoded | `what section 5 directs about` (ie-general.l4); whose intention follows the kind of Act (limbs (i), (ii)) or the maker (s 5(2)); a penal or other sanction takes the provision out. Test: tests-general.l4. |
| 99 | s 5(2)(a): (a) that is obscure or ambiguous, or | 116 | encoded | `what section 5 directs about` (ie-general.l4); whose intention follows the kind of Act (limbs (i), (ii)) or the maker (s 5(2)); a penal or other sanction takes the provision out. Test: tests-general.l4. |
| 100 | s 5(2)(b): (b) that on a literal interpretation would be absurd or would fail to ... | 117 | encoded | `what section 5 directs about` (ie-general.l4); whose intention follows the kind of Act (limbs (i), (ii)) or the maker (s 5(2)); a penal or other sanction takes the provision out. Test: tests-general.l4. |
| 101 | s 6 heading: Construing provisions in changing circumstances | 119 | inert 1 | A marginal note: not part of the enactment (s 18(g)). |
| 102 | s 6: In construing a provision of any Act or statutory instrument, a court ... | 119 | fork | F27 (a change on the very day). `a court may make allowance for the change in construing the provision` (ie-general.l4). Test: tests-general.l4. |
| 103 | s 7 heading: Supplemental provision to sections 5 and 6 | 120 | inert 1 | A marginal note: not part of the enactment (s 18(g)). |
| 104 | s 7(1): (1) In construing a provision of an Act for the purposes of section 5 ... | 120 | fork | F30 (an instrument), F45 (paragraphs (b), (c)). `section 7(1) lets a court make use of the matter notwithstanding section 18(g)` (ie-general.l4); the three paragraphs are told apart in ie-citation-and-text.l4. Test: tests-general.l4, tests-citation-and-text.l4. |
| 105 | s 7(1)(a): (a) in the case of an Act of the Oireachtas, the signed text of such ... | 121 | encoded | `the text that section 7(1)(a) names` (ie-citation-and-text.l4). Test: tests-citation-and-text.l4. |
| 106 | s 7(1)(b): (b) in the case of an Act of the Oireachtas of Saorstát Éireann, the ... | 122 | fork | F45 (both map to limb (b) of 'Act' in s 2(1)). `the text that section 7(1)(b) names`, `the text that section 7(1)(c) names` (ie-citation-and-text.l4). Test: tests-citation-and-text.l4. |
| 107 | s 7(1)(c): (c) in the case of any other Act, such text of that Act as ... | 123 | fork | F45 (both map to limb (b) of 'Act' in s 2(1)). `the text that section 7(1)(b) names`, `the text that section 7(1)(c) names` (ie-citation-and-text.l4). Test: tests-citation-and-text.l4. |
| 108 | s 7(2): (2) For the purposes of subsection (1), it shall be presumed, until ... | 124 | encoded | `it is presumed that the copy is a copy of the text to which section 7(1) relates` (ie-general.l4). Test: tests-general.l4. |
| 109 | s 8 heading: Reading provisions together as one and summary proceedings for ... | 125 | inert 1 | A marginal note: not part of the enactment (s 18(g)). |
| 110 | s 8: Where— | 125 | encoded | `section 8 lets the specified person bring summary proceedings for the offence` (ie-general.l4). Test: tests-general.l4. |
| 111 | s 8(a): (a) an Act or portion of an Act (whenever passed)— | 126 | encoded | `section 8 lets the specified person bring summary proceedings for the offence` (ie-general.l4). Test: tests-general.l4. |
| 112 | s 8(a)(i): (i) provides that summary proceedings for offences under it may be ... | 127 | encoded | `section 8 lets the specified person bring summary proceedings for the offence` (ie-general.l4). Test: tests-general.l4. |
| 113 | s 8(a)(ii): (ii) is subsequently read together as one with any provision of ... | 128 | encoded | `section 8 lets the specified person bring summary proceedings for the offence` (ie-general.l4). Test: tests-general.l4. |
| 114 | s 8(b): (b) an offence is created under that provision which can be ... | 130 | encoded | `section 8 lets the specified person bring summary proceedings for the offence` (ie-general.l4). Test: tests-general.l4. |
| 115 | s 9 heading: References in enactments to Parts, etc | 132 | inert 1 | A marginal note: not part of the enactment (s 18(g)). |
| 116 | s 9(1): (1) A reference in an enactment to a Part, Chapter, section, Schedule ... | 132 | encoded | `a reference to a division is read as a reference to a division of` (ie-general.l4); 'other division, by whatever name called' is an open case that refuses. Test: tests-general.l4. |
| 117 | s 9(2): (2) A reference in an enactment to a subsection, paragraph, ... | 133 | encoded | `a reference to a division is read as a reference to a division of` (ie-general.l4); 'other division, by whatever name called' is an open case that refuses. Test: tests-general.l4. |
| 118 | s 10 heading: Enactment always speaking | 134 | inert 1 | A marginal note: not part of the enactment (s 18(g)). |
| 119 | s 10: An enactment continues to have effect and may be applied from time to ... | 134 | encoded | `an enactment may be applied on the occasion` (ie-powers-duties-continuing.l4). Test: tests-powers-duties.l4. |
| 120 | s 11 heading: References in enactments to examples | 135 | inert 1 | A marginal note: not part of the enactment (s 18(g)). |
| 121 | s 11: If under the heading— | 135 | encoded | `the effect of an example under the heading`, `the heading is one the section names` (ie-general.l4). Test: tests-general.l4. |
| 122 | s 11(a): (a) in the Irish language “Sampla” or “Samplaí”, or | 136 | encoded | `the effect of an example under the heading`, `the heading is one the section names` (ie-general.l4). Test: tests-general.l4. |
| 123 | s 11(b): (b) in the English language “Example” or “Examples”, | 137 | encoded | `the effect of an example under the heading`, `the heading is one the section names` (ie-general.l4). Test: tests-general.l4. |
| 124 | s 11(i): (i) is not to be read as exhaustive of the provision, and | 139 | encoded | `the effect of an example under the heading`, `the heading is one the section names` (ie-general.l4). Test: tests-general.l4. |
| 125 | s 11(ii): (ii) may extend, but does not limit, the meaning of the provision. | 140 | encoded | `the effect of an example under the heading`, `the heading is one the section names` (ie-general.l4). Test: tests-general.l4. |
| 126 | s 12 heading: Deviation from form | 141 | inert 1 | A marginal note: not part of the enactment (s 18(g)). |
| 127 | s 12: Where a form is prescribed in or under an enactment, a deviation from ... | 141 | fork | F19 ('or' read literally). `section 12 saves the form used` (ie-general.l4). Test: tests-general.l4, tests-red-control.l4. |
| 128 | PART3: PART 3 Citation and Operation of Enactments | 142 | inert 1 | A Part heading: not part of the enactment (s 18(g)). |
| 129 | s 13 heading: Judicial notice | 143 | inert 1 | A marginal note: not part of the enactment (s 18(g)). |
| 130 | s 13: An Act is a public document and shall be judicially noticed. | 143 | fork | F30 (an instrument). `it is a public document that shall be judicially noticed` (ie-general.l4). Test: tests-general.l4. |
| 131 | s 14 heading: Citation and references to amended enactments | 144 | inert 1 | A marginal note: not part of the enactment (s 18(g)). |
| 132 | s 14(1): (1) An Act may be cited in any enactment or other document— | 144 | fork | F20 (the session). `section 14(1) lets an Act be cited` (ie-general.l4). Test: tests-general.l4. |
| 133 | s 14(1)(a): (a) by the long title or short title of the Act, | 145 | encoded | `section 14(1) lets an Act be cited` (ie-general.l4); the Act's own table of citations is ie-acts-referred-to.l4. Test: tests-general.l4, tests-acts-referred-to.l4. |
| 134 | s 14(1)(b): (b) where appropriate, by the consecutive number of the Act in the ... | 146 | encoded | `section 14(1) lets an Act be cited` (ie-general.l4); the Act's own table of citations is ie-acts-referred-to.l4. Test: tests-general.l4, tests-acts-referred-to.l4. |
| 135 | s 14(1)(c): (c) where the Act was passed prior to the enactment of the ... | 147 | fork | F20 (the session). `section 14(1) lets an Act be cited` (ie-general.l4). Test: tests-general.l4. |
| 136 | s 14(2): (2) A citation of or a reference to an enactment shall be read as a ... | 148 | encoded | `a citation of or reference to an enactment is read as a citation of or reference to the enactment as changed` (ie-citation-and-text.l4). Test: tests-citation-and-text.l4. |
| 137 | s 14(3): (3) In citing— | 149 | fork | F39 (which commas the qualifier governs). `section 14(3) lets the comma be omitted` (ie-citation-and-text.l4). Test: tests-citation-and-text.l4. |
| 138 | s 14(3)(a): (a) an Act by its short title, or | 150 | fork | F39 (which commas the qualifier governs). `section 14(3) lets the comma be omitted` (ie-citation-and-text.l4). Test: tests-citation-and-text.l4. |
| 139 | s 14(3)(b): (b) any other enactment by its citation (if any), | 151 | fork | F39 (which commas the qualifier governs). `section 14(3) lets the comma be omitted` (ie-citation-and-text.l4). Test: tests-citation-and-text.l4. |
| 140 | s 15 heading: Date of passing of Acts of Oireachtas | 153 | inert 1 | A marginal note: not part of the enactment (s 18(g)). |
| 141 | s 15(1): (1) The date of the passing of an Act of the Oireachtas is the date ... | 153 | fork | F15 (passed or published), F16 (a Saorstat Eireann statute). `the date of the passing of an Act of the Oireachtas signed on` (ie-interpretation-time.l4). Test: tests-commencement.l4. |
| 142 | s 15(2): (2) Immediately after the Bill for an Act of the Oireachtas is signed ... | 154 | fork | F43 ('immediately'). `the date the Clerk of Dail Eireann must endorse on the Act`, `the endorsed date is taken to be part of the Act`, `the latest moment by which the Clerk of Dail Eireann must have endorsed the date` (ie-citation-and-text.l4). Test: tests-citation-and-text.l4. |
| 143 | s 16 heading: Commencement | 155 | inert 1 | A marginal note: not part of the enactment (s 18(g)). |
| 144 | s 16(1): (1) Subject to subsection (2), every provision of an Act comes into ... | 155 | fork | F11 (no moment), F16. `the commencement of`, `the moment at which the enactment comes into operation` (ie-interpretation-time.l4), which call the helpers named section 16(1) commencement and the commencement of an Act. Test: tests-commencement.l4, tests-worked-cases.l4. |
| 145 | s 16(2): (2) Where an Act or a provision of an Act is expressed to come into ... | 156 | fork | F12 (a day to be fixed), F9. `the commencement of`, `the moment at which the enactment comes into operation` (ie-interpretation-time.l4), which call the helper named section 16(2) commencement. Test: tests-commencement.l4, tests-worked-cases.l4. |
| 146 | s 16(3): (3) Subject to subsection (4), every provision of a statutory ... | 157 | fork | F13, F9. `the commencement of`, `the moment at which the enactment comes into operation` (ie-interpretation-time.l4), which call the helper named section 16(3) commencement. Test: tests-commencement.l4, tests-worked-cases.l4. |
| 147 | s 16(4): (4) Where a statutory instrument or a provision of a statutory ... | 158 | fork | F14, F9. `the commencement of`, `the moment at which the enactment comes into operation` (ie-interpretation-time.l4), which call the helper named section 16(4) commencement. Test: tests-commencement.l4. |
| 148 | s 17 heading: Exercise of statutory powers before commencement of Act | 159 | inert 1 | A marginal note: not part of the enactment (s 18(g)). |
| 149 | s 17: Where an Act or a provision of an Act is expressed to come into ... | 159 | encoded | `section 17 applies` (ie-operation-and-construction.l4): the day expressed is subsequent to the date of the passing. Test: tests-operation.l4. |
| 150 | s 17(a): (a) if the day on which the Act or the provision comes into operation ... | 160 | fork | F28 (a thing done on the day of the passing). `the instrument, act or thing that fixes the day may be made or done on`, `the power to make a statutory instrument or do an act or thing may be exercised on` (ie-operation-and-construction.l4). Test: tests-operation.l4. |
| 151 | s 17(b): (b) if, for the purposes of the Act or the provision, the Act confers ... | 161 | fork | F28 (a thing done on the day of the passing). `the instrument, act or thing that fixes the day may be made or done on`, `the power to make a statutory instrument or do an act or thing may be exercised on` (ie-operation-and-construction.l4). Test: tests-operation.l4. |
| 152 | PART4: PART 4 Meaning and Construction of Words and Expressions | 162 | inert 1 | A Part heading: not part of the enactment (s 18(g)). |
| 153 | s 18 heading: General rules of construction | 163 | inert 1 | A marginal note: not part of the enactment (s 18(g)). |
| 154 | s 18: The following provisions apply to the construction of an enactment: | 163 | encoded | `the section 18 rules apply to the construction of the enactment` (ie-words-and-meaning.l4), which applies s 4(1). Test: tests-words-and-meaning.l4. |
| 155 | s 18(a): (a) Singular and plural. A word importing the singular shall be read ... | 164 | encoded | `the numbers a word is read as importing`, `a word importing ... is read as also importing` (ie-words-and-meaning.l4). Test: tests-words-and-meaning.l4. |
| 156 | s 18(b): (b) Gender. | 165 | encoded | `a word importing the ... gender is read as also importing the other gender in an enactment of kind` (ie-operation-and-construction.l4). Test: tests-operation.l4. |
| 157 | s 18(b)(i): (i) A word importing the masculine gender shall be read as also ... | 166 | encoded | `a word importing the ... gender is read as also importing the other gender in an enactment of kind` (ie-operation-and-construction.l4). Test: tests-operation.l4. |
| 158 | s 18(b)(ii): (ii) In an Act passed on or after 22 December 1993, and in a ... | 167 | fork | F21 ('on or after' for an Act, 'after' for an instrument). `a word importing the ... gender is read as also importing the other gender in an enactment of kind` (ie-operation-and-construction.l4). Test: tests-operation.l4, tests-red-control.l4. |
| 159 | s 18(c): (c) Person. “Person” shall be read as importing a body corporate ... | 168 | fork | F42 (the list of kinds is not closed). `the word person is read as importing`, `a pronoun used in place of person is read as importing` (ie-words-and-meaning.l4). Test: tests-words-and-meaning.l4. |
| 160 | s 18(d): (d) Adopted child. A reference, however expressed, to a child of a ... | 169 | fork | F22. `a reference to a child of the person includes the adopted child` (ie-operation-and-construction.l4). Test: tests-operation.l4. |
| 161 | s 18(d)(i): (i) in an Act passed after the passing of the Adoption Act 1976 a ... | 170 | fork | F22 ('a child to whom subparagraph (i) relates'). `a reference to a child of the person includes the adopted child` (ie-operation-and-construction.l4). Test: tests-operation.l4. |
| 162 | s 18(d)(ii): (ii) in an Act passed on or after 14 January 1988 (the commencement ... | 171 | fork | F22 ('a child to whom subparagraph (i) relates'). `a reference to a child of the person includes the adopted child` (ie-operation-and-construction.l4). Test: tests-operation.l4. |
| 163 | s 18(e): (e) Distance. A word or expression relating to the distance between ... | 172 | fork | F32 (the horizontal projection). `the distance between ... within the meaning of section 18(e)` (ie-operation-and-construction.l4). Test: tests-operation.l4. |
| 164 | s 18(f): (f) Series description. Where a consecutive series is described by ... | 173 | encoded | `the number ... is a member of the series from`, `the number of members of the series from` (ie-operation-and-construction.l4). Test: tests-operation.l4. |
| 165 | s 18(g): (g) Marginal and shoulder notes, etc. Subject to section 7, none of ... | 174 | encoded | `the matter is taken to be part of the enactment`, `the matter may be construed or judicially noticed in construing the enactment` (ie-operation-and-construction.l4), subject to s 7. Test: tests-operation.l4. |
| 166 | s 18(g)(i): (i) a marginal note placed at the side, or a shoulder note placed at ... | 175 | encoded | `the matter is taken to be part of the enactment`, `the matter may be construed or judicially noticed in construing the enactment` (ie-operation-and-construction.l4), subject to s 7. Test: tests-operation.l4. |
| 167 | s 18(g)(ii): (ii) a heading or cross-line placed in or at the head of or at the ... | 176 | encoded | `the matter is taken to be part of the enactment`, `the matter may be construed or judicially noticed in construing the enactment` (ie-operation-and-construction.l4), subject to s 7. Test: tests-operation.l4. |
| 168 | s 18(h): (h) Periods of time. Where a period of time is expressed to begin on ... | 177 | fork | F1 to F8 (counting, months and years, weeks, rest days). `the last day of a period of` ... (ie-interpretation-time.l4); the alternative readings, which are not the Act's, are in ie-month-year-readings.l4. Test: tests-periods.l4, tests-rest-days-and-words.l4, tests-commencement.l4, tests-worked-cases.l4, tests-readings.l4. |
| 169 | s 18(i): (i) Time. Where time is expressed by reference to a specified hour or ... | 178 | fork | F38 (the borrowed Act). `the clock time of a specified hour in an enactment` (ie-interpretation-time.l4) refuses when no offset is supplied; `the moment in UTC of a time expressed by reference to a specified hour` (ie-words-and-meaning.l4) takes the 1971 Act's offset as an input. Test: tests-rest-days-and-words.l4, tests-words-and-meaning.l4. |
| 170 | s 18(j): (j) Offences by corporations. A reference to a person in relation to ... | 179 | fork | F46 ('whether punishable on indictment or on summary conviction'). `section 18(j) reads the reference as including a body corporate` (ie-words-and-meaning.l4). Test: tests-words-and-meaning.l4. |
| 171 | s 19 heading: Construction of statutory instruments | 180 | inert 1 | A marginal note: not part of the enactment (s 18(g)). |
| 172 | s 19: A word or expression used in a statutory instrument has the same ... | 180 | encoded | `the meaning in the statutory instrument of a word` (ie-words-and-meaning.l4), subject to s 4(1). Test: tests-words-and-meaning.l4. |
| 173 | s 20 heading: Interpretation provisions | 181 | inert 1 | A marginal note: not part of the enactment (s 18(g)). |
| 174 | s 20(1): (1) Where an enactment contains a definition or other interpretation ... | 181 | encoded | `the definition or interpretation provision is read as applicable` (ie-operation-and-construction.l4). Test: tests-operation.l4. |
| 175 | s 20(1)(a): (a) the enactment itself, or | 182 | encoded | `the definition or interpretation provision is read as applicable` (ie-operation-and-construction.l4). Test: tests-operation.l4. |
| 176 | s 20(1)(b): (b) the Act under which the enactment is made. | 183 | encoded | `the definition or interpretation provision is read as applicable` (ie-operation-and-construction.l4). Test: tests-operation.l4. |
| 177 | s 20(2): (2) Where an enactment defines or otherwise interprets a word or ... | 184 | encoded | `section 20(2) gives the form a corresponding meaning` (ie-words-and-meaning.l4). Test: tests-words-and-meaning.l4. |
| 178 | s 21 heading: Interpretation of words and expressions in Schedule | 185 | inert 1 | A marginal note: not part of the enactment (s 18(g)). |
| 179 | s 21(1): (1) In an enactment, a word or expression to which a particular ... | 185 | encoded | `section 21(1) gives the Part 1 word its meaning in the enactment` (ie-schedule-definitions.l4), with the table `the Part 1 entry for`; subject to s 4(1). Test: tests-schedule-definitions.l4. |
| 180 | s 21(2): (2) In an enactment which comes into operation after the commencement ... | 186 | fork | F23 ('after' is strict). `Part 2 of the Schedule applies to the enactment` (ie-operation-and-construction.l4), which calls the function named the enactment comes into operation after the commencement of this Act; `section 21(2) gives the Part 2 word its meaning in the enactment` (ie-schedule-definitions.l4). Test: tests-operation.l4, tests-schedule-definitions.l4, tests-red-control.l4. |
| 181 | PART5: PART 5 Powers and Duties | 187 | inert 1 | A Part heading: not part of the enactment (s 18(g)). |
| 182 | s 22 heading: Powers under enactments | 188 | inert 1 | A marginal note: not part of the enactment (s 18(g)). |
| 183 | s 22(1): (1) A power conferred by an enactment may be exercised from time to ... | 188 | encoded | `a power conferred by an enactment may be exercised on the occasion` (ie-powers-duties-continuing.l4). Test: tests-powers-duties.l4. |
| 184 | s 22(2): (2) A power conferred by an enactment on the holder of an office as ... | 189 | fork | F44 (two holders, a vacancy). `the holder for the time being of the office on`, `the person may exercise the power on` (ie-powers-duties-continuing.l4). Test: tests-powers-duties.l4. |
| 185 | s 22(3): (3) A power conferred by an enactment to make a statutory instrument ... | 190 | encoded | `a power to make a statutory instrument is read as including the power` (ie-powers-and-service.l4). Test: tests-powers-service.l4. |
| 186 | s 23 heading: Duties under enactments | 191 | inert 1 | A marginal note: not part of the enactment (s 18(g)). |
| 187 | s 23(1): (1) A duty imposed by an enactment shall be performed from time to ... | 191 | encoded | `a duty imposed by an enactment shall be performed on the occasion` (ie-powers-duties-continuing.l4). Test: tests-powers-duties.l4. |
| 188 | s 23(2): (2) A duty imposed by an enactment on the holder of an office as that ... | 192 | fork | F44 (two holders, a vacancy). `the holder for the time being of the office, for a duty, on`, `the person shall perform the duty on` (ie-powers-duties-continuing.l4). Test: tests-powers-duties.l4. |
| 189 | s 24 heading: Rules of court | 193 | inert 1 | A marginal note: not part of the enactment (s 18(g)). |
| 190 | s 24: Where an enactment confers a new jurisdiction on a court or extends ... | 193 | encoded | `the authority has power to make rules or orders for the practice and procedure of the court in the exercise of the jurisdiction, as conferred, extended or varied` (ie-powers-duties-continuing.l4). Test: tests-powers-duties.l4. |
| 191 | s 25 heading: Service by post | 194 | inert 1 | A marginal note: not part of the enactment (s 18(g)). |
| 192 | s 25: Where an enactment authorises or requires a document to be served by ... | 194 | fork | F29 (time zone; 'unless the contrary is proved'). `service by post may be effected under section 25`, `the time at which service is deemed to have been effected`, `the date in UTC on which service is deemed to have been effected` (ie-powers-and-service.l4). Test: tests-powers-service.l4. |
| 193 | PART6: PART 6 Amendment of Enactments, Etc. | 195 | inert 1 | A Part heading: not part of the enactment (s 18(g)). |
| 194 | s 26 heading: Repeals and substitutions | 196 | inert 1 | A marginal note: not part of the enactment (s 18(g)). |
| 195 | s 26(1): (1) Where an enactment repeals another enactment and substitutes ... | 196 | fork | F25 (until when). `the repealed enactment is in force throughout` (ie-repeal.l4). Test: tests-repeal.l4. |
| 196 | s 26(2): (2) Where an enactment (“former enactment”) is repealed and ... | 197 | encoded | The lead-in is the condition shared by paragraphs (a) to (f): the `reenacted` fact of each function (ie-repeal.l4). Test: tests-repeal.l4. |
| 197 | s 26(2)(a): (a) a person appointed under the former enactment shall continue to ... | 198 | encoded | `a person appointed under the former enactment continues to act on` (ie-repeal.l4). Test: tests-repeal.l4. |
| 198 | s 26(2)(b): (b) a bond, guarantee or other security of a continuing nature given ... | 199 | encoded | `the security remains in force`, `the data, books, papers, forms and things may continue to be used` (ie-repeal.l4). Test: tests-repeal.l4. |
| 199 | s 26(2)(c): (c) proceedings taken under the former enactment may, subject to ... | 200 | fork | F26 (how s 27(1) limits the continuation). `the proceedings may be continued under the new enactment` (ie-repeal.l4). Test: tests-repeal.l4. |
| 200 | s 26(2)(d): (d) if after the commencement of this Act— | 201 | encoded | `what paragraph (d) does to the instrument` (ie-repeal.l4), which calls the function named the enactment comes into operation after the commencement of this Act (ie-operation-and-construction.l4). Test: tests-repeal.l4. |
| 201 | s 26(2)(d)(i): (i) any provision of a former enactment, that provided for the making ... | 202 | encoded | `what paragraph (d) does to the instrument` (ie-repeal.l4), which calls the function named the enactment comes into operation after the commencement of this Act (ie-operation-and-construction.l4). Test: tests-repeal.l4. |
| 202 | s 26(2)(d)(ii): (ii) such statutory instrument is in force immediately before such ... | 203 | encoded | `what paragraph (d) does to the instrument` (ie-repeal.l4), which calls the function named the enactment comes into operation after the commencement of this Act (ie-operation-and-construction.l4). Test: tests-repeal.l4. |
| 203 | s 26(2)(e): (e) to the extent that the provisions of the new enactment express ... | 205 | encoded | `the idea in the new enactment is not taken to be different merely because a different form of words is used` (ie-repeal.l4). Test: tests-repeal.l4. |
| 204 | s 26(2)(f): (f) a reference in any other enactment to the former enactment shall, ... | 206 | encoded | `how a reference in any other enactment to the former enactment is read` (ie-repeal.l4). Test: tests-repeal.l4. |
| 205 | s 27 heading: Effect of repeal of enactment | 207 | inert 1 | A marginal note: not part of the enactment (s 18(g)). |
| 206 | s 27(1): (1) Where an enactment is repealed, the repeal does not— | 207 | encoded | The lead-in is the condition shared by paragraphs (a) to (e): the `the enactment has been repealed` facts of each function (ie-repeal.l4). Test: tests-repeal.l4. |
| 207 | s 27(1)(a): (a) revive anything not in force or not existing immediately before ... | 208 | encoded | `what section 27(1)(a) says of a thing that` (ie-repeal.l4). Test: tests-repeal.l4. |
| 208 | s 27(1)(b): (b) affect the previous operation of the enactment or anything duly ... | 209 | encoded | `the repeal does not affect a thing done or suffered on` (ie-repeal.l4). Test: tests-repeal.l4. |
| 209 | s 27(1)(c): (c) affect any right, privilege, obligation or liability acquired, ... | 210 | encoded | `the repeal does not affect a right, privilege, obligation or liability acquired, accrued or incurred on` (ie-repeal.l4). Test: tests-repeal.l4. |
| 210 | s 27(1)(d): (d) affect any penalty, forfeiture or punishment incurred in respect ... | 211 | encoded | `the repeal does not affect a penalty, forfeiture or punishment for an offence or contravention committed on` (ie-repeal.l4). Test: tests-repeal.l4. |
| 211 | s 27(1)(e): (e) prejudice or affect any legal proceedings (civil or criminal) ... | 212 | encoded | `the repeal does not prejudice or affect the legal proceedings` (ie-repeal.l4). Test: tests-repeal.l4. |
| 212 | s 27(2): (2) Where an enactment is repealed, any legal proceedings (civil or ... | 213 | encoded | `the proceedings may be instituted, continued or enforced, and the penalty imposed and carried out, as if the enactment had not been repealed` (ie-repeal.l4). Test: tests-repeal.l4. |
| 213 | SCH-heading: SCHEDULE Interpretation of Particular Words and Expressions | 214 | inert 1 | A heading of the Schedule or its cross-reference to s 21: not operative; s 21(1) and (2) are encoded in ie-schedule-definitions.l4. |
| 214 | SCH-xref: Section 21 . | 215 | inert 1 | A heading of the Schedule or its cross-reference to s 21: not operative; s 21(1) and (2) are encoded in ie-schedule-definitions.l4. |
| 215 | SCH-PT1-heading: PART 1 | 216 | inert 1 | A heading of the Schedule or its cross-reference to s 21: not operative; s 21(1) and (2) are encoded in ie-schedule-definitions.l4. |
| 216 | Sch Pt 1 "affidavit": “affidavit”, in the case of a person for the time being allowed by ... | 217 | fork | the constant `Part 1 entry: affidavit`, reached by `the Part 1 entry for` `affidavit` (ie-schedule-definitions.l4). F47 (open list); `the entry names the thing` applies it, with the case 'allowed by law to declare instead of swearing' an input. Test: tests-schedule-definitions.l4. |
| 217 | Sch Pt 1 "British statute": “British statute” means an Act of the Parliament of the former United ... | 218 | encoded | the constant `Part 1 entry: British statute`, reached by `the Part 1 entry for` `British statute` (ie-schedule-definitions.l4).  Test: tests-schedule-definitions.l4. |
| 218 | Sch Pt 1 "Circuit Court": “Circuit Court” means the Circuit Court as established and for the ... | 219 | encoded | the constant `Part 1 entry: Circuit Court`, reached by `the Part 1 entry for` `Circuit Court` (ie-schedule-definitions.l4). The 'as established and for the time being maintained by law' is a borrowed fact the caller supplies. Test: tests-schedule-definitions.l4. |
| 219 | Sch Pt 1 "commencement": “commencement”, when used in relation to an enactment, means the time ... | 220 | encoded | the constant `Part 1 entry: commencement`, reached by `the Part 1 entry for` `commencement` (ie-schedule-definitions.l4). Worked out in ie-interpretation-time.l4 (`the commencement of the enactment, as the Schedule defines the word`). Test: tests-schedule-definitions.l4, tests-commencement.l4. |
| 220 | Sch Pt 1 "Constitution": “Constitution” means the Constitution of Ireland enacted by the ... | 221 | encoded | the constant `Part 1 entry: Constitution`, reached by `the Part 1 entry for` `Constitution` (ie-schedule-definitions.l4). `it is the Constitution within the meaning of the Schedule` compares the day of enactment, 1 July 1937. Test: tests-schedule-definitions.l4. |
| 221 | Sch Pt 1 "Dáil Éireann": “Dáil Éireann” means the House of the Oireachtas to which that name ... | 222 | encoded | the constant `Part 1 entry: Dail Eireann`, reached by `the Part 1 entry for` `Dail Eireann` (ie-schedule-definitions.l4). Points at section 1 of Article 15 of the Constitution, a borrowed provision. Test: tests-schedule-definitions.l4. |
| 222 | Sch Pt 1 "District Court": “District Court” means the District Court as established and for the ... | 223 | encoded | the constant `Part 1 entry: District Court`, reached by `the Part 1 entry for` `District Court` (ie-schedule-definitions.l4). The 'as established and for the time being maintained by law' is a borrowed fact the caller supplies. Test: tests-schedule-definitions.l4. |
| 223 | Sch Pt 1 "financial year": “financial year”, in relation to an exchequer financial year, means ... | 224 | encoded | the constant `Part 1 entry: financial year`, reached by `the Part 1 entry for` `financial year` (ie-schedule-definitions.l4). Worked out in ie-interpretation-time.l4 (`the exchequer financial year containing`). Test: tests-schedule-definitions.l4, tests-rest-days-and-words.l4. |
| 224 | Sch Pt 1 "Government": “Government” means the Government mentioned in Article 28 of the ... | 225 | encoded | the constant `Part 1 entry: Government`, reached by `the Part 1 entry for` `Government` (ie-schedule-definitions.l4). Points at Article 28 of the Constitution. Test: tests-schedule-definitions.l4. |
| 225 | Sch Pt 1 "Great Britain": “Great Britain” does not include the Channel Islands or the Isle of ... | 226 | fork | the constant `Part 1 entry: Great Britain`, reached by `the Part 1 entry for` `Great Britain` (ie-schedule-definitions.l4). F47 ('does not include' excludes only what it names), F48 (three members: the printed phrase and each of the two); `the entry names the thing` applies it. Test: tests-schedule-definitions.l4. |
| 226 | Sch Pt 1 "High Court": “High Court” means the High Court as established and for the time ... | 227 | encoded | the constant `Part 1 entry: High Court`, reached by `the Part 1 entry for` `High Court` (ie-schedule-definitions.l4). Points at Article 34 of the Constitution. Test: tests-schedule-definitions.l4. |
| 227 | Sch Pt 1 "land": “land” includes tenements, hereditaments, houses and buildings, land ... | 228 | fork | the constant `Part 1 entry: land`, reached by `the Part 1 entry for` `land` (ie-schedule-definitions.l4). F47 (open list), F48 (ten members: the five items as the line prints them and the things two of them list); `the entry names the thing` applies it. Test: tests-schedule-definitions.l4. |
| 228 | Sch Pt 1 "local financial year": “local financial year” means a period which is coextensive with a ... | 229 | encoded | the constant `Part 1 entry: local financial year`, reached by `the Part 1 entry for` `local financial year` (ie-schedule-definitions.l4). Worked out in ie-interpretation-time.l4 (`the local financial year containing`). Test: tests-schedule-definitions.l4, tests-rest-days-and-words.l4. |
| 229 | Sch Pt 1 "midnight": “midnight” means, in relation to a particular day, the point of time ... | 230 | fork | the constant `Part 1 entry: midnight`, reached by `the Part 1 entry for` `midnight` (ie-schedule-definitions.l4). F9 (days tile with no gap). Worked out in ie-interpretation-time.l4 (`Midnight`). Test: tests-schedule-definitions.l4, tests-commencement.l4. |
| 230 | Sch Pt 1 "Minister of the Government": “Minister of the Government” means a member of the Government having ... | 231 | encoded | the constant `Part 1 entry: Minister of the Government`, reached by `the Part 1 entry for` `Minister of the Government` (ie-schedule-definitions.l4). `the person is a Minister of the Government` takes the two limbs as facts. Test: tests-schedule-definitions.l4. |
| 231 | Sch Pt 1 "month": “month” means a calendar month; | 232 | fork | the constant `Part 1 entry: month`, reached by `the Part 1 entry for` `month` (ie-schedule-definitions.l4). F4, F5 (a calendar month; a period that begins part-way). Worked out in ie-interpretation-time.l4 (`the calendar month containing`, the months limb of `the last day of a period of`). Test: tests-schedule-definitions.l4, tests-periods.l4, tests-rest-days-and-words.l4. |
| 232 | Sch Pt 1 "oath": “oath”, in the case of a person for the time being allowed by law to ... | 233 | fork | the constant `Part 1 entry: oath`, reached by `the Part 1 entry for` `oath` (ie-schedule-definitions.l4). F47 (open list), F48 (three members: the printed phrase and each of the two); `the entry names the thing` applies it, with the case 'allowed by law to affirm or declare instead of swearing' an input. Test: tests-schedule-definitions.l4. |
| 233 | Sch Pt 1 "Oireachtas": “Oireachtas” means the National Parliament provided for by Article 15 ... | 234 | encoded | the constant `Part 1 entry: Oireachtas`, reached by `the Part 1 entry for` `Oireachtas` (ie-schedule-definitions.l4). Points at Article 15 of the Constitution. Test: tests-schedule-definitions.l4. |
| 234 | Sch Pt 1 "ordnance map": “ordnance map” means a map made under the powers conferred by the ... | 235 | encoded | the constant `Part 1 entry: ordnance map`, reached by `the Part 1 entry for` `ordnance map` (ie-schedule-definitions.l4). Points at the Survey (Ireland) Acts 1825 to 1870, a borrowed Act. Test: tests-schedule-definitions.l4. |
| 235 | Sch Pt 1 "President": “President” means the President of Ireland or any Commission, or ... | 236 | fork | the constant `Part 1 entry: President`, reached by `the Part 1 entry for` `President` (ie-schedule-definitions.l4). F40 ('exercising the powers and performing the duties' read as both); `it is the President within the meaning of the Schedule` applies it. Test: tests-schedule-definitions.l4. |
| 236 | Sch Pt 1 "pre-union Irish statute": “pre-union Irish statute” means an Act passed by a Parliament sitting ... | 237 | fork | the constant `Part 1 entry: pre-union Irish statute`, reached by `the Part 1 entry for` `pre-union Irish statute` (ie-schedule-definitions.l4). F41 (an Act passed on 1 January 1801 itself); `it is a pre-union Irish statute` applies it. Test: tests-schedule-definitions.l4. |
| 237 | Sch Pt 1 "rateable valuation": “rateable valuation” means the valuation under the Valuation Act 2001 ... | 238 | encoded | the constant `Part 1 entry: rateable valuation`, reached by `the Part 1 entry for` `rateable valuation` (ie-schedule-definitions.l4). Points at the Valuation Act 2001, a borrowed Act. Test: tests-schedule-definitions.l4. |
| 238 | Sch Pt 1 "rules of court": “rules of court” means rules made by the authority for the time being ... | 239 | encoded | the constant `Part 1 entry: rules of court`, reached by `the Part 1 entry for` `rules of court` (ie-schedule-definitions.l4). The authority is the one s 24 names (ie-powers-duties-continuing.l4). Test: tests-schedule-definitions.l4. |
| 239 | Sch Pt 1 "Saorstát Éireann statute": “Saorstát Éireann statute” means an Act of the Oireachtas of Saorstát ... | 240 | encoded | the constant `Part 1 entry: Saorstat Eireann statute`, reached by `the Part 1 entry for` `Saorstat Eireann statute` (ie-schedule-definitions.l4).  Test: tests-schedule-definitions.l4. |
| 240 | Sch Pt 1 "Seanad Éireann": “Seanad Éireann” means the House of the Oireachtas to which that name ... | 241 | encoded | the constant `Part 1 entry: Seanad Eireann`, reached by `the Part 1 entry for` `Seanad Eireann` (ie-schedule-definitions.l4). Points at section 1 of Article 15 of the Constitution, a borrowed provision. Test: tests-schedule-definitions.l4. |
| 241 | Sch Pt 1 "statutory declaration": “statutory declaration” means a declaration made under the Statutory ... | 242 | encoded | the constant `Part 1 entry: statutory declaration`, reached by `the Part 1 entry for` `statutory declaration` (ie-schedule-definitions.l4). Points at the Statutory Declarations Act 1938, a borrowed Act. Test: tests-schedule-definitions.l4. |
| 242 | Sch Pt 1 "Supreme Court": “Supreme Court” means the Supreme Court as established and for the ... | 243 | encoded | the constant `Part 1 entry: Supreme Court`, reached by `the Part 1 entry for` `Supreme Court` (ie-schedule-definitions.l4). Points at Article 34 of the Constitution. Test: tests-schedule-definitions.l4. |
| 243 | Sch Pt 1 "swear": “swear”, in the case of a person for the time being allowed by law to ... | 244 | fork | the constant `Part 1 entry: swear`, reached by `the Part 1 entry for` `swear` (ie-schedule-definitions.l4). F47 (open list), F48 (three members: the printed phrase and each of the two); `the entry names the thing` applies it, with the case an input. Test: tests-schedule-definitions.l4. |
| 244 | Sch Pt 1 "week": “week” means the period between midnight on any Saturday and midnight ... | 245 | fork | the constant `Part 1 entry: week`, reached by `the Part 1 entry for` `week` (ie-schedule-definitions.l4). F6 (a week runs Sunday to Saturday). Worked out in ie-interpretation-time.l4 (`the week containing`). Test: tests-schedule-definitions.l4, tests-periods.l4, tests-rest-days-and-words.l4. |
| 245 | Sch Pt 1 "week-day": “week-day” means a day which is not a Sunday; | 246 | fork | the constant `Part 1 entry: week-day`, reached by `the Part 1 entry for` `week-day` (ie-schedule-definitions.l4). F7 (not `daydate`'s `is weekday`). Worked out in ie-interpretation-time.l4 (`is a week-day`). Test: tests-schedule-definitions.l4, tests-rest-days-and-words.l4. |
| 246 | Sch Pt 1 "writing": “writing” includes printing, typewriting, lithography, photography, ... | 247 | fork | the constant `Part 1 entry: writing`, reached by `the Part 1 entry for` `writing` (ie-schedule-definitions.l4). F47 (open list), F48 (eight members: the six items as the line prints them and the two modes one of them joins); `the entry names the thing` applies it. Test: tests-schedule-definitions.l4. |
| 247 | Sch Pt 1 "year": “year”, when used without qualification, means a period of 12 months ... | 248 | fork | the constant `Part 1 entry: year`, reached by `the Part 1 entry for` `year` (ie-schedule-definitions.l4). F4, F5. Worked out in ie-interpretation-time.l4 (`the year containing`, the years limb of `the last day of a period of`). Test: tests-schedule-definitions.l4, tests-periods.l4, tests-rest-days-and-words.l4. |
| 248 | SCH-PT2-heading: PART 2 | 249 | inert 1 | A heading of the Schedule or its cross-reference to s 21: not operative; s 21(1) and (2) are encoded in ie-schedule-definitions.l4. |
| 249 | Sch Pt 2 "Companies Acts": “Companies Acts” means the Companies Acts 1963 to 2001 and every ... | 250 | encoded | the constant `Part 2 entry: Companies Acts`, reached by `the Part 2 entry for` `Companies Acts` (ie-schedule-definitions.l4). `it is within the Companies Acts as the Schedule defines them` takes the two limbs as facts. Test: tests-schedule-definitions.l4. |
| 250 | Sch Pt 2 "full age": “full age”, in relation to a person, means the time when the person ... | 251 | fork | the constant `Part 2 entry: full age`, reached by `the Part 2 entry for` `full age` (ie-schedule-definitions.l4). F24 (the two days are inputs). Worked out in ie-operation-and-construction.l4 (`the day on which the person attains full age`). Test: tests-schedule-definitions.l4, tests-operation.l4. |
| 251 | Sch Pt 2 "functions": “functions” includes powers and duties, and references to the ... | 252 | fork | the constant `Part 2 entry: functions`, reached by `the Part 2 entry for` `functions` (ie-schedule-definitions.l4). F47 (open list), F48 (six members: the two items as the line prints them and the four things they list); `the entry names the thing` applies it. Test: tests-schedule-definitions.l4. |
| 252 | Sch Pt 2 "Member State": “Member State” means, where the context so admits, a Member State of ... | 253 | encoded | the constant `Part 2 entry: Member State`, reached by `the Part 2 entry for` `Member State` (ie-schedule-definitions.l4). `it is a Member State within the meaning of the Schedule` takes 'where the context so admits' as a fact. Test: tests-schedule-definitions.l4. |
| 253 | Sch Pt 2 "Minister of State": “Minister of State” means a person appointed under section 1 of the ... | 254 | encoded | the constant `Part 2 entry: Minister of State`, reached by `the Part 2 entry for` `Minister of State` (ie-schedule-definitions.l4). Points at section 1 of the Ministers and Secretaries (Amendment) (No. 2) Act 1977, a borrowed Act. Test: tests-schedule-definitions.l4. |
| 254 | Sch Pt 2 "public holiday": “public holiday” means a public holiday determined in accordance with ... | 255 | encoded | the constant `Part 2 entry: public holiday`, reached by `the Part 2 entry for` `public holiday` (ie-schedule-definitions.l4). The Organisation of Working Time Act 1997 is a borrowed Act, so holidays are an input function (ie-interpretation-time.l4, `is a working day`). Test: tests-schedule-definitions.l4, tests-rest-days-and-words.l4. |
| 255 | Sch Pt 2 "Social Welfare Acts": “Social Welfare Acts” means the Social Welfare (Consolidation) Act ... | 256 | encoded | the constant `Part 2 entry: Social Welfare Acts`, reached by `the Part 2 entry for` `Social Welfare Acts` (ie-schedule-definitions.l4). `it is within the Social Welfare Acts as the Schedule defines them` takes the two limbs as facts. Test: tests-schedule-definitions.l4. |
| 256 | Sch Pt 2 "working day": “working day” means a day which is not a Saturday, Sunday or public ... | 257 | fork | the constant `Part 2 entry: working day`, reached by `the Part 2 entry for` `working day` (ie-schedule-definitions.l4). F7 (Monday to Friday, not a public holiday). Worked out in ie-interpretation-time.l4 (`is a working day`). Test: tests-schedule-definitions.l4, tests-rest-days-and-words.l4. |

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
| F34 | Which language text has authority? | **not decided.** This is an encoding of the English text only. | The English text of the Act says nothing on it. `../../SOURCE-LICENSE.md` (the subject's licence note) records, citing the sibling subject `ie/sick-leave-act-2022` (checked 2026-09-22), that Article 25.4 of the Constitution makes the Irish text prevail where both are enrolled and conflict; that is not in this Act, was not used here, and this Act's signed language was not checked. |
| F35 | Accented letters in identifiers | transliterated to ASCII (`Saorstat Eireann`, `Sampla`, `Samplai`) | The brief requires ASCII filenames, and the identifiers follow. The quoted text keeps its accents. |
| F36 | Target compiler | `unstable` | Section 1. |
| F37 | Is the enacted text the current text? | **yes, on the file's own statement** | The file says the directory lists no amendment. It was not re-checked. |

### 5.5 Looked at and not forked

Read for ambiguity and left alone, because no reading changes an answer: s 1(2) (a date), s 2(2) (a closed list of five conditions), s 9 (two lists with an open "other division, by whatever name called", encoded as an open case that refuses), s 11 (four named headings), s 18(f) (a series including its first and last; a last before the first refuses), s 22(3), s 26(2)(a), (b), (d), (e), (f), s 27(1)(a) to (e) and (2).
Read in pass 2 and left alone for the same reason: s 10, s 22(1) and s 23(1) ("from time to time" puts no limit on the number of occasions, so the number of earlier uses is varied in the tests and read by no rule), s 14(2) (all three limbs, an amendment made before, on or after the day, give one answer), s 18(a) (both directions), s 19 (one rule, with the contrary intention asked as an input), s 20(2) (three relations of a form to a defined word), s 21(1) and (2), s 24 ("may at any time exercise" excludes no day), and the Schedule entries that say "means" (an entry that means is not a list of inclusions, and a test pins that).
"No ambiguity" is a claim about what was read, not about the Act.

### 5.6 Forks found in pass 2

Same columns as 5.3.
Each is pinned by a test that asserts the chosen reading and, where the reading is a refusal, the reason.
Test sections are cited by heading; line numbers move.

| id | question | readings seen | reading taken | text and where tested |
| --- | --- | --- | --- | --- |
| F39 | s 14(3): does "that is not required for the purpose of punctuation" qualify both commas, or only the comma after the year? | (a) both: a comma before a year or after one may be omitted unless it is required for punctuation; (b) only the second: the comma before a year may always be omitted | **(a)** | s 14(3): "a comma immediately before a reference to a year and a comma immediately after such a reference that is not required for the purpose of punctuation may be omitted". Under (b) a comma before a year that punctuation requires could be omitted; the test for "before" with the comma required asserts that it may not. `section 14(3) lets the comma be omitted` (ie-citation-and-text.l4); tests-citation-and-text.l4, section 14(3). |
| F40 | Schedule Pt 1 "President": "exercising the powers and performing the duties": both, or either? | (a) both; (b) either | **(a) both** | The entry joins them with "and". A body that exercises the powers and does not perform the duties is not the President under (a); under (b) it would be. `it is the President within the meaning of the Schedule` (ie-schedule-definitions.l4); tests-schedule-definitions.l4, "Part B: President" (the cases where the body does only one of the two are asserted NOT). |
| F41 | Schedule Pt 1 "pre-union Irish statute": an Act passed on 1 January 1801 itself | before the coming into force of the Act of Union; not before it | **not answered (REFUSE)** | The entry says "at any time before the coming into force on 1 January 1801" and gives no moment within the day, so an Act passed on that day cannot be placed before or after. Same family as F27 and F28. `it is a pre-union Irish statute` (ie-schedule-definitions.l4); tests-schedule-definitions.l4, "Part B: pre-union Irish statute" (1800-12-31 yes, 1801-01-02 no, 1801-01-01 refuses). |
| F42 | s 18(c): is the list of kinds of party that "person" imports closed? | (a) closed: a party of another kind is not imported (FALSE); (b) the text does not say: not answered | **(b) not answered (REFUSE)** | s 18(c) says what person "shall be read as importing" and does not say that nothing else is imported. `the word person is read as importing` (ie-words-and-meaning.l4); tests-words-and-meaning.l4, section 18(c). The pronoun limb answers FALSE when no pronoun stands in place of a further use of "person", because the section gives nothing then. |
| F43 | s 15(2): "Immediately after the Bill ... is signed" and a date other than the date of the passing | (a) no measure of time, so no latest moment; (b) the same day; (c) the next day. For a different date endorsed: (a) the section is silent; (b) the endorsement is void | **no latest moment (REFUSE); a different date endorsed: REFUSE; nothing endorsed: FALSE** | s 15(2) deems the date of the passing, endorsed, to be part of the Act; it names no measure for "immediately" and says nothing of an endorsement of any other date. `the latest moment by which the Clerk of Dail Eireann must have endorsed the date`, `the endorsed date is taken to be part of the Act` (ie-citation-and-text.l4); tests-citation-and-text.l4, section 15(2). |
| F44 | ss 22(2), 23(2): "the holder for the time being" when two persons hold the office on the same day, or none does | two holders: (a) refuse; (b) the later appointed; (c) both. None: (a) NOTHING; (b) refuse | **two holders REFUSE; none: NOTHING** | The sections speak of "the holder", singular, and say nothing of two or none. A day on which no one holds the office gives the power or duty to no one: NOTHING, so the person-level functions answer FALSE. `the holder for the time being of the office on`, `the holder for the time being of the office, for a duty, on` (ie-powers-duties-continuing.l4); tests-powers-duties.l4, sections 22(2) and 23(2). |
| F45 | s 7(1)(b) and (c): which limb of "Act" in s 2(1) is each? | (b) a statute of Saorstat Eireann continued in force; (c) the same, or another kind | **both are limb (b)** | s 2(1) "Act" has two limbs: an Act of the Oireachtas, and a statute in force in Saorstat Eireann before the Constitution and continued by Article 50. Paragraph (a) is the first limb; "any other Act" in (c) reads as the rest of the second limb. `the kind of enactment, for section 7(1), of` (ie-citation-and-text.l4); tests-citation-and-text.l4, section 7(1). Existing F30 (an instrument) stands. |
| F46 | s 18(j): "(whether punishable on indictment or on summary conviction)": two ways named, or illustration of any way | (a) names two ways; an offence punishable in another way is not answered; (b) illustrative: every offence | **(a) REFUSE for another way** | The parenthesis names two ways and does not say "or otherwise". `section 18(j) reads the reference as including a body corporate` (ie-words-and-meaning.l4); tests-words-and-meaning.l4, section 18(j). A reference that is not to a person in relation to an offence answers FALSE. |
| F47 | Schedule entries that say "includes" or "does not include": open or closed? | "includes": (a) open list: a thing not named is not answered; (b) closed list: FALSE. "does not include": (a) excludes only what it names; (b) excludes everything else | **"includes" is open and "does not include" excludes only what it names: a thing not named is REFUSED in both cases** | "includes" is the word the text uses; the same word was read as open for "repeal" in s 2(1) (F18). `the entry names the thing` (ie-schedule-definitions.l4); tests-schedule-definitions.l4, "Part B: entries that say what a word includes or does not include". An entry that limits itself to a case ("in the case of a person ... allowed by law to declare") gives nothing where the case does not exist: FALSE. |
| F48 | Schedule "includes" and "does not include" entries: what is a member of the list? | (a) only the whole phrase between the line's commas, "and" and "or" inside it (the module before the 2026-10-29 fixes); (b) only the things the phrase lists, one member each; (c) both: the item as the line prints it, and each thing it lists | **(c)** | The line prints the items and a caller may ask with either form, so a query for "powers" and a query for "powers and duties" both name an item the line includes. Items with constituents: "powers and duties" (powers, duties) and "the exercise of the powers and the carrying out of the duties" (the exercise of the powers, the carrying out of the duties), Pt 2 "functions"; "houses and buildings" (houses, buildings) and "any estate, right or interest in or over land" (any estate in or over land, any right in or over land, any interest in or over land), Pt 1 "land"; "other modes of representing or reproducing words in visible form" (other modes of representing words in visible form, other modes of reproducing words in visible form), Pt 1 "writing"; "affirmation or declaration" (affirmation, declaration), Pt 1 "oath"; "affirm and declare" (affirm, declare), Pt 1 "swear"; "the Channel Islands or the Isle of Man" (the Channel Islands, the Isle of Man), Pt 1 "Great Britain". "in or over land" is read as qualifying each of estate, right and interest (the other reading, that it qualifies only "interest", would leave "any estate" and "any right" unqualified). "any information kept in a non-legible form, whether stored electronically or otherwise, which is capable by any means of being reproduced in a legible form" has no constituents, because "whether stored electronically or otherwise" qualifies it and lists nothing. A thing the line does not list still refuses (F47). **Sweep, 2026-10-29, by script over lines 217 to 257 of the text:** 40 Schedule entries; 7 are not `means` entries. Extended: land, writing, functions, oath, swear, Great Britain (six). Checked and left: "affidavit" (one item, "declaration", no joiner). The other 33 say "means", and `the entry names the thing` refuses for them, so their member lists are never queried and were not changed. History: the module first held only the whole phrases, (a), which refused "powers" alone; the first fix held only the constituents, (b), which made the Act's own printed phrases refuse; (c) is the present state. `the Part N entry for` (ie-schedule-definitions.l4); tests-schedule-definitions.l4, Part A (land, writing, functions, oath, swear, Great Britain) and Part B. |

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

### 6.4 Answers added in pass 2

Each was run (`tests-words-and-meaning.l4`, `tests-powers-duties.l4`, `tests-citation-and-text.l4`, `tests-schedule-definitions.l4`).
The offset in the first row is an input; its value here is an example and is not taken from the 1971 Act, which is not in the text.

| question | answer | section |
| --- | --- | --- |
| 15:00 on 2026-03-10, the standard time that day being 60 minutes ahead of UTC (supplied) | 14:00 UTC the same day (minute 840 of 2026-03-10); with offset 0, 15:00 UTC; midnight (hour 0) with offset 60: 23:00 UTC on 2026-03-09 | s 18(i) |
| hour 24, hour -1, hour 1.5 | **REFUSE**: "an hour that is not a whole number from 0 to 23 is not answered" | s 18(i) |
| the holder of an office is Alice to 2026-06-30 and Bob from 2026-07-01: who may exercise a power conferred on the holder | on 2026-06-30 Alice; on 2026-07-01 Bob; before Alice's first day, NOTHING; a day on which both hold: **REFUSE** | s 22(2); F44 |
| an Act cited by its short title: may the comma immediately before a year be left out | yes, when it is not required for punctuation; no when it is; no for a comma elsewhere; no for something that is not an Act or an enactment cited by its citation | s 14(3); F39 |
| the Bill is signed on 2026-03-10: what date must the Clerk endorse, and if 2026-03-11 is endorsed | 2026-03-10; **REFUSE** for 2026-03-11; nothing endorsed: the section deems nothing part of the Act | s 15(2); F43 |
| an Act of the Oireachtas passed on 1800-12-31; on 1801-01-02; on 1801-01-01 | a pre-union Irish statute if it was passed by a Parliament sitting in Ireland on 1800-12-31; not on 1801-01-02; **REFUSE** on 1801-01-01 | Sch Pt 1 "pre-union Irish statute"; F41 |
| the Constitution enacted on 1937-07-01; 1937-06-30 | yes; no | Sch Pt 1 "Constitution" |
| "affidavit" includes "declaration" for a person allowed by law to declare instead of swearing | yes when the case exists; FALSE when it does not; "a sworn statement" is **not answered** | Sch Pt 1 "affidavit"; F47 |

## 7. What `check.sh` prints

Run from this directory, after `_work/` was removed:

```
SRC_RAW=../../registers/source-bundle/No.-23-of-2005.txt \
L4=<L4_BIN> L4_TARGET=unstable ./check.sh
```

`SRC_RAW` is the raw text; without it the source-quote gate prints that it was NOT RUN and nothing else changes.
`L4_TARGET` defaults to `unstable` in this row's `check.sh`.
Printed on 2026-10-29 on the binary in `encoding.json`, re-run after the three edits that fixed the includes lookup (finding 13):

```
check.sh: the target is unstable, so the main check was skipped.
module                                    errors satisfied  failed  refused  expected
ie-acts-referred-to.l4                         0         0       0        0         0
ie-citation-and-text.l4                        0         0       0        0         0
ie-general.l4                                  0         0       0        0         0
ie-interpretation-time.l4                      0         0       0        0         0
ie-month-year-readings.l4                      0         0       0        0         0
ie-operation-and-construction.l4               0         0       0        0         0
ie-powers-and-service.l4                       0         0       0        0         0
ie-powers-duties-continuing.l4                 0         0       0        0         0
ie-repeal.l4                                   0         0       0        0         0
ie-schedule-definitions.l4                     0         0       0        0         0
ie-words-and-meaning.l4                        0         0       0        0         0
tests-acts-referred-to.l4                      0        68       0        0         0
tests-citation-and-text.l4                     0        67       0        0         0
tests-commencement.l4                          0        57       0        0         0
tests-general.l4                               0       102       0        0         0
tests-operation.l4                             0       112       0        0         0
tests-periods.l4                               0        96       0        0         0
tests-powers-duties.l4                         0        57       0        0         0
tests-powers-service.l4                        0        31       0        0         0
tests-readings.l4                              0        59       0        0         0
tests-red-control.l4                           8         0       8        0         8
tests-repeal.l4                                0       105       0        0         0
tests-rest-days-and-words.l4                   0        57       0        0         0
tests-schedule-definitions.l4                  0       421       0        0         0
tests-words-and-meaning.l4                     0        64       0        0         0
tests-worked-cases.l4                          0        26       0        0         0
TOTAL (26 modules)                             8      1322       8        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
srcrefs check: 438 src: lines, 254 runs, 312 locators, 0 problems
```

The exit status of the run was 0.
`python3 -I srcrefs.py check --refs <raw text> ie-*.l4` and `... check --strict <raw text> ie-*.l4` each printed the same `srcrefs check` line with 0 problems.

Baseline against pass 1 (measured before any change, on the same binary): 16 modules, 645 satisfied, 8 failed (all expected), 0 refused, srcrefs 261 src lines, 132 runs, 172 locators, 0 problems.
Every pass-1 module prints exactly its baseline numbers in the table above.
Added in pass 2: 10 modules (five `ie-*`, five `tests-*`), 677 satisfied (421 + 64 + 57 + 67 + 68), 177 src lines, 122 runs, 140 locators.

How to read it:

- The eleven `ie-*.l4` modules have no assertions of their own; they type-check with 0 errors.
- Eight failures are expected and are all in `tests-red-control.l4`, whose eight assertions are deliberately wrong (the file header says which wrong reading each guards against).
  `check.sh` counts them in its `expected` column and `encoding.json` records them under `expected_red`; the gate fails if the file produces more or fewer than eight.
  They are finding 8 in section 10.
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
11. **The ten forks found in pass 2 (F39 to F48)**, section 5.6: which commas s 14(3)'s qualifier governs, "and" in the "President" entry, the first day of 1801, the list of kinds in s 18(c), "immediately" in s 15(2), two holders of one office, the limbs of "Act" that s 7(1)(b) and (c) name, the two ways of punishing in s 18(j), whether "includes" lists in the Schedule are open, and what counts as one member of such a list.
12. **Who may enforce a duty** under s 15(2) and s 23: the text names the person who must act and not the person who may ask.
    The encoding does not name one either (`## Jural relations`).

### 8.1 What would need doing before the encoding is worth relying on

1. **A domain expert (an Irish lawyer) reads it against the official text, in both languages.**
   Nothing here has been compared with the official text; the source is a converter's rendering, and the Irish-language text was not consulted (F34).
2. **Settle the ten pass-2 forks and the older ones that change an answer** (F2, F5, F6, F8, F11, F23, F27, F28, F29), at least by recording the expert's reading in section 5.
3. **Check that the enacted text is still the current text** (F37).
   The file says the directory lists no amendment; this run did not re-check it.
4. **Supply the borrowed facts or encode the Acts they come from.**
   The Standard Time (Amendment) Act 1971 (the offset in s 18(i) and the time zone in s 25), the Organisation of Working Time Act 1997 (public holidays) and the Constitution (Articles 15, 28, 34 and 50, which several Schedule entries and s 2(1) point at, and Article 25.4.5, which s 7(1) points at) are inputs or pointers here.
5. **There is no individual-seat layer.**
   The brief asks for one only "if the row has one", and this row has none: the Act is a rule of reading addressed to courts and drafters, and no provision gives an individual a claim.
   A seat layer would be a separate module with questions a person would ask ("when was this notice treated as served", "when did the instrument that affects me come into operation", "by when must I act if a period of N days runs from this day") answered by calling the functions here; it is not written.
6. **Spot-check the entry-by-entry tests of the Schedule.**
   Part A of `tests-schedule-definitions.l4` (421 assertions in all, Parts A and B) takes the word, the part, the kind of meaning and the case from each entry's source line by pattern, and the count and first and last of the things named were read off the line by hand; each source line is quoted in a comment beside its assertions so any one can be read against the text.
7. **Run on `main`.**
   The encoding needs `unstable` (`@lang en`, `REFUSE`, `YMD`); it cannot be checked on `main`.

## 9. What the text does not answer

Places where the Act has no answer and the encoding returns a named refusal or an explicit `NOTHING`, sorted by whether the caller sees them.
All are asserted in a test.

**Refusals that name the gap (the caller sees a message):**

| question | what the Act lacks | fork |
| --- | --- | --- |
| a period of months or years that does not begin where the unit begins; a period of weeks that does not begin on a Sunday | any corresponding-date rule | F4, F5, F6 |
| a period counted "after" an event | s 18(h) speaks only of a period that begins on, is reckoned from, ends on or is reckoned to a day | F2 |
| a last day that falls on a day of rest, recess or holiday | any rule that moves it. The whole text was read for one, section by section and in the Schedule; the nearest provisions are s 18(h), which says only that the first and last days are included, and the Schedule's "week-day", "working day" and "public holiday", which define kinds of day and move nothing | F8 |
| the moment on the day of passing under s 16(1); a Saorstat Eireann statute that is silent on commencement | a moment of day; a rule for the date of the passing of a statute that is not an Act of the Oireachtas | F11, F16 |
| a change, passing or making on the very day (ss 6, 17) | a time of day | F27, F28 |
| a deemed time of service where the contrary is proved; the time zone of the time of delivery | what applies once the contrary is proved; a time zone | F29 |
| a time by reference to an hour (s 18(i)); an hour that is not a whole number from 0 to 23 | the Standard Time (Amendment) Act 1971; a meaning for an hour outside the day | F38 |
| s 15(2): a measure of "immediately"; a different date endorsed | a time limit; what follows from another date | F43 |
| s 18(c), s 18(j): a party of another kind; an offence punishable in another way | whether the lists are closed | F42, F46 |
| ss 22(2), 23(2): two holders of one office on one day | which of them | F44 |
| a pre-union Irish statute passed on 1 January 1801 | a moment within that day | F41 |
| a Schedule entry that "includes" or "does not include": a thing it does not name | whether the list is closed | F47 |
| s 19: a word in an instrument where a contrary intention appears under s 4(1) | what the word means then | F17 |

**Answers that are `NOTHING` or `FALSE` and are easy to misread as "no":**

- A day on which no one holds the office (ss 22(2), 23(2)) gives `NOTHING`: the section gives the power or duty to no one that day.
- `FALSE` always means "the section does not give X" (section 3.3).

**Not a question of the Act's text:**

- What a "day" is: the Act does not define it, and the encoding takes a day to be a calendar date from one midnight to the next (F9).
- Who may enforce a duty under s 15(2) and s 23: the Act names no claim-holder.

## 10. Numbered findings

Each finding says where it can be checked.
Counts were taken on 2026-10-29.

1. **34 of the 38 pass-1 `inert` rows were operative.**
   They move to `encoded` or `fork`; four keep `inert` (the long title; headings and marginal notes; s 1(1), reason 2; the Schedule heading and cross-reference).
   The reasons pass 1 gave were not among the three the brief allows.
   Check: the verdict table in the audit section, one row each.
2. **The text has 256 units.
   Pass 1's table had 114 rows, of which 4 were not text; 26 rows covered more than one unit (167 units shared a row) and 5 units (the lead-ins of s 2(1), s 17, s 18, s 26(2) and s 27(1)) were named in no row.**
   Check: the counts section of the audit; two line-level cross-checks agree with the counter (27 section numbers, 36 subsections, 67 paragraph-level units, 44 defined-term entries).
3. **The coverage table now has one row per unit:** 111 `encoded`, 64 `fork`, 80 `inert` reason 1, 1 `inert` reason 2, none repealed or blank.
   Pass 1's `not applicable` (4) and `silent` (4) rows are gone; the `silent` items are kept in section 9 as questions the text does not answer.
4. **Ten forks were found in pass 2 (F39 to F48).** Section 5.6. F48 was added when the includes-lookup defect (finding 13) was fixed.
   Each is pinned by a test that asserts the chosen reading and, for a refusal, its message.
5. **The text names a duty-bearer and no claim-holder** in s 15(2) (the Clerk of Dail Eireann) and s 23 (the person on whom the enactment imposes the duty).
   The encoding does not invent one. `## Jural relations`.
6. **s 18(i) was a bare refusal in pass 1;** it now has a function that takes the 1971 Act's offset as an input and returns a moment in UTC.
   The old refusal stays as the answer for a caller with no offset.
   The offset in the tests is an example value, not a fact about Irish standard time, because that Act is not in the text.
7. **No defect was found in pass 1, so no pass-1 file was edited.**
   A defect in a pass-2 module was found afterwards and fixed (finding 13).
   Check: every pass-1 file has the modification time of the copy made when pass 2 began (15:06:15 on 2026-10-29), and the 16 pass-1 modules print their baseline numbers in section 7.
   The new modules call pass-1 functions (s 4(1), s 7(1), s 15(1), s 21(2)) and the new tests pass, which is evidence that those functions agree with the new readings and is not a review of them.
8. **`tests-red-control.l4` still fails exactly 8 times**, as it did before pass 2.
   The eight are deliberate wrong expectations that make the gate show it catches a wrong value; `encoding.json` lists them under `expected_red`.
9. **The Part A schedule tests are partly machine-extracted from the text.**
   A script read each Schedule entry's source line and wrote the expected word, part, kind of meaning and case; the count and the first and last of the things each entry names were read off the line by hand.
   The first run had 9 failures, all in the script (it kept a trailing comma on a case phrase and missed a case that follows the verb, as in "midnight means, in relation to a particular day,"); the module's data were right.
   The script was fixed, not the module and not an expected value copied from the module.
10. **Binary change.** Pass 1 ran on a binary that printed `dev`; pass 2 runs on the unstable prerelease in `encoding.json`.
    The 16 pass-1 modules print the same numbers on both.
11. **All 90 diagnostics of Hint severity across the 26 files are the `@lang en` Hint;** there is no Warning, and the only Errors are the eight in `tests-red-control.l4`.
    The positive control for the census: it found those eight.
12. **The Acts Referred to table is a lookup, not a rule.**
    It has 18 rows, one per Act printed in the table, and the lookup takes a title from a closed list of those 18, so an Act that is not in the table cannot be asked.
    The tests were typed from the table's lines and assert each row's fields.
    Because the lookup takes a closed list, this module has no "not covered" case of its own; the refusals in the other modules supply that case for the encoding as a whole.
13. **The lookup for "includes" entries stored whole phrases as members** (found by the independent test pass, 2026-10-29).
    Pt 2 "functions" held "powers and duties" as one member, so "powers" alone, "duties" alone, "the exercise of the powers" and "the carrying out of the duties" were answered "not answered" although the line lists each.
    The same flaw was in Pt 1 "land" and "writing"; the other includes entries were already one member per item.
    The first fix kept only the constituents, which made the Act's own printed phrases ("houses and buildings", "any estate, right or interest in or over land", "powers and duties") refuse; the second fix keeps both the item as the line prints it and each thing it lists (F48), and a third edit, after a script sweep of all 40 Schedule entries, applied the rule to "oath", "swear" and "Great Britain".
    Controls: the test file run against the original module fails 14 times, and against the constituents-only module fails 8 times.
    Details: the section "Changes to existing modules" at the end of this file.

## Jural relations

Hohfeld's correlatives: a claim (right) with a duty; a privilege (liberty) with a no-right; a power with a liability; an immunity with a disability.
One row per provision.
A provision that creates no relation is listed once as `none`, with the reason.
Each relation is stated once, from the side of its holder; the L4 rule is one function and is not written twice.
Where the text names one party and not the other, the cell says "not named" and the encoding does not invent one.

**Provisions that create a relation**

| provision | holder | kind | other party | correlative | L4 rule |
| --- | --- | --- | --- | --- | --- |
| s 6 | a court construing a provision of an Act or instrument | privilege | a party to the proceedings | no-right | `a court may make allowance for the change in construing the provision` (ie-general.l4). The text names the court and not the party; the correlative is read in. |
| s 7(1) | a court construing a provision of an Act under s 5 or 6 | privilege | a party to the proceedings | no-right (cannot object under s 18(g)); read in, as for s 6 | `section 7(1) lets a court make use of the matter notwithstanding section 18(g)` (ie-general.l4); the three paragraphs: `the text of an Act that section 7(1) names for` (ie-citation-and-text.l4) |
| s 8 | the specified person | power (to bring summary proceedings) | the person who committed the offence under the other Act | liability | `section 8 lets the specified person bring summary proceedings for the offence` (ie-general.l4). Not named by the text: the offender. Limited by "unless some other person is authorised". |
| s 15(2) | not named | claim | the Clerk of Dail Eireann | duty (to endorse the date of the passing) | `the date the Clerk of Dail Eireann must endorse on the Act`, `the endorsed date is taken to be part of the Act` (ie-citation-and-text.l4) |
| s 17(a), (b) | the person who is to fix the day, or on whom the Act confers a power needed before its commencement | power | not named | liability | `the instrument, act or thing that fixes the day may be made or done on`, `the power to make a statutory instrument or do an act or thing may be exercised on` (ie-operation-and-construction.l4) |
| s 22(1) | the person on whom the enactment confers a power | power | not named | liability | `a power conferred by an enactment may be exercised on the occasion` (ie-powers-duties-continuing.l4) |
| s 22(2) | the holder for the time being of an office | power | not named | liability | `the person may exercise the power on`, `the holder for the time being of the office on` (ie-powers-duties-continuing.l4) |
| s 22(3) | the person with power to make a statutory instrument | power | the persons subject to the instrument | liability | `a power to make a statutory instrument is read as including the power` (ie-powers-and-service.l4). Not named by the text: the persons subject. |
| s 23(1) | not named | claim | the person on whom the enactment imposes a duty | duty | `a duty imposed by an enactment shall be performed on the occasion` (ie-powers-duties-continuing.l4) |
| s 23(2) | not named | claim | the holder for the time being of an office | duty | `the person shall perform the duty on`, `the holder for the time being of the office, for a duty, on` (ie-powers-duties-continuing.l4) |
| s 24 | the authority with power to make rules or orders regulating the practice and procedure of the court | power | persons who litigate in the court in the new, extended or varied jurisdiction | liability | `the authority has power to make rules or orders for the practice and procedure of the court in the exercise of the jurisdiction, as conferred, extended or varied` (ie-powers-duties-continuing.l4) |
| s 25 | the person authorised or required to serve a document | power (to effect service by post, and to have service deemed at the time of delivery in the ordinary course) | the person served | liability (to be treated as served; the contrary may be proved) | `service by post may be effected under section 25`, `the time at which service is deemed to have been effected` (ie-powers-and-service.l4) |

**Provisions that keep a relation created elsewhere.**
The Act creates none of its own here: the parties are those of the repealed or re-enacted enactment, which this text does not name, so the encoding takes what is kept as an input.

| provision | what is kept | L4 rule |
| --- | --- | --- |
| s 26(2)(a) | the appointment of a person under the former enactment | `a person appointed under the former enactment continues to act on` (ie-repeal.l4) |
| s 26(2)(b) | a bond, guarantee or other security of a continuing nature; the use of data, books, papers and forms | `the security remains in force`, `the data, books, papers, forms and things may continue to be used` (ie-repeal.l4) |
| s 26(2)(c) | proceedings taken under the former enactment | `the proceedings may be continued under the new enactment` (ie-repeal.l4) |
| s 27(1)(c) | a right, privilege, obligation or liability acquired, accrued or incurred | `the repeal does not affect a right, privilege, obligation or liability acquired, accrued or incurred on` (ie-repeal.l4) |
| s 27(1)(d) | a penalty, forfeiture or punishment incurred for an earlier offence | `the repeal does not affect a penalty, forfeiture or punishment for an offence or contravention committed on` (ie-repeal.l4) |
| s 27(1)(e) | legal proceedings pending at the time of the repeal | `the repeal does not prejudice or affect the legal proceedings` (ie-repeal.l4) |
| s 27(2) | the power to institute, continue or enforce proceedings and to impose and carry out a penalty | `the proceedings may be instituted, continued or enforced, and the penalty imposed and carried out, as if the enactment had not been repealed` (ie-repeal.l4) |

**Provisions that create no relation (`none`).**

| provision | reason |
| --- | --- |
| s 1(1), s 1(2) | short title; the Act's own commencement: they name no party |
| s 2(1) (four definitions), s 2(2) | definitions, and a deeming of repeal: no party |
| s 3(1), s 3(2)(a), (b) | the repeal of four Acts, and a saving of meaning: no party (the persons whose rights arose under them are in s 27) |
| s 4(1), s 4(2) | application and contrary intention: no party |
| s 5(1), s 5(2) | a direction to whoever construes a provision, in the passive ("shall be given a construction"): names no bearer |
| s 7(2) | a presumption about a copy of an Act: evidence, not a relation |
| s 9, s 10, s 11, s 13 | rules of reading, continuity, examples and judicial notice: no party |
| s 12 | a validity rule for a form used: names no holder and no counterparty |
| s 14(1), s 14(2), s 14(3) | a permission to cite, a reading of citations, and a permission to omit commas: no one holds a claim that another not cite or not omit |
| s 15(1), s 16(1) to (4) | the date of passing, and when provisions come into operation: no party |
| s 18(a) to (j) | rules of reading: no party. s 18(j) widens who is within an offence provision and creates no relation of its own |
| s 19, s 20(1), s 20(2), s 21(1), s 21(2) | rules of meaning: no party |
| s 26(1), s 26(2)(d), (e), (f) | continuity of a repealed enactment, a deeming of an instrument, and rules of reading: no party |
| s 27(1)(a), (b) | what a repeal does not revive and does not affect: no party |
| the Schedule, Parts 1 and 2 | defined words: no party |
| the "Acts Referred to" table | a table of citations: no party |
| the title, long title, enacting words, date, headings and arrangement | not operative: no party |

## Changes to existing modules

Made on 2026-10-29 after the independent test pass, for one defect (finding 13), in three edits to the same lookup.
No pass-1 module or test was edited; the two files changed are pass-2 files, and the 20 pass-1 files still carry the modification time of the copy made when pass 2 began.
Nothing else was changed, and nothing the reviewer recorded as a known limit was touched.

The first edit split each listed phrase into its constituents; the reviewer then showed that this made the Act's own printed phrases refuse, so the second edit made both forms members for land, writing and functions (F48); the third edit applied the same rule to oath, swear and Great Britain after a sweep of all 40 Schedule entries.
The table gives the state after the third edit.

| file | what changed | why | text |
| --- | --- | --- | --- |
| `ie-schedule-definitions.l4` | `Part 1 entry: land`: the members were "tenements", "hereditaments", "houses and buildings", "land covered by water", "any estate, right or interest in or over land" (5). They are now those five and also "houses", "buildings", "any estate in or over land", "any right in or over land", "any interest in or over land" (10). | A query for a thing the line lists was answered "not answered" when it named a part of a printed phrase, and, after the first edit, when it named the printed phrase. | line 228: "land" includes tenements, hereditaments, houses and buildings, land covered by water and any estate, right or interest in or over land |
| `ie-schedule-definitions.l4` | `Part 1 entry: writing`: "other modes of representing or reproducing words in visible form" stays a member and "other modes of representing words in visible form" and "other modes of reproducing words in visible form" are added (6 members to 8). | as above | line 247 |
| `ie-schedule-definitions.l4` | `Part 2 entry: functions`: the members were "powers and duties" and the whole second clause (2). They are now "powers and duties", "powers", "duties", "the exercise of the powers and the carrying out of the duties", "the exercise of the powers", "the carrying out of the duties" (6). The whole second clause is no longer a member: it is a statement about references to the performance of functions, not an item of the list. | as above; the case the reviewer raised | line 252: "functions" includes powers and duties, and references to the performance of functions include, with respect to powers and duties, references to the exercise of the powers and the carrying out of the duties |
| `ie-schedule-definitions.l4` | `Part 1 entry: oath`: "affirmation or declaration" added to "affirmation" and "declaration" (2 members to 3). | The line prints the joined phrase; a caller may use it. | line 233: "oath", in the case of a person for the time being allowed by law to affirm or declare instead of swearing, includes affirmation or declaration |
| `ie-schedule-definitions.l4` | `Part 1 entry: swear`: "affirm and declare" added to "affirm" and "declare" (2 to 3). | as above | line 244: "swear", in the case of a person for the time being allowed by law to affirm or declare instead of swearing, includes affirm and declare |
| `ie-schedule-definitions.l4` | `Part 1 entry: Great Britain`: "the Channel Islands or the Isle of Man" added to "the Channel Islands" and "the Isle of Man" (2 to 3). All three are things the entry does not include. | as above | line 226: "Great Britain" does not include the Channel Islands or the Isle of Man |
| `tests-schedule-definitions.l4` | Part A: the counts for land (5 to 10), writing (6 to 8), functions (2 to 6), oath (2 to 3), swear (2 to 3) and Great Britain (2 to 3), and `elem` assertions for the printed phrases and the constituents; the `elem` assertions for the whole second clause of "functions" were replaced. Part B: each printed phrase and each constituent is asserted a member (for oath and swear under both values of the case flag, and for Great Britain as not included); things the line does not list are asserted REFUSED with the message ("privileges", "the exercise of the duties", "speech", "a motor vehicle", "houses and gardens", "any lease, estate or interest in or over land", "affirmation or promise", "affirm and promise", and "Scotland"). | The old assertions asserted the old whole-string behaviour; none was deleted without a replacement for the same entry. | lines 226, 228, 233, 244, 247, 252 |

Net assertions in `tests-schedule-definitions.l4`: 383 to 421 (+20 from the first edit, +8 from the second, +10 from the third).
Comments citing F48 were added after the entries in the module and above the changed assertions in the test file.

**The sweep.** All 40 Schedule entries (32 in Part 1, 8 in Part 2, lines 217 to 257 of the text) were read by script on 2026-10-29: the script took each entry's line, classified it as `means`, `includes` or `does not include` from the words after the defined term, and printed the entry's list text with its top-level segments and the segments that still contain "and" or "or".
It found 7 entries that are not `means`, and the verdict on each is:

| entry | verdict |
| --- | --- |
| Pt 1 "land" | extended (printed items "houses and buildings" and "any estate, right or interest in or over land"; the constituents) |
| Pt 1 "writing" | extended ("other modes of representing or reproducing words in visible form"); the last item ("any information kept in a non-legible form, whether stored electronically or otherwise, which is capable by any means of being reproduced in a legible form") has no constituents, because "whether stored electronically or otherwise" qualifies it and lists nothing |
| Pt 2 "functions" | extended ("powers and duties"; "the exercise of the powers and the carrying out of the duties"); "with respect to powers and duties" is a qualifier, not an item |
| Pt 1 "oath" | extended ("affirmation or declaration") |
| Pt 1 "swear" | extended ("affirm and declare") |
| Pt 1 "Great Britain" | extended ("the Channel Islands or the Isle of Man") |
| Pt 1 "affidavit" ("includes declaration") | checked and left: one item and no joiner |

The other 33 entries say "means".
`the entry names the thing` refuses for them ("an entry that says what a word means is not a list of inclusions"), so their member lists are never queried and were not changed.
Three of them (Pt 1 "President", Pt 2 "Companies Acts" and "Social Welfare Acts") hold lists split at "or" or "and" for the Part A checks; their printed form is the whole definition and not an item of a list.

Outside the Schedule: s 2(1) "repeal" ("includes revoke, rescind, abrogate or cancel") was checked and left alone, a closed enumeration with one constructor for each word, tested one by one in `tests-general.l4`.
s 2(1) "statutory instrument" ("references ... include references to made, issued, granted or otherwise created") was checked and left alone: it is a boolean over the definition, not a list of members that a caller queries.

**Check.** `check.sh` after the third edit: 26 modules, 1322 satisfied (only `tests-schedule-definitions.l4` moved, 383 to 421), 8 failed (expected), 0 refused; srcrefs 438 src lines, 254 runs, 312 locators, 0 problems under `--strict` and `--refs`.
Controls: the test file against the module as it stood before the first edit gives 14 failed assertions; against the constituents-only module (after the first edit) it gives 8; against the module with the three entries of the third edit reverted it gives 6 failed assertions and the printed-phrase assertions for them do not answer.

## 11. Independent test pass

A separate agent that had not seen this encoding, its NOTES.md or its brief wrote `ANSWERS.md` from the text alone before it opened any `.l4` file: 393 numbered scenarios over every Part, section and Schedule entry, including cases where the text is silent.
It then wrote `tests-independent.l4`, one `#ASSERT` per scenario that the encoding has a function for, and ran it against this encoding.
`ANSWERS.md` is not kept in this folder; the scenario numbers `S<n>` in `tests-independent.l4` refer to it, and each assertion carries its provision and text line.

| step | assertions | satisfied | failed | refused |
| --- | --- | --- | --- | --- |
| first run against the pass-2 encoding | 362 | 348 | 2 | 12 |
| after the includes-list fix and the reconciliation below | 362 | 362 | 0 | 0 |

The 31 scenarios the encoding has no function for are the `GAP` lines in the test file (31 + 362 = 393); they are limits of the encoding, not passes.

**What the 14 disagreements turned out to be.**

- **Four were an encoder defect, now fixed.** The lookup for Schedule entries that say "includes" held each comma-separated phrase as one member, so "houses" was not a member of "land" although the Act names it.
  Part 1 "land" and "writing" and Part 2 "functions" now hold both the phrase as the Act prints it and each thing inside it, and the same was done for "oath", "swear" and "Great Britain" after a script sweep of all 40 Schedule entries (fork F48 and finding 13 give the detail).
  A first version of the fix held only the constituents, which made the Act's own printed phrases refuse; the independent file caught that too, and both forms are members now.
- **Ten were the independent author's expectation, not the encoding, and are reconciled in the test file.**
  Each is rewritten in place (`#ASSERT REFUSED`, or `#ASSERT NOT` where the Act names a list that does not close), with a `-- RECONCILED S<n>` comment above it that quotes the original assertion and gives the reason; none is deleted.
  S186 and S188 rest on fork F8 (nothing in section 18(h) moves a last day that falls on a day of rest, recess or holiday), S202 on fork F5 (a period of months that does not begin on the first of a month), S218 on section 19 with section 4(1) (where a contrary intention appears the Act does not say what the word then means), S239 and S240 on section 22(3) (a list of what a power is read as including does not say it excludes anything else), and S324 and S349 on the open "includes" lists of "land" and "writing".
  S269 and S295 rest on the convention that `FALSE` means "the section does not give it", not "the thing is lost": the Act does not say the security lapses, or that a right never acquired is unprotected, so the assertion is `#ASSERT REFUSED`.
  Read the `RECONCILED` comments before relying on any of the ten.

**Known limits shown by the gaps.** The encoding answers whole days, not times of day (S6, S136, S211); it has no membership function for `means` entries (S302, S303, S331, S338, S340, S342, S344, S367); and it takes "clear days", "like consent" and the unless-the-contrary-is-proved limb of section 25 as inputs or not at all (S190, S238, S260). The others are one-line comments in the file.

**Check.** `check.sh` with `tests-independent.l4` in the folder: 27 modules, 1684 satisfied, 8 failed (the expected eight in `tests-red-control.l4`), 0 refused, run on 2026-10-29 with the same binary as the other counts in this file.
