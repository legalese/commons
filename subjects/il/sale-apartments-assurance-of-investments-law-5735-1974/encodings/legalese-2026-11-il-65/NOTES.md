# Row il-65: two references in the Sale (Apartments) (Assurance of Investments of Persons Acquiring Apartments) Law, 5735-1974, recorded as typed values with their tests

Status: draft, version 0.1.0, 2026-11-10, target compiler main.
How each claim was checked: every quotation of an official instrument was typed from a page image that was looked at, and each Hebrew word of the 14 quotation lines (printed pages 365, 366 and 367 of Sefer HaChukim 3510, which are PDF pages 17, 18 and 19 of the whole file) was then searched in the text layer of that page of the whole file by an ad hoc search made on 2026-11-10.
Of the 103 words of the quotation lines, 80 were found as whole words of the page's text layer, 5 were found only inside a longer run of the text layer (a word fused with its punctuation or with a neighbour), and 18 were not found.
All 18 are tokens of the three footer lines: the text layer carries the footer line of each page in a garbled form (the name of the issue runs together with a repeated piece, and the date is broken up), so those words were read from the images only.
No word was absent outside the footer lines, and no line of any page was skipped.
The search is not a tool in `tools/`: no PDF is deposited, so no `pdfcheck.py` is shipped, and the search ran against the whole file, which is not deposited.
Every quotation of a consolidation is expanded by `tools/srcquote.py` from the deposited excerpts, not typed.
A marker carries the revision id, `--@SRC 3085793:107`, because the two revisions of one page number their lines differently; `tools/srcquote.py` and `tools/hebcheck.py` were changed for that (see "The check").
A statement that names "the source notes" comes from notes made while this reference was searched for; those notes are not deposited, and each such statement says which instruments the builder of this row read itself.
Quoted lines that rest only on a consolidation are CONSOLIDATION-ONLY unless they are read from an official page, and each says which.
No domain expert has read this against the source.

## Scope

This row is NOT an encoding of the Sale (Apartments) (Assurance of Investments of Persons Acquiring Apartments) Law, 5735-1974, called "the Assurance Law" here (its original publication is Sefer HaChukim, Hebrew year 5735, p. 14, as footnote 33 on the page printed 365 of Sefer HaChukim 3510 gives it; 5735 is the year in the Law's own title, not an issue number).
It records two things, as typed values with tests, and keeps each defect as expected-red tests.
The files label them I1 and I2.
"The Act" is the Act in Sefer HaChukim 3510 (13 Nisan 5786, 31 March 2026); its s 31 amends the Assurance Law.
I1 is a citation: a definition that item (1) of s 31 inserts into s 1 of the Assurance Law defines the term "בעל רישיון נותן שירותי תשלום יציבותי" as whoever holds a licence under the name "רישיון נותן תשלום יציבותי", as defined in s 36ט of the Banking (Licensing) Law, 5741-1981.
The consolidation of the Banking (Licensing) Law prints in s 36ט a definition for "רישיון נותן שירותי תשלום יציבותי", whose name holds the word "שירותי" that the name in the citing words lacks.
I2 is an instruction: item (6), paragraph (ב), of s 31 says that in subsection (ב) of s 3ג2 (the section that item (6) opens with), in every place, the words "התאגיד הבנקאי או המבטח" are replaced by "התאגיד הבנקאי, נותן הערבות האחר או המבטח".
In paragraph (2) of that subsection the earlier revision of the consolidation prints those words at one place and a spelling of them with a one-letter prefix at another place.
The current revision prints the replacing words at the first place, and prints the second place as in the earlier revision, followed by an editorial note.
Each item has a sound control beside it.
The row states what each instrument prints and what the row records; it does not say that the Law or anyone is wrong, and it does not say what a court would do with the words.
The row states no commencement day and says nothing about whether any provision of the Act is in force.
The row has no date item, so the Hebrew-calendar routine was not run, and there is no REFUSE, because the target is main.

## Seat

The seat is the buyer of an apartment (the "קונה" of s 3ג2(ב)), the individual to whom subsection (ב) says the fund pays back an amount.
This row asks no question from the seat, because it records two references, not a rule.

## Coverage

This row does not encode the Assurance Law, so almost all of it is out of scope; the table says why for each part.

| Part | Status | Reason |
| --- | --- | --- |
| The heading of s 31 of the Act, with its margin note, and the opening words of its item (1), printed page 365 | encoded | I1, the place the definition is inserted. Read from the official page. |
| The definition of "בעל רישיון נותן שירותי תשלום יציבותי" in item (1) of s 31, printed page 366, and the same definition in the current revision of the consolidation (line 26) | encoded | I1, the citing words. The page is read from its image; the consolidation's line is CONSOLIDATION-ONLY. |
| The heading of s 36ט of the Banking (Licensing) Law and its definition of the licence, as the current revision of that consolidation prints them (lines 631 and 644) | encoded | I1, the target. CONSOLIDATION-ONLY. |
| The opening words of item (6) of s 31 of the Act (printed page 366) and the heading of s 3ג2 in both revisions of the consolidation (lines 100 and 93) | encoded | Control for I1, and the place that tells which section I2 amends. |
| Paragraph (ב) of item (6) of s 31, printed page 367 | encoded | I2, the instruction. Read from the official page. |
| Subsection (ב) of s 3ג2, its opening words and paragraphs (1), (2) and (3), in the earlier and the current revision of the consolidation (lines 98 to 101 and 105 to 108) | encoded | I2, the places, and the control for I2. CONSOLIDATION-ONLY. The opening lines of subsection (ג) (lines 102 and 109) are copied into the excerpts and no test reads them. |
| Every other provision of the Assurance Law and of the Act | out-of-scope | This row records two references and does not encode the Assurance Law. Encoding a provision means encoding what it entitles a person to ask or obliges a person to do, which needs its own scope, its own seat questions and its own tests; none of that is attempted here, and nothing is said about any other provision. |

## Fork register

F1 (I1). What the citing words name.
Reading taken: the words after "מי שבידו" name a licence under the name "רישיון נותן תשלום יציבותי" and cite s 36ט of the Banking (Licensing) Law, 5741-1981 for its definition.
The words are the `ext:[SH 3510 p.366 ...]` lines at the head of that page's quotation and the `src:3085793:26` line.
Reading rejected: that the citing words name the licence under the longer name; the page prints the shorter one, and the row records the two strings as printed.

F2 (I1). What the target prints.
Reading taken: the current revision of the consolidation of the Banking (Licensing) Law (revision 3078251, last edited 2026-08-21T05:00:09Z) prints a heading for s 36ט (line 631) and, as line 644, a definition for "רישיון נותן שירותי תשלום יציבותי".
The two deposited lines print the longer name and do not print the shorter one.
The builder also searched the whole content of that revision for the shorter name and found it on no line; the whole page is not deposited, so a reader cannot repeat that search from the deposit.
The row records 1 thing named and 0 of it present under that name.
Reading rejected: that the target is anywhere else in the Banking (Licensing) Law; only lines 631 and 644 were read, and the lines between them are not deposited.
The instrument that the heading's tag names was not read, and the row says nothing about the scope in which s 36ט's definitions apply.

F3 (I1). Whether the page and the consolidation print the same words.
Reading taken: the definition on the page printed 366 and line 26 of the current revision of the Assurance Law's consolidation read the same, word for word; the quotation marks differ in form, and the consolidation's link markup is reduced to its visible text by `tools/srcquote.py`.
The page is limb (b); the consolidation's line is a second print of the same words and is CONSOLIDATION-ONLY.
Reading rejected: that the consolidation shows the Act's words by itself; only the page does.

F4 (I1). Where the definition sits.
Reading taken: the definition stands between the opening words of item (1) of s 31, at the foot of the page printed 365, and item (2), on the page printed 366; that it belongs to item (1), and so is inserted into s 1 of the Assurance Law, rests on that order.
The lines of both pages between the words deposited are not deposited and were not read for this row.
Reading rejected: that the crops show a continuous text.

F5 (I1 control). Whether a second citation of the same section resolves.
Reading taken: item (6) of s 31 opens, at the foot of the page printed 366, with the words that cite s 3ג2 of the Assurance Law by number; the consolidation prints a heading with the number 3ג2 in the current revision (line 100) and in the earlier one (line 93); so the control resolves, 1 of 1.
The control checks that a section with that number is printed in the consolidation; it does not check the text of the target.
Reading rejected: that the control is a citation inside item (1) of s 31; the lines of item (1) other than the definition were not read for this row, so no citation in them was tried, and the control is taken from item (6) of the same section, as printed on the same page as the definition.

F6 (I2). What the instruction names and how it applies.
Reading taken: the instruction names one string, "התאגיד הבנקאי או המבטח", says it applies in every place of subsection (ב), and gives one replacement, "התאגיד הבנקאי, נותן הערבות האחר או המבטח"; the printed words are the `ext:[SH 3510 p.367 ...]` lines.
That subsection (ב) is subsection (ב) of s 3ג2 rests on item (6) opening with the number 3ג2 on the page printed 366; the instruction (א) of item (6), which stands between that opening and paragraph (ב), is not deposited and was not read for this row.
Reading rejected: that the instruction names a different section.

F7 (I2). The places.
Reading taken: a place is a position in lines 98 to 101 of the earlier revision where the exact string or a one-letter-prefixed spelling of it is printed; there are five: the opening words of (ב), paragraph (1), paragraph (2) twice, and paragraph (3).
The exact string occurs once in each of those four lines (98, 99, 100 and 101), and the prefixed spelling "לתאגיד הבנקאי או למבטח" occurs once, in line 100; the builder checked this by an ad hoc substring test on the whole lines, which is not shipped.
The exact string is not a substring of the prefixed spelling, which has the prefix on the first and on the last word.
Reading rejected: that the row decides whether "in every place" covers a spelling that is not the exact string; it records the printed words of the instruction and what each revision prints.

F8 (I2). What the current revision prints.
Reading taken: in lines 105 to 108 of the current revision, the opening words of (ב), paragraph (1), the first place of paragraph (2) and paragraph (3) print the replacing words, 4 of 5 places; the second place of paragraph (2) is printed as it was in the earlier revision, and line 107 ends with an editorial note of the consolidation, printed as [note: או לנותן הערבות האחר].
The row does not say what the note is for, who wrote it, or what follows from it, and it does not say that the instruction reaches or does not reach the second place.
Reading rejected: that the row records anything about the legal effect of the instruction.

F9 (I2). The revisions.
The earlier revision is 2968704 (last edited 2025-12-17T11:00:11Z) and the current one is 3085793 (last edited 2026-09-30T07:30:55Z); the fields of the places are named by the revision ids.
The row states no commencement day and says nothing about when, or whether, the instruction takes effect.

F10 (I2). The limit of the search for earlier instruments.
The source notes record that the instrument that last touched s 3ג2 before 2026 (cited there as Sefer HaChukim 5777, page 528; 5777 is a Hebrew year, the one the tag on the heading of s 3ג2 gives as תשע״ז in both revisions' excerpts, and not an issue number) was searched in its text layer only and was not read from an image.
The builder of this row did not read it, and the statement is that of the source notes.

F11. The pages of Sefer HaChukim 3510.
The source notes give printed page = PDF page + 348, so printed pages 365, 366 and 367 are PDF pages 17, 18 and 19.
The builder confirmed it by rendering the three pages of the whole file and reading the footers: PDF page 17 is printed 365, 18 is 366 and 19 is 367.
The builder read, from the images, the lines deposited and, for the citation of the Law's original publication, footnote 33 of the page printed 365 (not deposited).

F12. The name of the consolidation's page.
The source notes name the Assurance Law's page with the year after a comma; the Wikisource API returns the page's title as "חוק המכר (דירות) (הבטחת השקעות של רוכשי דירות)" (page id 281425), and the title line of the page content, line 2, prints "חוק המכר (דירות) (הבטחת השקעות של רוכשי דירות), תשל״ה–1974".
Both revisions were fetched by revision id from that page; the Banking (Licensing) Law's current revision was fetched by page title.

F13. The fields in `as65-nouns.l4`.
Reading taken: the names of the fields are mine, written from the words quoted; two revisions are named by their ids so that no field says anything about what is in force.
Reading rejected: using the Law's own words as field names, because the Law does not describe its provisions by kind.

## Answer table

| | I1: the definition cites s 36ט for a licence | I2: the instruction replaces a string in s 3ג2(ב) |
| --- | --- | --- |
| What the citing words say | The licence is the one defined, under the name "רישיון נותן תשלום יציבותי", in s 36ט of the Banking (Licensing) Law, 5741-1981. | In every place of subsection (ב), "התאגיד הבנקאי או המבטח" is replaced by "התאגיד הבנקאי, נותן הערבות האחר או המבטח". |
| What the target prints | s 36ט prints a definition for "רישיון נותן שירותי תשלום יציבותי"; the two deposited lines print no definition under the shorter name. | In paragraph (2) of (ב), the earlier revision prints the exact string once and the prefixed spelling once; the current revision prints the replacing words at the first place and the second place as before, with an editorial note. |
| Present under that name | The target named has 0 of the 1 licences the words name, under that name. | The exact string stands at 1 of the 2 places of paragraph (2); the replacing words stand at 1 of the 2 in the current revision. |
| Limb (a) | The consolidation only (the Banking (Licensing) Law, revision 3078251); the instrument that the heading's tag names was not read. | The places: the consolidation only (revisions 2968704 and 3085793). |
| Limb (b) | The official page (Sefer HaChukim 3510, printed page 366), read from its image, the crop deposited; the consolidation's line 26 reads the same. | The official page (Sefer HaChukim 3510, printed page 367), read from its image, the crop deposited. |
| Limit | F2. | F10. |
| Page read | Sefer HaChukim 3510 (31 March 2026), printed pages 365 and 366. | Sefer HaChukim 3510, printed pages 366 and 367. |
| Control | Item (6) of s 31 cites s 3ג2, and the consolidation prints a heading with that number: 1 of 1. | The places outside paragraph (2): the exact string at 3 of 3 in the earlier revision and the replacing words at 3 of 3 in the current one. |

## The four expected-red assertions, one by one

`as65-tests-xrefs-red.l4` holds four assertions, all failing, and `check.sh` and `encoding.json` declare that count (4).
1. `the target prints the name the citing words print` for I1 is FALSE: the citing words print "רישיון נותן תשלום יציבותי" and the target prints "רישיון נותן שירותי תשלום יציבותי".
2. `the target has everything the citing words name` for I1 is FALSE: the target has 0 of the 1 licences named, under that name.
3. `the replaced string stands at every one of the places` for the places of paragraph (2) is FALSE: it stands at 1 of 2 in the earlier revision.
4. `the replacing words stand at every one of the places` for the places of paragraph (2) is FALSE: they stand at 1 of 2 in the current revision.

## The check

Run from this folder with `L4=$HOME/.cache/l4-main/98/l4 ./check.sh`; the `l4` that wrote the row was 1.6.98 (main, 7689b0d, 2026-10-19) and the main build it was compared with was 1.6.109 (main, 4c887e0, 2026-11-04).

| module | errors | satisfied | failed | refused | expected failed | main: errors | satisfied | failed | refused | main verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| as65-cross-references.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| as65-nouns.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| as65-tests-xrefs-red.l4 | 4 | 0 | 4 | 0 | 4 | 4 | 0 | 4 | 0 | same |
| as65-tests-xrefs.l4 | 0 | 40 | 0 | 0 | 0 | 0 | 40 | 0 | 0 | same |

The four errors are the four failed assertions, each reading "assertion failed", on lines 11, 13, 18 and 20 of the red module; no other error, and no refusal.
Positive control: in two scratch copies, (1) the target's printed name and the count under that name were changed to the citing words' name and 1, and the two I1 red assertions then passed (2 of 4 failed) while four sound assertions turned red; (2) the second place of paragraph (2) was given the exact string in the earlier revision and the replacing words in the current one, and the two I2 red assertions then passed (2 of 4 failed) while ten sound assertions turned red; both copies were deleted.
`tools/srcquote.py` and `tools/hebcheck.py` are copied from row il-64 and changed (the change is said in each file's second line): a marker or `src:` line carries the revision id, one run of `srcquote.py` expands only the markers of the excerpt it is given, and `hebcheck.py` takes every argument ending in `.excerpt.txt` as a source.
`python3 -I tools/hebcheck.py ../../registers/source-bundle/*.excerpt.txt *.l4 NOTES.md` exits 0: every run of Hebrew outside a quotation line occurs in the deposited excerpts.

## The deposits

UNOFFICIAL aids: three excerpts of Hebrew Wikisource consolidations, each of whole lines only, each carrying its line numbers in the whole page, so that `src:3085793:26` means line 26 of revision 3085793.
- `sale-apartments-assurance-law-rev3085793.he.wiki.excerpt.txt`: the Assurance Law, revision 3085793 (last edited 2026-09-30T07:30:55Z), lines 2, 26, 100 and 105 to 109. The whole page content has sha256 8a7ce9f04bdb846e5f4138d3bc6db7f16292e41a9d091b612896934e36f2992c and 58602 bytes (256 newline-terminated lines); the excerpt has sha256 cff3207aa201a048d0ce7efb547c3f6a844bf21243458a90f78ecae758017c81 and 3063 bytes.
- `sale-apartments-assurance-law-rev2968704.he.wiki.excerpt.txt`: the Assurance Law, revision 2968704 (last edited 2025-12-17T11:00:11Z), lines 93 and 98 to 102. The whole page content has sha256 7ded095545133d448a573df2a89e1e25df22a3ff1e7dea607c6214070930a87b and 54087 bytes (249 newline-terminated lines); the excerpt has sha256 7ef5330a7eba74bb39513e2e99a997d2ca17dcbc517a604a538af9473115d6d1 and 2401 bytes.
- `banking-licensing-law-rev3078251.he.wiki.excerpt.txt`: the Banking (Licensing) Law, revision 3078251, the current revision when it was fetched on 2026-11-10 (last edited 2026-08-21T05:00:09Z), lines 631 and 644. The whole page content has sha256 064a11f844385ecc36b39e80f151b589c0667f5387aad770d0045f85c919ccc9 and 187105 bytes (936 newline-terminated lines); the excerpt has sha256 72bdd9a2920fa41dd63db6b265fc44d6201ae819fd2dc30ef0e422915c135c2c and 1017 bytes.

Official pages, in `registers/source-bundle/official/`, each a crop composed of bands separated by grey bars, each viewed before it was deposited:
- `sh3510-5786-p365-bands.png`, Sefer HaChukim 3510, printed page 365 (PDF page 17), 41262 bytes, sha256 01d983d4eedd474242eb95bf4b2f10a1837825b971367c7e10c06d82d476d2a3: the heading (margin note) of s 31 with its number and first line and the first line of its item (1), and the footer line.
- `sh3510-5786-p366-bands.png`, Sefer HaChukim 3510, printed page 366 (PDF page 18), 34252 bytes, sha256 a19bb728fe0db621a6b09924c57ee7d54cc9dee6b41f0451f1fefd46b9e84987: the two lines of the definition, the words that open item (6), and the footer line.
- `sh3510-5786-p367-bands.png`, Sefer HaChukim 3510, printed page 367 (PDF page 19), 29315 bytes, sha256 ef69108143b409afc7e6b7dcee32de6515d46730f077da38d1a67c1677c95bc6: the two lines of paragraph (ב) of item (6), and the footer line.

Only the pages read are deposited, as crops, and no PDF and no full-page image of any page is deposited.
`registers/source-bundle/SOURCES.json` gives the whole file's sha256 and size for Sefer HaChukim 3510 and each crop's and excerpt's own sha256 and size; the Knesset address is the one the source notes give, and was not re-fetched.

## What was not done

No instrument other than Sefer HaChukim 3510 was read by the builder of this row, and the statement about the earlier instrument in F10 is that of the source notes.
The lines of the pages printed 365 and 366 other than the lines deposited were seen on the rendered pages, where they share a page with the lines read, and are not deposited; nothing of them is recorded.
Subsections (א) and (ג) of s 3ג2 and every other provision of the Assurance Law were not read.
The Banking (Licensing) Law was read only at lines 631 and 644 of one revision, and no instrument that amended it was read.
The footnote that gives the Assurance Law's original publication (Sefer HaChukim, Hebrew year 5735, p. 14) was read from the page image of printed page 365 and is in no deposit.
The Knesset address of the whole file of Sefer HaChukim 3510 was not re-fetched.
