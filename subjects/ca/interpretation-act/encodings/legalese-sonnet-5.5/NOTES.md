# NOTES: Interpretation Act (Canada), R.S.C., 1985, c. I-21

Row `legalese-sonnet-5.5`: one Sonnet 5.5 agent working alone, no subagents, no other encoding read.
Pass 1 (2026-10-21) wrote the time, calendar, repeal and rules modules from `BRIEF-pass1.md`.
Pass 2 (2026-10-29) is the completion pass to "whole" (Meng's ruling of 2026-10-22): every unit of the text has a row below, and the modules `nouns`, `reading`, `powers` and `definitions` and the test files `definitions`, `reading`, `powers` and `schedule` are new.
Pass 3 (2026-10-29) answers an independent test pass (an author who had not seen these notes ran 635 assertions; the lead's message gives 583 satisfied, 5 failed, 47 refused, and says the lead triaged all 52 against the Act and sent back the items that were this encoding's).
It adds the modules `commencement` and `resolutions` and the test files `transition` and `resolutions`, corrects two defects and one wrongly inert row, and registers more forks: see `## Changes to existing modules` and `## Pass 3`.
Version 0.3.0. Status: `draft`. No domain expert has read it against the statute.

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
- **Target.** The pass-2 brief names `unstable` (the folder uses `REFUSE`, `@lang en`, `#ASSERT REFUSED` and `YMD`, which a `main` build rejects; `references/dialects.md` of the writing-l4-rules skill).
  `check.sh` was run with `L4_TARGET=unstable`, and the main comparison was not made.
- **Binary.** Pass 2 ran `l4-unstable-0528`, whose `--version` line is `unstable-20261028-5e95b5a (unstable, 5e95b5a, 2026-10-28)`, sha256 `0f0f1b86d37164af242ca2b6c03aa31ddeedef752bd10474f1459b78cf539e9d` (the hash the brief gives; recomputed with `shasum -a 256` on 2026-10-29).
  Pass 1 used another build (`dev`, sha256 `2d912dd2...07d7`); the pass-2 baseline run of the unchanged pass-1 files gave the same numbers with the new binary.
- **One Hint on every module.** The linter prints, for the line `@lang en`: "A module that declares nothing is English; this line can go." The brief requires the line, so it stays; the Hint is not an error and is not counted by `check.sh`.

## Re-disposition audit

Written on 2026-10-29, **before any new L4**, from the raw text (`R.S.C.-1985-c.-I-21.txt`, sha256 `ea96eac5...8c15`) and pass 1's coverage table.
Pass 2 does not trust pass 1's dispositions; each is re-derived below.
The numbers in this section are from the audit date; the final coverage counts are in the coverage-table section, and `coverage.py` regenerates both.

### Counts

`units.py` reads the raw file and prints every unit, so the count is a script's, not a reader's.
**354 units**: title block 3 (title, citation, long title); group headings 35; sections with no subsections 23; subsections 83; paragraphs 56; subparagraphs 5; closing words after a list of paragraphs 3 (ss 8(2.2), 22(2)(a), 43); definition entries 61 (6 in s 2(1), 55 in s 35(1), of which 5 are shown repealed); paragraphs and closing words inside definition entries 32; the Schedule heading 1 and its 51 rows; the Related Provisions item 1.

- **Marginal notes are labels, not units.** There are 104 of them (the italic heading in front of a section or subsection). Section 14 of the Act says marginal notes form no part of the enactment, so each is carried as the label of its provision's row. If a reviewer counts them as units the total is 458 and every one of the 104 is `inert` reason 1 (a heading).
- **Lines 1 to 3 of the raw file** are the depositor's notice (UNOFFICIAL TEXT, source URL, omitted notes), not the Act, and are not units.
- **The enacting clause quoted in s 4(1)** (line 38) is part of unit s 4(1), not a unit.
- **Pass 1's table had 94 rows.** Against the 354 units: 139 units have a pass-1 row that names them (`row`); 176 are covered only by an aggregate row that does not name them (`group`: the 41 s 35(1) definitions in one row, the 51 Schedule entries in one row, every paragraph under its subsection's row); 39 have no row at all (`none`).
- **Pass 2's table has 354 rows**, one per unit, generated by `coverage.py` from `dispositions.txt`, which refuses to print the table unless every unit matches exactly one line.

The 39 units with no pass-1 row: the title, the citation and the long title; the chapeaux `s 2(1)` ("In this Act,") and `s 35(1)` ("In every enactment,"); and 34 group headings (Short Title, Interpretation, Application, Enacting Clause of Acts, Operation, Royal Assent, Day Fixed for Commencement or Repeal, Regulation Prior to Commencement, Territorial Operation, Rules of Construction, Property and Civil Rights, Indigenous Peoples, Private Acts, Law Always Speaking, Imperative and Permissive Construction, Enactments Remedial, Preambles and Marginal Notes, Application of Interpretation Provisions, Her Majesty, Proclamations, Oaths, Reports to Parliament, Corporations, Majority and Quorum, Appointment, Retirement and Powers of Officers, Evidence, Computation of Time, Miscellaneous Rules, Offences, Powers to Enter Dwelling-houses to Carry out Arrests, Definitions, References and Citations, Repeal and Amendment, Demise of Crown).
Titles and headings are `inert`, reason 1.
The two chapeaux are rules: they say where the definitions apply, and they are encoded.

### The rules the table follows

- **Dispositions.** `encoded`, `inert` (three reasons only), `fork`, `repealed`. "Not applicable" is not a disposition: pass 1's two such rows were made `inert` (reason 2) in pass 2; one of them, the Related Provisions item, is `encoded` since pass 3 (see the table below and `## Pass 3`).
- **Inert reasons used.** 1 (not operative: the title block, group headings, the Schedule heading): 39 units. 2 (machinery): s 1 (short title): 1 unit. 3 is the `repealed` disposition.
  Reason 2 means machinery that only operates the Act: a short title, a commencement clause, a repeal of what is already repealed.
  A provision that tells someone what to do or says what a thing is is not machinery, however old, and "it affects no one now" is not a reason.
  Pass 2 filed the Related Provisions item under reason 2 on exactly that ground; pass 3 corrected it.
- **A unit is `fork` exactly when the fork register has an entry licensed by that unit.** Pass 1 listed forks in a register but marked the rows `encoded`; that made `fork` mean nothing. `coverage.py` enforces the rule both ways (a fork id on a non-fork row, or a fork row with no id, is an error).
- **The register is sorted into two classes**, so that `fork` is kept for a text that can be read two ways with different outcomes. Class A: text forks, attached to units. Class B: conventions of the encoder (not a reading of the text), settled-by-the-text entries (the text decides, there is no second licensed reading), and silences (the text says nothing). Pass 1's 36 entries sort into 17 class A and 19 class B (list below); pass 2 added 8 class A, and pass 3 adds 7 (6 new entries, and F-39-AFFIRM moved from class B).
- **Seat.** The Guide asks for a seat layer for the individual. The brief for this pass asks for none, the folder has none, and none was added; NOTES.md says so under what would need doing.

### Verdict on every pass-1 row that is not `encoded`

Pass 1 had 30 `inert` rows, 2 `repealed or blank` rows and 2 `not applicable` rows.
Its own reasons for the 30 inert rows are the ones the brief now rules out: "a reading rule", "addresses an official", "refers to another Act not in the text", "no input from which an answer would differ", "an interpretive canon".

| pass-1 row (text lines) | pass-1 disposition | verdict | pass 2 |
| --- | --- | --- | --- |
| s 1 short title (11) | not applicable | keeps: machinery (short title) | inert, reason 2 |
| s 2(1) "Act", "enact", "enactment", "public officer", "repeal" (16-19, 23) | inert | moves: a definition is encoded | encoded; "public officer" is a fork (F-PUBLIC-OFFICER) |
| s 3(2) application to this Act (31) | inert | moves: a rule with one answer is still a rule | fork (F-3-2) |
| s 3(3) rules of construction not excluded (33) | inert | moves | encoded |
| s 4(1), (2) enacting clause (37-40) | inert | moves: states a form and an order | encoded |
| s 5(1) endorsement of assent (46) | inert | moves: "addresses an official" is not a reason | encoded |
| s 8(3) pre-1931 Acts (81) | inert | moves: the intention is a plain input | encoded |
| s 8.1 property and civil rights (87) | inert | moves: the provincial rules are a borrowed fact | encoded |
| s 8.3(1), (2) Indigenous peoples (93-95) | inert | moves: the Constitution Act term is a borrowed fact | encoded |
| s 10 law always speaking (103) | inert | moves: "a canon" is not a reason | encoded |
| s 12 enactments remedial (111) | inert | moves: which construction best attains the objects is a plain input | encoded |
| s 13 preamble (115) | inert | moves | encoded |
| s 14 marginal notes (117) | inert | moves; two readings of the scope | fork (F-14-SCOPE) |
| s 15(1), (2) (121-125) | inert | moves; (1) and (2)(a) conflict on a contrary intention | fork (F-15) |
| s 16 words in regulations (127) | inert | moves | encoded |
| s 18(1), (2) proclamations (135-137) | inert | moves: "identities with no input" is not a reason | encoded |
| s 21(2) corporate name (162) | inert | moves | encoded |
| s 23(4) remuneration (186) | inert | moves: a grant of power is a rule | encoded |
| s 24(1)-(5) implied powers (190-205) | inert | moves: the facts about offices are plain inputs | encoded |
| s 25(2) Queen's Printer (211) | inert | moves; "Queen's" against the King | fork (F-QUEENS) |
| s 31(1)-(4) miscellaneous powers (238-244) | inert | moves | encoded |
| s 33(1)-(3) gender, number, grammatical forms (248-252) | inert | moves: encoded over a typed representation of the words | encoded |
| s 34.1 entry into dwelling-houses (269-271) | inert | moves: the Criminal Code terms are borrowed facts | encoded |
| s 35(1), the other 41 definitions (276-360) | inert | moves: each is a row of its own | encoded; two are forks ("Canada", "Governor General in Council"), and paragraph (c) of "superior court" is a fork |
| s 36 telegraph (364) | inert | moves: "a constant with no input" is not a reason | encoded |
| s 38 common names (373) | inert | moves | encoded |
| s 40(1) citation (385-387) | inert | moves | encoded |
| s 40(2) citation includes amendment (389) | inert | moves; pass 1 saw that the Act names no date | fork (F-40-2-DATE) |
| s 41(2)-(5) (393-399) | inert | moves: the enclosing enactment or provision is a plain input | encoded |
| s 42(1)-(3) (403-407) | inert | moves: a reservation of power is a Hohfeld relation | encoded |
| s 45(1)-(4) (430-436) | inert | moves: the text says "shall not be deemed", so the answer is stated | encoded |
| s 18(4), s 35(1) five repealed entries (140, 295, 300-302, 315) | repealed or blank | keeps | repealed (6 units) |
| Related Provisions, 1998, c. 30, s. 10 (499-503) | not applicable | pass 2 kept it out of the code as "a transitional provision ... it affects no one now", and that was wrong (corrected 2026-10-29): "it affects no one now" is not a reason the brief allows, and the text is operative, because it says how a proceeding commenced before the section came into force is carried on; a proceeding of that age could in principle still be running | encoded in `ca-interpretation-commencement.l4`, with a Hohfeld row (R1998-10) |
| Schedule (446-497) | encoded | keeps; but pass 1 tested 6 of 51 names | encoded, with `ca-tests-schedule.l4` testing all 51 against the text |

Of the 30 pass-1 inert rows, **0 stay inert**: every one moves to `encoded` or `fork`.

### Pass-1 rows that were `encoded` and become `fork`

Under the rule above these units carry class A forks (the rule they encode is unchanged): s 5(3), 6(1), 6(2) (F-FIXED-LATER, F-DAY); s 26 (F-26-UNITS, F-26-GAP, F-26-ON-HOLIDAY); s 27(4), 27(5), 28 (F-FROM, F-LASTDAY, F-BEFORE); s 30 (F-DAY, F-30-LEAP); s 34(1)(a), (b) (F-34); s 35(1) "standard time" (b)-(e) (F-STD-TIME); s 37(1) (F-YEAR, F-FROM); s 39(1)(a)-(d) (F-39-THEN, F-39-LAYING); s 39(2) (F-39-2-MOMENT); s 43(d), 43 closing words, 44(e) (F-44-E); s 2(1) "regulation" (F-REG-DEF); s 35(1) "holiday" (F-HOLIDAY-BIRTHDAY, new in pass 2 but attached to a row pass 1 had as encoded).

### Pass 1's 36 fork entries, sorted

- **Class A, kept (17), attached to units:** F-DAY, F-FROM, F-LASTDAY, F-BEFORE, F-YEAR, F-26-UNITS, F-26-GAP, F-26-ON-HOLIDAY, F-FIXED-LATER, F-REG-DEF, F-39-THEN, F-39-LAYING, F-39-2-MOMENT, F-30-LEAP, F-STD-TIME, F-34, F-44-E.
- **Class B, conventions of the encoder (5):** F-LANG, F-TARGET, F-NEGATIVE, F-BOUNDS, F-HOLIDAYS.
- **Class B, settled by the text (9):** F-COUNT-START (ss 27(4), 27(5), 28(b) say the day is not included), F-MONTH (s 35(1) "month", s 28(c)), F-26-WHICH (s 26 says "holiday"), F-26-SEVERAL (s 26: "the day next following that is not a holiday"), F-6-MOMENT (s 6(1): "the expiration of the previous day"), F-ASSENT (the text keys on assent), F-REG-SILENT (s 6(2)(b) decides by two borrowed facts), F-23-3 (s 23(3): "more than sixty days"), F-22 (for whole numbers "at least one-half" gives the same answer whether or not it is rounded up).
- **Class B, silences (5):** F-WEEK, F-SERVICE, F-6-3, F-39-AFFIRM, F-41. (Pass 3 moved F-39-AFFIRM to class A.)

The reclassification changes what `fork` means in the table, not any rule or test.

### Final counts (the coverage table below, run `coverage.py counts`)

```
units: 354
  encoded: 261
  fork: 47
  inert: 40
  repealed: 6
inert by reason: {'1': 39, '2': 1}
pass-1 coverage of the units: {'group': 176, 'none': 39, 'row': 139}
units by kind: {'closing': 3, 'def-closing': 1, 'def-paragraph': 31, 'def-repealed': 5, 'definition': 56, 'group': 35, 'paragraph': 56, 'related': 1, 'schedule-head': 1, 'schedule-row': 51, 'section': 23, 'subparagraph': 5, 'subsection': 83, 'title': 3}
```

Rows in the table: 94 before (pass 1), 354 after (pass 2), 354 after pass 3.
Units with no pass-1 row: 39, all now in the table (title block 3, chapeaux 2, group headings 34).
Inert at the end: 40, of which 39 are reason 1 (the title block 3, the 35 group headings, the Schedule heading) and 1 is reason 2 (s 1, the short title); reason 3 is the `repealed` disposition (6 units).
After pass 2 the counts were encoded 267, fork 40, inert 41, repealed 6; pass 3 moved one row from inert to encoded and seven rows from encoded to fork (list in `## Pass 3`).

## 1. What is encoded

Ten modules and fourteen test files (counts in section 6).
Imports: the time and repeal modules import `prelude` and `daydate`; the calendar module imports `prelude`, `daydate` and the time module; the rules module imports `prelude`; `nouns` imports `prelude`; `reading` imports `prelude`, `daydate` and `nouns`; `powers` imports `prelude`; `definitions` imports `prelude`, `nouns`, `rules` and `reading`; `commencement` imports `prelude` and `daydate`; `resolutions` imports `prelude`.

**Pass 1** (unchanged in pass 2; changed in two places in pass 3, see "Changes to existing modules"):

- **Time module** (`ca-interpretation-time.l4`): the last day of a period of N days, months or years after, from or before a day (ss 27(4), 27(5), 28, 37(1)); the clear-day and between-events counts (s 27(1), (2)); the words that tie a time to a day (s 27(3)-(5)); whether a date falls inside a period; the last day on which a thing may be done when the time ends on a holiday (s 26), for periods in days, months and years and for several holidays in a row; the day, and the moment within the day, from which an Act, a regulation, a provision postponing its own commencement and a proclamation bind or take effect (ss 5, 6, 7, 18(3), 23(2), (3), (5)); when an enactment ceases to have effect (s 6(1)); age (s 30); the calendar, financial and Dominical year (s 37); the calendar month (s 35(1)); the time within which a regulation is laid before Parliament (s 39(1)); the definition of "regulation" (s 2(1)).
- **Calendar module** (`ca-interpretation-calendar.l4`): the three days of "holiday" that the text dates; the combination with the caller's holidays and with s 26; "commencement"; "standard time" and s 29; "local time" (refused).
- **Repeal module** (`ca-interpretation-repeal.l4`): ss 2(2), 39(2), 43, 44, 46.
- **Rules module** (`ca-interpretation-rules.l4`): ss 3(1), 8(1)-(2.2), 8.2, 9, 11, 17, 19, 20, 21(1), (3), 22, 23(1), 25(1), 32, 34, 35(1) "corporation" and "security", 41(1), 35(2) and the Schedule.

**Pass 2** (new):

- **Nouns module** (`ca-interpretation-nouns.l4`): types only, shared by the other new modules: kinds of instrument, the thirteen provinces and territories, the parts of an enactment as printed, the kinds of division a reference points at, what a word imports, grammatical number, forms of a word, ways of citing an enactment.
- **Reading module** (`ca-interpretation-reading.l4`): the rules for reading an enactment that pass 1 had marked inert: ss 3(2), 3(3), 4, 5(1), 8(3), 8.1, 8.3, 10, 12, 13, 14, 15, 16, 18(1)-(2), 21(2), 25(2), 33, 36, 38, 40, 41(2)-(5), 42, 45. Each rule is a function over a small typed representation of what it operates on (a part of the printed text, a kind of division, what a word imports, what is done to an enactment).
- **Powers module** (`ca-interpretation-powers.l4`): ss 23(4), 24(1)-(5), 31(1)-(4), 34.1.
- **Definitions module** (`ca-interpretation-definitions.l4`): every defined term of s 2(1) and s 35(1) that pass 1 did not encode (all but "commencement", "corporation", "security", "holiday" dates, "month", "local time", "standard time", "Commonwealth", "British Commonwealth" and "regulation", which pass 1 encoded in the calendar, rules and time modules): a table, `A definition`, with the terms it defines, its section, the word the Act uses, the members it names, what it excludes and what it points at; one generic function, `the term defined by` d `covers` x, that answers "is x within this term?" by the Act's own words; and a bespoke function for each term that turns on facts (a transmission's frequency, how many justices, the zones of the sea by state, the kinds of holiday, the superior courts by place). Plain gloss in the heading comment of each entry. The chapeaux "In this Act," and "In every enactment," are encoded as `a definition of section 2(1) applies` and `a definition of section 35(1) applies`.

**Pass 3** (new, 2026-10-29, after the independent test pass):

- **Commencement module** (`ca-interpretation-commencement.l4`): the precondition of s 5(4) (`section 5(4) deems a provision of an Act to have come into force on the date of assent, given that` ..., and the date it deems); the permission of s 7 (`a power of the kind` k `may be exercised before the commencement of the enactment where` ..., for a power to make regulations or to do any other thing); and the Related Provisions item, 1998, c. 30, s. 10 (a proceeding commenced before that section came into force is taken up and continued under the amended provision, without any further formality).
- **Resolutions module** (`ca-interpretation-resolutions.l4`): s 39(1)(a) to (d): the body a regulation is laid before, which House or Houses a resolution of each expression needs, whether coming into force depends on a resolution, whether a regulation can have come into force once affirmed, and whether it is annulled.
- **Definitions module, added to**: s 3(1) by kind of instrument (`the provisions of the Act apply to an instrument of the kind` k `unless` ...), built on the module's own test of what an enactment is.

**Holidays, days of rest and recess are inputs.**
The time module takes a function `DATE -> BOOLEAN` from the caller and has no calendar.
The calendar module adds the three days the text dates and leaves the rest, which the text names without a date, to the caller.
The definitions module sorts the kinds of day that "holiday" lists (`A kind of day`) and adds the place condition on a provincial or civic holiday.

**Borrowed terms are asked as facts.** The Bank Act (is the bank listed in Schedule I or II), the Oceans Act (the extent of the zones of the sea is a pointer, not computed), the Criminal Code (s 34.1: is the requirement of subsection 529.4(1) met), the Constitution Act, 1982 (s 8.3: is the right one recognised and affirmed by section 35; is the people within "aboriginal peoples of Canada"), the Statutory Instruments Act (ss 6(2)(b), 24(3)), the National Defence Act ("regular force", "reserve force"), the Canada Evidence Act ("statutory declaration"). None is imported.

**Refused, never defaulted** (the text is silent or names only some cases): weeks; deemed service or notice; a day of rest, recess or closed office that is not a holiday; a count that is not a whole number of at least one; an anniversary that does not exist (s 30); an Act whose day is still to be fixed; a regulation that is neither registered nor of an exempted class; a boundary meridian; the cases each of ss 3(3), 4(1), 8(2.1), 8(2.2), 8(3), 8.1, 8.3, 10, 13, 14, 15(2)(b), 16, 18, 19, 20, 21, 22, 24, 25, 31, 32, 33, 34, 34.1, 36, 38, 40, 41, 42, 43, 44, 45 and 46 does not name; every `includes` definition for a thing it does not name (thirteen of them).

**Nothing is left out.** Every unit of the text has a row in section 2. The inert rows are the title block, the headings, the Schedule heading and the short title; none of the thirty pass-1 inert rows stays inert, and the Related Provisions item, which pass 2 had filed as inert, is encoded.

## 2. Coverage table

One row per unit of the text: 354 rows, generated by `coverage.py table` from `dispositions.txt` and `units.py` (which reads the raw text).
`python3 -I coverage.py <raw text> check --strict` reports 0 problems: every unit has exactly one disposition, every `fork` row names a fork id, every `encoded` and `fork` row names a module heading and a test heading that exist as section lines of the named files, and every relation key is in `relations.txt`.
"Lines" are lines of the deposited text (the numbering `srcrefs.py` uses).
"Pass 1" says what pass 1's table had for the unit: `row` (a row named it), `group` (only an aggregate row covered it), `none` (no row).
"Where" is `module::heading` and "tests" is `tests::heading`, for the file `ca-interpretation-<module>.l4` or `ca-tests-<tests>.l4`.
A marginal note is the label of its provision's row, not a unit (audit, above).
Dispositions: `encoded`; `fork` (the unit is read two ways, and the fork id is a class A entry of section 3); `inert (n)` with the reason number 1, 2 or 3 of the brief; `repealed` (the text shows "[Repealed, ...]").

| unit | lines | disposition | forks | pass 1 | where | tests |
| --- | --- | --- | --- | --- | --- | --- |
| title | 5 | inert (1) |  | none | - | - |
| citation | 6 | inert (1) |  | none | - | - |
| long title | 7 | inert (1) |  | none | - | - |
| H: Short Title | 9 | inert (1) |  | none | - | - |
| s 1 | 11 | inert (2) |  | row | - | - |
| H: Interpretation | 13 | inert (1) |  | none | - | - |
| s 2(1) | 15 | encoded |  | none | definitions::where the definitions apply | definitions::where the definitions apply |
| s 2(1) "Act" | 16 | encoded |  | row | definitions::s 2(1) "Act" | definitions::s 2(1) "Act" |
| s 2(1) "enact" | 17 | encoded |  | row | definitions::s 2(1) "enact" | definitions::s 2(1) "enact" |
| s 2(1) "enactment" | 18 | encoded |  | row | definitions::s 2(1) "enactment" | definitions::s 2(1) "enactment" |
| s 2(1) "public officer" | 19 | fork | F-PUBLIC-OFFICER | row | definitions::s 2(1) "public officer" | definitions::s 2(1) "public officer" |
| s 2(1) "regulation" | 20 | fork | F-REG-DEF | row | time::Section 2(1): "regulation" | commencement::Section 2(1) "regulation" |
| s 2(1) "regulation" (a) | 21 | fork | F-REG-DEF | row | time::Section 2(1): "regulation" | commencement::Section 2(1) "regulation" |
| s 2(1) "regulation" (b) | 22 | fork | F-REG-DEF | row | time::Section 2(1): "regulation" | commencement::Section 2(1) "regulation" |
| s 2(1) "repeal" | 23 | encoded |  | row | definitions::s 2(1) "repeal" | definitions::s 2(1) "repeal" |
| s 2(2) | 25 | encoded |  | row | repeal::Section 2(2) | repeal::Section 2(2) |
| H: Application | 27 | inert (1) |  | none | - | - |
| s 3(1) | 29 | encoded |  | row | rules::Section 3(1), section 8(1) and section 9 ; definitions::Section 3(1) | rules::Sections 3(1), 8(1), 9 and 17 ; definitions::Section 3(1) |
| s 3(2) | 31 | fork | F-3-2 | row | reading::Section 3(2) | reading::Section 3(2) |
| s 3(3) | 33 | encoded |  | row | reading::Section 3(3) | reading::Section 3(3) |
| H: Enacting Clause of Acts | 35 | inert (1) |  | none | - | - |
| s 4(1) | 37 | encoded |  | row | reading::Section 4 | reading::Section 4 |
| s 4(2) | 40 | encoded |  | row | reading::Section 4 | reading::Section 4 |
| H: Operation | 42 | inert (1) |  | none | - | - |
| H: Royal Assent | 44 | inert (1) |  | none | - | - |
| s 5(1) | 46 | encoded |  | row | reading::Section 5(1) | reading::Section 5(1) |
| s 5(2) | 48 | encoded |  | row | time::Sections 5 and 6 | commencement::Worked case 1 |
| s 5(3) | 50 | fork | F-FIXED-LATER,F-5-3-THAT | row | time::Sections 5 and 6 | commencement::Worked case 1 ; commencement::Worked case 2 |
| s 5(4) | 52 | encoded |  | row | time::Sections 5 and 6 ; commencement::Section 5(4) | commencement::Worked case 1 ; transition::Section 5(4) |
| H: Day Fixed for Commencement or Repeal | 54 | inert (1) |  | none | - | - |
| s 6(1) | 56 | fork | F-DAY,F-FIXED-LATER | row | time::Sections 5 and 6 ; time::Section 6(1), second limb | commencement::An Act that names a particular day ; commencement::An enactment expressed to expire |
| s 6(2) | 58 | fork | F-FIXED-LATER | row | time::Sections 5 and 6 | commencement::Worked case 2 |
| s 6(2)(a) | 59 | encoded |  | row | time::Sections 5 and 6 | commencement::Worked case 1 |
| s 6(2)(b) | 60 | encoded |  | row | time::Section 6(2)(b) and 6(3) | commencement::Worked case 3 |
| s 6(3) | 62 | encoded |  | row | time::Section 6(2)(b) and 6(3) | commencement::Section 6(3) |
| H: Regulation Prior to Commencement | 64 | inert (1) |  | none | - | - |
| s 7 | 66 | encoded |  | row | time::Section 7 ; commencement::Section 7 | commencement::Section 7 ; transition::Section 7 |
| H: Territorial Operation | 68 | inert (1) |  | none | - | - |
| s 8(1) | 70 | encoded |  | row | rules::Section 3(1), section 8(1) and section 9 | rules::Sections 3(1), 8(1), 9 and 17 |
| s 8(2) | 72 | encoded |  | row | rules::Section 3(1), section 8(1) and section 9 | rules::Section 8(2) |
| s 8(2.1) | 74 | encoded |  | row | rules::Section 3(1), section 8(1) and section 9 | rules::Sections 8(2.1) and 8(2.2) |
| s 8(2.2) | 76 | encoded |  | row | rules::Section 3(1), section 8(1) and section 9 | rules::Sections 8(2.1) and 8(2.2) |
| s 8(2.2)(a) | 77 | encoded |  | group | rules::Section 3(1), section 8(1) and section 9 | rules::Sections 8(2.1) and 8(2.2) |
| s 8(2.2)(b) | 78 | encoded |  | group | rules::Section 3(1), section 8(1) and section 9 | rules::Sections 8(2.1) and 8(2.2) |
| s 8(2.2) closing words | 79 | encoded |  | group | rules::Section 3(1), section 8(1) and section 9 | rules::Sections 8(2.1) and 8(2.2) |
| s 8(3) | 81 | encoded |  | row | reading::Section 8(3) | reading::Section 8(3) |
| H: Rules of Construction | 83 | inert (1) |  | none | - | - |
| H: Property and Civil Rights | 85 | inert (1) |  | none | - | - |
| s 8.1 | 87 | encoded |  | row | reading::Section 8.1 | reading::Section 8.1 |
| s 8.2 | 89 | fork | F-8-2-TERRITORIES | row | rules::Section 3(1), section 8(1) and section 9 | rules::Section 8.2 |
| H: Indigenous Peoples | 91 | inert (1) |  | none | - | - |
| s 8.3(1) | 93 | encoded |  | row | reading::Section 8.3 | reading::Section 8.3 |
| s 8.3(2) | 95 | encoded |  | row | reading::Section 8.3 | reading::Section 8.3 |
| H: Private Acts | 97 | inert (1) |  | none | - | - |
| s 9 | 99 | encoded |  | row | rules::Section 3(1), section 8(1) and section 9 | rules::Sections 3(1), 8(1), 9 and 17 |
| H: Law Always Speaking | 101 | inert (1) |  | none | - | - |
| s 10 | 103 | encoded |  | row | reading::Section 10 | reading::Section 10 |
| H: Imperative and Permissive Construction | 105 | inert (1) |  | none | - | - |
| s 11 | 107 | encoded |  | row | rules::Section 11 | rules::Section 11 |
| H: Enactments Remedial | 109 | inert (1) |  | none | - | - |
| s 12 | 111 | encoded |  | row | reading::Section 12 | reading::Section 12 |
| H: Preambles and Marginal Notes | 113 | inert (1) |  | none | - | - |
| s 13 | 115 | encoded |  | row | reading::Section 13 | reading::Section 13 |
| s 14 | 117 | fork | F-14-SCOPE | row | reading::Section 14 | reading::Section 14 |
| H: Application of Interpretation Provisions | 119 | inert (1) |  | none | - | - |
| s 15(1) | 121 | fork | F-15 | row | reading::Section 15 | reading::Section 15 |
| s 15(2) | 123 | fork | F-15 | row | reading::Section 15 | reading::Section 15 |
| s 15(2)(a) | 124 | fork | F-15 | group | reading::Section 15 | reading::Section 15 |
| s 15(2)(b) | 125 | fork | F-15 | group | reading::Section 15 | reading::Section 15 |
| s 16 | 127 | encoded |  | row | reading::Section 16 | reading::Section 16 |
| H: Her Majesty | 129 | inert (1) |  | none | - | - |
| s 17 | 131 | encoded |  | row | rules::Section 3(1), section 8(1) and section 9 | rules::Sections 3(1), 8(1), 9 and 17 |
| H: Proclamations | 133 | inert (1) |  | none | - | - |
| s 18(1) | 135 | encoded |  | row | reading::Section 18(1) and (2) | reading::Section 18(1) and (2) |
| s 18(2) | 137 | encoded |  | row | reading::Section 18(1) and (2) | reading::Section 18(1) and (2) |
| s 18(3) | 139 | encoded |  | row | time::Section 18(3) | commencement::Section 18(3) |
| s 18(4) | 140 | repealed |  | row | - | - |
| H: Oaths | 142 | inert (1) |  | none | - | - |
| s 19(1) | 144 | encoded |  | row | rules::Section 19 | rules::Section 19 |
| s 19(1)(a) | 145 | encoded |  | group | rules::Section 19 | rules::Section 19 |
| s 19(1)(b) | 146 | encoded |  | group | rules::Section 19 | rules::Section 19 |
| s 19(2) | 148 | encoded |  | row | rules::Section 19 | rules::Section 19 |
| H: Reports to Parliament | 150 | inert (1) |  | none | - | - |
| s 20 | 152 | encoded |  | row | rules::Section 20 | rules::Section 20 |
| H: Corporations | 154 | inert (1) |  | none | - | - |
| s 21(1) | 156 | encoded |  | row | rules::Section 21 | rules::Section 21 |
| s 21(1)(a) | 157 | encoded |  | group | rules::Section 21 | rules::Section 21 |
| s 21(1)(b) | 158 | encoded |  | group | rules::Section 21 | rules::Section 21 |
| s 21(1)(c) | 159 | encoded |  | group | rules::Section 21 | rules::Section 21 |
| s 21(1)(d) | 160 | encoded |  | group | rules::Section 21 | rules::Section 21 |
| s 21(2) | 162 | encoded |  | row | reading::Section 21(2) | reading::Section 21(2) |
| s 21(3) | 164 | encoded |  | row | rules::Section 21 | rules::Section 21 |
| H: Majority and Quorum | 166 | inert (1) |  | none | - | - |
| s 22(1) | 168 | encoded |  | row | rules::Section 22 | rules::Section 22 |
| s 22(2) | 170 | encoded |  | row | rules::Section 22 | rules::Section 22 |
| s 22(2)(a) | 171 | encoded |  | group | rules::Section 22 | rules::Section 22 |
| s 22(2)(a)(i) | 172 | encoded |  | group | rules::Section 22 | rules::Section 22 |
| s 22(2)(a)(ii) | 173 | encoded |  | group | rules::Section 22 | rules::Section 22 |
| s 22(2)(a) closing words | 174 | encoded |  | group | rules::Section 22 | rules::Section 22 |
| s 22(2)(b) | 175 | encoded |  | group | rules::Section 22 | rules::Section 22 |
| s 22(2)(c) | 176 | encoded |  | group | rules::Section 22 | rules::Section 22 |
| H: Appointment, Retirement and Powers of Officers | 178 | inert (1) |  | none | - | - |
| s 23(1) | 180 | encoded |  | row | rules::Section 23(1) | rules::Section 23(1) |
| s 23(2) | 182 | encoded |  | row | time::Section 23 | commencement::Section 23 |
| s 23(3) | 184 | encoded |  | row | time::Section 23 | commencement::Section 23 |
| s 23(4) | 186 | encoded |  | row | powers::Section 23(4) | powers::Section 23(4) |
| s 23(5) | 188 | encoded |  | row | time::Section 23 | commencement::Section 23 |
| s 24(1) | 190 | encoded |  | row | powers::Section 24 | powers::Section 24 |
| s 24(1)(a) | 191 | encoded |  | group | powers::Section 24 | powers::Section 24 |
| s 24(1)(b) | 192 | encoded |  | group | powers::Section 24 | powers::Section 24 |
| s 24(1)(c) | 193 | encoded |  | group | powers::Section 24 | powers::Section 24 |
| s 24(2) | 195 | encoded |  | row | powers::Section 24 | powers::Section 24 |
| s 24(2)(a) | 196 | encoded |  | group | powers::Section 24 | powers::Section 24 |
| s 24(2)(b) | 197 | encoded |  | group | powers::Section 24 | powers::Section 24 |
| s 24(2)(c) | 198 | encoded |  | group | powers::Section 24 | powers::Section 24 |
| s 24(2)(d) | 199 | encoded |  | group | powers::Section 24 | powers::Section 24 |
| s 24(3) | 201 | fork | F-24-DEPUTY | row | powers::Section 24 | powers::Section 24 |
| s 24(4) | 203 | fork | F-24-DEPUTY | row | powers::Section 24 | powers::Section 24 |
| s 24(5) | 205 | encoded |  | row | powers::Section 24 | powers::Section 24 |
| H: Evidence | 207 | inert (1) |  | none | - | - |
| s 25(1) | 209 | encoded |  | row | rules::Section 25(1) | rules::Section 25(1) |
| s 25(2) | 211 | fork | F-QUEENS | row | reading::Section 25(2) | reading::Section 25(2) |
| H: Computation of Time | 213 | inert (1) |  | none | - | - |
| s 26 | 215 | fork | F-26-UNITS,F-26-GAP,F-26-ON-HOLIDAY,F-HOLIDAY-PLACE | row | time::Section 26 | holidays::Section 26 |
| s 27(1) | 217 | encoded |  | row | time::Section 27 | counting::Section 27(1) |
| s 27(2) | 219 | encoded |  | row | time::Section 27 | counting::Section 27(2) |
| s 27(3) | 221 | encoded |  | row | time::Section 27 | counting::Section 27(3) |
| s 27(4) | 223 | fork | F-FROM,F-LASTDAY | row | time::Section 27 | periods::s 27(4), (5) |
| s 27(5) | 225 | fork | F-FROM,F-LASTDAY,F-BEFORE | row | time::Section 27 | periods::s 27(4), (5) |
| s 28 | 227 | fork | F-FROM,F-BEFORE | row | time::Section 28 | periods::s 28(c) |
| s 28(a) | 228 | encoded |  | group | time::Section 28 | other::Section 28 |
| s 28(b) | 229 | encoded |  | group | time::Section 28 | other::Section 28 |
| s 28(c) | 230 | encoded |  | group | time::Section 28 | other::Section 28 |
| s 29 | 232 | encoded |  | row | calendar::Section 29 | holidays::Section 35(1) "standard time" and section 29 |
| s 30 | 234 | fork | F-DAY,F-30-LEAP | row | time::Section 30 | other::Section 30 |
| H: Miscellaneous Rules | 236 | inert (1) |  | none | - | - |
| s 31(1) | 238 | encoded |  | row | powers::Section 31 | powers::Section 31 |
| s 31(2) | 240 | encoded |  | row | powers::Section 31 | powers::Section 31 |
| s 31(3) | 242 | encoded |  | row | powers::Section 31 | powers::Section 31 |
| s 31(4) | 244 | encoded |  | row | powers::Section 31 | powers::Section 31 |
| s 32 | 246 | fork | F-32 | row | rules::Section 32 | rules::Section 32 |
| s 33(1) | 248 | encoded |  | row | reading::Section 33 | reading::Section 33 |
| s 33(2) | 250 | encoded |  | row | reading::Section 33 | reading::Section 33 |
| s 33(3) | 252 | encoded |  | row | reading::Section 33 | reading::Section 33 |
| H: Offences | 254 | inert (1) |  | none | - | - |
| s 34(1) | 256 | encoded |  | row | rules::Section 34 | rules::Section 34 |
| s 34(1)(a) | 257 | fork | F-34 | group | rules::Section 34 | rules::Section 34 |
| s 34(1)(b) | 258 | fork | F-34 | group | rules::Section 34 | rules::Section 34 |
| s 34(1)(c) | 259 | encoded |  | group | rules::Section 34 | rules::Section 34 |
| s 34(2) | 261 | encoded |  | row | rules::Section 34 | rules::Section 34 |
| s 34(3) | 263 | encoded |  | row | rules::Section 34 | rules::Section 34 |
| s 34(3)(a) | 264 | encoded |  | group | rules::Section 34 | rules::Section 34 |
| s 34(3)(b) | 265 | encoded |  | group | rules::Section 34 | rules::Section 34 |
| H: Powers to Enter Dwelling-houses to Carry out Arrests | 267 | inert (1) |  | none | - | - |
| s 34.1 | 269 | encoded |  | row | powers::Section 34.1 | powers::Section 34.1 |
| s 34.1(a) | 270 | encoded |  | group | powers::Section 34.1 | powers::Section 34.1 |
| s 34.1(b) | 271 | encoded |  | group | powers::Section 34.1 | powers::Section 34.1 |
| H: Definitions | 273 | inert (1) |  | none | - | - |
| s 35(1) | 275 | encoded |  | none | definitions::where the definitions apply | definitions::where the definitions apply |
| s 35(1) "Act" | 276 | encoded |  | group | definitions::s 35(1) "Act" | definitions::s 35(1) "Act" |
| s 35(1) "bank" | 277 | encoded |  | group | definitions::s 35(1) "bank" | definitions::s 35(1) "bank" |
| s 35(1) "British Commonwealth or British Commonwealth of Nations" | 278 | encoded |  | row | rules::Section 35(2) and the Schedule | rules::The Schedule and section 35(1) |
| s 35(1) "broadcasting" | 279 | encoded |  | group | definitions::s 35(1) "broadcasting" | definitions::s 35(1) "broadcasting" |
| s 35(1) "Canada" | 280 | fork | F-CANADA-EEZ | group | definitions::s 35(1) "Canada" | definitions::s 35(1) "Canada" |
| s 35(1) "Canadian waters" | 281 | encoded |  | group | definitions::s 35(1) "Canadian waters" | definitions::s 35(1) "Canadian waters" |
| s 35(1) "Clerk of the Privy Council or Clerk of the Queen’s Privy Council" | 282 | encoded |  | group | definitions::s 35(1) "Clerk of the Privy Council or Clerk of the Queen’s Privy Council" | definitions::s 35(1) "Clerk of the Privy Council or Clerk of the Queen’s Privy Council" |
| s 35(1) "commencement" | 283 | encoded |  | row | calendar::Section 35(1) "commencement" | commencement::Worked case 1 |
| s 35(1) "Commonwealth or Commonwealth of Nations" | 284 | encoded |  | row | rules::Section 35(2) and the Schedule | rules::The Schedule and section 35(1) |
| s 35(1) "Commonwealth and Dependent Territories" | 285 | encoded |  | group | definitions::s 35(1) "Commonwealth and Dependent Territories" | definitions::s 35(1) "Commonwealth and Dependent Territories" |
| s 35(1) "contiguous zone" | 286 | encoded |  | group | definitions::s 35(1) "contiguous zone" | definitions::s 35(1) "contiguous zone" |
| s 35(1) "contiguous zone" (a) | 287 | encoded |  | group | definitions::s 35(1) "contiguous zone" | definitions::s 35(1) "contiguous zone" |
| s 35(1) "contiguous zone" (b) | 288 | encoded |  | group | definitions::s 35(1) "contiguous zone" | definitions::s 35(1) "contiguous zone" |
| s 35(1) "continental shelf" | 289 | encoded |  | group | definitions::s 35(1) "continental shelf" | definitions::s 35(1) "continental shelf" |
| s 35(1) "continental shelf" (a) | 290 | encoded |  | group | definitions::s 35(1) "continental shelf" | definitions::s 35(1) "continental shelf" |
| s 35(1) "continental shelf" (b) | 291 | encoded |  | group | definitions::s 35(1) "continental shelf" | definitions::s 35(1) "continental shelf" |
| s 35(1) "contravene" | 292 | encoded |  | group | definitions::s 35(1) "contravene" | definitions::s 35(1) "contravene" |
| s 35(1) "corporation" | 293 | encoded |  | row | rules::Section 35(1): "corporation" and "security" | rules::Section 35(1): "corporation" and "security" |
| s 35(1) "county" | 294 | encoded |  | group | definitions::s 35(1) "county" | definitions::s 35(1) "county" |
| s 35(1) "county court" | 295 | repealed |  | row | - | - |
| s 35(1) "diplomatic or consular officer" | 296 | encoded |  | group | definitions::s 35(1) "diplomatic or consular officer" | definitions::s 35(1) "diplomatic or consular officer" |
| s 35(1) "exclusive economic zone" | 297 | encoded |  | group | definitions::s 35(1) "exclusive economic zone" | definitions::s 35(1) "exclusive economic zone" |
| s 35(1) "exclusive economic zone" (a) | 298 | encoded |  | group | definitions::s 35(1) "exclusive economic zone" | definitions::s 35(1) "exclusive economic zone" |
| s 35(1) "exclusive economic zone" (b) | 299 | encoded |  | group | definitions::s 35(1) "exclusive economic zone" | definitions::s 35(1) "exclusive economic zone" |
| s 35(1) "Federal Court" | 300 | repealed |  | row | - | - |
| s 35(1) "Federal Court — Appeal Division or Federal Court of Appeal" | 301 | repealed |  | row | - | - |
| s 35(1) "Federal Court — Trial Division" | 302 | repealed |  | row | - | - |
| s 35(1) "Governor, Governor General or Governor of Canada" | 303 | encoded |  | group | definitions::s 35(1) "Governor, Governor General or Governor of Canada" | definitions::s 35(1) "Governor, Governor General or Governor of Canada" |
| s 35(1) "Governor General in Council or Governor in Council" | 304 | fork | F-QUEENS | group | definitions::s 35(1) "Governor General in Council or Governor in Council" | definitions::s 35(1) "Governor General in Council or Governor in Council" |
| s 35(1) "Great Seal" | 305 | encoded |  | group | definitions::s 35(1) "Great Seal" | definitions::s 35(1) "Great Seal" |
| s 35(1) "Her Majesty, His Majesty, the Queen, the King or the Crown" | 306 | encoded |  | group | definitions::s 35(1) "Her Majesty, His Majesty, the Queen, the King or the Crown" | definitions::s 35(1) "Her Majesty, His Majesty, the Queen, the King or the Crown" |
| s 35(1) "Her Majesty’s Realms and Territories or His Majesty’s Realms and Territories" | 307 | encoded |  | group | definitions::s 35(1) "Her Majesty’s Realms and Territories or His Majesty’s Realms and Territories" | definitions::s 35(1) "Her Majesty’s Realms and Territories or His Majesty’s Realms and Territories" |
| s 35(1) "herein" | 308 | encoded |  | group | definitions::s 35(1) "herein" | definitions::s 35(1) "herein" |
| s 35(1) "holiday" | 309 | fork | F-HOLIDAY-BIRTHDAY,F-HOLIDAY-PLACE | row | calendar::Section 35(1) "holiday" ; definitions::s 35(1) "holiday" | holidays::Section 35(1) "holiday" ; definitions::s 35(1) "holiday" |
| s 35(1) "holiday" (a) | 310 | fork | F-HOLIDAY-PLACE | group | calendar::Section 35(1) "holiday" ; definitions::s 35(1) "holiday" | holidays::Section 35(1) "holiday" ; definitions::s 35(1) "holiday" |
| s 35(1) "holiday" (b) | 311 | fork | F-HOLIDAY-PLACE | group | calendar::Section 35(1) "holiday" ; definitions::s 35(1) "holiday" | holidays::Section 35(1) "holiday" ; definitions::s 35(1) "holiday" |
| s 35(1) "internal waters" | 312 | encoded |  | group | definitions::s 35(1) "internal waters" | definitions::s 35(1) "internal waters" |
| s 35(1) "internal waters" (a) | 313 | encoded |  | group | definitions::s 35(1) "internal waters" | definitions::s 35(1) "internal waters" |
| s 35(1) "internal waters" (b) | 314 | encoded |  | group | definitions::s 35(1) "internal waters" | definitions::s 35(1) "internal waters" |
| s 35(1) "legislative assembly, legislative council or legislature" | 315 | repealed |  | row | - | - |
| s 35(1) "legislative assembly or legislature" | 316 | encoded |  | group | definitions::s 35(1) "legislative assembly or legislature" | definitions::s 35(1) "legislative assembly or legislature" |
| s 35(1) "lieutenant governor" | 317 | encoded |  | group | definitions::s 35(1) "lieutenant governor" | definitions::s 35(1) "lieutenant governor" |
| s 35(1) "lieutenant governor in council" | 318 | encoded |  | group | definitions::s 35(1) "lieutenant governor in council" | definitions::s 35(1) "lieutenant governor in council" |
| s 35(1) "lieutenant governor in council" (a) | 319 | encoded |  | group | definitions::s 35(1) "lieutenant governor in council" | definitions::s 35(1) "lieutenant governor in council" |
| s 35(1) "lieutenant governor in council" (b) | 320 | encoded |  | group | definitions::s 35(1) "lieutenant governor in council" | definitions::s 35(1) "lieutenant governor in council" |
| s 35(1) "lieutenant governor in council" (c) | 321 | encoded |  | group | definitions::s 35(1) "lieutenant governor in council" | definitions::s 35(1) "lieutenant governor in council" |
| s 35(1) "lieutenant governor in council" (d) | 322 | encoded |  | group | definitions::s 35(1) "lieutenant governor in council" | definitions::s 35(1) "lieutenant governor in council" |
| s 35(1) "local time" | 323 | encoded |  | row | calendar::Section 29 and section 35(1) "standard time" | holidays::Section 35(1) "standard time" and section 29 |
| s 35(1) "military" | 324 | encoded |  | group | definitions::s 35(1) "military" | definitions::s 35(1) "military" |
| s 35(1) "month" | 325 | encoded |  | row | time::Section 37 and section 35(1) | other::Section 35(1): "month" |
| s 35(1) "oath" | 326 | encoded |  | group | definitions::s 35(1) "oath" | definitions::s 35(1) "oath" |
| s 35(1) "Parliament" | 327 | encoded |  | group | definitions::s 35(1) "Parliament" | definitions::s 35(1) "Parliament" |
| s 35(1) "person" | 328 | encoded |  | group | definitions::s 35(1) "person" | definitions::s 35(1) "person" |
| s 35(1) "proclamation" | 329 | encoded |  | group | definitions::s 35(1) "proclamation" | definitions::s 35(1) "proclamation" |
| s 35(1) "province" | 330 | encoded |  | group | definitions::s 35(1) "province" | definitions::s 35(1) "province" |
| s 35(1) "radio or radiocommunication" | 331 | encoded |  | group | definitions::s 35(1) "radio or radiocommunication" | definitions::s 35(1) "radio or radiocommunication" |
| s 35(1) "regular force" | 332 | encoded |  | group | definitions::s 35(1) "regular force" | definitions::s 35(1) "regular force" |
| s 35(1) "reserve force" | 333 | encoded |  | group | definitions::s 35(1) "reserve force" | definitions::s 35(1) "reserve force" |
| s 35(1) "security" | 334 | encoded |  | row | rules::Section 35(1): "corporation" and "security" | rules::Section 35(1): "corporation" and "security" |
| s 35(1) "standard time" | 335 | fork | F-STD-TIME | row | calendar::Section 29 and section 35(1) "standard time" | holidays::Section 35(1) "standard time" and section 29 |
| s 35(1) "standard time" (a) | 336 | encoded |  | group | calendar::Section 29 and section 35(1) "standard time" | holidays::Section 35(1) "standard time" and section 29 |
| s 35(1) "standard time" (b) | 337 | fork | F-STD-TIME | group | calendar::Section 29 and section 35(1) "standard time" | holidays::Section 35(1) "standard time" and section 29 |
| s 35(1) "standard time" (c) | 338 | fork | F-STD-TIME | group | calendar::Section 29 and section 35(1) "standard time" | holidays::Section 35(1) "standard time" and section 29 |
| s 35(1) "standard time" (d) | 339 | fork | F-STD-TIME | group | calendar::Section 29 and section 35(1) "standard time" | holidays::Section 35(1) "standard time" and section 29 |
| s 35(1) "standard time" (e) | 340 | fork | F-STD-TIME | group | calendar::Section 29 and section 35(1) "standard time" | holidays::Section 35(1) "standard time" and section 29 |
| s 35(1) "standard time" (f) | 341 | encoded |  | group | calendar::Section 29 and section 35(1) "standard time" | holidays::Section 35(1) "standard time" and section 29 |
| s 35(1) "standard time" (g) | 342 | encoded |  | group | calendar::Section 29 and section 35(1) "standard time" | holidays::Section 35(1) "standard time" and section 29 |
| s 35(1) "statutory declaration" | 343 | encoded |  | group | definitions::s 35(1) "statutory declaration" | definitions::s 35(1) "statutory declaration" |
| s 35(1) "superior court" | 344 | encoded |  | group | definitions::s 35(1) "superior court" | definitions::s 35(1) "superior court" |
| s 35(1) "superior court" (a) | 345 | encoded |  | group | definitions::s 35(1) "superior court" | definitions::s 35(1) "superior court" |
| s 35(1) "superior court" (a.1) | 346 | encoded |  | group | definitions::s 35(1) "superior court" | definitions::s 35(1) "superior court" |
| s 35(1) "superior court" (b) | 347 | encoded |  | group | definitions::s 35(1) "superior court" | definitions::s 35(1) "superior court" |
| s 35(1) "superior court" (c) | 348 | fork | F-QUEENS | group | definitions::s 35(1) "superior court" | definitions::s 35(1) "superior court" |
| s 35(1) "superior court" (d) | 349 | encoded |  | group | definitions::s 35(1) "superior court" | definitions::s 35(1) "superior court" |
| s 35(1) "superior court" (e) | 350 | encoded |  | group | definitions::s 35(1) "superior court" | definitions::s 35(1) "superior court" |
| s 35(1) "superior court" closing words | 351 | encoded |  | group | definitions::s 35(1) "superior court" | definitions::s 35(1) "superior court" |
| s 35(1) "telecommunications" | 352 | encoded |  | group | definitions::s 35(1) "telecommunications" | definitions::s 35(1) "telecommunications" |
| s 35(1) "territorial sea" | 353 | encoded |  | group | definitions::s 35(1) "territorial sea" | definitions::s 35(1) "territorial sea" |
| s 35(1) "territorial sea" (a) | 354 | encoded |  | group | definitions::s 35(1) "territorial sea" | definitions::s 35(1) "territorial sea" |
| s 35(1) "territorial sea" (b) | 355 | encoded |  | group | definitions::s 35(1) "territorial sea" | definitions::s 35(1) "territorial sea" |
| s 35(1) "territory" | 356 | encoded |  | group | definitions::s 35(1) "territory" | definitions::s 35(1) "territory" |
| s 35(1) "two justices" | 357 | encoded |  | group | definitions::s 35(1) "two justices" | definitions::s 35(1) "two justices" |
| s 35(1) "United Kingdom" | 358 | encoded |  | group | definitions::s 35(1) "United Kingdom" | definitions::s 35(1) "United Kingdom" |
| s 35(1) "United States" | 359 | encoded |  | group | definitions::s 35(1) "United States" | definitions::s 35(1) "United States" |
| s 35(1) "writing" | 360 | fork | F-WRITING | group | definitions::s 35(1) "writing" | definitions::s 35(1) "writing" |
| s 35(2) | 362 | encoded |  | row | rules::Section 35(2) and the Schedule | rules::The Schedule and section 35(1) |
| s 36 | 364 | encoded |  | row | reading::Section 36 | reading::Section 36 |
| s 37(1) | 366 | fork | F-YEAR,F-FROM | row | time::Section 37(1) | other::Section 37(1) |
| s 37(1)(a) | 367 | encoded |  | group | time::Section 37 and section 35(1) | other::Section 37(1) |
| s 37(1)(b) | 368 | encoded |  | group | time::Section 37 and section 35(1) | other::Section 37(1) |
| s 37(1)(c) | 369 | encoded |  | group | time::Section 37 and section 35(1) | other::Section 37(1) |
| s 37(2) | 371 | encoded |  | row | time::Section 37 and section 35(1) | other::Section 37(2) |
| s 38 | 373 | encoded |  | row | reading::Section 38 | reading::Section 38 |
| s 39(1) | 375 | encoded |  | row | time::Section 39(1) ; resolutions::Section 39(1): the four expressions | other::Section 39(1) ; resolutions::Section 39(1): the body |
| s 39(1)(a) | 376 | fork | F-39-THEN,F-39-LAYING,F-39-AFFIRM | group | time::Section 39(1) ; resolutions::Section 39(1)(a) and (b) | other::Section 39(1)(a) and (b) ; resolutions::Section 39(1)(a) and (b) |
| s 39(1)(b) | 377 | fork | F-39-THEN,F-39-LAYING,F-39-AFFIRM | group | time::Section 39(1) ; resolutions::Section 39(1)(a) and (b) | other::Section 39(1)(a) and (b) ; resolutions::Section 39(1)(a) and (b) |
| s 39(1)(c) | 378 | fork | F-39-THEN,F-39-LAYING | group | time::Section 39(1) ; resolutions::Section 39(1)(c) and (d) | other::Section 39(1) ; resolutions::Section 39(1)(c) and (d) |
| s 39(1)(d) | 379 | fork | F-39-THEN,F-39-LAYING | group | time::Section 39(1) ; resolutions::Section 39(1)(c) and (d) | other::Section 39(1) ; resolutions::Section 39(1)(c) and (d) |
| s 39(2) | 381 | fork | F-39-2-MOMENT | row | repeal::Section 39(2) | repeal::Section 39(2) |
| H: References and Citations | 383 | inert (1) |  | none | - | - |
| s 40(1) | 385 | encoded |  | row | reading::Section 40 | reading::Section 40 |
| s 40(1)(a) | 386 | encoded |  | group | reading::Section 40 | reading::Section 40 |
| s 40(1)(b) | 387 | encoded |  | group | reading::Section 40 | reading::Section 40 |
| s 40(2) | 389 | fork | F-40-2-DATE | row | reading::Section 40 | reading::Section 40 |
| s 41(1) | 391 | encoded |  | row | rules::Section 41(1) | rules::Section 41(1) |
| s 41(2) | 393 | encoded |  | row | reading::Section 41(2) | reading::Section 41(2) |
| s 41(3) | 395 | encoded |  | row | reading::Section 41(2) | reading::Section 41(2) |
| s 41(4) | 397 | encoded |  | row | reading::Section 41(2) | reading::Section 41(2) |
| s 41(5) | 399 | encoded |  | row | reading::Section 41(2) | reading::Section 41(2) |
| H: Repeal and Amendment | 401 | inert (1) |  | none | - | - |
| s 42(1) | 403 | encoded |  | row | reading::Section 42 | reading::Section 42 |
| s 42(2) | 405 | encoded |  | row | reading::Section 42 | reading::Section 42 |
| s 42(3) | 407 | encoded |  | row | reading::Section 42 | reading::Section 42 |
| s 43 | 409 | encoded |  | row | repeal::Section 43 | repeal::Section 43 |
| s 43(a) | 410 | encoded |  | group | repeal::Section 43 | repeal::Section 43 |
| s 43(b) | 411 | encoded |  | group | repeal::Section 43 | repeal::Section 43 |
| s 43(c) | 412 | encoded |  | group | repeal::Section 43 | repeal::Section 43 |
| s 43(d) | 413 | fork | F-44-E | group | repeal::Section 43 | repeal::Section 43 |
| s 43(e) | 414 | encoded |  | group | repeal::Section 43 | repeal::Section 43 |
| s 43 closing words | 415 | fork | F-44-E | group | repeal::Section 43 | repeal::Section 43 |
| s 44 | 417 | encoded |  | row | repeal::Section 44 | repeal::Section 44 |
| s 44(a) | 418 | encoded |  | row | repeal::Section 44 | repeal::Section 44 |
| s 44(b) | 419 | encoded |  | row | repeal::Section 44 | repeal::Section 44 |
| s 44(c) | 420 | encoded |  | row | repeal::Section 44 | repeal::Section 44 |
| s 44(d) | 421 | encoded |  | row | repeal::Section 44 | repeal::Section 44 |
| s 44(d)(i) | 422 | encoded |  | group | repeal::Section 44 | repeal::Section 44 |
| s 44(d)(ii) | 423 | encoded |  | group | repeal::Section 44 | repeal::Section 44 |
| s 44(d)(iii) | 424 | encoded |  | group | repeal::Section 44 | repeal::Section 44 |
| s 44(e) | 425 | fork | F-44-E | row | repeal::Section 44 | repeal::Section 44 |
| s 44(f) | 426 | encoded |  | row | repeal::Section 44 | repeal::Section 44 |
| s 44(g) | 427 | encoded |  | row | repeal::Section 44 | repeal::Section 44 |
| s 44(h) | 428 | encoded |  | row | repeal::Section 44 | repeal::Section 44 |
| s 45(1) | 430 | encoded |  | row | reading::Section 45 | reading::Section 45 |
| s 45(2) | 432 | encoded |  | row | reading::Section 45 | reading::Section 45 |
| s 45(3) | 434 | encoded |  | row | reading::Section 45 | reading::Section 45 |
| s 45(4) | 436 | encoded |  | row | reading::Section 45 | reading::Section 45 |
| H: Demise of Crown | 438 | inert (1) |  | none | - | - |
| s 46(1) | 440 | encoded |  | row | repeal::Section 46 | repeal::Section 46 |
| s 46(1)(a) | 441 | encoded |  | group | repeal::Section 46 | repeal::Section 46 |
| s 46(1)(b) | 442 | encoded |  | group | repeal::Section 46 | repeal::Section 46 |
| s 46(2) | 444 | encoded |  | row | repeal::Section 46 | repeal::Section 46 |
| Schedule | 446 | inert (1) |  | row | - | - |
| Schedule row 1 | 447 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 2 | 448 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 3 | 449 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 4 | 450 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 5 | 451 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 6 | 452 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 7 | 453 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 8 | 454 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 9 | 455 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 10 | 456 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 11 | 457 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 12 | 458 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 13 | 459 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 14 | 460 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 15 | 461 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 16 | 462 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 17 | 463 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 18 | 464 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 19 | 465 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 20 | 466 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 21 | 467 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 22 | 468 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 23 | 469 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 24 | 470 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 25 | 471 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 26 | 472 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 27 | 473 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 28 | 474 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 29 | 475 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 30 | 476 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 31 | 477 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 32 | 478 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 33 | 479 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 34 | 480 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 35 | 481 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 36 | 482 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 37 | 483 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 38 | 484 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 39 | 485 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 40 | 486 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 41 | 487 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 42 | 488 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 43 | 489 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 44 | 490 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 45 | 491 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 46 | 492 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 47 | 493 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 48 | 494 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 49 | 495 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 50 | 496 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| Schedule row 51 | 497 | encoded |  | group | rules::Section 35(2) and the Schedule | schedule::Schedule rows |
| H: RELATED PROVISIONS | 499 | inert (1) |  | row | - | - |
| 1998, c. 30, s. 10 | 501-503 | encoded |  | row | commencement::Related Provisions, 1998, c. 30, s. 10 | transition::Related Provisions, 1998, c. 30, s. 10 |

## Changes to existing modules

Pass 3 (2026-10-29) edited two pass-1 modules and two pass-1 test files.
Every other pass-1 file is byte-identical to its pass-2 state (checked with `cmp` against a copy taken before the edits; the list of files that differ is in section 8).
Each change says what changed, why, and the text that licenses it.

1. `ca-interpretation-time.l4`: the function `a regulation subject to affirmative resolution can have come into force, given that`, and a new function `the day a regulation subject to affirmative resolution comes into force, once affirmed on`.
   Defect, an over-refusal found by the independent test pass (#568, #571).
   Pass 1 returned a refusal when the regulation had been affirmed.
   The refusal answered "on what day", which the function's name does not ask.
   The name asks whether it can have come into force, and the text answers it: the regulation "shall not come into force unless and until it is affirmed", so the bar stands before affirmation (FALSE) and is lifted after it (TRUE).
   The "on what day" question is now the new function, which refuses (F-39-AFFIRM).
   The comment above the function was rewritten, because it said "an affirmed regulation is not answered".
   Licensing text: s 39(1)(a), (b) (lines 376-377).
   Tests: `ca-tests-other.l4`, `Section 39(1)(a) and (b)`: the affirmed case is now an assertion of TRUE and the refusal is asserted of the day function.
2. `ca-interpretation-rules.l4`: `a reference from` first `to` last `includes` n.
   Defect, an over-refusal found by the independent test pass (#597).
   Pass 1 returned TRUE for the two ends and a refusal for every other number, so "from 12 to 16" refused 13, 14 and 15.
   A number between the ends is in the reference by its own words, so it is TRUE; a number outside the two ends still refuses.
   The ends are tested on their own, so a reference written the other way round ("from 16 to 12") still includes its two ends.
   The refusal function was renamed to say what it now leaves open: `section 41(1) says that the two ends and the numbers between them are included and says nothing of a number outside them`.
   The comment above the function was rewritten, because it said the section does not say whether a number between is included.
   Licensing text: s 41(1) (line 391).
   Tests: `ca-tests-rules.l4`, `Section 41(1)`: the assertion that refused 5 in "from 3 to 7" is now an assertion of TRUE; 4 and 6 are TRUE, 2 and 9 refuse, "from 12 to 16" includes 12 to 16 and refuses 11 and 17, and "from 16 to 12" includes 16 and 12.

Pass-2 files edited in pass 3 (written in pass 2, so not "existing modules" in the sense above): `ca-interpretation-definitions.l4` (a new section `Section 3(1)`, and comments for F-WRITING and F-HOLIDAY-PLACE), `ca-interpretation-powers.l4` (a comment for F-24-DEPUTY), `ca-interpretation-reading.l4` (a comment for C-3-1-GATE), `ca-tests-definitions.l4` (ten assertions on s 3(1)) and `ca-tests-reading.l4` (an import of the rules module and two assertions on the gate).
New files: `ca-interpretation-commencement.l4`, `ca-interpretation-resolutions.l4`, `ca-tests-transition.l4`, `ca-tests-resolutions.l4`.
Bookkeeping files edited: `NOTES.md`, `dispositions.txt`, `relations.txt`, `encoding.json`, `PROGRESS.md`, `SOURCE-LICENSE.md`, `check-output.txt`.
The fork pointers for F-5-3-THAT, F-32 and F-8-2-TERRITORIES are in the register only: the code they describe is in pass-1 modules, which pass 3 edited only for the two defects above, so no comment naming those forks was added there.

## Pass 3

An independent test author, who had not seen these notes, ran 635 assertions against this deposit.
The lead's message of 2026-10-29 gives 583 satisfied, 5 failed and 47 refused, and says the lead triaged all 52 against the Act and found most to be the test author's own errors or conventions.
This section covers the items the lead sent back as this encoding's.
Each was read against the text; line numbers are those of the deposited text.
The "#" numbers are the test author's scenario numbers, as the lead passed them on.

### A. A row that was wrongly inert

Related Provisions, 1998, c. 30, s. 10 (line 503) was `inert`, reason 2, on the ground that it "affects no one now".
That is not a reason the brief allows, and the text is operative: it says how a proceeding commenced before the section came into force is carried on.
It is encoded in `ca-interpretation-commencement.l4`, `Related Provisions, 1998, c. 30, s. 10`.
`a proceeding is taken up and continued under the amended provision, being commenced on` d `where the section is first in force on` e `and` applies is TRUE for a proceeding commenced before the first day the section is in force and in respect of which a provision amended by sections 12 to 16 applies.
It refuses for any other proceeding, because the text says nothing of one commenced on or after that day or of one to which no amended provision applies.
`a further formality is needed to take up and continue under the amended provision a proceeding commenced on` d ... is FALSE for the same case ("without any further formality") and refuses otherwise.
The day the section came into force is an input, because the deposited text gives none.
Section 6(1) of this Act puts the coming into force of an enactment expressed to come into force on a day at the expiration of the day before, so a proceeding commenced on the first day the section is in force was commenced after it.
Tests: `ca-tests-transition.l4`, same heading (the dates in it are invented for the test).
Jural relation: R1998-10 (claim / duty).

**Re-audit of every other inert row**, against the criterion: inert only if (1) not operative text, (2) machinery such as a short title, a commencement clause or the repeal of what is already repealed, (3) repealed or blank.
40 rows are inert now; the 6 `repealed` units are not among them.

| rows | reason | verdict |
| --- | --- | --- |
| title, citation, long title (lines 5-7) | 1 | stay: they name the Act and say nothing to do |
| the 35 group headings, including RELATED PROVISIONS (lines 9-499) | 1 | stay: a heading carries no sentence; nothing in the Act makes a heading operative |
| the Schedule heading, `SCHEDULE (Section 35)` (line 446) | 1 | stays: it only places the list; the 51 entries below it are encoded rows |
| s 1, the short title (line 11) | 2 | stays: "This Act may be cited as the Interpretation Act" is machinery |
| the 6 units shown as repealed (s 18(4) and five entries of s 35(1)) | disposition `repealed` | stay: the text shows them repealed |

**Rows re-dispositioned: one.**
The Related Provisions item moved from inert (2) to encoded.
No other `inert` row moved.

### Coverage rows moved by pass 3

| unit | from | to | why |
| --- | --- | --- | --- |
| 1998, c. 30, s. 10 | inert (2) | encoded | section A above |
| s 8.2 | encoded | fork | F-8-2-TERRITORIES |
| s 24(3), s 24(4) | encoded | fork | F-24-DEPUTY |
| s 32 | encoded | fork | F-32 |
| s 35(1) "holiday" (a), (b) | encoded | fork | F-HOLIDAY-PLACE |
| s 35(1) "writing" | encoded | fork | F-WRITING |

Rows that were already `fork` and gained a fork id: s 5(3) (F-5-3-THAT), s 26 and s 35(1) "holiday" (F-HOLIDAY-PLACE), s 39(1)(a) and (b) (F-39-AFFIRM, reclassified from class B).
Rows that stay `encoded` and gained a module or test heading: s 3(1) (the definitions module, by kind of instrument), s 5(4) and s 7 (the commencement module), s 39(1) and s 39(1)(c), (d) (the resolutions module).
One citation was changed as well, in a pass-2 row that was not asked for: the test headings of s 5(3) were `Worked case 2` only (its F-FIXED-LATER cases) and are now `Worked case 1` and `Worked case 2`, because the assertion on the moment of a provision that postpones commencement (F-5-3-THAT) is under `Worked case 1`.
The table has 354 rows before and after.

### B. Rules the Act states that no function could be asked

- **Section 39(1)(a) to (d), the four expressions** (`ca-interpretation-resolutions.l4`, new; tests in `ca-tests-resolutions.l4`).
  Each paragraph says three things.
  The regulation is laid before a body: Parliament in (a) and (c), the House of Commons in (b) and (d).
  For (a) and (b) the regulation "shall not come into force unless and until it is affirmed" by a resolution of both Houses (a) or of the House of Commons (b).
  For (c) and (d) it "may be annulled" by a resolution of both Houses (c) or of the House of Commons (d).
  The functions:
  - `the body before which a regulation must be laid under` e names the body.
  - `the resolutions that the expression` e `names have been passed, given that the Senate has passed one is` s `and the House of Commons has passed one is` c takes the Senate and the House of Commons as two booleans: (a) and (c) need both, (b) and (d) the House of Commons alone.
  - `the coming into force of a regulation depends on a resolution if it is` e is TRUE for (a) and (b) and FALSE for (c) and (d).
  - `a regulation can have come into force as far as section 39(1) is concerned, being subject to` e `where the Senate has passed an affirming resolution is` s `and the House of Commons has passed one is` c is, for (a) and (b), TRUE only once the resolutions the expression names have been passed, so a resolution of the House of Commons alone does not meet (a) (#569).
    For (c) and (d) it is always TRUE, because they put no condition on coming into force.
  - `a regulation is annulled, being subject to` e `where the Senate has passed an annulling resolution is` s `and the House of Commons has passed one is` c is, for (c), TRUE for a resolution of each House (#572) and FALSE for one of the House of Commons alone (#573).
    For (d) it is TRUE for a resolution of the House of Commons alone (#574).
    For (a) and (b), which say nothing of annulment, it refuses.
  Laying within the fifteen days is the time module's `the regulation made on` d `may be laid on` e `given the days the body sits` s, which the four paragraphs share because they use the same words.
  Section 39(2), what an annulment does, stays in the repeal module.
  Three choices, each from the text, recorded so that a reader can disagree.
  First, a resolution "of both Houses" is read as one passed by each of the Senate and the House of Commons; a single joint resolution is not distinguished.
  Second, a resolution of the wrong House under (c) or (d) is FALSE, not a refusal, because the paragraphs "mean" and so give the whole meaning.
  Third, "remains in force unless annulled" (#575) is not said in these words by (c) or (d), and the encoding has no one function that says it.
  Its pieces are separate assertions in `ca-tests-resolutions.l4`: with no resolution the regulation is not annulled and the way to coming into force is open, and section 39(2) revokes only an annulled regulation, on the day of the resolution.
- **Section 7, the permission** (`ca-interpretation-commencement.l4`, `Section 7`; #71, #75, #76).
  `a power of the kind` k `may be exercised before the commencement of the enactment where` ... is TRUE for a power to make regulations and for a power to do any other thing alike.
  It is TRUE when the enactment is not in force, contains the provisions that confer the power, and the exercise is for the purpose of making the enactment effective on its commencement.
  An exercise for another purpose, an enactment already in force, and a power the enactment does not confer refuse: the text does not address them, and does not say that they are forbidden.
  The second limb (no effect until commencement, except as necessary) was already in the time module.
- **Section 3(1) by kind of instrument** (`ca-interpretation-definitions.l4`, `Section 3(1)`; #34, #677).
  `the provisions of the Act apply to an instrument of the kind` k `unless` ... answers for an enactment with the gate's answer.
  An enactment is an Act of Parliament, a regulation, or a portion of either; the test is the module's own `is an enactment within section 2(1)`.
  For an Act of a legislature, or an instrument of no listed kind, it refuses.
  The text settles what an enactment is ("means"), so an Act of a legislature is no enactment; of whether any provision applies to such an instrument section 3(1) says nothing (S-3-1-KIND).
- **Section 5(4), its precondition** (`ca-interpretation-commencement.l4`, `Section 5(4)`; #52).
  `section 5(4) deems a provision of an Act to have come into force on the date of assent, given that` ... is TRUE only when the Act gives some provisions another day and the provision asked about is not one of them.
  When no provision names another day the subsection's condition is not met and it deems nothing.
  That is FALSE, because the question is about the section's own condition; the date of commencement is then the date of assent by section 5(2), which gives the same date.
  This is a departure from the house rule (F-NEGATIVE: a case the text does not address is a refusal, not FALSE), taken deliberately because the question asks whether the section itself operates; a reader who prefers a refusal there should change that one function.

### C. Two encoder defects

Both are over-refusals and both are in "Changes to existing modules": the affirmed regulation of section 39(1)(a), (b) (#568, #571), and the numbers between the ends of a reference in section 41(1) (#597).

### D. Where each ambiguity on the test author's list landed

| test pass | ambiguity | landed |
| --- | --- | --- |
| A1 | s 5(3) "that provision" | new, class A: F-5-3-THAT |
| A3 | s 32 "not affecting the substance or calculated to mislead" | new, class A: F-32 |
| A5 | s 24(3), (4): the deputy of a public officer who is not a minister | new, class A: F-24-DEPUTY |
| A6 | s 8.2 "the other provinces" and the territories | new, class A: F-8-2-TERRITORIES |
| A9 | s 3(1) letting a contrary intention displace s 8.3(1) | not a fork: the text licenses one reading; recorded as the convention C-3-1-GATE (class B) |
| A10 | s 37(1): the end of a year of twelve consecutive months | found: F-YEAR, extended by a sentence on a year that "commences on" a day |
| A12 | s 35(1) "writing" | new, class A: F-WRITING |
| A13 | s 26 with s 35(1) "holiday": the place where a thing is "done" | new, class A: F-HOLIDAY-PLACE (replaces the class B entry S-HOLIDAY-PLACE) |
| A14 | s 35(1) "standard time": a place exactly on a boundary meridian | found: F-STD-TIME, which already refuses a west longitude exactly on a boundary; no change |
| A15 | s 22(2)(a) "at least one-half" of an odd number | found: F-22, class B kept; for a whole number present the readings agree (see the entry) |
| A17 | s 39(1)(a) "shall not come into force unless and until" | found: F-39-AFFIRM, filed as a silence; now class A and extended |
| A18 | s 2(1) "public officer" | found: F-PUBLIC-OFFICER; no change |
| named by the lead as already registered | F-QUEENS, F-39-2-MOMENT, F-CANADA-EEZ, F-HOLIDAY-BIRTHDAY, F-PUBLIC-OFFICER, F-FIXED-LATER | found, all present; cross-reference only |

### E. Limits of reading a result

Stated once, in `## Reading a result`.

## Jural relations

Hohfeld's correlatives: a claim is the other party's duty; a privilege is the other party's no-right; a power is the other party's liability (being subject to the power); an immunity is the other party's disability.
Each relation is stated once, from the side of the party who holds the right, privilege, power or immunity, and named neutrally.
Generated by `python3 -I coverage.py <raw text> relations` from `relations.txt` and `dispositions.txt`; the "units" column lists the units that carry the relation.
A provision that creates no such relation (a definition, a counting rule, a rule of reading, a heading, the Schedule) is listed once, in the last line, as `none`.

| relation | holder | bearer of the correlative | type | section | L4 rule | units |
| --- | --- | --- | --- | --- | --- | --- |
| R5-1 | no holder is named by the text | the Clerk of the Parliaments | claim / duty | s 5(1) | reading::Section 5(1) | s 5(1) |
| R7 | the person on whom a not-yet-effective enactment confers a power to make regulations or do a thing | the persons whom the regulation or thing will affect after commencement | power / liability | s 7 | time::Section 7 | s 7 |
| R8-3 | the Aboriginal and treaty rights of Indigenous peoples recognised and affirmed by s 35 of the Constitution Act, 1982 | every enactment, as to a construction that abrogates or derogates from them | immunity / disability | s 8.3(1) | reading::Section 8.3 | s 8.3(1); s 8.3(2) |
| R9 | a person whose rights a private Act does not mention | a provision in a private Act | immunity / disability | s 9 | rules::Section 3(1), section 8(1) and section 9 | s 9 |
| R17 | Her Majesty, and Her Majesty's rights and prerogatives | an enactment | immunity / disability | s 17 | rules::Section 3(1), section 8(1) and section 9 | s 17 |
| R18-3 | the Governor General issuing a proclamation under an order of the Governor in Council | the persons to whom the proclamation applies | power / liability | s 18(3) | time::Section 18(3) | s 18(3) |
| R19 | a person listed in s 19 (the person authorised by the enactment or rule, a judge, a notary public, a justice of the peace, a commissioner for taking affidavits, a notary public or commissioner for taking oaths under s 19(2)) | the person who is to make, take or swear the oath | power / liability | s 19 | rules::Section 19 | s 19(1); s 19(1)(a); s 19(1)(b); s 19(2) |
| R20 | the person who laid the report or document before Parliament at a session | any person who would require it to be laid again at a later session | privilege / no-right | s 20 | rules::Section 20 | s 20 |
| R21-1a | a corporation established by words in an enactment (to sue and be sued, to contract, to hold property, to have a seal and succession) | the persons who deal with the corporation | power / liability | s 21(1)(a) | rules::Section 21 | s 21(1)(a) |
| R21-1c | a majority of the members of the corporation (to bind the others by their acts) | the other members | power / liability | s 21(1)(c) | rules::Section 21 | s 21(1)(c) |
| R21-1d | an individual member of the corporation who does not contravene the enactment (from personal liability for its debts, obligations or acts) | a creditor or other person claiming against the member | immunity / disability | s 21(1)(d) | rules::Section 21 | s 21(1)(d) |
| R21-3 | a corporation (disabled from carrying on the business of banking unless the power is expressly conferred) | no one is named by the text as the holder of the immunity | disability / immunity | s 21(3) | rules::Section 21 | s 21(3) |
| R22-1 | a majority of three or more persons whom an enactment requires or authorises to do an act or thing | the minority and anyone relying on the act | power / liability | s 22(1) | rules::Section 22 | s 22(1) |
| R22-2 | the members of a board, court, commission or other body present at a meeting, if they are a quorum (their act is the association's) | the association and the members absent | power / liability | s 22(2) | rules::Section 22 | s 22(2)(b) |
| R23-1 | the appointing authority (to end the appointment at pleasure) | a public officer appointed by or under an enactment | privilege / no-right | s 23(1) | rules::Section 23(1) | s 23(1) |
| R23-4 | the appointing authority (to fix, vary or terminate the remuneration) | the person appointed to the office | power / liability | s 23(4) | powers::Section 23(4) | s 23(4) |
| R24-1 | the authority in whom the power of appointment of a public officer to hold office during pleasure is vested (to terminate, remove, suspend, re-appoint, reinstate, appoint another) | the public officer | power / liability | s 24(1) | powers::Section 24 | s 24(1) |
| R24-2 | a minister acting for another, a designated minister, a successor, a deputy, or a person appointed to serve in the department or ministry (to do what words empower a minister to do) | the persons affected by what is done | power / liability | s 24(2) | powers::Section 24 | s 24(2) |
| R24-4 | the successor or deputy of a public officer other than a minister | the persons affected by what is done | power / liability | s 24(4) | powers::Section 24 | s 24(4) |
| R24-5 | the person for the time being charged with the execution of the powers and duties of an office (power to exercise, duty to perform) | the persons affected by the exercise, and those entitled to the performance | power and duty / liability and claim | s 24(5) | powers::Section 24 | s 24(5) |
| R25-1 | the party who relies on a document an enactment makes evidence of a fact | the party who disputes the fact (to put in evidence to the contrary) | claim / duty | s 25(1) | rules::Section 25(1) | s 25(1) |
| R26 | the person who is to do a thing within a time that expires or falls on a holiday (to do it on the next day that is not a holiday) | any person who would treat the thing as late | privilege / no-right | s 26 | time::Section 26 | s 26 |
| R31-1 | a person whom a thing is to be done by or before (the act is valid only if done by one whose jurisdiction or powers extend to the place) | an official whose jurisdiction does not extend to the place | immunity / disability | s 31(1) | powers::Section 31 | s 31(1) |
| R31-2 | a person, officer or functionary given power to do or enforce an act or thing (the necessary powers are also given) | the persons affected by the necessary acts | power / liability | s 31(2) | powers::Section 31 | s 31(2) |
| R31-3 | the holder of a power or duty (to exercise it from time to time as occasion requires) | the persons affected, and those entitled to the performance | power and duty / liability and claim | s 31(3) | powers::Section 31 | s 31(3) |
| R31-4 | the maker of regulations (to repeal, amend or vary them and make others, in the same manner and on the same conditions) | the persons subject to the regulations | power / liability | s 31(4) | powers::Section 31 | s 31(4) |
| R32 | a person who uses a prescribed form that deviates from it in a way that does not affect the substance and is not calculated to mislead | whoever would treat the form used as invalid | immunity / disability | s 32 | rules::Section 32 | s 32 |
| R34-1c | a person convicted on summary conviction of an offence that may be prosecuted by indictment or on summary conviction | any authority that would treat the person as convicted of an indictable offence by reason only of the summary conviction | immunity / disability | s 34(1)(c) | rules::Section 34 | s 34(1)(c) |
| R34-1 | a person who may be prosecuted for an offence created by an enactment (liable to the class of proceedings s 34 assigns) | the prosecutor | liability / power | s 34(1), (2), (3) | rules::Section 34 | s 34(1) |
| R34-1a | a person who is the subject of a warrant to arrest or apprehend under an Act of Parliament other than the Criminal Code | a person who may issue the warrant (to authorise entry into a dwelling-house, with or without prior announcement) | liability / power | s 34.1 | powers::Section 34.1 | s 34.1; s 34.1(a); s 34.1(b) |
| R35-2 | the Governor in Council (to amend the schedule by order, adding or deleting a country) | the countries named, and those who rely on the list of the Commonwealth | power / liability | s 35(2) | rules::Section 35(2) | s 35(2) |
| R37-2 | the Governor in Council (to prescribe which twelve-month period is a year for an enactment on the affairs of Parliament or the Government of Canada) | the persons subject to the enactment | power / liability | s 37(2) | time::Section 37 and section 35(1) | s 37(2) |
| R39-1 | Parliament, or the House of Commons (to have a regulation laid before it within fifteen days, or on the first sitting days after) | the maker of the regulation | claim / duty | s 39(1) | time::Section 39(1) | s 39(1) |
| R39-2 | a person who took or did not take action in compliance with a regulation later annulled by a resolution (the validity of the action is not affected) | the resolution, as to that validity | immunity / disability | s 39(2) | repeal::Section 39(2) | s 39(2) |
| R42-1 | Parliament (to repeal or amend an Act, and to revoke, restrict or modify a power, privilege or advantage vested in or granted to a person) | every person holding such a power, privilege or advantage under an Act | power / liability | s 42(1) | reading::Section 42 | s 42(1) |
| R42-2 | Parliament (to amend or repeal an Act by an Act passed in the same session) | every person holding a power, privilege or advantage under the first Act | power / liability | s 42(2) | reading::Section 42 | s 42(2) |
| R43 | a person who acquired, or had accrued or incurred, a right, privilege, obligation or liability under an enactment later repealed; and the enactment's previous operation | the repeal | immunity / disability | s 43(a)-(e) | repeal::Section 43 | s 43(a); s 43(b); s 43(c); s 43(d); s 43(e) |
| R43-closing | whoever may institute, continue or enforce an investigation, legal proceeding or remedy, or impose a punishment, penalty or forfeiture, for a thing under the repealed enactment | the person against whom it is brought | power / liability | s 43 closing words | repeal::Section 43 | s 43 closing words |
| R44a | a person who was acting under the former enactment (continues to act as if appointed under the new) | the persons affected by the acts | power and duty / liability and claim | s 44(a) | repeal::Section 44 | s 44(a) |
| R44b | the obligee of a bond or security given by a person appointed under the former enactment | the person who gave it | claim / duty | s 44(b) | repeal::Section 44 | s 44(b) |
| R44e | a person on whom a punishment, penalty or forfeiture is imposed after the repeal, where the new enactment reduces or mitigates it | the court or authority, as to imposing more than the reduced one | immunity / disability | s 44(e) | repeal::Section 44 | s 44(e) |
| R46 | a holder of an office under the Crown in right of Canada, and a party to a writ, action or other process or proceeding before a court established by an Act (not affected by a demise of the Crown) | the demise of the Crown | immunity / disability | s 46 | repeal::Section 46 | s 46(1); s 46(1)(a); s 46(1)(b); s 46(2) |
| R1998-10 | a party to a proceeding commenced before the section came into force and in respect of which a provision amended by sections 12 to 16 applies (that it be taken up and continued under the amended provision, without any further formality) | the court or authority before which the proceeding is pending | claim / duty | 1998, c. 30, s. 10 | commencement::Related Provisions, 1998, c. 30, s. 10 | 1998, c. 30, s. 10 |

none: 298 units create no relation (definitions, counting rules, rules of reading, headings, the Schedule).

## Seat

The Commons Guide (`ENCODING-GUIDE.md`, sections 2 and 3) asks for a seat layer for the individual to whom the law is applied.
This row has none: the brief for pass 2 says "if the row has one", pass 1's folder has none, and none was added.
An Interpretation Act is read by the person reading another enactment, so the individual's seat would be questions of the form "I have 30 days from 2026-03-01: when is the last day?", "is 2026-03-08 a holiday?", "does a definition of 'person' reach my company?", which the existing functions already answer.
Writing the seat module (with `@export` and `@desc` on each question and a case file) is listed under "Before relying on this".

## Findings

1. **The pass-1 inert rows were not a stable set.** None of the thirty stays inert. The reasons pass 1 gave ("a reading rule", "addresses an official", "no input from which an answer would differ") are the ones the brief now rules out, and each moved to `encoded` or `fork` with a test.
2. **`includes` and `means` differ in what they answer.** `means` gives the whole meaning, so an unnamed thing is FALSE; `includes` does not, so an unnamed thing is a refusal. Thirteen definitions say `includes` (S-INCLUDES in section 3). A reader who asks "is a partnership a person?" of s 35(1) "person" gets a refusal, and that is what the text supports.
3. **Section 45 can be answered in full from its own words.** It says "shall not be deemed" four times, so the answers are FALSE, not refusals; but repeal and the adoption of a construction (s 45(4) names re-enactment, revision, consolidation and amendment only) is a refusal (S-45-ADOPTION), and s 45(3) ("any declaration") reaches the declarations of (1) and (2) (C-45-ANY).
4. **Pass 1 tested six of the fifty-one countries in the Schedule.** `ca-tests-schedule.l4` tests all of them, the count and the order, from the text by script. The full-list assertion also shows that the pass-1 list typed into the rules module equals the text's.
5. **The text says "Queen's" in three operative places while the Sovereign is a King** (F-QUEENS). The Act's own definition of "the Queen" and "the King" does not reach the names of bodies. The encoding takes one reading and lists the alternative; a human should rule.
6. **Section 8(2.1) says the exclusive economic zone is applied to "in addition to" Canada, and section 35(1) "Canada" does not list it** (F-CANADA-EEZ). The two do not decide the question together; the answer is a refusal.
7. **Section 3(2) has no contrary-intention qualifier and section 3(1) has one** (F-3-2). The encoding reads the difference as meant.
8. **Section 35(1) "holiday" is a list of kinds of day, and only three are dated by the text.** The definitions module sorts the kinds; the calendar module dates three; the rest are inputs. A day appointed for one place is not said to be a holiday for a thing done in another (F-HOLIDAY-PLACE).
9. **The Act's definitions of the zones of the sea are not computed.** "As determined under the Oceans Act" is carried as the string the text uses, with the airspace, bed and subsoil it adds. A reader who wants the zone's extent needs that Act.
10. **`ca-tests-red.l4` still holds ten expectations that fail on purpose** and `check.sh` counts them (`expected_failed` = 10). They are not a defect in the encoding; they show the harness can fail.
11. **No assertion fails and none is refused, apart from the ten.** A refused result in a `#ASSERT REFUSED` is the assertion satisfied; it is the encoding saying "the text does not answer".
12. **The expected values were written from the text, but the encoder is one agent.** Every `FALSE` claimed from "means" and every refusal claimed from "includes" is a reading of one word; the register above is where a second reader should start.

## Reading a result

Three limits on what a result means.
An independent test pass met each repeatedly.
None is a defect to be fixed in code: each is how the encoding is built, and each is stated here so that a reader does not mistake it for a ruling of the Act.

1. **A refusal is not the statement "this section does not reach this case".**
   Where a clause states its conditions (a list of named things, an "if", a "where", a "so far as"), the encoding returns TRUE for a case that meets them and a named refusal for any other case it is asked about.
   It does not return FALSE for the unaddressed case, because FALSE is kept for what the text says in terms: "shall not be deemed", "does not include", or a "means" that gives the whole meaning (F-NEGATIVE).
   So a refusal says that the text does not answer this case; it does not say that section X does not apply.
   By the lead's count, 24 of the independent test author's assertions turned on this difference: the author expected FALSE, or "not covered by section X", and the encoding refuses.
   Read a refusal as a gap in the text, and read its name, which says what the text leaves open.
2. **The record `What a zone is` holds a bare list.**
   Its field `what it also includes` is a list of strings, the things the Act says a zone also includes (the airspace above the internal waters, the bed and subsoil below a zone).
   A membership question (is this item in the list?) returns FALSE for an item the Act does not name.
   That FALSE means "not named", not "excluded": the Act says "includes", and "includes" does not exhaust.
   The record does not carry that difference, and the generic function `the term defined by` d `covers` x, which does (it refuses for an unnamed thing under "includes"), is not what answers for the zones.
3. **The Commonwealth schedule is matched by printed names.**
   `is a country named in the schedule` tests whether a string is one of the names printed in the Schedule, and `is a member of the Commonwealth after orders under section 35(2), if` ... builds on it with the orders of section 35(2).
   A name a country has taken since the text was printed ("Samoa" for "Western Samoa", "Eswatini" for "Swaziland") gets FALSE with no refusal, because the list is closed over the printed names and the Act does not say whether a renamed country is the same member.
   Ask with the printed name, or supply the country through the order input.

## What the text does not answer

These are the explicit "not covered" values the tests assert.

- Weeks; deemed service or notice; a day of rest, recess or closed office that is not a holiday; an anniversary that a year does not have (pass 1).
- Whether the exclusive economic zone of Canada is part of "Canada" (F-CANADA-EEZ). (The text of s 8(2.2) raises the same question for the continental shelf; the definitions tests assert only the exclusive economic zone.)
- Whether a person outside the federal public administration on whom a duty is imposed is a public officer (F-PUBLIC-OFFICER).
- Whether a day appointed for one province or district is a holiday for a thing done in another (F-HOLIDAY-PLACE).
- Whether section 3(2) is subject to a contrary intention (F-3-2), and on what date a citation is "as amended" (F-40-2-DATE).
- What the Act makes of any form of enacting clause but the one it gives (s 4(1)), any way of citing an Act or regulation it does not list (s 40(1)), any thing Parliament may do to an Act that s 42(1) does not name, and any person or thing that s 24(1), (2), (4) says words "include" but does not exhaust.
- Whether "oath" includes an affirmation where none may be made instead of an oath (S-OATH), whether "writing" includes words not in visible form (F-WRITING), and whether a repeal involves the adoption of a construction (S-45-ADOPTION).
- Whether the expression "telegraph" includes "telephone" where it is used in a provincial Act enacted before the province joined Canada on a subject outside Parliament's powers, or anywhere else (s 36).
- Any rule of the French version, and the day a regulation takes effect if it is neither registered nor of an exempted class (pass 1).
- The day on which an affirmed regulation comes into force (F-39-AFFIRM); whether a resolution annuls a regulation subject to affirmative resolution (the text says nothing of annulment there); whether a number outside the two ends of a reference is included (s 41(1)).
- Whether any provision of the Act applies to an instrument that is not an enactment, such as an Act of a legislature (S-3-1-KIND); and the exercise before commencement of a power for any purpose but making the enactment effective on its commencement (s 7).
- The proceedings of the Related Provisions item that it does not name: one commenced on or after the day the section came into force, or one to which no amended provision applies.

## Before relying on this

1. A Canadian lawyer, or a second encoder, must read it against the **official** consolidation. The text here is an unofficial plain-text rendering; nothing was verified against the official text.
2. The French version has not been compared (F-LANG). Four definitions carry "(Version anglaise seulement)".
3. The licence: the subject's `STUB-SOURCE-LICENSE.md` now records a ruling of 2026-10-25 on whether an L4 encoding may quote the text (read it there; pass 1 of this file called the question open, and that is out of date). The quoted lines must keep the not-official notice and the attribution the stub names. No human has checked that the quotation here meets it.
4. The seventeen class A forks that pass 1 left, the eight that pass 2 added and the seven that pass 3 added (thirty-two in all) need a ruling (section 3).
5. A seat layer for the individual (the Guide, sections 2 and 3) is not written.
6. The borrowed terms (section 1) are inputs, not imports; the encodings of the Bank Act, the Oceans Act, the Criminal Code, the Constitution Act, 1982, the Statutory Instruments Act, the National Defence Act and the Canada Evidence Act could replace them.
7. The holidays the text names without a date are the caller's; no calendar is written.
8. The encoding was written for `unstable`; a `main` build would reject it (F-TARGET). Porting is a separate job.

## 3. Fork register

Every ambiguity I saw, the readings, the one taken and the text that licenses it.
A comment in a module that says "fork F-..." names an entry here.

Class A entries (a text that can be read two ways with different outcomes) are attached to the units that license them; `coverage.py forks` prints this list from `dispositions.txt`:

```
F-14-SCOPE: s 14
F-15: s 15(1); s 15(2); s 15(2)(a); s 15(2)(b)
F-24-DEPUTY: s 24(3); s 24(4)
F-26-GAP: s 26
F-26-ON-HOLIDAY: s 26
F-26-UNITS: s 26
F-3-2: s 3(2)
F-30-LEAP: s 30
F-32: s 32
F-34: s 34(1)(a); s 34(1)(b)
F-39-2-MOMENT: s 39(2)
F-39-AFFIRM: s 39(1)(a); s 39(1)(b)
F-39-LAYING: s 39(1)(a); s 39(1)(b); s 39(1)(c); s 39(1)(d)
F-39-THEN: s 39(1)(a); s 39(1)(b); s 39(1)(c); s 39(1)(d)
F-40-2-DATE: s 40(2)
F-44-E: s 43(d); s 43 closing words; s 44(e)
F-5-3-THAT: s 5(3)
F-8-2-TERRITORIES: s 8.2
F-BEFORE: s 27(5); s 28
F-CANADA-EEZ: s 35(1) "Canada"
F-DAY: s 6(1); s 30
F-FIXED-LATER: s 5(3); s 6(1); s 6(2)
F-FROM: s 27(4); s 27(5); s 28; s 37(1)
F-HOLIDAY-BIRTHDAY: s 35(1) "holiday"
F-HOLIDAY-PLACE: s 26; s 35(1) "holiday"; s 35(1) "holiday" (a); s 35(1) "holiday" (b)
F-LASTDAY: s 27(4); s 27(5)
F-PUBLIC-OFFICER: s 2(1) "public officer"
F-QUEENS: s 25(2); s 35(1) "Governor General in Council or Governor in Council"; s 35(1) "superior court" (c)
F-REG-DEF: s 2(1) "regulation"; s 2(1) "regulation" (a); s 2(1) "regulation" (b)
F-STD-TIME: s 35(1) "standard time"; s 35(1) "standard time" (b); s 35(1) "standard time" (c); s 35(1) "standard time" (d); s 35(1) "standard time" (e)
F-WRITING: s 35(1) "writing"
F-YEAR: s 37(1)
```

Class B entries (an encoder's convention, a point the text settles, or a silence) are not attached to a row: F-LANG, F-TARGET, F-NEGATIVE, F-BOUNDS, F-HOLIDAYS (conventions); F-COUNT-START, F-MONTH, F-26-WHICH, F-26-SEVERAL, F-6-MOMENT, F-ASSENT, F-REG-SILENT, F-23-3, F-22 (settled by the text); F-WEEK, F-SERVICE, F-6-3, F-41 (silences); and the pass-2 and pass-3 entries C-LGIC, C-45-ANY, C-3-1-GATE, S-INCLUDES, S-45-ADOPTION, S-OATH, S-3-1-KIND at the end of this section.
F-39-AFFIRM was a class B silence in pass 1 and is class A since pass 3; S-HOLIDAY-PLACE was class B in pass 2 and is replaced by the class A entry F-HOLIDAY-PLACE.

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
- Taken: Twelve consecutive months: N years after a day is 12N months after it, counted by s 28.
  A start on 29 February thus ends on 28 February in a year that has no 29 February and on 29 February in one that has.
- Licensing text: s 37(1) (line 366): "The expression year means any period of twelve consecutive months", except a reference to a calendar year, a financial year or fiscal year, or a Dominical year (lines 367-369), which are encoded separately (`the calendar year numbered`, `the financial year or fiscal year beginning in`, `the Dominical year numbered`).
- A year that "commences on" a given day (pass 3, the independent test pass's A10): the encoding states the end of a year counted "after" a day, as above, and the end of the three named years, which begin on 1 January or 1 April.
  For any other twelve consecutive months that begin on a given day the text does not say on which day the period ends, and the encoding has no function that asks it, so none is asserted.

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

- Readings seen: (A) affirmation is a necessary condition only: it lifts the bar, and the regulation comes into force by its own terms or under s 6; (B) affirmation is also sufficient, and the regulation comes into force on the day it is affirmed, because "unless and until" fixes the moment; (C) later.
- Taken: for the question "can it have come into force", not affirmed is FALSE ("shall not come into force unless and until it is affirmed") and affirmed is TRUE, because the bar is lifted on every reading (corrected 2026-10-29: pass 1 returned a refusal for the affirmed case, which answered "on what day", a different question).
  For the question "on what day" the readings differ, so `the day a regulation subject to affirmative resolution comes into force, once affirmed on` refuses.
- Licensing text: s 39(1)(a), (b) (lines 376-377): "shall not come into force unless and until it is affirmed by a resolution of both Houses of Parliament" (and, in (b), "of the House of Commons").
- Encoded in `ca-interpretation-time.l4`, the two functions that follow `Section 39(1)` (`a regulation subject to affirmative resolution can have come into force, given that` and the day function); tested in `ca-tests-other.l4`, `Section 39(1)(a) and (b)`.
  Which House affirmed is asked in `ca-interpretation-resolutions.l4`.
- Class A since 2026-10-29: pass 1 filed it as a silence; the text has two readings with different outcomes on the day, so it is attached to s 39(1)(a) and (b).

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
- Licensing text: s 22(2)(a)(i) (line 172): "at least one-half of the number of members".
  A majority is more than half (s 22(1), 22(2)(b)).
- Checked again in pass 3 (the independent test pass's A15): for a whole number p present and n members, p is at least n/2 exactly when p is at least n/2 rounded up, so the two readings above always agree and the entry stays class B.
  A third candidate, rounding the half down (so that two of five is a quorum), is not a reading of "at least one-half": two is less than one-half of five.

**F-34. An offence the enactment does not provide may be prosecuted by indictment, but the context indicates is indictable: which class?**

- Readings seen: Indictable; summary.
- Taken: Not answered: refused.
- Licensing text: s 34(1)(a) deems indictable only an offence the enactment provides may be prosecuted by indictment; (b) deems summary an offence "if there is nothing in the context to indicate that the offence is an indictable offence" (lines 257-258).

**F-41. What does a reference to two or more provisions include, other than the first and last mentioned?**

- Readings seen: Every number between; only the two ends.
- Taken: The two ends are included, and so is every number between them, because a reference "from 12 to 16" names 13, 14 and 15 by its own words (corrected 2026-10-29: pass 1 refused a number between the ends, which was an over-refusal).
  A number outside the two ends refuses: the section does not say.
  A reference written the other way round ("from 16 to 12") still includes its two ends and has nothing between.
- Licensing text: s 41(1) (line 391): "shall be read as including the number or letter first mentioned and the number or letter last mentioned".
- Encoded in `ca-interpretation-rules.l4`, `Section 41(1)`; tested in `ca-tests-rules.l4`, `Section 41(1)`.

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

**F-PUBLIC-OFFICER. Does "in the federal public administration" qualify both limbs of "public officer"?**

- Readings seen: (a) it qualifies both limbs, so a public officer is a person in the federal public administration who is authorized by or under an enactment to do a thing or exercise a power, or on whom a duty is imposed by or under an enactment; (b) it qualifies only the first limb, so any person on whom an enactment imposes a duty is a public officer.
- Taken: the text does not choose. Where the readings agree (in the federal public administration, and authorized or charged with a duty) the answer is TRUE. Where they differ (outside it, with a duty imposed) the answer is the named refusal. "Includes" also leaves open that someone else is a public officer, so every other case is a refusal too.
- Licensing text: s 2(1) "public officer" (line 19): "includes any person in the federal public administration who is authorized by or under an enactment to do or enforce the doing of an act or thing or to exercise a power, or on whom a duty is imposed by or under an enactment". The phrase "in the federal public administration" stands before "who is authorized" and the "or" that opens the second limb has no second noun phrase of its own.
- Encoded in `ca-interpretation-definitions.l4`, heading `s 2(1) "public officer"`; tested in `ca-tests-definitions.l4`, same heading.

**F-3-2. Is the Act's application to its own interpretation subject to a contrary intention?**

- Readings seen: (A) section 3(2) is flat: the provisions of the Act apply to the interpretation of the Act, whatever the Act itself says; (B) section 3(2) carries over the "unless a contrary intention appears" of section 3(1).
- Taken: (A).
- Licensing text: s 3(1) (line 29) says "Every provision of this Act applies, unless a contrary intention appears, to every enactment"; s 3(2) (line 31) says only "The provisions of this Act apply to the interpretation of this Act". The Act is itself an enactment (s 2(1) "enactment", line 18), so (B) would make s 3(2) repeat s 3(1). The readings differ only where a contrary intention appears in the Act itself.
- Encoded in `ca-interpretation-reading.l4`, `Section 3(2)`; used by the definitions module's chapeau (`a definition of section 35(1) applies`), where the Act's own case ignores the contrary-intention input.

**F-14-SCOPE. What does "that appear after the end of a section or other division in an enactment" qualify in section 14?**

- Readings seen: (A) only "references to former enactments", so marginal notes form no part of the enactment wherever they stand; (B) both, so only marginal notes that appear after the end of a section are outside the enactment.
- Taken: (A). A marginal note is not printed after the end of a section, so (B) would leave the sentence saying nothing about marginal notes.
- Licensing text: s 14 (line 117): "Marginal notes and references to former enactments that appear after the end of a section or other division in an enactment form no part of the enactment, but are inserted for convenience of reference only." A reference to a former enactment that appears elsewhere in the printed text is not addressed by either reading; the encoding refuses it.
- Encoded in `ca-interpretation-reading.l4`, `Section 14`; the case outside the section is `a reference to a former enactment that appears elsewhere in the printed text`, asserted as refused.

**F-15. Does section 15(2)(a) qualify section 15(1)?**

- Readings seen: (A) subsection (1) states the reach of an enactment's definitions and rules of interpretation (every provision, including the one that contains them) and subsection (2)(a) adds that an interpretation section applies only if a contrary intention does not appear, so a contrary intention displaces a definition even in its own enactment; (B) subsection (1) is unconditional and (2)(a) concerns only provisions other than those within the enactment.
- Taken: (A).
- Licensing text: s 15(1) (line 121) has no qualifier; s 15(2) (lines 123-125) says an interpretation section "shall be read and construed (a) as being applicable only if a contrary intention does not appear; and (b) as being applicable to all other enactments relating to the same subject-matter unless a contrary intention appears". (B) leaves (2)(a) nothing to say. Subsection (2)(b) is encoded as stated: the same subject-matter is a plain input and a different subject-matter is a refusal.
- Encoded in `ca-interpretation-reading.l4`, `Section 15`.

**F-QUEENS. What do the words "Queen's" in a text current to 2026-09-30 name while the Sovereign is a King?**

- Readings seen: (A) the body or office named is the one that now exists under the Sovereign's current style (the King's Printer; the Privy Council for Canada; the court styled King's Bench); (B) only a body styled "Queen's" counts, so nothing now qualifies.
- Taken: (A), in three places. Section 25(2): the titles "the King's Printer and Controller of Stationery" and "the King's Printer" are listed beside the two the text prints. Section 35(1) "Governor General in Council": the body is the Privy Council for Canada under whatever style the reigning Sovereign gives it, an input. Section 35(1) "superior court" (c): the list for New Brunswick, Manitoba, Saskatchewan and Alberta carries "the Court of King's Bench for the Province" beside "the Court of Queen's Bench for the Province".
- Licensing text: s 25(2) (line 211), s 35(1) "Governor General in Council" (line 304) and "superior court" (c) (line 348) print "Queen's". The Act's own s 35(1) "Her Majesty, His Majesty, the Queen, the King or the Crown" (line 306) makes "the Queen" and "the King" one Sovereign, but it defines those words and not the names of bodies, so it does not decide the question. The text also prints "Clerk of the Queen's Privy Council" beside "Clerk of the Privy Council" (line 282), which gives one meaning to the two names.
- Encoded in `ca-interpretation-reading.l4` (`Section 25(2)`) and `ca-interpretation-definitions.l4` (`s 35(1) "Governor General in Council or Governor in Council"`, `s 35(1) "superior court"`).

**F-40-2-DATE. As amended on what date?**

- Readings seen: (A) as amended up to the day on which the citation is read and applied; (B) as amended on the day the citation was written.
- Taken: (A): `the amendments a citation of an enactment includes, read and applied on` d returns the amendments made not later than d. The input d is the day of application, and a caller who prefers (B) passes the day of writing.
- Licensing text: s 40(2) (line 389): "A citation of or reference to an enactment is deemed to be a citation of or reference to the enactment as amended." The text names no date. The Act's own s 8.1 (line 87) refers to the rules "in force in the province at the time the enactment is being applied", which shows the Act using the day of application elsewhere; that is an analogy, not a statement about s 40(2).
- Encoded in `ca-interpretation-reading.l4`, `Section 40`.

**F-HOLIDAY-BIRTHDAY. Is the birthday of the reigning Sovereign a holiday when a proclamation fixes another day?**

- Readings seen: (A) "the birthday or the day fixed by proclamation for the celebration of the birthday" lists two days, and each is a holiday; (B) a proclamation fixes the day for the celebration, which replaces the birthday for that year.
- Taken: (A). The two kinds of day are separate constructors of `A kind of day`, and each returns TRUE.
- Licensing text: s 35(1) "holiday" (line 309): "the birthday or the day fixed by proclamation for the celebration of the birthday of the reigning Sovereign". The text does not date the birthday or say what a proclamation displaces. The calendar module takes the dates of such days from the caller.
- Encoded in `ca-interpretation-definitions.l4`, `s 35(1) "holiday"`.

**F-CANADA-EEZ. Is the exclusive economic zone of Canada part of Canada?**

- Readings seen: (A) it is; (B) it is not, and section 8(2.1) extends enactments to it "in addition to" their application to Canada.
- Taken: the text does not choose. `Canada` "for greater certainty, includes the internal waters of Canada and the territorial sea of Canada". Asked whether it covers "the exclusive economic zone of Canada", the answer is the named refusal, because "includes" is not exhaustive and the text of section 8(2.1) points both ways.
- Licensing text: s 35(1) "Canada" (line 280); s 8(2.1) (line 74): "applies, in addition to its application to Canada, to the exclusive economic zone of Canada". The same applies to the continental shelf (s 8(2.2), line 79).
- Encoded in `ca-interpretation-definitions.l4`, `s 35(1) "Canada"`; asserted as refused in `ca-tests-definitions.l4`.

**F-5-3-THAT. What does "that provision" in s 5(3) name?**

- Readings seen: (A) the provision that says the Act, or a portion of it, is to come into force on a later day, that is, the commencement clause itself; (B) the Act or portion that is to come into force later.
- Taken: (A).
  The commencement clause is deemed in force from the date of assent, so the later day it names is itself operative.
  Under (B) the postponed portion would be deemed in force at assent, and the later day would do nothing.
- Licensing text: s 5(3) (line 50): "Where an Act contains a provision that the Act or any portion thereof is to come into force on a day later than the date of assent to the Act, that provision is deemed to have come into force on the date of assent to the Act."
  The antecedent of "that provision" is "a provision that the Act ... is to come into force on a day later".
- Encoded in `ca-interpretation-time.l4`, `Sections 5 and 6` (`the moment from which a provision postponing commencement is itself in force, for an Act assented to on`); tested in `ca-tests-commencement.l4`, `Worked case 1` (the assertion on `the moment from which a provision postponing commencement is itself in force, for an Act assented to on`).
  That module is a pass-1 file and carries no comment naming this fork; this entry is the pointer.

**F-32. Does a deviation from a prescribed form need to be free of both faults, or of either?**

- Readings seen: (A) "not affecting the substance or calculated to mislead" means neither fault: a deviation that does not affect the substance and is not calculated to mislead does not invalidate the form; (B) either suffices: a deviation that does not affect the substance is saved, and so is one that is not calculated to mislead.
- Taken: (A) for the answer TRUE: a deviation with neither fault does not invalidate the form.
  Every other deviation refuses, because on (B) some of them are saved and on (A) the text does not say what follows.
- Licensing text: s 32 (line 246): "deviations from that form, not affecting the substance or calculated to mislead, do not invalidate the form used".
  "Not X or Y" can be read as "neither X nor Y" or as "not X, or [not] Y".
- Encoded in `ca-interpretation-rules.l4`, `Section 32`; tested in `ca-tests-rules.l4`, `Section 32`.
  That module is a pass-1 file and carries no comment naming this fork; this entry is the pointer.

**F-24-DEPUTY. Does s 24(3) restrict the deputy of a public officer who is not a minister?**

- Readings seen: (A) subsection (3) restricts only the persons named in paragraphs (2)(c) and (d), a minister's deputy and a person appointed to serve in the department, so the deputy of a public officer other than a minister, whom subsection (4) names, may exercise an authority to make a regulation as defined in the Statutory Instruments Act; (B) subsection (3)'s evident purpose, a restriction as to public servants, reaches the deputy named in subsection (4) too.
- Taken: (A).
  The function for subsection (4) has no input about making a regulation, so it applies no restriction to the deputy.
  The marginal note "Restriction as to public servants" cannot widen subsection (3): marginal notes form no part of the enactment (s 14).
- Licensing text: s 24(3) (line 201): "Nothing in paragraph (2)(c) or (d) shall be construed as authorizing the exercise of any authority conferred on a minister to make a regulation"; s 24(4) (line 203) names the deputy of any public officer other than a minister.
- Encoded in `ca-interpretation-powers.l4`, `Section 24`; tested in `ca-tests-powers.l4`, `Section 24`.

**F-8-2-TERRITORIES. Are the territories among "the other provinces" of s 8.2?**

- Readings seen: (A) yes: section 35(1) "province" "means a province of Canada, and includes Yukon, the Northwest Territories and Nunavut", and section 3(2) applies the Act's provisions, including that definition, to the Act itself; (B) no: "provinces" has its ordinary sense of the ten provinces, and the Act says nothing of the territories.
- Taken: (A) in effect, without testing what a province is.
  The function takes one input, whether the place is the Province of Quebec; the answer for every other place the caller names is the common law terminology or meaning.
  A caller who holds (B) must not ask it about a territory.
  A place that is neither a province nor a territory (a place outside Canada) is not distinguished, and takes the same path.
- Licensing text: s 8.2 (line 89): "the civil law terminology or meaning is to be adopted in the Province of Quebec and the common law terminology or meaning is to be adopted in the other provinces"; s 35(1) "province" (line 330).
- Encoded in `ca-interpretation-rules.l4`, under `Section 3(1), section 8(1) and section 9` (`the terminology or meaning adopted, where an enactment contains both civil law and common law terminology, is` ...); tested in `ca-tests-rules.l4`, `Section 8.2`.
  That module is a pass-1 file and carries no comment naming this fork; this entry is the pointer.

**F-WRITING. Does "writing" include words that are not in visible form?**

- Readings seen: (A) "in visible form" qualifies the whole list, so words not in visible form (a spoken word) are not writing; (B) "in visible form" qualifies only the last mode ("any mode of representing or reproducing words in visible form"), and "includes" does not say that nothing else is writing.
- Taken: neither.
  Each listed mode, and any other mode of representing or reproducing words in visible form, is TRUE.
  Words not in visible form refuse (S-INCLUDES), because the readings differ on them.
- Licensing text: s 35(1) "writing" (line 360): "includes words printed, typewritten, painted, engraved, lithographed, photographed or represented or reproduced by any mode of representing or reproducing words in visible form".
- Encoded in `ca-interpretation-definitions.l4`, `s 35(1) "writing"`; tested in `ca-tests-definitions.l4`, same heading.

**F-HOLIDAY-PLACE. Is a day appointed or made a holiday for one place a holiday for a thing done in another?**

- Readings seen: (A) a day appointed or made a holiday for a province, city or district is a holiday only for a thing done in that place; (B) it is a holiday for a thing done anywhere, since the definition lists "any of the following days"; (C) the place that counts for a federal time limit is where the thing is "done", and the text does not say where a thing is done.
- Taken: whether the day was appointed or made for the place where the thing is to be done is an input.
  If yes, TRUE; if no, the named refusal.
  The time module takes the caller's holiday test as the test for the place where the thing is done and does not ask.
- Licensing text: s 26 (line 215): "the time limited for the doing of a thing expires or falls on a holiday"; s 35(1) "holiday" (lines 309-311): (a) "in any province, any day appointed by proclamation of the lieutenant governor of the province ... within the province, and any day that is a non-juridical day by virtue of an Act of the legislature of the province" and (b) "in any city, town, municipality or other organized district, any day appointed to be observed as a civic holiday".
  A day appointed by proclamation to be observed as a day of general prayer or mourning or of public rejoicing or thanksgiving, without a place, is listed before the additional days.
- Encoded in `ca-interpretation-definitions.l4`, `s 35(1) "holiday"` (the place condition) and `ca-interpretation-time.l4`, `Section 26` (the caller's test); tested in `ca-tests-definitions.l4` and `ca-tests-holidays.l4`, same headings.
  This entry replaces the class B entry S-HOLIDAY-PLACE of pass 2 (the independent test pass's A13, #290).

### Pass-2 entries of class B

**C-LGIC. Do the paragraphs of "lieutenant governor in council" for the territories govern, or paragraph (a)?** A convention, not a fork. Paragraph (a) speaks of "the province indicated by the enactment" and the text elsewhere makes "province" include the territories; paragraphs (b) to (d) name Yukon, the Northwest Territories and Nunavut. Taken: the named paragraphs govern the territories and (a) the provinces (s 35(1), lines 318-322); the two would give the same person in substance.

**C-45-ANY. Does section 45(3) reach the declarations that (1) and (2) name?** Taken: yes, so a repeal is not deemed to involve a declaration that the law was different, and an amendment is not deemed to involve a declaration that the enactment was in force, because (3) says "any declaration as to the previous state of the law" (line 434). The cells are FALSE and cite (3).

**S-INCLUDES. What does an `includes` definition say of a thing it does not name?** Nothing. The encoding returns the named refusal for "enact", "repeal", "public officer", "Act" (s 35(1)), "Canadian waters", "contravene", "county", "diplomatic or consular officer", "legislative assembly or legislature", "person", "Canada" ("for greater certainty, includes"), "oath" and "writing". A `means` definition gives the whole meaning and the answer is FALSE.

**S-HOLIDAY-PLACE.** Replaced on 2026-10-29 by the class A entry F-HOLIDAY-PLACE above, which says what was taken and why.

**S-45-ADOPTION. Does a repeal involve an adoption of the construction placed on the language?** Section 45(4) names re-enactment, revision, consolidation and amendment, not repeal. Refused.

**S-OATH. What does "oath" include where no solemn affirmation or declaration may be made instead of an oath?** The text states the inclusion for the cases where one may be made. Refused otherwise.

**C-3-1-GATE. Where is the contrary intention of s 3(1) asked?**
A convention, not a fork.
Section 3(1) applies "every provision of this Act" "unless a contrary intention appears", and that includes section 8.3(1), so a contrary intention in an enactment can displace section 8.3(1) like any other provision.
One reading is licensed by the text, so this is not a class A fork.
Taken: the contrary intention is asked once, by the gate `a provision of the Act applies to an enactment unless` (`ca-interpretation-rules.l4`, `Section 3(1), section 8(1) and section 9`), which a caller applies first.
The rule functions carry no contrary-intention input, except section 8(1), which says "unless a contrary intention is expressed" itself, and `a definition of section 35(1) applies`, which routes through the gate.
Tested in `ca-tests-reading.l4`, `Section 8.3`.
(The independent test pass's A9, #111.)

**S-3-1-KIND. Does s 3(1) apply the Act to an instrument that is not an enactment?**
The text settles what an enactment is: "enactment means an Act or regulation or any portion of an Act or regulation" and "Act means an Act of Parliament", and `means` gives the whole meaning.
So an Act of a legislature is no enactment (`is an enactment within section 2(1)` is FALSE for it), and section 3(1), which applies the provisions "to every enactment", says nothing of whether they apply to anything else.
Refused: `the provisions of the Act apply to an instrument of the kind` k `unless` ...
(`ca-interpretation-definitions.l4`, `Section 3(1)`).
(The independent test pass's #34 and #677.)

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

Run on 2026-10-29, after the pass-3 edits, in this directory with `L4=/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/ca81f332-162b-4c52-8cc3-57ed15b3f6fa/scratchpad/bin/l4-unstable-0528 L4_TARGET=unstable ./check.sh`; exit status 0.
The binary is `unstable-20261028-5e95b5a (unstable, 5e95b5a, 2026-10-28)`, sha256 `0f0f1b86d37164af242ca2b6c03aa31ddeedef752bd10474f1459b78cf539e9d`.
The output is also in `check-output.txt` here, byte for byte.

```
check.sh: the target is unstable, so the main check was skipped.
module                                    errors satisfied  failed  refused  expected
ca-interpretation-calendar.l4                  0         0       0        0         0
ca-interpretation-commencement.l4              0         0       0        0         0
ca-interpretation-definitions.l4               0         0       0        0         0
ca-interpretation-nouns.l4                     0         0       0        0         0
ca-interpretation-powers.l4                    0         0       0        0         0
ca-interpretation-reading.l4                   0         0       0        0         0
ca-interpretation-repeal.l4                    0         0       0        0         0
ca-interpretation-resolutions.l4               0         0       0        0         0
ca-interpretation-rules.l4                     0         0       0        0         0
ca-interpretation-time.l4                      0         0       0        0         0
ca-tests-commencement.l4                       0        60       0        0         0
ca-tests-counting.l4                           0        73       0        0         0
ca-tests-definitions.l4                        0       289       0        0         0
ca-tests-holidays.l4                           0       105       0        0         0
ca-tests-other.l4                              0        60       0        0         0
ca-tests-periods.l4                            0       193       0        0         0
ca-tests-powers.l4                             0        49       0        0         0
ca-tests-reading.l4                            0       154       0        0         0
ca-tests-red.l4                               10         0      10        0        10
ca-tests-repeal.l4                             0        53       0        0         0
ca-tests-resolutions.l4                        0        39       0        0         0
ca-tests-rules.l4                              0       133       0        0         0
ca-tests-schedule.l4                           0        55       0        0         0
ca-tests-transition.l4                         0        25       0        0         0
TOTAL (24 modules)                            10      1288      10        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
srcrefs gate on /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/ca81f332-162b-4c52-8cc3-57ed15b3f6fa/scratchpad/runs/iaw-ca/deposit/encodings/legalese-sonnet-5.5/../../registers/source-bundle/R.S.C.-1985-c.-I-21.txt:
srcrefs check: 645 src: lines, 328 runs, 378 locators, 0 problems
```

The baseline it replaced (the unchanged pass-1 folder, run before any change with this binary, in `PROGRESS.md`): 12 modules, 663 satisfied, 10 errors and 10 failed (all in `ca-tests-red.l4`), 0 refused; `srcrefs check: 381 src: lines, 157 runs, 179 locators, 0 problems`.
After pass 2 the same run gave 20 modules, 1198 satisfied, 10 failed, 0 refused, and `srcrefs check: 608 src: lines, 311 runs, 347 locators, 0 problems`.

Read it as follows.

- Twenty-four modules ran: ten encodings (no assertions of their own; they must check with no error) and fourteen test files.
- **1288 assertions are satisfied, none is refused, and none fails except the ten in `ca-tests-red.l4`**, which are meant to fail (`expected` = 10).
  The red file's errors (10) are those same ten failed assertions, which check.sh counts as errors; the TOTAL row's 10 errors and 10 failed are therefore the red file and nothing else.
- Every pass-2 number holds or grows by added assertions; two change by replacement of a wrong pass-1 assertion, logged under "Changes to existing modules": `ca-tests-other.l4` 59 to 60 and `ca-tests-rules.l4` 120 to 133.
  The other five pass-1 test files are as they were (periods 193, counting 73, holidays 105, commencement 60, repeal 53), and so are the red file's 10 and `ca-tests-schedule.l4`'s 55, `ca-tests-powers.l4`'s 49.
  Pass 3 adds 90 satisfied: transition 25, resolutions 39, definitions 10, reading 2, and 14 net in the two corrected pass-1 files (rules 13, other 1).
- The target is `unstable`, so the main comparison did not run.
- The `srcrefs` gate found 645 quotation lines in 328 runs and 378 locators in the ten modules, and no problem.
  It checks that each `-- src:N | text` line is exactly line N of the text and that each `@ref ... (src:N-M)` locator points at lines that were quoted; it does not check that the code does what the quotation says.
- `python3 -I coverage.py <raw text> check --strict` printed `coverage check: 354 units, 0 problems`.
- Every `l4 run` of a module or a test file, read for its diagnostics, shows only Hints (the `@lang en` Hint, "A module that declares nothing is English; this line can go.") and the Information lines that report satisfied assertions; no `DiagnosticSeverity_Error` or `_Warning` appears except the ten errors in the red file.

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
10. **Licence.** Settled in the subject's `STUB-SOURCE-LICENSE.md` ("Recorded 2026-10-25"), which pass 1 of this file did not have. What remains is for a human to confirm that the hundreds of `-- src:` quotation lines here keep the notice and attribution it asks for. See `SOURCE-LICENSE.md`.

11. **"Queen's" and the King.** The text, current to 2026-09-30, names the Queen's Printer (s 25(2)), the Queen's Privy Council for Canada (s 35(1) "Governor General in Council") and the Court of Queen's Bench (s 35(1) "superior court" (c)). Is the encoder's reading, that the body is the one now styled for the King, the reading a court would take? (F-QUEENS)
12. **Section 3(2).** Is the Act's own application to its interpretation subject to a contrary intention appearing in the Act itself? (F-3-2)
13. **"Public officer".** Does "in the federal public administration" reach a person on whom a duty is imposed? (F-PUBLIC-OFFICER)
14. **"Canada" and the exclusive economic zone.** Is the zone part of Canada? (F-CANADA-EEZ)
15. **Citation "as amended".** On what date? (F-40-2-DATE)
16. **The birthday.** Is the Sovereign's birthday a holiday in a year when a proclamation fixes another day? (F-HOLIDAY-BIRTHDAY)
17. **Sections 14 and 15.** The scope of "that appear after the end of a section" (F-14-SCOPE) and whether s 15(2)(a) qualifies s 15(1) (F-15).
18. **Borrowed terms.** The encoding asks as facts, and does not import, the Bank Act's Schedules I and II, the Oceans Act's zones, the Criminal Code's s 529.4(1), the Constitution Act, 1982's s 35, the National Defence Act's forces and the Canada Evidence Act's s 41. Which of these should become imports of those Acts' own encodings?
19. **Section 32.** Does "not affecting the substance or calculated to mislead" save a deviation that has neither fault, or one that lacks either? (F-32)
20. **Section 24(3) and (4).** Does the restriction on making a regulation reach the deputy of a public officer who is not a minister? (F-24-DEPUTY)
21. **Section 8.2 and the territories.** Are Yukon, the Northwest Territories and Nunavut among "the other provinces"? (F-8-2-TERRITORIES)
22. **Holidays and places.** Is a day appointed for one province, city or district a holiday for a thing done in another, and where is a thing "done" for a federal time limit? (F-HOLIDAY-PLACE)
23. **"Writing".** Does it include words that are not in visible form? (F-WRITING)
24. **Section 5(3).** Is "that provision" the commencement clause or the postponed portion? (F-5-3-THAT)
25. **An affirmed regulation.** On what day does a regulation subject to affirmative resolution come into force once it is affirmed? (F-39-AFFIRM)
26. **The Related Provisions item.** On what day did section 10 of the 1998 Act come into force, and which provisions did sections 12 to 16 of that Act amend? The deposited text gives neither, so the day is an input and the provisions are a fact the caller states.

## 8. Process notes

- **peeked.** Pass 2: nothing forbidden was opened (nothing under `commons`, `commonswt`, `canon`, another `runs/` directory or `~/.claude/`). One library grep outside the brief's allow-list: `jl4-core/libraries/prelude.l4` was grepped for `append` and `concat` (library behaviour, not an encoding of any Act). Pass 1 recorded that it read `jl4-core/libraries/daydate.l4` and grepped `prelude.l4` for library behaviour as well.
  Pass 1, outside the brief's allow-list (INPUTS_DIR, the two skills and their references, `doc/`), read `jl4-core/libraries/daydate.l4` and grepped `jl4-core/libraries/prelude.l4`, both for library behaviour (`YMD` strict, `Date` lenient, `add months` clamping, `Weekday of`, `elem`, `count`); neither is an encoding of an interpretation law.
- **Pass 3: peeked.**
  The reads of this session that were not asked for or are outside the brief's allow-list, reported because the brief asks for every one.
  The harness delivered attachments into this session, after a context summary, that named four files outside `runs/iaw-ca` and the skills: the contents of a backlog file in a commons worktree (`subjects/je/BACKLOG.md`) and of a script under `~/.claude/state/<session>/` (`reconcile.py`), and the paths only of the triage files of two other rows (`runs/iaw-au/review/triage.md` and `runs/iaw-uk/review/triage.md`).
  An earlier version of this paragraph said this session had read them; a search of its tool calls finds no read of any of the four, only one directory listing of the lead's state folder.
  None is an encoding of any Act, none was used for any decision here, and no encoding of any Act was read.
  The triage file of this row (`runs/iaw-ca/review/triage.md`, in this row's own run directory) was read for the scenario numbers quoted in `## Pass 3`.
- **Pass 3: what changed on disk.**
  `cmp` against a copy of the folder taken before the first pass-3 edit lists these `.l4` files as differing: `ca-interpretation-definitions.l4`, `ca-interpretation-powers.l4`, `ca-interpretation-reading.l4`, `ca-interpretation-rules.l4`, `ca-interpretation-time.l4`, `ca-tests-definitions.l4`, `ca-tests-other.l4`, `ca-tests-reading.l4`, `ca-tests-rules.l4`.
  New files: `ca-interpretation-commencement.l4`, `ca-interpretation-resolutions.l4`, `ca-tests-resolutions.l4`, `ca-tests-transition.l4`.
  Other files that differ: `NOTES.md`, `PROGRESS.md`, `SOURCE-LICENSE.md`, `check-output.txt`, `dispositions.txt`, `encoding.json`, `relations.txt`.
  Every other pass-1 file is byte-identical to its pass-2 state.
- **Pass 3: NOTES.md edited by exact anchors.**
  A script (kept outside this folder) located each target by an exact anchor, which is a heading, the start of a line, or a string asserted to occur exactly once in the file.
  After each edit it checked that the heading list had not lost a heading.
  Headings before: 26; after: 34, the 8 added being `## Pass 3` and its six subsections (`A`, `Coverage rows moved by pass 3`, `B`, `C`, `D`, `E`), and `## Reading a result`.
  The coverage table has 354 rows before and after (356 lines with its header and separator).
- **Pass 3: heads.**
  The resolutions module first had two functions whose heads began with the same keyword (`a regulation subject to`), the clash of pass 1; the heads were renamed before the module was run, by reading them against that list.
  The commencement module first lacked `IMPORT daydate`, and the checker said so loudly (`There are multiple definitions for the identifier __LT__`, because `<` on dates needs the library).
  A record built on one line inside an `#ASSERT` was a parse error; the tests build it with a helper function, as `ca-tests-commencement.l4` does.
- **Pass 3: expected values.**
  Each expected value in the two new test files and in the added assertions was written from the text beside the assertion before the module was run, and none was changed after a run.
  The two pass-1 assertions of a refusal that were wrong (the affirmed regulation, the number between the ends) were replaced, and the replacement is logged under "Changes to existing modules".
  That every new assertion passed on the first complete run is a reason to ask a reader to look at the expected values, not evidence that they are right.
- **Pass 3: positive control.**
  Before the new tests were trusted, wrong assertions (a TRUE claimed to be FALSE, a value claimed to be a refusal, a refusal claimed to be a value) were appended to scratch copies of `ca-tests-transition.l4` and `ca-tests-resolutions.l4`; 4 were counted as failed and 1 as refused, as intended, and the copies were deleted.
- **Pass 3: a reviewer model was consulted once, before the edits.**
  Its points were applied: keep the ends-included test in s 41(1) so that a reversed reference still includes its ends; correct the definition of inert reason 2 wherever it was stated; call the module's test of what an enactment is rather than copy it; decide the class of each fork and let the table follow; carry the fork pointers for pass-1 code in the register.
- **A slip of mine in a test, and what was done.** Two rows of `ca-tests-other.l4` ("the day counted in the month with index") first failed because I had typed the wrong month index for the day I expected (24347 and 24323 for February 2029 and December 2027, which are 24349 and 24335). The expected days were kept and the indices corrected to the months those days belong to; the comment in the file says so. No other expected value was changed after a run.
- **Heads renamed, for two different reasons.**
  First, a mixfix function whose head ENDS with a keyword (a keyword after the last parameter) is not recognised in an importing module (probed: `unexpected` / `could not find a definition` on the keyword).
  The heads that did this were in the time module (the s 23(5) head and `the calendar month ...`, now `the calendar month containing`) and in the rules module (the s 22 and s 35(1) "security" heads); each was reworded so that it ends on a parameter, and its callers were updated.
  Second, the calendar module's s 26 wrapper first shared a head keyword with the time module's s 26 function, and two operators that share a head keyword clash; it was renamed `the last day for a thing under the Act's own dated holidays when ...`.
- **Positive controls.** A deliberately wrong `#ASSERT` on a date counted as failed, `#ASSERT REFUSED` on a value counted as failed, and `#ASSERT` on a refusal counted as refused, in a scratch file, before the tests were trusted; `ca-tests-red.l4` keeps ten wrong expectations that fail on purpose.
- **Pass 2: heads that end in a keyword, hit again.** The same trap as in pass 1 (a mixfix head whose last element is a keyword is not recognised in an importing module) was hit once by a test error (`writing, section 35(1)` in the definitions module: the importing test file printed "expects 1 input, but here it is given 2" and "I could not find a definition") and three more times found by reading each head of the reading module (`s 10`, `s 41`, `s 42`). It is loud. Each head was renamed so that it ends on a parameter.
- **Pass 2: a precedence trap.** `NOT p OR q` on one line negates the whole disjunction; the checker says so (`ca-interpretation-reading.l4` s 4(2)). The expression was bracketed as `(NOT p) OR q`.
- **Pass 2: a parameter order trap.** In a mixfix head the parameters appear in the order of the head; the `GIVEN` list must be in the same order or the checker says "The names in a type signature must match those in the definition." (s 45).
- **Pass 2: the quotation lines.** `requote.py` rewrote the `-- src:N | text` lines of the new modules from the raw text after every edit, so the quotations are a script's, not typed. The gate runs over `ca-interpretation-*.l4`, so the new modules are named to match.
- **Pass 2: the Schedule test is generated.** `ca-tests-schedule.l4` was written by a script that reads lines 447 to 497 of the text, so no country name is typed by hand; it asserts each of the 51 rows, the count, and the whole list in order.
- **Pass 2: positive control.** Before the definitions tests were trusted, three deliberately wrong assertions were appended to `ca-tests-definitions.l4` (`#ASSERT` of a false claim, `#ASSERT REFUSED` of a value, `#ASSERT NOT` of a true claim); all three were reported as failed, and the file was restored.
- **Pass 2: expected values.** Each expected value in the four new test files was written from the text of the section, beside the assertion, after the module compiled and before any assertion was evaluated, and no expected value was changed after a run. No assertion failed at any run; the only first-run errors were syntax and type errors (the head that ended in a keyword; a precedence error; a parameter order error; a list written across lines inside a condition). That is a reason to ask a reader to look at the expected values, not evidence that they are right.

## Generators and checkers used and not shipped

Some files this document names were used while the encoding was written and are not in this folder: `coverage.py`, `dispositions.txt`, `relations.txt`, `units.py`.
They were scripts and tables written for one run and are not part of the encoding.
The counts and tables they produced are copied into this file, and the `.l4` modules, not the scripts, are the source of truth.
Where a script generated a module, the module in this folder is the file to edit, and its template is not shipped.
The lead keeps them outside this repository.

## Independent test pass

A separate agent that had not seen this encoding, its NOTES.md or its brief wrote `ANSWERS.md` from the text alone before it opened any `.l4` file: 678 numbered scenarios over every section, definition entry and the Schedule of the Act, including 61 where the text is silent.
It then wrote `tests-independent.l4`, one `#ASSERT` per scenario that the encoding has a function for (635 assertions), and ran it against this encoding.
`ANSWERS.md` is not kept in this folder; the scenario numbers `#N` in `tests-independent.l4` refer to it, and each assertion carries its provision.

| step | assertions | satisfied | failed | refused |
| --- | --- | --- | --- | --- |
| first run against the pass-2 encoding | 635 | 583 | 5 | 47 |
| after pass 3 (section "Pass 3") and the reconciliation below | 635 | 635 | 0 | 0 |

The 44 scenarios the encoding had no function for are the `-- GAP #N` lines in the test file; pass 3 added functions for several of them, and the rest are limits (section "Pass 3", part E).
Of the first-run passes, 38 are `#ASSERT REFUSED` where the encoding refused, 51 repeat another call (marked `dup of #N`), and 13 are day-level stand-ins for moment-of-day scenarios, so 635 is not 635 independent checks.

**What the 52 disagreements turned out to be.**

- **Three led to changes in the encoding (pass 3):** `a regulation subject to affirmative resolution can have come into force` refused for an affirmed regulation instead of answering that the bar is lifted (#568, #571, now TRUE), and the numbers between the two stated in "from 12 to 16" refused (#597, now TRUE; 11 still refuses, which is defensible and is reconciled).
  The author's gap list led to further changes: the Related Provision of 1998, c. 30, s. 10 had been left inert on a ground that is not valid and is now encoded, and s 39(1)(c) and (d) negative resolutions, the body before which a regulation is laid, s 7's permission limb and s 5(4) got functions (section "Pass 3", parts A and B).
- **Forty-two were the independent author's expectation, not the encoding, and are reconciled in the test file.**
  Each is rewritten in place (`#ASSERT REFUSED`, `#ASSERT NOT`, or the encoding's value) with a `-- RECONCILED #N` comment above it that quotes the original assertion and gives the reason; none is deleted.
  Twenty-four are cases the clause's own conditions do not reach: the encoding refuses outside a clause's stated conditions and does not say "section X does not reach this case", where the author wrote "no".
  Ten asked for a value (a day, a class, a name) in a case where the Act gives none.
  Three are inferences from a list or from silence (#167, #171, #556), two are scenarios for which the encoding has no function (#369, #370), and three asked the wrong question of a function (#149, #662, #663).
- **Six are genuine forks, registered in the fork register:** #266 (King's Printer, F-QUEENS), #290 (a day proclaimed in one province, F-HOLIDAY-PLACE), #410 and #411 (s 32, F-32), #580 and #581 (s 39(2), F-39-2-MOMENT).
- **One is a limit, stated in "Pass 3", part E, and reconciled:** #462, the zone record cannot tell "named" from "not addressed"; #662 and #663 above rest on the schedule of Commonwealth countries being matched by the names it prints, so "Samoa" or "Eswatini" answers `FALSE` without a refusal.

**Independence caveat.** The harness delivered attachments naming files that the lead's session had read before a context summary into the test author's session and into this encoder's session.
The test author's session received, at 08:52Z, the contents of a backlog file and of three of the lead's scripts (reconciliation, review set-up, verification) and the path of a fourth; its `ANSWERS.md` was last changed at 08:29Z, before that, and it had begun writing `tests-independent.l4` at 08:36Z.
This encoder's session received the contents of the backlog file and the reconciliation script, and the paths of two other rows' triage files.
A search of every tool call of both sessions finds no read of any of these beyond what was delivered, except one directory listing of the lead's state folder by this encoder.
The reviewer of this row records that it saw one helper script, which shows how a reconciled `refused` is written, before it weighed its "REACH" and "SHAPE" labels, and says its numbers and quotations do not depend on that.
The reconciliations above were decided by the lead from the text of the Act, not from those labels.

**Check.** `check.sh` with `tests-independent.l4` in the folder: 25 modules, 1923 satisfied, 10 failed (the expected ten in `ca-tests-red.l4`), 0 refused, run on 2026-10-29.
