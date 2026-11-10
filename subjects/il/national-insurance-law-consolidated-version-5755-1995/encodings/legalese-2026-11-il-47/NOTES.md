# Row il-47: the citations of "Schedule B" in four regulations, and of the local professional committee in a fifth, under the National Insurance Law [Consolidated Version], 5755-1995

Status: draft, version 0.1.0, target compiler main.
No domain expert has read this against the source.
Every claim below was checked against a text in the source bundle or a page image named beside it; where it was not, it says so.

## 1. Scope

This row is not an encoding of the National Insurance Law [Consolidated Version], 5755-1995, and not an encoding of any regulation made under it.
It records citations as typed values that tests check: for each citation, what the citing words say they point at, what the target is, and where each of the two readings comes from.
Part one records eight citations in five regulations of the schedule that the Law of 1995 letters ב: six that do not point at what the words say, kept as expected-red tests, and two sound controls that cite the schedule the Law of 1995 letters ט.
Part two records six references in the Long-Term Care Insurance regulations (choice of a cash benefit): five that name the local professional committee or section 232 of the Law, which the Law no longer has, kept as expected-red tests, and one sound control.
Part two is in its own two files (`il47-references-044.l4`, `il47-tests-044-red.l4`) and is listed apart in `check.sh` and in `encoding.json`, so it can be removed without touching part one.
The row states only what the texts say; it states no purpose and no effect on any person.
No domain expert has read this against the source.

The seat is a named individual in each part, and the row asks no question from the seat, because it records references and not duties, so no `@export` module is written.
For part one it is a widow who has remarried and whose husband's income is tested against a twelfth of the amount in item 1 of Schedule B (regulation 2 of the survivors-pension regulations: אלמנה שחזרה ונישאה).
For part two it is a person entitled to a nursing benefit (a זכאי) who asks to receive it in cash (regulation 1(א) of the care regulations).

## 2. Sources

The regulations are read from seven Hebrew Wikisource consolidations, which are unofficial aids and are deposited in `../../registers/source-bundle/aids/` with revision ids; their sha256 values were recomputed with Python hashlib on 2026-11-10 and equal the values in `../../registers/source-bundle/aids/SOURCES.json`.
Every statement that rests only on one of them says CONSOLIDATION-ONLY.

| tag | regulations (Hebrew Wikisource consolidation) | revision | last edited | sha256 |
| --- | --- | --- | --- | --- |
| r010 | Vocational Training and Subsistence Allowance, 5739-1979 | 2980516 | 2026-01-27T07:00:23Z | ddb3db7e10ea99921bce3665680cf2b4722ea05fae77299ad9b230b370905027 |
| r024 | Determining Income in Old-Age and Survivors Insurance, 5737-1976 | 2926263 | 2025-05-13T11:40:56Z | 8b989d3e0f26990253fc02635debff79e7c1987ab0231cbfe1e1fd8bf548ed51 |
| r030 | Definition of Disabled Persons Income, 5736-1975 | 2926226 | 2025-05-13T11:36:50Z | 6a8753cd442951f63ba6e667adaf9a3438a22e90fdeca39461282ac5de42ca19 |
| r036 | Proportional Old-Age Pension, 5731-1971 | 2980517 | 2026-01-27T07:00:26Z | a8d27bd1ecc1df4df88dfa594ce5b1293321936fc13ae0194e18f8d16db3b26c |
| r042 | Grants for Reasons of Justice, 5735-1975 | 2926234 | 2025-05-13T11:37:44Z | 3e4d4f92493f7f100e2e4590fbb3f6a9856e4c7668620bfb7c65401f09d19604 |
| r044 | Long-Term Care Insurance, Choice of a Cash Benefit, 5774-2014 | 2926212 | 2025-05-13T11:35:30Z | aafa905c2a1443c4da3e1e37362bba8373fc8970b730537d4921aafcbf959b68 |
| r045 | Survivors Pension for a Remarried Widow, 5737-1976 | 2926265 | 2025-05-13T11:41:10Z | 0ac4c23977033588ebcc3cea93286538e0105bb9fcb2585dd7b2dcf734243053 |


The official instruments are in `../../registers/source-bundle/official/` (and the Sefer HaChukim of 1995 in `../../registers/source-bundle/amending-laws/13_lsr_203774.pdf`, which was already in the bundle), each with the page images read, rendered at 100 dpi into `official/img/`.
Every PDF in `official/` is an extract of only the pages the row reads from, cut with qpdf from the whole issue: `sh2774-5779-p152-153-nii-amendment-210.pdf` (printed pp. 152 to 153; 2 of 3 PDF pages), `kt6573-5767-p648-regulations-14-march-2007.pdf` (p. 648; 1 of 8), `kt7669-5776-p1328-1329-regulations-9-june-2016.pdf` (pp. 1328 to 1329; 2 of 28) and `kt3608-5737-p223-regulations-28-oct-1976.pdf` (p. 223; 1 of 33, image only).
For Sefer HaChukim 2511 no PDF page is deposited, because printed pages 247 and 248 carry the text of other provisions: three strips cropped from the page images are deposited instead (`official/img/sh2511-p247-heading-strip.png`, `sh2511-p248-schedule-b-repealed-strip.png`, `sh2511-p249-s31-commencement-strip.png`).
For Sefer HaChukim 1522 pp. 299 and 301 only the lines of the schedule the row reads are deposited, as crops of the page images (`official/img/sh1522-p299-schedule-b-as-enacted-crop.png` and `official/img/sh1522-p301-schedule-t-as-enacted-crop.png`).
The whole files are not in the bundle; `official/SOURCES.json` gives the URL, retrieval date, sha256 and size of each whole file as downloaded (under `whole_files_not_deposited` and in the `whole_file` field of each extract) and the sha256 and size of each deposited file, all recomputed on 2026-11-10.
The Knesset files were fetched from fs.knesset.gov.il; the Kovetz HaTakanot files were fetched from olaw.org.il, an unofficial archive of Reshumot issues that is not the Knesset's own site.

| instrument | pages | read from | what it is used for |
| --- | --- | --- | --- |
| Sefer HaChukim 1522 (15 May 1995), the Law as enacted | 299, 301 | crops of the page images | the schedule lettered ב (Treasury allocation, items 1 and 2, with [י״ד] beside it) and the schedule lettered ט (the amount for a person without dependants, one dependant and each further dependant, with [ב׳] beside it) |
| Sefer HaChukim 2511 (30 November 2015), the Economic Efficiency Law for the 2015 and 2016 budget years | 247 (heading, opening of s 30), 248 (items (3) and (4) of s 30), 249 (s 31) | strips cropped from the page images; no PDF page deposited | item (4) of the instruction on p. 248 repeals the schedule lettered ב; s 31 on p. 249 commences the Subsection on 20 Tevet 5776 = 1 January 2016 |
| Kovetz HaTakanot 3608 (28 October 1976) | 223 | page image (the PDF has no text layer) | regulation 2 of the survivors-pension regulations as made |
| Kovetz HaTakanot 6573 (14 March 2007) | 648 | text layer only | the latest instrument found for regulation 1 of the vocational-training regulations; deletes one definition in regulation 1 and replaces a phrase in regulations 6 and 12 and in the Addendum |
| Sefer HaChukim 2774 (1 Shevat 5779 = 7 January 2019), National Insurance Law Amendment 210 | 152, 153 | page image | s 1 strikes the committee's definition from s 223; ss 2 to 4 name the Institute where the committee was named; s 5 repeals ss 231 and 232; s 7 commences the Amendment on 27 Iyar 5779 = 1 June 2019 for claims submitted from that day |
| Kovetz HaTakanot 7669 (3 Sivan 5776 = 9 June 2016) | 1328, 1329 | page image | the 2016 amendment of the care regulations: s 1 (regulation 2(ג)(1)), s 2 (regulation 3), s 3 (regulation 4(א)), s 4; signed 5 Adar II 5776 = 15 March 2016 |

The Hebrew of an official page is typed from the page image on a line `-- ext:[SH <issue> p.<page>, ...] | ...` in `il47-cross-references.l4` or `il47-references-044.l4`.
`tools/pdfcheck.py` checks that every Hebrew word of such a line occurs in the text layer of that page: 18 quotation lines checked, 5 on a page with no text layer here (not checkable), 0 problems.
It does not check digits, punctuation or the order of words (the text layers reverse and interleave runs); on a copy of the file, a changed Hebrew word was reported and a changed digit was not.
So every digit and date in those lines was compared with the page image by eye, and the lines typed from pages that have no text layer here (two from Kovetz HaTakanot 3608 p. 223, which is image only, and three from the strips of Sefer HaChukim 2511) cannot be checked by the script at all.
The Hebrew of the consolidations is expanded mechanically by `tools/extquote.py` (`ext:[r010]` and the other `ext:[rNNN]` lines).
`tools/hebcheck-all.sh *.l4 NOTES.md` finds every other run of Hebrew in the `.l4` files and in this file in the consolidations and exits 0.
The Hebrew dates were run through a calendar routine after it reproduced 30 Kislev 5785 = 31 December 2024: 20 Tevet 5776 = 1 January 2016, 5 Adar II 5776 = 15 March 2016, 27 Iyar 5779 = 1 June 2019, 1 Shevat 5779 = 7 January 2019, 3 Sivan 5776 = 9 June 2016, 18 Kislev 5776 = 30 November 2015.
Every pair matches the Gregorian date printed beside it.

## 3. Files

| file | what it holds |
| --- | --- |
| `il47-nouns.l4` | the kinds of provision, the sources of a reading, and the record of a citation; no rule |
| `il47-cross-references.l4` | part one: the functions, and one typed value per citation with the words of the citing regulation and of the target quoted beside it |
| `il47-tests-xrefs.l4` | part one: 40 assertions that hold: the controls, the second reading of each defect, what was read from where, whether the cited item exists, the day the schedule was repealed |
| `il47-tests-xrefs-red.l4` | part one: 13 assertions that fail, on purpose (section 7) |
| `il47-references-044.l4` | part two: its own record type and functions, five references that name the committee or section 232 and one control, and 17 assertions that hold |
| `il47-tests-044-red.l4` | part two: 10 assertions that fail, on purpose (section 7) |
| `check.sh`, `fetch-main-l4.sh` | the check; `check.sh` declares 13 and 10 expected failures for the two red files |
| `tools/` | `extquote.py`, `srcquote.py`, `hebcheck.py`, `hebcheck-all.sh`, `pdfcheck.py` |

## 4. Coverage

| provision | status |
| --- | --- |
| survivors-pension regulations (5737-1976), regulation 2, item 1 of לוח ב׳ | encoded; a defect; both limbs official, with the proviso on limb (b) in section 5 |
| vocational-training regulations (5739-1979), regulation 1, definition of הכנסה מותרת, items 1 and 3 of לוח ב׳ | encoded; two defects; limb (a) official, limb (b) CONSOLIDATION-ONLY plus a text-layer reading of the 2007 instrument |
| proportional-pension regulations (5731-1971), regulation 1(2) | encoded; a defect; limb (a) official, limb (b) CONSOLIDATION-ONLY |
| grants regulations (5735-1975), regulations 4(א) and 17 | encoded; two defects; limb (a) official, limb (b) CONSOLIDATION-ONLY |
| determining-income regulations (5737-1976), regulation 1(ב); disabled-persons-income regulations (5736-1975), regulation 1א(1), both citing לוח ט׳ לחוק | encoded; two sound controls; both limbs CONSOLIDATION-ONLY |
| care regulations (5774-2014), regulations 2(ג)(1), 3(א) twice, 3(ב), 4(א): the committee and section 232 | encoded in part two; five defects |
| care regulations, regulation 3(א), the documents listed in regulation 1 | encoded in part two; a sound control |
| care regulations, the citation of section 231(ד) in the opening words that give the Minister's powers | not encoded and not asserted: it is an enacting-formula citation, which is not a reference the regulations rely on to operate |
| every other provision of the seven sets of regulations | out-of-scope: this row reads only the sentences that carry the citations above and says nothing of what the rest of those regulations provide, nor of any other citation in them |
| every other provision of the National Insurance Law | out-of-scope: this row does not encode the Law; it reads two schedules as enacted, the instruction that repealed one of them, and the instructions of Amendment 210 that bear on the committee, and says nothing of the rest of the text |
| the amending instruments of the seven sets of regulations other than those in section 2 | out-of-scope: the consolidations list them and they were not read; where that matters it is said in the answer table |
| whether the Interpretation Law, 5741-1981 bears on how a changed lettering or a repealed provision in a cited law is read | not checked |

## 5. Answer tables

"Stands" means that the target is in the official text of the Law today.
Limb (a) asks whether the target is what the citing words say; limb (b) asks whether the citing words still read so in the latest official text of the citing provision.
The two descriptions of the target in the first table are the literal reading (the letter as the Law of 1995 prints it) and the reading through the old lettering (fork R1); the table gives the literal one in the "target says" column and the other in the "if read through the old lettering" column.

### Part one: the schedule lettered ב

| citation | citing words say | target says (literal) | if read through the old lettering | the cited item exists | stands | limb (a) | limb (b) | pages read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| survivors pension, regulation 2, item 1 | the amount named in item 1 of לוח ב׳ לחוק (a twelfth of it is the limit on the husband's income) | item 1 of the schedule lettered ב: a base (old-age and survivors insurance contributions) and a rate of 15% | item 1 of the schedule lettered ט: the amount for a person without dependants, 57% of the average wage | yes | the schedule lettered ב: no, from 1 January 2016 | official | official as made (Kovetz HaTakanot 3608 p. 223, image); that no later instrument touched it is CONSOLIDATION-ONLY (the consolidation lists none) | SH 1522 pp. 299, 301; SH 2511 pp. 248, 249; KT 3608 p. 223 |
| vocational training, regulation 1, item 1 | the amount in item 1 of לוח ב׳ לחוק (definition of הכנסה מותרת) | as above | as above | yes | no, from 1 January 2016 | official | CONSOLIDATION-ONLY, plus Kovetz HaTakanot 6573 p. 648 (text layer only), which deletes another definition in regulation 1 and whose text layer has none of the three strings searched for (the defined term and the headings of the two schedules; see the comment in `il47-cross-references.l4`; the search was run on the whole 8-page issue on 2026-11-10, before the PDF was cut to the one page deposited, and cannot be repeated from the bundle) | SH 1522 pp. 299, 301; SH 2511 pp. 248, 249 |
| vocational training, regulation 1, item 3 | the amount in item 3 of לוח ב׳ לחוק (for each further orphan) | no item 3: the schedule lettered ב has items 1 and 2 only | item 3 of the schedule lettered ט: 7% of the average wage for each further dependant | no | no, from 1 January 2016 | official | as above | as above |
| proportional pension, regulation 1(2) | the amount in לוח ב׳ לחוק | the schedule lettered ב as a whole | the schedule lettered ט as a whole | yes | no, from 1 January 2016 | official | CONSOLIDATION-ONLY (the instrument the consolidation lists, Kovetz HaTakanot 5731 p. 859, was not read) | as above |
| grants, regulation 4(א) | the amount in לוח ב׳ לחוק, by the number of dependants | as above | as above | yes | no, from 1 January 2016 | official | CONSOLIDATION-ONLY (the two instruments the consolidation lists were not read) | as above |
| grants, regulation 17 | the amount in לוח ב׳ לחוק | as above | as above | yes | no, from 1 January 2016 | official | as above | as above |
| control: determining income, regulation 1(ב) | the amount in לוח ט׳ לחוק | the schedule lettered ט | the same | yes | not answered (NOTHING) | CONSOLIDATION-ONLY (the same schedule is printed under the same letter, items 1 to 3, in SH 1522 p. 301) | CONSOLIDATION-ONLY | SH 1522 p. 301 |
| control: disabled persons income, regulation 1א(1) | the amount in לוח ט׳ לחוק | the schedule lettered ט | the same | yes | not answered (NOTHING) | as above | CONSOLIDATION-ONLY | as above |

What is read from the page images in part one: that SH 1522 p. 299 prints the schedule lettered ב under the heading about the Treasury's allocation to the Institute, section 32, with [י״ד] beside the letter, items 1 and 2; that p. 301 prints the schedule lettered ט, section 245, with [ב׳] beside it and items 1 to 3; that SH 2511 p. 248 item (4) repeals "לוח ב'"; that SH 2511 p. 249 s 31 commences the Law as worded in that Subsection on 20 Tevet 5776 = 1 January 2016; and the wording of regulation 2 of the survivors-pension regulations as made (KT 3608 p. 223).
What is not read: the Law of 1968 as it stood when the regulations were made; the instruments the consolidations list for regulations 036 and 042; the 1980, 1988, 1994 and 1998 amendments of the vocational-training regulations; the 1993, 2003, 2005 and 2011 amendments of the determining-income regulations; the 1993, 2003 and 2005 amendments of the disabled-persons-income regulations.
The page that heads the repealing Subsection (SH 2511 p. 247) is read from the strip of its image that holds the heading and the opening of s 30.

### Part two: the care regulations

Transitional s 7 of Amendment 210 limits the new regime to claims submitted from 1 June 2019, and no saving for earlier claims was seen in ss 5 and 6 of that Amendment; that is a fork (F1), not a conclusion.

| reference | citing words say | target says | exists | limb (a) | limb (b) | pages read |
| --- | --- | --- | --- | --- | --- | --- |
| regulation 2(ג)(1) | the application goes to לוועדה המקומית המקצועית; the change takes effect from its receipt there | the committee's definition is struck from s 223 (s 1); the Institute is named where the committee was named (ss 2 to 4); ss 231 and 232 are repealed (s 5) | no, for a claim submitted from 1 June 2019; before that, not answered (NOTHING) | official, SH 2774 pp. 152, 153 | official: the words were written by KT 7669 p. 1328 s 1 (2016) | SH 2774 pp. 152, 153; KT 7669 p. 1328 |
| regulation 3(א), the committee | the Institute passes the application to the committee for the committee's function under s 232 | as above | as above | official | the words of 3(א) as made in 2014 (Kovetz HaTakanot 5774 p. 628) were not read; KT 7669 p. 1328 s 2 marks the existing text "(א)" and does not change it; so: the consolidation, and the latest amending instrument read from its page image | as above |
| regulation 3(א), section 232 | the committee's function under section 232 of the Law | s 232 is repealed (SH 2774 p. 152 s 5); the Law names no section where the words point; the Amendment writes section 225(א1) in place of section 232 in s 225ב(א) (s 4) and in no other place on the pages read | no | official | as the row above | as above |
| regulation 3(ב) | the committee's belief that a closer examination is needed, and its written reasons | as above | no, for a claim submitted from 1 June 2019; before that, NOTHING | official | official: the words were written by KT 7669 p. 1328 s 2 | SH 2774 pp. 152, 153; KT 7669 p. 1328 |
| regulation 4(א) | a local professional committee, or someone on its behalf, makes two visits a year | as above | as above | official | KT 7669 p. 1329 s 3 changes one word in regulation 4(א) and leaves the committee words as they were; those words are read from the consolidation; so: the consolidation, and the latest amending instrument read from its page image | SH 2774 pp. 152, 153; KT 7669 p. 1329 |
| control: regulation 3(א), "בתקנה 1" | the documents and data listed in regulation 1 | regulation 1 of the same regulations: the form and the employment agreement (consolidation line 15) | yes by the consolidation; the 2016 amendment has four sections and none touches regulation 1 (KT 7669 pp. 1328 and 1329, read from the images) | CONSOLIDATION-ONLY | the consolidation, and the latest amending instrument read from its page image | KT 7669 pp. 1328, 1329 |

## 6. Fork register

Each fork gives the reading taken, the reading rejected, and the Hebrew that licenses each.

- K1, the kinds.
  The kinds in `What a provision is about` and `What regulation 044 names` are my plain descriptions, so that two descriptions of the same thing are the same kind; they are not the Law's terms.
  Taken: one kind per target as its heading or first words describe it.
  Rejected: comparing the Law's words as strings, which would make every citation fail on punctuation.
- R1, the lettering of the schedules (part one).
  The regulations were made between 1971 and 1979, before the Law of 1995, and cite לוח ב׳ לחוק.
  Reading A, the letter as the Law of 1995 prints it: SH 1522 p. 299 prints the schedule under the letter ב with the heading that names the Treasury's allocation to the Institute (typed in `il47-cross-references.l4`) and items 1 and 2, so the words reach a schedule of the Treasury's allocation, whose item 1 states a rate of 15%, and whose item 3 does not exist.
  This is what the failing assertions state.
  Reading B, a court reads the old lettering as the new: SH 1522 p. 301 prints the schedule lettered ט with [ב׳] beside it and the heading that names the maximum income for an old-age pension (typed in `il47-cross-references.l4`), with items 1 to 3 that state amounts as a share of the average wage; the regulations speak of הסכום הנקוב, an amount, set against income.
  On this reading the six citations reach the income schedule, and the passing assertions for reading B state it.
  I read the brackets as the letter the schedule carried before 1995; no page read says what the brackets mean, and the Law of 1968 was not read.
  Neither reading is asserted as the law; both are recorded.
- I1, item 3 of the vocational-training definition.
  On reading A the schedule has no item 3 (SH 1522 p. 299 prints items 1 and 2); on reading B the income schedule has item 3 (SH 1522 p. 301: 3 בעד כל תלוי נוסף).
  The row records both and asserts that, as enacted, item 3 does not exist in the schedule lettered ב.
- D1, a day before the repeal.
  No source in the bundle says when the schedule lettered ב was added or that it stood on a given earlier day.
  Taken: for 31 December 2015 and any earlier day the answer is NOTHING; for 1 January 2016 and every later day it is JUST FALSE.
  Rejected: JUST TRUE for earlier days, which no page read states.
  A control has no recorded repeal, so its answer is NOTHING on every day; that is not a statement that its target stands.
- F1, the claims before 1 June 2019 (part two).
  SH 2774 p. 153 s 7 says the Amendment begins on 27 Iyar 5779 = 1 June 2019 and applies to a claim for a nursing benefit submitted from that day (the Hebrew is typed in `il47-references-044.l4`).
  Taken: for a claim submitted before that day the answer is NOTHING; from that day it is JUST FALSE that the committee or section 232 stands in the Law.
  Rejected, first: JUST TRUE for earlier claims, because the words of s 7 limit the application of the Amendment but ss 5 and 6, which repeal ss 231 and 232 and replace s 233, contain no saving and no sentence that keeps the committee for earlier claims; no page read says either.
  Rejected, second: JUST FALSE for every day, for the same reason.
- F2, reading through the Amendment's own substitutions (part two).
  Reading A: the regulations name a committee and a section that the Law no longer has, so the words point at nothing in the Law.
  Reading B: a court reads the Institute into the committee's role, which is what SH 2774 p. 152 writes in ss 2 and 3 (the Hebrew is typed in `il47-references-044.l4`: the committee and the Institute "are permitted" is replaced by the Institute "is permitted"), and reads section 225(א1) in place of section 232, which s 4 of the same page writes in s 225ב(א) (the Hebrew is typed in `il47-references-044.l4`).
  The row records what the Amendment writes, as passing assertions, and asserts that the words do not point at what the Law names today; it does not assert that the regulations are read through the substitution.
  The substitution for section 232 is written by the Amendment in one other provision; whether it carries into regulation 3(א) is not answered on the pages read.
- F3, the dates in part two.
  The 2016 amendment is signed 5 Adar II 5776 = 15 March 2016 (KT 7669 p. 1329) and published on 9 June 2016; Amendment 210 was published on 7 January 2019 and begins on 1 June 2019.
  The row says only that the committee was written into regulations 2(ג)(1) and 3(ב) in 2016 and removed from the Law's text in 2019; it states no consequence.
- N1, an enacting-formula citation.
  The opening words of the 2014 regulations and of the 2016 amendment cite section 231(ד) among the sections that give the Minister power.
  That is an enacting-formula citation; no assertion is made about it.
- N2, the Interpretation Law is not checked (section 4).

## 7. Expected red

Part one, `il47-tests-xrefs-red.l4`, 13 assertions fail on purpose, one group per defect, and the count (13) is declared in `check.sh` and in `encoding.json`.
For each of the six defects: `the citation points at what it says` (the words say the income schedule or its item; the literal target is the Treasury allocation schedule or has no such item) and `the target stands in the official text on` 10 November 2026, expected JUST TRUE (the answer is JUST FALSE, because the schedule lettered ב was repealed from 1 January 2016).
The thirteenth states that the cited item exists in the target for the vocational-training item 3 (it does not exist in the schedule lettered ב).
Part two, `il47-tests-044-red.l4`, 10 assertions fail on purpose, two for each of the five references: `the reference points at what the Law names today` and `the target stands in the Law for a claim submitted on` 10 November 2026, expected JUST TRUE (the answer is JUST FALSE).
The count (10) is declared in `check.sh` and in `encoding.json`.
Nothing in any file was edited to make a red assertion pass.

## 8. Check numbers

Run as `L4=~/.local/bin/l4 ./check.sh`; the main build is 1.6.109 (main, 4c887e0, 2026-11-04).
Both binaries give the same four counts for every file.

| file | errors | satisfied | failed | refused | expected failed | main: errors | satisfied | failed | refused | main columns |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `il47-cross-references.l4` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| `il47-nouns.l4` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| `il47-references-044.l4` | 0 | 17 | 0 | 0 | 0 | 0 | 17 | 0 | 0 | same |
| `il47-tests-044-red.l4` | 10 | 0 | 10 | 0 | 10 | 10 | 0 | 10 | 0 | same |
| `il47-tests-xrefs-red.l4` | 13 | 0 | 13 | 0 | 13 | 13 | 0 | 13 | 0 | same |
| `il47-tests-xrefs.l4` | 0 | 40 | 0 | 0 | 0 | 0 | 40 | 0 | 0 | same |
| total (6 files) | 23 | 57 | 23 | 0 |  | 23 | 57 | 23 | 0 | same |

The check counts error diagnostics and assertion lines and nothing else; it does not see a difference that no assertion exercises.
The 23 errors are the 23 expected failures; each failure message in the two red files is `assertion failed`, and the same functions return TRUE and JUST FALSE in the passing files, which is the positive control for the red assertions.
No mutation control was run on these tests.

## 9. Open questions for a domain expert

- Does the schedule lettered ב in the regulations of 1971 to 1979 mean the schedule the Law of 1995 letters ט (fork R1)? The Law of 1968 was not read.
- Did an instrument not read (the instruments the consolidations list for regulations 036 and 042, and the 1980, 1988, 1994 and 1998 amendments of regulation 010) change the lettering in any of the regulations?
- What does the Law provide for a claim for a nursing benefit submitted before 1 June 2019 as to the committee (fork F1)?
- Is the substitution of section 225(א1) for section 232 in section 225ב(א) meant to carry into regulation 3(א) (fork F2)?
- Does the Interpretation Law bear on any of the above (not checked)?

No domain expert has read this against the source.
