# Row il-55: five citations in the Planning and Building Law, 5725-1965, and its regulations, that do not point at what their words say (four defects, three controls)

Status: draft, version 0.1.0, target compiler main.
No domain expert has read this against the source.
Every claim below was checked against a text in the source bundle or a page image named beside it; where it was not, it says so.

## 1. Scope

This row is not an encoding of the Planning and Building Law, 5725-1965, or of any regulation made under it.
It records five citations as typed values that tests check, and keeps the ones that do not point at what their words say as expected-red tests.
Defect A is sub-paragraph (א) of paragraph (7) of subsection (ב) of section 145ב, which cites "145(א2)(4)" and "145(א3)(4)": the consolidation prints no paragraph (4) in subsection (א2), and prints paragraph (4) of subsection (א3) as a rule about an application the engineer did not answer, while the citing words describe the Minister's setting of preconditions.
Defect B is regulation 83(א) of the Planning and Building (Building Licensing) Regulations, 5776-2016, which cites "257א", a section that Amendment 116, 5777-2017, repealed.
Defect C is the definition of "respondent" in the Planning and Building (Procedure on an Application for a Decision before an Arbitrator Appraiser or an Advisory Appraiser) Regulations, 5769-2008, which cites "198א", and the consolidation prints no section with that number.
Defect D is regulation 2(ד) of the Planning and Building (Pay of an Arbitrator Appraiser and an Advisory Appraiser) Regulations, 5769-2009, which cites "202(ה)(2)", and the consolidation prints section 202 with no subsections.
For each citation the row types two descriptions, what the citing words say they point at and what the target is, and records where each of the two readings comes from.
Defects C and D each have a second value, a reading that I supplied and that no page prints (forks F4 and F5); the text does not say which reading is meant, and the row does not rule.
Each defect has a control that is a sound citation in the same text or beside it: section 145ב(ב)(9) cites "152(א2)" (A); the enacting formula of the licensing regulations cites "145א" (B); the next definition in the procedure regulations cites "202ג" (C and D).
The row does not say what section 257א provided before its repeal, because its wording is in none of the deposited pages (fork F1).

## 2. The seat

The seat is the person who files an application for a building permit, and the drafter of that application, who makes the declaration that section 145ב(ב)(7) requires (whole-page line 2346 of the Law excerpt).
The regulations in defects C and D concern a request that an appraiser decide a dispute, and the regulation in defect B concerns the licensing authority; the row asks no question from any of these seats, because it records references and not duties, so no `@export` module is written.

## 3. Sources

The Law is read from the Hebrew Wikisource consolidation, page "חוק התכנון והבניה", revision 3099048, last edited 2026-10-29T14:00:44Z, retrieved on 2026-11-10; it is an UNOFFICIAL aid.
Only an excerpt is deposited, at `../../registers/source-bundle/planning-and-building-law-5725-1965.he.wiki.excerpt.txt` (7697 bytes, sha256 38bb4b65b17821d05019d286d9e5898812b0bf4340f7559afc1475191ceaaade): thirteen blocks of whole-page lines copied unaltered, with the whole page's size and sha256 and the line numbers copied in its first lines.
The whole page as retrieved is 1378771 bytes, 5632 lines counted by splitting at newlines (5631 newline characters), sha256 2f555344e2b136371afbc50ccdb0c48af8411d6962203e51494c05f9965e0529; the whole page is not deposited.
Three Wikisource consolidations of regulations are read, each UNOFFICIAL and each deposited in `../../registers/source-bundle/`:

| page | what is deposited | whole page as retrieved |
| --- | --- | --- |
| Building Licensing Regulations, 5776-2016 (tag `lic`) | an excerpt of three blocks (2157 bytes, sha256 424d4ea307e29ff67c9e53fa4b33acf171cf9db5360f21edcefb1b1a178fac24) | 249045 bytes, 1384 lines (1383 newline characters), sha256 362681fc10ee727c3ccc35dfc65fd2f662118c6708d6bb0bf4c5f90035732360 |
| Pay of an Arbitrator Appraiser Regulations, 5769-2009 (tag `fee`) | an excerpt of three blocks (1604 bytes, sha256 15d459f1efe13092765c221051938705f5d26361e17a1f4ae93d9ced84a9c086) | 15408 bytes, 86 lines, sha256 eefaae8dca0aae5f4c996a9033893f6767ccf19bd1c9fb60a8f0a732d2e9afdf |
| Arbitrator Procedure Regulations, 5769-2008 (tag `proc`) | the whole page (21358 bytes, sha256 6296708aab254d98bb27af657f0658a1b87b27632982676f1fd8509361e73eae); it is short | the same |

A `src:N` line in `plan55-cross-references.l4` is whole-page line N of the Law, and a `src:lic:N`, `src:fee:N` or `src:proc:N` line is line N of the page of that tag; each is expanded mechanically by `tools/srcquote.py`, which maps N through an excerpt's `#### whole-page lines A-B` marker lines, or counts lines from 1 in the whole page.
The revision id of the Law came from a page-history query made in the same session, not from matching the fetched file to a history row; the revision ids of the three regulation pages were not recorded (fork F8).
Every statement that rests only on a consolidation says CONSOLIDATION-ONLY.
That the consolidation prints no section 198א was checked on the whole page of the Law, which is not deposited: a search for a section heading whose number begins 198 finds one line, the heading of section 198 at whole-page line 3584, and a search for the characters 198א anywhere on the page finds none (CONSOLIDATION-ONLY; both were run on 2026-11-10 on the retrieved file).

The official pages are in `../../registers/source-bundle/amending-laws/` (Sefer HaChukim) and `../../registers/source-bundle/official/` (Kovetz HaTakanot), each with a 100 dpi page image of every page read from it; `../../registers/source-bundle/SOURCES.json` gives the URL, retrieval date, sha256 and size of every file, and the sha256 values were recomputed with `shasum -a 256` on 2026-11-10.
The Sefer HaChukim files come from the Knesset's file server, and the Kovetz HaTakanot files are copies held by olaw.org.il, an archive that is not the Knesset's; the page footers of every page read carry the issue number and date.
Only the pages read are deposited: for each instrument below the file as downloaded holds more pages than the ones this row reads, so those pages are cut out with qpdf, and the sha256, page count and size of each whole file as downloaded are in `SOURCES.json`.
The printed pages deposited, each with its page image, are: Sefer HaChukim 2450 p. 510; Sefer HaChukim 2635 pp. 920 and 923; Sefer HaChukim 2165 p. 634; Kovetz HaTakanot 7682 pp. 1512 and 1535; Kovetz HaTakanot 6729 p. 194; Kovetz HaTakanot 6922 p. 1556.

| instrument | pages read from the page image | what the page shows |
| --- | --- | --- |
| Sefer HaChukim 2450, 7 Nisan 5774 (7 April 2014), Amendment 101 | p. 510 | section 145ב(ב), paragraph (7) with sub-paragraph (א), and paragraph (9), as published |
| Sefer HaChukim 2635, 29 Nisan 5777 (25 April 2017), Amendment 116 | p. 920 | s 5 replaces section 257; s 6: section 257א is repealed |
| the same | p. 923 | s 16(א): the Amendment commences six months after publication |
| Sefer HaChukim 2165, 7 Tammuz 5768 (10 July 2008) | p. 634 | the end of the section that comes before section 202ד, section 202ד, and the heading and opening words of section 202ה, with its paragraphs |
| Kovetz HaTakanot 7682, 28 Sivan 5776 (4 July 2016) | p. 1512 | the enacting formula of the licensing regulations |
| the same | p. 1535 | regulation 83(א) as published |
| Kovetz HaTakanot 6729, 10 Kislev 5769 (7 December 2008) | p. 194 | the definitions in regulation 1, among them "respondent" and "arbitrator appraiser" |
| Kovetz HaTakanot 6922, 12 Elul 5770 (22 August 2010) | p. 1556 | s 1(2): subsections (ד) and (ה) are added to regulation 2 |

The Hebrew of an official page is typed by me from the page image on a line `-- ext:[SH <issue> p.<page>, read from the page image] | ...` or `-- ext:[KT <issue> p.<page>, read from the page image] | ...` in `plan55-cross-references.l4`.
`tools/pdfcheck.py` checks every Hebrew word of such a line against the text layer of that page (13 lines, 0 problems); it cannot see the order of the words or the digits.
I looked at the digits in the text layers of p. 510, p. 920, p. 1512 of KT 7682, p. 194 and p. 1556 by hand, with a search for the cited numbers, and they match what I typed (145(א2)(4) and 145(א3)(4) and 145(ב3) and 145(ד)(2) and 257א and 202(ה)(2) and 198א and 202ג and the numbers in the enacting formula); that is a spot check made once, not a script.
The page of Kovetz HaTakanot 6729 p. 194 was also rendered at 300 dpi and the lines of the definition of "respondent" cropped (`official/kt6729-5769-p194-definition-300dpi-crop.png`): the letter א follows 198 directly, with no parentheses, while the same definition prints "198(ה)(1)" with them.
`tools/hebcheck-all.sh *.l4 NOTES.md` finds every other run of Hebrew in the `.l4` files and in this file in the four deposited consolidation texts, and exits 0.
The calendar routine reproduced 30 Kislev 5785 = 31 December 2024 before it was used; then 28 Sivan 5776 = 4 July 2016, 10 Kislev 5769 = 7 December 2008, 7 Nisan 5774 = 7 April 2014, 29 Nisan 5777 = 25 April 2017, 12 Elul 5770 = 22 August 2010 and 7 Tammuz 5768 = 10 July 2008, each of which matches the Gregorian date the page prints beside it.
Nothing else of any issue is deposited, and nothing else of it was read for this row.

## 4. Files

| file | what it holds |
| --- | --- |
| `plan55-nouns.l4` | the kinds of provision, the five sources of a reading, the record of a cross-reference; no rule |
| `plan55-cross-references.l4` | the three functions, and one typed value per cross-reference, with the words of the texts quoted beside it |
| `plan55-tests-xrefs.l4` | 65 assertions: the controls, the two second readings, what was read from where, what the descriptions say, and the day each named text stopped being in force |
| `plan55-tests-xrefs-red.l4` | 6 assertions that fail, on purpose (section 8) |
| `check.sh`, `fetch-main-l4.sh` | the check; `check.sh` declares 6 expected failures for the file above |
| `tools/` | `srcquote.py`, `hebcheck.py`, `hebcheck-all.sh`, `pdfcheck.py` |

## 5. Coverage

| provision | status |
| --- | --- |
| section 145ב(ב)(7)(א), the words "145(א2)(4)" | encoded; defect A, first citation; limb (a) the consolidation only, limb (b) from the page image of the words as published |
| section 145ב(ב)(7)(א), the words "145(א3)(4)" | encoded; defect A, second citation; the same |
| section 145ב(ב)(9), the words "152(א2)" | encoded; a sound control chosen by me (fork F7) |
| regulation 83(א) of the licensing regulations, the words "257א" | encoded; defect B; limb (a) from the official pages with the caveat in section 6, limb (b) from the page image of the words as published |
| the enacting formula of the licensing regulations, the words "145א" | encoded; a sound control chosen by me (forks F7 and F9) |
| the definition of "respondent" in the procedure regulations, the words "198א" | encoded; defect C as printed, and the second reading 198(א); limb (a) the consolidation only |
| the definition of "arbitrator appraiser" in the procedure regulations, the words "202ג" | encoded; a sound control chosen by me (fork F7) |
| regulation 2(ד) of the pay regulations, the words "202(ה)(2)" | encoded; defect D as printed, and the second reading 202ה(2) |
| the other citations in the definition of "respondent": "198(ה)(1)" and the Third Schedule item cited there | out-of-scope: the row did not open the targets and says nothing about whether they stand |
| section 119ד(ב), applying sections 198 and 199 | noted from the consolidation, which prints section 199 with the note (בוטל); not encoded, not opened further; CONSOLIDATION-ONLY on both limbs |
| the 1985 regulations on service of orders, which name two sections that Amendment 116 replaced | noted from the consolidation's own editorial note; not encoded; CONSOLIDATION-ONLY |
| the 2008 regulations on procedure in a request under section 207, which name three sections that Amendment 116 replaced | noted from the consolidation's own editorial note; not encoded; CONSOLIDATION-ONLY |
| the fees regulations, Second Schedule item 8.02, which cites section 10א | noted from the consolidation, which prints section 10א with the note (בוטל); not encoded; CONSOLIDATION-ONLY on both limbs |
| the other citations in the licensing, pay and procedure regulations | out-of-scope: the row opened only the citations named above |
| the rest of the Law: what each section requires, allows or forbids, and the procedures it sets | out-of-scope: this row does not encode the Law |
| the Law's other amending instruments | out-of-scope: the row opened only the instruments that the four defects and their controls need |

## 6. The cross-references: answer table

"Stands" means that the target is in the text of its law today as the consolidation prints it, which is an unofficial aid.
Limb (a) asks whether the target is what the citing words say; limb (b) asks whether the citing words still read so in the latest official text of the citing provision.
"Official, with the caveat" means that the repeal and its commencement were read from page images of the official instruments, and that nothing later brought the section back or touched the same words rests on the consolidation, which is CONSOLIDATION-ONLY.

| item | the citing words say it points at | the target is | stands today | limb (a) | limb (b) | pages read |
| --- | --- | --- | --- | --- | --- | --- |
| A1: 145ב(ב)(7)(א) to 145(א2)(4) | a provision of section 145 under which an application becomes absorbed | no such paragraph: (א2) is printed as one sentence | no, on the consolidation | CONSOLIDATION-ONLY | the words as published, from the page image; that later instruments left them alone is CONSOLIDATION-ONLY | SH 2450 p. 510 |
| A2: 145ב(ב)(7)(א) to 145(א3)(4) | the Minister's setting of preconditions for absorbing an application | the treating of an application as absorbed when the engineer gives no notice in the Minister's period | the descriptions differ, on the consolidation | CONSOLIDATION-ONLY | as A1 | SH 2450 p. 510 |
| A control: 145ב(ב)(9) to 152(א2) | the objection a holder of a right in the land may file against a short-route application | the same | yes, by the consolidation | CONSOLIDATION-ONLY | as A1 | SH 2450 p. 510 |
| B: reg 83(א) to 257א | a section under which inspectors are authorised, whose wording was not read | a repealed section | no, from 26 October 2017 on the counting in fork F2 | official, with the caveat: SH 2635 p. 920 s 6 and p. 923 s 16(א) | the words as published, from the page image; that later instruments left them alone is CONSOLIDATION-ONLY | SH 2635 pp. 920, 923; KT 7682 p. 1535 |
| B control: enacting formula to 145א | section 145א, by number and heading | the same | yes, by the consolidation | CONSOLIDATION-ONLY | as A1 | KT 7682 p. 1512 |
| C, reading A: respondent definition to 198א | a definition of the respondent in a section 198א | no such section on the consolidation | no, on the consolidation | CONSOLIDATION-ONLY | the words as published, from the page image and a 300 dpi crop; one later instrument was not read (fork F3) | KT 6729 p. 194 |
| C, reading B: the same words read as 198(א) | the definition of the respondent in subsection (א) of section 198 | the same | yes, by the consolidation | CONSOLIDATION-ONLY | supplied by me; no page prints it | KT 6729 p. 194 |
| C and D control: arbitrator definition to 202ג | the list of arbitrator appraisers | the same | yes, by the consolidation | CONSOLIDATION-ONLY | as A1 | KT 6729 p. 194 |
| D, reading A: reg 2(ד) to 202(ה)(2) | the conditions of qualification, in a paragraph (2) of a subsection (ה) of section 202 | section 202, one paragraph on compensation, no subsections | no, on the consolidation | CONSOLIDATION-ONLY | the words as published, from the page image | KT 6922 p. 1556 |
| D, reading B: the same words read as 202ה(2) | paragraph (2) of section 202ה, a condition of qualification | the same | yes: the page image prints the section as published in 2008; that nothing later touched it is CONSOLIDATION-ONLY | the page image of SH 2165 p. 634, with the caveat | supplied by me; no page prints it | SH 2165 p. 634; KT 6922 p. 1556 |

What limb (a) of defect B rests on, sorted by how strong it is.
Read from the page image: SH 2635 p. 920, s 6, repeals section 257א; p. 923, s 16(א), commences the Amendment six months after publication, with an exception for a sub-chapter of Chapter י as worded in section 4 of the Amendment, and section 6 is not named in it.
CONSOLIDATION-ONLY: that nothing later brought section 257א back, because the consolidation prints it with the note (בוטל) (whole-page line 4451), and its heading carries three amendment tags (whole-page line 4450).
Not read: what section 257א said before the repeal (fork F1), and p. 924, where section 17 of the Amendment continues.
What limb (b) of defect B rests on.
Read from the page image: KT 7682 p. 1535 prints regulation 83(א) with the words "257א".
CONSOLIDATION-ONLY: that the regulation's heading carries no amendment tag (src:lic:718) and that its subsection (א) is printed with the same words (src:lic:719).
What defects A, C and D rest on for limb (a): only the consolidation.
For defect A the lines are whole-page lines 2246 to 2250 of the Law; the heading of section 145 is not deposited and I did not read which instrument last touched (א2) or (א3), nor how Amendment 101 itself words them (fork F6).
For defect C the consolidation's line 3585 is the only line of section 198 the row deposits, and that it is subsection (א) of that section is my reading of the consolidation's structure, since its heading line is not deposited.
For defect D the section 202 lines are whole-page lines 3637 and 3638, and reading B's target is the page image of SH 2165 p. 634 (heading 202ה and its paragraphs), which I read as published in 2008; its paragraph (2) is not quoted in this row.

## 7. Fork register

Each fork gives the reading taken, the reading rejected or held aside, and the Hebrew that licenses each.
The Hebrew of an official page is on the `ext:` lines of `plan55-cross-references.l4`, which this file points at and does not repeat.

- F1, the wording of section 257א and what authorises inspectors now.
  The wording of section 257א before its repeal is in none of the deposited pages, and I did not read it.
  Reading A, taken as the row's statement: regulation 83(א) cites a section that no longer exists, whatever it said and whichever section carries the work now.
  What licenses it: s 6 of Amendment 116 repeals the whole section (SH 2635 p. 920), and the consolidation prints the section with the note (בוטל) (whole-page line 4451).
  Reading B, held aside: another section of the Law now authorises inspectors and the regulation's citation is read as that section.
  What would license it: a successor section that I did not read and a rule that a citation of a replaced provision is read as its replacement, which I did not read for this row; I do not say which section, if any.
  Reading C, held aside: a transitional provision, section 17 of the Amendment, which runs from p. 923 onto p. 924, treats an authorisation given before the start day as given under the new provisions; p. 924 is not deposited as an image and the row does not rely on it.
  The row does not rule between A, B and C.
  It records the citation as a defect because under A the words as they stand cite a repealed section.
- F2, how six months from 25 April 2017 are counted.
  SH 2635 p. 923, s 16(א), commences the Amendment six months after publication, and the issue is dated 29 Nisan 5777 = 25 April 2017.
  Taken: the first day certain on either counting is 26 October 2017, so the value is JUST (Date 26 10 2017), and 25 October 2017 and every earlier day answer NOTHING.
  Rejected: 25 October 2017 as the commencement day, because the rule that counts a period of months was not read, so I do not choose between the same-numbered day and the day after the period ends.
  The two red assertions that mention defect B and the day tests on 27 October 2017 and 10 November 2026 do not depend on the choice.
- F3, whether a later instrument touched the definition of "respondent".
  The consolidation's list of amending instruments for the procedure regulations shows one instrument after Kovetz HaTakanot 6729: an issue of the year 5772, p. 1388.
  I did not read it.
  Taken: the definition reads as the page prints it, because the consolidation prints the same words (src:proc:18); that is the only evidence that the later instrument left it alone, and it is CONSOLIDATION-ONLY.
- F4, the two readings of "198א".
  Reading A, taken as the row's statement: the words print 198א, and the consolidation prints no section with that number, so the citation points at nothing as printed.
  What licenses it: the page prints the letter א directly after 198 with no parentheses (the 300 dpi crop), and the consolidation page has no section 198א.
  Reading B, supplied by me: the parentheses were dropped and the words cite subsection (א) of section 198, whose consolidation text holds the words that define the respondent (whole-page line 3585).
  What licenses it: that subsection holds the definition, and the same definition prints "198(ה)(1)" with parentheses elsewhere in the sentence.
  The text does not say which reading is meant, and the row records both as values and does not rule.
  Held aside: that a later amendment of the Law moved the definition; I did not read one.
- F5, the two readings of "202(ה)(2)".
  Reading A, taken as the row's statement: the number is as printed, and the consolidation prints section 202 as one paragraph with no subsection (ה) and no paragraph (2) (whole-page lines 3637 and 3638).
  Reading B, supplied by me: the number is read as 202ה(2); the page image of SH 2165 p. 634 prints section 202ה under a heading on qualification to serve as an arbitrator appraiser, and the citing words speak of the conditions of qualification.
  The text does not say which reading is meant, and the row records both as values and does not rule.
  The row does not say what paragraph (2) of section 202ה provides beyond that it is a condition of qualification; the page image shows it.
- F6, what the citations of defect A were meant to cite.
  The row says what the citing words describe and what the consolidation prints at each number, and does not say which provisions the words were meant to cite.
  What the consolidation prints: subsection (א2) is one sentence (whole-page line 2246); paragraph (2) of subsection (א3) is the Minister's setting of preconditions (line 2248); paragraph (4) of subsection (א3) is the treating of an application as absorbed when the engineer gives no notice in the Minister's period (line 2250).
  I did not read how Amendment 101 itself words section 145(א2) and (א3), which are on earlier pages of SH 2450, so I do not know whether the numbers were wrong when enacted or became so later.
  No second reading is recorded as a value for defect A.
- F7, the controls.
  The three controls are chosen by me, and are assumed, not ruled; nothing else depends on the choice.
  Control A is paragraph (9) of the same subsection, on the same page, citing 152(א2); control B is the enacting formula of the same regulations, citing 145א, described by the section's number and heading only; control C and D is the next definition in the procedure regulations, citing 202ג.
  What the pages show for each is the citing words; that each target stands today rests on the consolidation.
- F8, the revision ids.
  The revision id 3099048 of the Law comes from a page-history query, as section 3 says; it was not matched to the fetched file.
  The revision ids of the three regulation pages were not recorded.
- F9, an enacting-formula citation.
  This row does not treat an enacting-formula citation as a defect and records none as one.
  Control B is an enacting-formula citation recorded as a control, and the row does not say what section 145א provides.
- F10, the amendment tags.
  The consolidation's own header lists the amending instruments of the Law and their Sefer HaChukim pages; that header is not deposited.
  Taken: the amendment tags on the heading lines the row cites, which are in the excerpt, and a tag of the form `תשע״ד־2` read as the second law of the year 5774.
  The match between a tag and an issue is mine, by the year, and I did not check it against the header's list.
  Consequence: every statement that no later instrument touched the same words is CONSOLIDATION-ONLY, and the row does not call it official.

## 8. Expected red

Six assertions in `plan55-tests-xrefs-red.l4` fail on purpose, and the count (6) is declared in `check.sh` and in `encoding.json`.
Each states what the citing words need.

- Defect A: `the citation points at what it says`, once for each of the two citations (the citing words describe a provision; the target is a missing paragraph in one, and a different rule in the other).
- Defect B: `the citation points at what it says` (the citing words say a section under which inspectors are authorised; the target is a repealed section) and `the named text is in force on` 10 November 2026, expected JUST TRUE (the answer is JUST FALSE, because the repeal has commenced on either counting in fork F2).
- Defect C: `the citation points at what it says` for the words as printed; reading B passes and is in the tests file as a record of that reading.
- Defect D: `the citation points at what it says` for the number as printed; reading B passes and is in the tests file as a record of that reading.

Nothing in either file was edited to make it pass.

## 9. Check numbers

Run as `L4=~/.local/bin/l4 ./check.sh`; main is build 1.6.109 (4c887e0, 2026-11-04), and the installed `l4` reports its version as `dev`.
Both binaries give the same four counts for every file.

| file | errors | satisfied | failed | refused | expected failed | main: errors, satisfied, failed, refused |
| --- | --- | --- | --- | --- | --- | --- |
| `plan55-nouns.l4` | 0 | 0 | 0 | 0 | 0 | 0, 0, 0, 0 (same) |
| `plan55-cross-references.l4` | 0 | 0 | 0 | 0 | 0 | 0, 0, 0, 0 (same) |
| `plan55-tests-xrefs.l4` | 0 | 65 | 0 | 0 | 0 | 0, 65, 0, 0 (same) |
| `plan55-tests-xrefs-red.l4` | 6 | 0 | 6 | 0 | 6 | 6, 0, 6, 0 (same) |
| total | 6 | 65 | 6 | 0 | 6 | 6, 65, 6, 0 |

The six errors are the six expected failures; `l4 run` on the red module reports an `assertion failed` at the six assertions on lines 19, 21, 26, 28, 33 and 38.
Mutation control, on copies of the modules that were deleted afterwards: moving defect B's end day to 26 October 2018 made 2 assertions in the tests file fail; giving control B's target the repealed kind made 2 fail; giving reading B of defect C the kind `the consolidation only` for limb (b) made 1 fail; the unmutated modules make none fail.
So the tests can fail; the check does not see a difference that no assertion exercises.

## 10. Open questions for a domain expert

- What did section 257א say before its repeal, which present section authorises inspectors, and how is regulation 83(א) read (fork F1)?
- How does the Law count "six months from publication" for a commencement (fork F2)?
- Does section 17 of Amendment 116, which runs onto p. 924, postpone or limit the repeal of section 257א for a citation in a regulation (fork F1)?
- Which provisions was section 145ב(ב)(7)(א) meant to cite, and were its numbers wrong when enacted (fork F6)?
- Which instrument last touched section 145(א2) and (א3), and did the three later instruments that touched section 145ב leave paragraph (7)(א) alone (forks F6 and F10)?
- Is "198א" a dropped-parenthesis form of 198(א), and did the later instrument of the year 5772 touch the definition (forks F3 and F4)?
- Is "202(ה)(2)" a misprint for 202ה(2) (fork F5)?
- Does a rule of construction on a citation of an enactment in another save any of these citations, and how does a court read them? I did not read such a rule for this row.

No domain expert has read this against the source.
