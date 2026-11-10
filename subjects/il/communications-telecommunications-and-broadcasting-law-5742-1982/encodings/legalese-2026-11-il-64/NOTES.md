# Row il-64: two references in the Communications (Telecommunications and Broadcasting) Law, 5742-1982, recorded as typed values with their tests

Status: draft, version 0.1.0, 2026-11-10, target compiler main.
How each claim was checked: every quotation of an official instrument was typed from a page image that was looked at, and each Hebrew word of the 34 quotation lines (printed pages 540, 541 and 551 of Sefer HaChukim 1807, printed pages 158 and 159 of Sefer HaChukim 2933, and printed pages 947 and 952 of Sefer HaChukim 2985, which are PDF pages 11, 12 and 22 of file sh5761-p530-amend25.pdf, PDF pages 80 and 81 of file sh5782-p158-econplan2122.pdf and PDF pages 15 and 20 of file sh5782-p934-amend76.pdf) was then searched in the text layer of that page of the whole file by an ad hoc search made on 2026-11-10.
Of the 312 words of the quotation lines, 234 were found as whole words of the page's text layer, 41 were found only inside a longer run of the text layer (a word fused with its punctuation or with a neighbour), and 37 were not found.
Of the 37, 35 are words and numerals of five of the seven footer lines and of three page numbers (the footer lines of the three pages of Sefer HaChukim 1807 are not in the text layer, and the dates of the footer lines of the two pages of Sefer HaChukim 2985 are scrambled in it); they were read from the images only.
The other two are the section number 6יב2 on printed page 541 (the text layer puts its raised numeral after the paragraph number, so the token 6יב2 does not occur) and the new number 21ג on printed page 551 (the text layer misreads it as "2 7ג"); both were read from the images, and every other word of the lines that carry them was found.
On the pages of Sefer HaChukim 2933 and 2985 no word was absent outside the footer lines of printed pages 947 and 952; no line of any page was skipped.
The search is not a tool in `tools/`: no PDF is deposited, so no `pdfcheck.py` is shipped, and the search ran against the whole files, which are not deposited.
Every quotation of the consolidation is expanded by `tools/srcquote.py` from the deposited excerpt, not typed.
A statement that names "the source notes" comes from notes made while this reference was searched for; those notes are not deposited, and each such statement says which instruments the builder of this row read itself.
Quoted lines that rest only on the consolidation are CONSOLIDATION-ONLY unless they are read from an official page, and each says which.
No domain expert has read this against the source.

## Scope

This row is NOT an encoding of the Communications (Telecommunications and Broadcasting) Law, 5742-1982 (Sefer HaChukim 5742 p. 218, as the footnote of the page printed 158 of Sefer HaChukim 2933 gives it).
It records two things, as typed values with tests, and keeps each defect as expected-red tests.
The files label them I1 and I2.
I1 is a reference: s 21ב(ג), in the consolidation, cites s 6ל(א) for the representative of the owners of apartments; the Act in Sefer HaChukim 1807 re-marked s 6ל as s 21ג, and the consolidation prints a note under the old number and the text about the owners' representative in s 21ג(א).
I2 is a reference: s 6ח4(ב) cites s 6יב2(1) for a way of acting that a licensee or its affiliate chose; the Act in Sefer HaChukim 2985 (Amendment 76), s 26, repeals ss 6יב1 to 6יב4, and the sentence has its own period of 8 years from the commencement of Amendment 25.
Each item has a sound control beside it.
The row states what each instrument prints and what the row records; it does not say that the Law or anyone is wrong, and it does not say what a court would do with the words.
The row has no date item, so the Hebrew-calendar routine was not run, and no end day of any period is computed; there is no REFUSE, because the target is main.

## Seat

The seat is the owner of an apartment or the licensee who needs to coordinate entry onto the property, the individual to whom s 21ב(ג) and s 6ח4(ב) are applied.
This row asks no question from the seat, because it records two references, not a rule.

## Coverage

This row does not encode the Law, so almost all of it is out of scope; the table says why for each part.

| Part | Status | Reason |
| --- | --- | --- |
| The words of s 21ב(ג) that cite s 6ל(א), as the consolidation prints them (line 1655), with the heading of s 21ב (line 1624) | encoded | I1, the citing words. CONSOLIDATION-ONLY. |
| The old s 6ל (the note, line 975) and s 21ג(א) (line 1665) in the consolidation; s 43 of the Act in Sefer HaChukim 1807, printed page 551 | encoded | I1, the target. The re-marking is read from the official page; the note and the text of s 21ג(א) are CONSOLIDATION-ONLY. |
| The three subsections that the same sentence of s 21ב(ג) cites after the semicolon, as s 20(1) of the Act in Sefer HaChukim 2933, printed pages 158 and 159, prints them | encoded | Control for I1. |
| Section 54 of the Act in Sefer HaChukim 2985, printed page 952 | recorded as words | Read to see whether it names s 21ב(ג); it names s 21ב(ז)(1). The words are on `ext:` lines and no test compares them. |
| Subsection (ב) of s 6ח4, with the heading and opening words of subsection (א), and the first line of the definition of the term in subsection (ג), as the Act in Sefer HaChukim 1807 prints them (printed pages 540 and 541) | encoded | I2, the citing words, and the control. |
| Section 26 of the Act in Sefer HaChukim 2985, printed page 947, and s 6יב2 as the consolidation prints it (lines 740 and 741) | encoded | I2, the target. The repeal is read from the official page; the note is CONSOLIDATION-ONLY. |
| Every other provision of the Law, and every other instrument | out-of-scope | This row records two references and does not encode the Law. Encoding a provision means encoding what it entitles a person to ask or obliges a licensee to do, which needs its own brief, its own seat questions and its own tests; none of that is attempted here, and nothing is said about whether any other reference in the Law resolves. |

## Fork register

F1 (I1). What the citing words name.
Reading taken: the words "6ל(א)" name section 6ל and, in it, subsection (א), and the sentence says that the representative of the owners of the apartments is as stated there.
The words are the `src:1655` line in `cm64-cross-references.l4`.
Reading rejected: that the number cited is read as the number the section now bears; the row takes the number at its letter and records separately that s 6ל was re-marked 21ג.

F2 (I1). What s 6ל is.
Reading taken: the Act in Sefer HaChukim 1807, s 43, says that s 6ל of the principal law shall be 21ג (the `ext:[SH 1807 p.551 ...]` line that begins with the section number), and the consolidation prints a note under the old number saying so (the `src:975` line, CONSOLIDATION-ONLY).
Reading rejected: that s 6ל still has text of its own; nothing read shows any.

F3 (I1). What s 21ג(א) holds.
Reading taken: the consolidation prints, in s 21ג(א), the sentence that makes the house committee the representative of all the owners of the apartments (the `src:1665` line, CONSOLIDATION-ONLY).
The page printed 551 shows only that item (1) of s 43 replaces words in subsection (א) and item (2) replaces words in subsection (ב); it does not show the text of subsection (א).
Reading rejected: that the page printed 551 shows what s 21ג(א) holds.

F4 (I1). How long the words have stood in s 21ב(ג).
Reading taken: the instrument that first wrote the words "6ל(א)" into s 21ב(ג) was not read, so the row does not say that the citation has been stale since 2001; it says that s 6ל was re-marked in 2001 and that the words stand in subsection (ג) as the consolidation prints them.
Reading rejected: that the citation was written before the re-marking, or after it; nothing read says which.

F5 (I1). The limit of the search for later instruments.
The limit, as the source notes word it: "No later instrument we read amends s 21ב(ג) or the words cited; the instruments read are those listed in the consolidation's header after SH 2933."
What was read: the Act in Sefer HaChukim 2933, s 20(1)(ג) (printed page 159, with the opening lines on printed page 158), read from the page images; its instruction rewrites other words of subsection (ג) and does not mention the words cited.
After it, Amendment 76 (Sefer HaChukim 2985), s 54, printed page 952, read from the page image: it names s 21ב(ז)(1) only.
The source notes add that another instrument listed after it was read from its page images and amends s 21ב(ב1)(1) only, not (ג), and that the rest were searched in their text layers only, with no page image of those read; the search of the text layers is ad hoc and has no positive control.
The builder of this row read the Act in Sefer HaChukim 2933 and s 54 of Amendment 76; the other statements of this paragraph are those of the source notes.

F6 (I1 control). Whether the three subsections that the sentence cites after the semicolon resolve.
Reading taken: the instruction (א) of s 20(1) of the Act in Sefer HaChukim 2933 names subsection (ב1), the instruction (ב) inserts (ב2) after it, and the first line of the inserted (ב3) is printed on page 159; so the three are there as that Act prints them, 3 of 3.
The consolidation's text of those subsections is not in the excerpt, and the row records nothing of it.
Reading rejected: that the three subsections are checked against the consolidation; they are not.

F7 (I2). What the citing words name.
Reading taken: the words "6יב2(1)" name section 6יב2 and, in it, paragraph (1), and the sentence says that the holder or its affiliate chose to act as stated there.
The printed page shows the numeral after 6יב as a small raised numeral, and the row types it as a plain digit, as the consolidation does.
The words are the `ext:[SH 1807 p.541 ...]` line that begins with the label of the subsection, (ב), and the `src:677` line.
Reading rejected: that the words name a section other than 6יב2.

F8 (I2). What the target is.
Reading taken: s 26 of Amendment 76 lists sections 6יב1 to 6יב4 of the principal law as repealed, and 6יב2 lies between the first and the last of them; the consolidation prints s 6יב2 as repealed (the `src:741` line, CONSOLIDATION-ONLY).
The row says that the section was repealed by Amendment 76, section 26, and nothing about when the repeal took effect; it states no date for the repeal.
Reading rejected: that the list excludes its end numbers; the section cited is between them, so the reading of the two ends does not matter.

F9 (I2). The period of the sentence.
Reading taken: the sentence runs for "up to the end of 8 years from the commencement of Amendment 25"; the row records 8 years and the starting point, and that the commencement day of Amendment 25 was not read.
This row computes no end day.
Reading rejected: that the period began on the date printed on the masthead of the Act; the commencement day was not read.

F10 (I2). The limit of the search for later instruments.
The limit, as the source notes word it: "No later instrument we read amends s 6ח4(ב) or the words cited; the instruments read are the three that the consolidation tags on the heading of s 6ח4 after SH 1807, and one later instrument from the consolidation's header, read from its page images, which amends s 6ח4(א)(1) only."
The first instrument tagged on the heading line of s 6ח4 (the `src:669` line) is the Act in Sefer HaChukim 1807 (Amendment 25): read from its page images, printed pages 540 and 541.
The three later instruments tagged on that line are recorded in the source notes as: Amendment 37 (Sefer HaChukim 5767, page 457), a search of its text layer only, its s 5 addresses subsection (א); an instrument in Sefer HaChukim 2505, page 7, a search of its text layer only, addressing (א)(1); and an instrument in Sefer HaChukim 5777, page 125, a search of its text layer only, addressing (א)(1).
The builder of this row read none of those three; the statements are those of the source notes.
The consolidation's tags are not claimed to be complete.
The source notes also record that Amendment 76 has one instruction on s 6ח, on subsection (ז) of that section, and none on s 6ח4.

F11 (I2 control). Whether the control is a citation.
Reading taken: the term "בעל זיכיון" used in subsection (ב) is defined in subsection (ג) of the same section, on the same page; this is a defined term and not a numbered citation, and the row says so; it is the one reference of subsection (ב) that the pages read let the row check.
Reading rejected: that there is a numbered citation in subsection (ב) other than the one of I2.

F12. The page of Sefer HaChukim 2933.
The source notes name PDF page 2 of the whole file for printed page 159; PDF page 2 of that file is the page printed 80, and the page printed 159 is PDF page 81 (and printed page 158 is PDF page 80), found by rendering the file and looking at the pages before cropping.
The other page mappings were checked by rendering and agree with the source notes.

F13. The kinds in `cm64-nouns.l4`.
Reading taken: `What a reference points at` has six values, each a short plain description I wrote from the words quoted; two descriptions of one thing are one value.
Reading rejected: using the Law's own words as the values, because the Law does not describe its provisions by kind.

## Answer table

| | I1: s 21ב(ג) cites s 6ל(א) | I2: s 6ח4(ב) cites s 6יב2(1) |
| --- | --- | --- |
| What the citing words say | The representative of the owners of the apartments is as stated in s 6ל(א): the words point at the text of a section about the representative. | The holder or its affiliate chose to act as stated in s 6יב2(1): the words point at the text of a paragraph that states a way of acting. |
| What the target says | The number 6ל was re-marked 21ג by the Act in Sefer HaChukim 1807, s 43; the consolidation prints a note under the old number, and the text about the owners' representative is in s 21ג(א). | Section 26 of Amendment 76 lists ss 6יב1 to 6יב4 as repealed, and s 6יב2 is among them; the consolidation prints s 6יב2 as repealed. |
| Exists | The target named, s 6ל(א), has 0 of the 1 sections the words name; the number now bears the text in s 21ג. | The target named, s 6יב2(1), has 0 of the 1 paragraphs the words name. |
| Limb (a) | The official page for the re-marking, the crop deposited; the note and the text of s 21ג(א) are CONSOLIDATION-ONLY. | The official page (Sefer HaChukim 2985, printed page 947), read from its image, the crop deposited; the note is CONSOLIDATION-ONLY. |
| Limb (b) | The words as the consolidation prints them, CONSOLIDATION-ONLY; the later instrument read (Sefer HaChukim 2933, s 20(1)(ג)) rewrites other words of subsection (ג) and does not mention them. | The official page (Sefer HaChukim 1807, printed pages 540 and 541), read from its image, the crops deposited. |
| Limit | F5. | F10. |
| Page read | Sefer HaChukim 1807 (9 August 2001), printed page 551; Sefer HaChukim 2933 (18 November 2021), printed pages 158 and 159; Sefer HaChukim 2985 (4 July 2022), printed page 952. | Sefer HaChukim 1807, printed pages 540 and 541; Sefer HaChukim 2985, printed page 947. |
| Control | The three subsections cited after the semicolon of the same sentence: all three are there (3 of 3). | The term defined in s 6ח4(ג) and used in s 6ח4(ב): defined there (1 of 1). |

## The six expected-red assertions, one by one

`cm64-tests-xrefs-red.l4` holds six assertions, all failing, and `check.sh` and `encoding.json` declare that count (6).
1. `the citation points at what it says` for I1 is FALSE: the words say the text of a section about the owners' representative, and the target is a note that the section was re-marked.
2. `the target has everything the citing words name` for I1 is FALSE: the target has 0 of the 1 sections named.
3. `the number the words cite is the number the section now bears` is FALSE: the number cited is 6ל and the instrument gave the section the number 21ג.
4. `the citation points at what it says` for I2 is FALSE: the words say the text of a paragraph, and the target is a section repealed by another instrument.
5. `the target has everything the citing words name` for I2 is FALSE: the target has 0 of the 1 paragraphs named.
6. `the section cited stands outside the repealed numbers` is FALSE: 6יב2 lies inside 6יב1 to 6יב4.

## The check

Run from this folder with `L4=$HOME/.cache/l4-main/98/l4 ./check.sh`; the `l4` that wrote the row was 1.6.98 (main, 7689b0d, 2026-10-19) and the main build it was compared with was 1.6.109 (main, 4c887e0, 2026-11-04).

| module | errors | satisfied | failed | refused | expected failed | main: errors | satisfied | failed | refused | main verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cm64-cross-references.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| cm64-nouns.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| cm64-tests-xrefs-red.l4 | 6 | 0 | 6 | 0 | 6 | 6 | 0 | 6 | 0 | same |
| cm64-tests-xrefs.l4 | 0 | 36 | 0 | 0 | 0 | 0 | 36 | 0 | 0 | same |

The six errors are the six failed assertions, each reading "assertion failed", on lines 11, 13, 15, 20, 22 and 24 of the red module; no other error, and no refusal.
Positive control: in a scratch copy, the repeal record's first number was changed from 1 to 3 and the control reference's target was changed to what its words say; two of the six red assertions then passed (4 of 6 failed) and five sound assertions turned red; the copy was deleted.
`python3 -I tools/hebcheck.py ../../registers/source-bundle/communications-telecommunications-and-broadcasting-law-5742-1982.he.wiki.excerpt.txt *.l4 NOTES.md` exits 0: every run of Hebrew outside a quotation line occurs in the deposited excerpt.

## The deposits

UNOFFICIAL aid: the Hebrew Wikisource consolidation of the Law, revision 3099061 (last edited 2026-10-29T14:02:24Z).
The whole page content has sha256 48fe94f6db7cd53b0810737aa120fb81c11a6909ef023dfa16f79118c7f48f47 and 582370 bytes as retrieved on 2026-11-10 (2734 newline-terminated lines); the excerpt deposited has sha256 38145ef396c36551f7172570faa1a31b5d01f12e38648e0f799d18da901c7d7a and 3250 bytes.
The excerpt holds nine lines of the page, whole: the title line (line 2), the heading of s 6ח4 (line 669), s 6ח4(ב) (line 677), s 6יב2 and its note (lines 740 and 741), the note under the old s 6ל (line 975), the heading of s 21ב (line 1624), s 21ב(ג) (line 1655) and s 21ג(א) (line 1665); each carries its number in the whole page, so that `src:N` means the line N of the page.
Official pages, in `registers/source-bundle/official/`, each a crop composed of bands separated by grey bars, each viewed before it was deposited:
- `sh1807-5761-p540-bands.png`, Sefer HaChukim 1807, printed page 540 (PDF page 11): the heading line of s 6ח4 with its margin note and the opening words of (א), and the footer line.
- `sh1807-5761-p541-bands.png`, Sefer HaChukim 1807, printed page 541 (PDF page 12): subsection (ב) of s 6ח4 with the line that opens (ג), the first line of the definition of the term in (ג), and the footer line.
- `sh1807-5761-p551-bands.png`, Sefer HaChukim 1807, printed page 551 (PDF page 22): s 43 with its margin note and its two items, and the footer line.
- `sh2933-5782-p158-bands.png`, Sefer HaChukim 2933, printed page 158 (PDF page 80): the opening lines of s 20 with the instructions (א) and (ב) of paragraph (1) and the first line of the inserted (ב2), and the footer line.
- `sh2933-5782-p159-bands.png`, Sefer HaChukim 2933, printed page 159 (PDF page 81): the first line of the inserted (ב3), the instruction (ג), and the footer line.
- `sh2985-5782-p947-bands.png`, Sefer HaChukim 2985, printed page 947 (PDF page 15): s 26 with its margin note, and the footer line.
- `sh2985-5782-p952-bands.png`, Sefer HaChukim 2985, printed page 952 (PDF page 20): s 54 with its margin note, and the footer line.
Only the pages read are deposited, as crops, and no PDF and no full-page image of any page is deposited.
`registers/source-bundle/SOURCES.json` gives the whole file's sha256 and size for each instrument and each crop's own sha256 and size; the Knesset addresses are the ones the source notes give, and were not re-fetched.

## What was not done

The instrument that first wrote the words "6ל(א)" into s 21ב(ג) was not read, and no end day was computed for the period of s 6ח4(ב), whose commencement day was not read.
No instrument other than those named in F5 and F10 was read by the builder of this row, and the statements about the other instruments are those of the source notes.
The consolidation's text of subsections (ב1), (ב2) and (ב3) of s 21ב is not in the excerpt and was not compared with the Act in Sefer HaChukim 2933.
The other items of the Acts in Sefer HaChukim 2933 and 2985 and of Amendment 25 were seen on the page images where they share a page with the lines read and are not deposited; nothing of them is recorded.
The footnote that gives the Law's original publication (Sefer HaChukim 5742, p. 218) was read from the page image of printed page 158 and is in no deposit.
The Knesset addresses of the three whole files were not re-fetched.
