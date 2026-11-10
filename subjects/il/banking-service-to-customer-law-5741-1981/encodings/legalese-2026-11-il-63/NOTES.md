# Row il-63: one reference in the Banking (Service to Customer) Law, 5741-1981, recorded as typed values with its tests

Status: draft, version 0.1.0, 2026-11-10, target compiler main.
How each claim was checked: every quotation of an official instrument was typed from a page image that was looked at, and each Hebrew word of the 17 quotation lines (printed pages 454 and 455 of Sefer HaChukim 2712, printed page 223 of Sefer HaChukim 2778 and printed page 397 of Sefer HaChukim 3510, which are PDF pages 4 and 5 of file 20_lsr_491979.pdf, PDF page 27 of file 20_lsr_528386.pdf and PDF page 49 of file 25_lsr_12224370.pdf) was then searched in the text layer of that page of the whole file by an ad hoc search made on 2026-11-10.
Of the 179 words of the quotation lines, 154 were found as whole words of the page's text layer, 8 were found only inside a longer run of the text layer (a word fused with its punctuation or with a neighbour), and 17 were not found; all 17 are words of the three footer lines (the issue's name, its month and its date), whose text layer is scrambled, and those lines were read from the images only.
The search is not a tool in `tools/`: no PDF is deposited, so no `pdfcheck.py` is shipped, and the search ran against the whole files, which are not deposited.
Every quotation of the consolidation is expanded by `tools/srcquote.py` from the deposited excerpt, not typed.
Quoted lines that rest only on the consolidation are CONSOLIDATION-ONLY unless they are read from an official page, and each says which.
No domain expert has read this against the source.

## Scope

This row is NOT an encoding of the Banking (Service to Customer) Law, 5741-1981 (Sefer HaChukim 5741 p. 258, as the footnotes of the pages read give it).
It records one thing, as typed values with tests, and keeps it as an expected-red test.
The files label it I1.
I1 is a reference: s 5ב(א) says that the term financial activity is as defined in subsection (ה) of s 5ב1.
In the Act that inserted those words (Sefer HaChukim 2712), the definition of the term is the last definition of subsection (א) of s 5ב1, and subsection (ה) holds a power of the Governor of the Bank of Israel, with the Minister of Finance's consent, to determine that the section does not apply to a bank, applies to it later, or applies to it only in part.
The row states what each instrument prints and what the row records; it does not say that the Law or anyone is wrong, and it does not say what a court would do with the words.
Two controls stand beside I1.
The first is a second reference to the same subsection (ה), in s 3 of the Act in Sefer HaChukim 3510, whose target holds what its words say.
The second is the words that the Act in Sefer HaChukim 2712 inserted into s 5ב(א) beside the words the consolidation prints at that place, which are the same words.
The row has no date item, so the Hebrew-calendar routine was not run and nothing in it returns NOTHING; there is no REFUSE, because the target is main.

## Seat

The seat is the customer of a banking corporation who asks to move accounts, the individual to whom s 5ב(א) is applied.
This row asks no question from the seat, because it records one reference, not a rule.

## Coverage

This row does not encode the Law, so almost all of it is out of scope; the table says why for each part.

| Part | Status | Reason |
| --- | --- | --- |
| The words of s 5ב(א) that name the definition of financial activity, as the instruction of s 2(1)(א) of the Act in Sefer HaChukim 2712, printed page 454, inserted them | encoded | I1, the citing words. |
| Subsection (ה) and the last definition of subsection (א) of s 5ב1, as printed on the page of that Act numbered 455 | encoded | I1, the target. |
| Section 3 of the Act in Sefer HaChukim 3510, printed page 397: its heading and its first line | encoded | Control: a second reference to subsection (ה) whose target holds what the words say. |
| The same words in the opening of s 5ב(א) of the consolidation (line 210 of revision 3079893) | encoded | Control: the words the instrument inserted and the words the consolidation prints are the same. CONSOLIDATION-ONLY. |
| Section 61(3) of the Act in Sefer HaChukim 2778, printed page 223 | recorded as words | Read to see whether it touched the opening words of s 5ב(א); it names paragraph (2) only. The words are on `ext:` lines and no test compares them. |
| Every other provision of the Law | out-of-scope | This row records one reference and does not encode the Law. Encoding a provision means encoding what it entitles a customer to ask or obliges a banking corporation to do, which needs its own brief, its own seat questions and its own tests; none of that is attempted here, and nothing is said about whether any other reference in the Law resolves. |
| The instruments that amended s 5ב or s 5ב1 after the Act in Sefer HaChukim 2778, and the other items of that Act | out-of-scope | They were not read as text; F4 says what the consolidation's amendment tags show and what the row does not say. |

## Fork register

F1 (I1). What the citing words name.
Reading taken: the words "פעילות פיננסית כהגדרתה בסעיף 5ב1(ה)" name section 5ב1 and, in it, subsection (ה), and say that the term is defined there.
The words are the third `ext:[SH 2712 p.454 ...]` line of the defect in `bk63-cross-references.l4` (the one that begins with the letter of the instruction, (א)), and the `src:210` line.
Reading rejected: that the words name the section as a whole and the letter (ה) is surplus, so that a definition anywhere in the section would satisfy them; the printed words name a subsection, and the row takes them at their letter.

F2 (I1). What subsection (ה) holds.
Reading taken: a power of the Governor, with the consent of the Minister of Finance, on the request of a bank of one of the kinds the sentence lists, to determine that the section's provisions do not apply to it, apply to it at the end of a period the Governor sets, or apply to it only as a receiving or an original bank.
The words are the `ext:[SH 2712 p.455 ...]` line that starts "(ה) הנגיד" and the `src:228` line.
The sentence does not contain the term "פעילות פיננסית" (checked on the 2018 quotation line and on the `src:228` line).
The typed kind is mine, a short description of that sentence.
Reading rejected: that the sentence also defines the term; the definition is the sentence quoted on the `ext:[SH 2712 p.455 ...]` line that starts with the term in quotation marks.

F3 (I1). Where the definition stands.
Reading taken: in subsection (א) of s 5ב1, as its last definition.
The page numbered 454 prints the line that opens s 5ב1 and its subsection (א) ("5ב1. (א) בסעיף זה –", in the deposited crop), and the definitions run on to the top of the page numbered 455, where the definition of the term is the first thing printed (in the deposited crop).
That a new subsection, (ב), begins directly under the definition on the page numbered 455, and that the definitions of other terms stand between the two crops, was seen on the page images and is in no deposit.
In the consolidation the definition is on the `src:223` line (CONSOLIDATION-ONLY); the line that opens subsection (א) (line 216 of the page) and the line that opens subsection (ב) (line 224) bound it there and are not in the excerpt.
Reading rejected: that the definition belongs to another subsection; nothing read puts it anywhere else.

F4 (I1). Whether a later instrument touched the words.
Reading taken: the row records what it read.
Item (3) of s 61 of the Act in Sefer HaChukim 2778 (printed page 223) names paragraph (2) of s 5ב(א) and no other part of it, and names no part of s 5ב1; the other four items of s 61 name other sections, none of them s 5ב1 (read from the page image on 2026-11-10; those four items are in no deposit, and a search of the page's text layer found no mention of s 5ב1 on it).
The consolidation of 2026-09-01 prints the same opening words of s 5ב(א) (line 210) and the same definition (line 223) (CONSOLIDATION-ONLY).
What the consolidation's amendment tags show, read on the whole page of revision 3079893 on 2026-11-10 and not deposited (the heading lines of s 5ב and s 5ב1 are lines 209 and 215 of the page, and they are not in the excerpt): the tag of s 5ב lists two entries after the one of the year 5779, and the tag of s 5ב1 lists three entries after the one of the year 5778; the 5779 entry is taken to be the Act in Sefer HaChukim 2778 and the 5778 entry the Act in Sefer HaChukim 2712, and neither correspondence was checked; in each tag one of the later entries is marked as a notice in Kovetz HaTakanot, and whether any later entry is the Act in Sefer HaChukim 3510 was not checked.
This reading of the tags is mine: an entry marked as a notice in Kovetz HaTakanot names a notice and any other entry names an Act; the convention was not checked.
None of those later entries was read, and a tag does not say which words an instrument touched.
So the row does not say that no later instrument touched the opening words of s 5ב(א) or s 5ב1; it says that item (3) of s 61 did not touch them and that the consolidation of 2026-09-01 still prints them.
Reading rejected: that the tags show that later instruments touched paragraph (2) only; they show that later instruments exist, not where they touched.

F5 (I1). Whether s 3 of the Act in Sefer HaChukim 3510 is a reference to subsection (ה) that resolves.
Reading taken: the first line says (in the Hebrew word that begins it, which is printed on the `ext:[SH 3510 p.397 ...]` lines) that a determination under s 5ב1(ה) of the Banking (Service to Customer) Law stands, and subsection (ה) is the provision in which the Governor determines; so the words and the target agree, and it is the control.
The rest of the sentence of s 3 is not deposited and the row does not record it.
Reading rejected: that the word names a determination made elsewhere in s 5ב1; the row read no other subsection of s 5ב1 for what it says about determinations.

F6 (I1). The bank kinds in subsection (ה).
Reading taken: the 2018 page lists two kinds of bank in the sentence of subsection (ה) and the consolidation of 2026-09-01 lists three (the consolidation's line 228 has one more kind in the list).
The row relies on neither list, and the typed kind of subsection (ה) does not name the kinds.
Reading rejected: that the difference matters to I1; it is recorded because it shows that subsection (ה) was changed after 2018, which F4 already says the tags suggest.

F7 (I1). The kinds in `bk63-nouns.l4`.
Reading taken: `What a reference points at` has three values, each a short plain description I wrote from the words quoted; two descriptions of one thing are one value.
Reading rejected: using the Law's own words as the values, because the Law does not describe its provisions by kind.

## Answer table

| | I1: the reference |
| --- | --- |
| What the citing words say | Financial activity is as defined in subsection (ה) of s 5ב1: the words point at a definition of the term. |
| What the target says | Subsection (ה) of s 5ב1 holds a power of the Governor, with the Minister's consent, to determine that the section does not apply to a bank, applies to it later, or applies to it only in part. The definition of the term is the last definition of subsection (א). |
| Exists | The target named, subsection (ה), has 0 of the 1 definitions the words name; the definition is in subsection (א). |
| Limb (a) | The official page of the instrument that wrote the structure of s 5ב1 (Sefer HaChukim 2712, printed pages 454 and 455), read from its image, the crops deposited; the consolidation prints the same structure (CONSOLIDATION-ONLY). |
| Limb (b) | The official page of the instrument that wrote the words (Sefer HaChukim 2712, printed page 454, the instruction of s 2(1)(א)), read from its image, the crop deposited; that the words are still in the Law rests on the consolidation (line 210), CONSOLIDATION-ONLY. |
| Page read | Sefer HaChukim 2712 (22 March 2018), printed pages 454 and 455; Sefer HaChukim 3510 (31 March 2026), printed page 397; Sefer HaChukim 2778 (9 January 2019), printed page 223. |
| Control | A second reference to subsection (ה), in s 3 of the Act in Sefer HaChukim 3510, whose target holds what its words say; and the words as inserted against the words as the consolidation prints them. |

## The three expected-red assertions, one by one

`bk63-tests-xrefs-red.l4` holds three assertions, all failing, and `check.sh` and `encoding.json` declare that count (3).
1. `the citation points at what it says` for the reference is FALSE: the words say a definition, the target is a power of the Governor.
2. `the target has everything the citing words name` for the reference is FALSE: the target has 0 of the 1 definitions named.
3. `the citing words name the subsection that holds what they say` for the reference is FALSE: the words name (ה), and the definition is in (א).

## The check

Run from this folder with `L4=$HOME/.cache/l4-main/98/l4 ./check.sh`; the `l4` that wrote the row was 1.6.98 (main, 7689b0d, 2026-10-19) and the main build it was compared with was 1.6.109 (main, 4c887e0, 2026-11-04).

| module | errors | satisfied | failed | refused | expected failed | main: errors | satisfied | failed | refused | main verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bk63-cross-references.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| bk63-nouns.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| bk63-tests-xrefs-red.l4 | 3 | 0 | 3 | 0 | 3 | 3 | 0 | 3 | 0 | same |
| bk63-tests-xrefs.l4 | 0 | 27 | 0 | 0 | 0 | 0 | 27 | 0 | 0 | same |

The three errors are the three failed assertions, each reading "assertion failed", on lines 11, 13 and 15 of the red module; no other error, and no refusal.
Positive control: in a scratch copy, the control reference's "says it points at" value was changed to the definition, and exactly one sound assertion (`the citation points at what it says` for the control) turned red; the copy was deleted.
`python3 -I tools/hebcheck.py ../../registers/source-bundle/banking-service-to-customer-law-5741-1981.he.wiki.excerpt.txt *.l4 NOTES.md` exits 0: every run of Hebrew outside a quotation line occurs in the deposited excerpt.

## The deposits

UNOFFICIAL aid: the Hebrew Wikisource consolidation of the Law, revision 3079893 (last edited 2026-09-01T07:01:43Z).
The whole page content has sha256 51a1bffff8cf24e878991ba9c0d64eb330df46305c0b08b048a86d56cbf5e005 and 144728 bytes as retrieved on 2026-11-10 (663 newline-terminated lines); the excerpt deposited has sha256 d06f63291889fb605562cbb761910ac77ba8fc8b33f6a51a4608f440d47b7bf3 and 2312 bytes.
The excerpt holds four lines of the page, whole: the title line (line 2), the opening of s 5ב(א) (line 210), the definition of the term (line 223) and subsection (ה) of s 5ב1 (line 228); each carries its number in the whole page, so that `src:N` means the line N of the page.
Official pages, in `registers/source-bundle/official/`, each a crop composed of bands separated by grey bars, each viewed before it was deposited:
- `sh2712-5778-p454-bands.png`, Sefer HaChukim 2712, printed page 454 (PDF page 4): the opening lines of s 2, the line "(1) בסעיף 5ב(א) –", the instruction (א) that inserts the words, the line that opens s 5ב1 and its subsection (א), and the footer line.
- `sh2712-5778-p455-bands.png`, Sefer HaChukim 2712, printed page 455 (PDF page 5): the definition of the term, subsection (ה) of s 5ב1, and the footer line.
- `sh3510-5786-p397-bands.png`, Sefer HaChukim 3510, printed page 397 (PDF page 49): the heading of s 3 with its section number, the first line of s 3, and the footer line.
- `sh2778-5779-p223-bands.png`, Sefer HaChukim 2778, printed page 223 (PDF page 27): the opening line of s 61, item (3), and the footer line (which prints the page number only).
The page numbered 223 prints no issue number; the issue number 2778 and the date 9 January 2019 are on the cover of the whole file (PDF page 1), read from its text layer and not deposited.
Only the pages read are deposited, as crops, and no PDF and no full-page image of any page is deposited.
`registers/source-bundle/SOURCES.json` gives the whole file's sha256 and size for each instrument and each crop's own sha256 and size; the Knesset addresses are the ones the file names map to, and were not re-fetched.

## What was not done

No instrument after the Act in Sefer HaChukim 2778 that touched s 5ב(א) or s 5ב1 was read; F4 says what the consolidation's tags show and what the row does not say.
The other items of s 61 of the Act in Sefer HaChukim 2778 were seen on the page image and are not deposited, and nothing of them is recorded beyond F4.
The title of the Act in Sefer HaChukim 3510 was not established by this row, because the page read does not carry it; the title of the Act in Sefer HaChukim 2712 stands at the head of the page numbered 454 (the Economic Plan Law for 2019, an unofficial rendering) and is not in the deposited crop.
The rest of the sentence of s 3 of the Act in Sefer HaChukim 3510, and the other subsections of s 5ב1, were not recorded.
The footnotes that give the Law's original publication (Sefer HaChukim 5741, p. 258) were read from the page images of printed pages 223 and 454 and are in no deposit.
The Knesset addresses of the three whole files were not re-fetched.
Only one comparison of the two printings of the inserted words was made, and it compares two transcriptions typed by this row's builder, one from the crop and one from the consolidation's line.
