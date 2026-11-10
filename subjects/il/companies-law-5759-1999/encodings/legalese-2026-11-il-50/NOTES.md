# Row il-50: three printed date pairs and one saving clause in the Companies Law, 5759-1999, and its regulations (four defects, six controls)

Status: draft, version 0.1.0, target compiler main.
No domain expert has read this against the source.
Every claim below was checked against a text in the source bundle or a page image named beside it; where it was not, it says so.

## 1. Scope

This row is not an encoding of the Companies Law, 5759-1999, and not an encoding of the Companies (Fees) Regulations, 5761-2001, or of the Companies (Motion for Compromise or Arrangement) Regulations, 5762-2002.
It records four places where the printed words disagree with themselves or with a later instrument, as typed values that tests check, and keeps the four defects as expected-red tests.
Defects 1, 2 and 4 are date pairs: a Hebrew date and a Gregorian date printed side by side as one date, whose two halves name different days; defect 4 is one signature line printed five times in one issue.
Defect 3 is a saving clause in the Companies Law that keeps Ordinance sections which a later law cancelled.
For each defect the row records what each half or each reading says and where it was read from, and it gives a control: for each date pair another pair in the same instrument that agrees, and for the saving clause two other saved Ordinance sections that no cancellation reaches.
The row asks no question from any seat, because it records printed facts and not duties, so no `@export` module is written.
Everything not named in section 4 is out of scope.

## 2. Sources

Four unofficial aids are deposited as EXCERPTS of the Hebrew Wikisource page, each behind a four-line header that gives the page revision, the size and sha256 of the whole page as retrieved, and the lines copied unchanged; no other line of the page is part of an excerpt.
The line numbers on the `ext:[comp]`, `ext:[fees]`, `ext:[compromise]` and `ext:[ord]` lines of the .l4 files are the EXCERPT's own line numbers, not the whole page's.

| excerpt, in `../../registers/source-bundle/` | page, revision and last edit | sha256 of the excerpt | the whole page as retrieved |
| --- | --- | --- | --- |
| `companies-law-5759-1999-s367.excerpt.he.wiki.txt` | the Companies Law, revision 3088229, 2026-10-12T09:30:10Z | bc98a83242c55239742133f84b0edfc0c79397505f33475a26ff40f1c1122981 | 625106 bytes, sha256 8d44f234a79dca23ef8058859084ba64bb7a69437b88e94aee036b3f1ab21279 |
| `companies-fees-regulations-5761-2001.excerpt.he.wiki.txt` | the Fees Regulations, revision 2966831, 2025-12-08T11:00:28Z | 53624de8df92b29068aa489d73ca91f3e9b2264fcdfa87021ce537ca2f598496 | 21267 bytes, sha256 01359302ad57c19048d25c6622334bd098b3bec3e379c0767ca88106f9096e94 |
| `companies-compromise-regulations-5762-2002.excerpt.he.wiki.txt` | the Compromise Regulations, revision 2926477, 2025-05-13T12:07:22Z | f8ec0a84a191cc637d9b85c47978ddb851fbec21d205be6afadfec1177b8a378 | 76619 bytes, sha256 e2c26f703afc5f58e73ac00ae2e8f7d3abe79f5bf3acf5f44504073967d22771 |
| `companies-ordinance-new-version-5743-1983.excerpt.he.wiki.txt` | the Companies Ordinance [New Version], revision 2992329, 2026-02-25T09:00:18Z | 13882d55240186017f0d1a8cbea9fdb186b5cfba584e1ac057abdcfe8fc1b79f | 250208 bytes, sha256 d5f465d04b9c0aa92695dd97acd9c746971454f7f333219e3f38d7f54aaf9066 |

The Companies Law revision is the one recorded when the page was retrieved on 2026-10-21 (the revision id from the page HTML, the time from the Last-Modified header of the raw response).
For the other three pages, on 2026-11-10 the sha1 of the whole retrieved file was matched to the page history (API, `prop=revisions`, `rvprop=ids|timestamp|sha1`), which gives each revision above as the current revision.
All four are unofficial aids; every statement that rests only on one of them says CONSOLIDATION-ONLY.

The official instruments are in `../../registers/source-bundle/official/` and `../../registers/source-bundle/amending-laws/`:

| file | what it is | sha256 |
| --- | --- | --- |
| `official/kt6074-5761-pp231-232-page-extract.pdf` | Kovetz HaTakanot 6074, the issue of 4 January 2001: a two-page extract, printed pp. 231 and 232 only (extract pages 1 and 2), cut out with qpdf from the 13-page file as downloaded (sha256 788ce5aefa7bd6b9e54abe52b6eb96715b27772ced88c238a63a29c298740dbc, 396141 bytes); an image-only scan with no text layer, so the printed pages deposited are exactly those two | d49cfa2d6550534ea36fe28c2b88d00d3539116d0eaf6cfc4ad777944e016690 |
| `official/kt6178-5762-pp883-904-page-extract.pdf` | Kovetz HaTakanot 6178, the issue printed as 27 June 2002: a two-page extract, printed pp. 883 and 904 only (extract pages 1 and 2), cut out with qpdf from the 41-page file as downloaded (sha256 90e4bb958774a836f0d4040b1b657a8e2b35f77bab8a59c95ef3e0ab570469c0, 1088609 bytes); an image-only scan with no text layer, so the printed pages deposited are exactly those two | 9e4e2d4ed961d25e572bd3bf76078f78f831b32d39156f941b0c43b614bc324f |
| `official/kt7639-5776-pp946-949-page-extract.pdf` | Kovetz HaTakanot 7639, 24 Adar II 5776 (printed 3 April 2016): a four-page extract, printed pp. 946, 947, 948 and 949 (extract pages 1 to 4), cut out with qpdf from the 8-page file as downloaded (sha256 0bb6b7796e7ad863df38c531ae18f33c502b942dc42969d2dbece84401005406, 104468 bytes), with a text layer whose order of words is garbled; only p. 946 was read from the page image | cf5572416668cba0fd832cbf66e236484b5c1d0d218288ae31aab3477efa0469 |
| `amending-laws/sh2708-5778-pp393-394-page-extract.pdf` | Sefer HaChukim 2708, 15 March 2018: a two-page extract, printed pp. 393 and 394 only (extract pages 1 and 2; printed page = page of the downloaded file + 296), cut out with qpdf from the 128-page file the Knesset serves (sha256 f6c352653ced3bf709ef5805474648405aa26c5d4b2da0934732d2d204d6a98b, 2081294 bytes as downloaded); the text layer of the extract is the one checked | 69792f94a90d4ad852650a63631db5d7fc975e570a3d2e3a46ec86771d20d3c4 |

The three Kovetz HaTakanot files come from `olaw.org.il`, a website that hosts scans of Reshumot issues and is not a government site; the Sefer HaChukim file comes from the Knesset's server.
Each cited page has a page image beside its PDF (`kt6074-5761-p231.png`, `kt6074-5761-p231-reg7-reg8-crop.png`, `kt6074-5761-p232.png`, `kt6074-5761-p232-signature-crop.png`, `kt6178-5762-p883.png`, `kt6178-5762-p904.png`, `kt7639-5776-p946.png`, `sh2708-5778-p393.png`, `sh2708-5778-p394.png`).
The printed pages deposited are listed here because two of the extracts are image-only scans with no text layer: KT 6074, printed pp. 231 and 232 only; KT 6178, printed pp. 883 and 904 only; KT 7639, printed pp. 946 to 949 only; SH 2708, printed pp. 393 and 394 only.
Printed pp. 405 and 406 of SH 2708 are not deposited: p. 405 carries text outside the row's scope, and items (11) to (19) of section 360 run across both pages.
Every deposited PDF with a text layer was searched page by page for text outside the row's scope before it was deposited; the two scans have no text layer, so their printed pages are listed above instead.
`../../registers/source-bundle/SOURCES.json` gives the URL, retrieval date, sha256 and size of every file, and the sha256 values were recomputed with `shasum -a 256` on 2026-11-10.

How the Hebrew was checked.
Every run of Hebrew in the .l4 files and in this file that is not on an `ext:[...] |` line occurs verbatim in the four excerpts or in the text layer of KT 7639 (`tools/hebcheck-all.sh` joins only those five texts, so it also keeps the row's Hebrew inside what is deposited); a line marked `[computed, not printed]` is skipped, because it holds a Hebrew date the row computed.
The three `ext:[SH 2708 ...]` lines, typed from the page images, and the thirteen `ext:[KT 7639 ...]` lines were checked against the text layer of the page (`tools/pdfcheck.py`: 16 lines, 0 problems); for the KT 7639 lines every Hebrew word and every numeral of the typed line must occur in the page's text layer, which catches a typing slip and does not prove the order of the words, because that layer prints right-to-left runs in a garbled order.
Of the KT 7639 lines, those on p. 946 were typed from the page image (the title of the first regulation, its signature line, and the title of the next); those on pp. 947, 948 and 949 were read in the text layer only, and the page images of those three pages were not read.
The `ext:[KT 6074 ...]` and `ext:[KT 6178 ...]` lines were typed from the page images and are NOT machine-checked, because those two Kovetz HaTakanot PDFs are image-only scans with no text layer.
Of the five KT 6074 and KT 6178 lines in the references module, three agree word for word with the consolidation's own line apart from the quotation marks (regulation 8, regulation 66, the compromise signature line); the Fees signature line differs in one letter in the Gregorian month word (section 5); the running date line of the issue has no counterpart in the consolidation.
That agreement is CONSOLIDATION-ONLY and is a check on my typing, not a second reading of the page.
The Hebrew dates were converted with a calendar routine that first reproduced 30 Kislev 5785 = 31 December 2024; its output for each date is in the comments of `comp50-cross-references.l4` and is not computed by L4 (fork D1).

## 3. Files

| file | what it holds |
| --- | --- |
| `comp50-nouns.l4` | the three kinds of reading, the record of a printed date pair and of a run of section numbers; no rule |
| `comp50-cross-references.l4` | the functions, and one typed value per date pair, control and run, with the words of the texts quoted beside it |
| `comp50-tests-xrefs.l4` | 85 assertions: the controls agree, what was read from where, the recorded facts about the three defects, and the days the two halves of a date pair answer differently (NOTHING) |
| `comp50-tests-xrefs-red.l4` | 8 assertions that fail, on purpose (section 7) |
| `check.sh`, `fetch-main-l4.sh` | the check; `check.sh` declares 8 expected failures for the file above |
| `tools/` | `extquote.py`, `hebcheck.py`, `hebcheck-all.sh`, `pdfcheck.py` |

## 4. Coverage

| provision | status |
| --- | --- |
| Fees Regulations, regulation 8 (the commencement day) | encoded as a date pair; defect 1; read from the page image of KT 6074 p. 231, with the CONSOLIDATION-ONLY caveat on later instruments |
| Fees Regulations, the Minister's signature line and the running date line of the issue | encoded as date pairs; controls 1 and 2; read from the page images of KT 6074 p. 232 |
| Fees Regulations, regulation 7 (the repeal of the earlier regulations) | read next to regulation 8 and not encoded: it names no day of its own, and what the earlier regulations required is not this row's subject |
| the rest of the Fees Regulations | out-of-scope: the row records one printed date; it does not say what any fee is or when it falls due, and the other regulations of the instrument were not examined for this row |
| Compromise Regulations, regulation 66 (the last day of a temporary provision) | encoded as a date pair; defect 2; read from the page image of KT 6178 p. 883, with the CONSOLIDATION-ONLY caveat on later instruments |
| Compromise Regulations, the Minister's signature line | encoded as a date pair; control 3; read from the page image of KT 6178 p. 904 |
| Compromise Regulations, regulation 1, paragraph (2) of the definition of the word for publication | quoted from the consolidation (CONSOLIDATION-ONLY) because regulation 66 limits it; the consolidation's own note on it records that it lapsed under regulation 66; not encoded |
| Compromise Regulations, regulation 65 (commencement 30 days from publication) | read next to regulation 66 and not encoded: it uses no date pair, so it has no pair to compare |
| the rest of the Compromise Regulations and their forms | out-of-scope: the row says nothing about the procedure the regulations govern, about any form in the schedule, or about any other regulation; they were not examined for this row |
| KT 7639 (3 April 2016), the five signature lines of 25 Adar I 5776 on pp. 946, 948 and 949 | encoded as five date pairs; defect 4; the first line read from the page image of p. 946, the other four in the text layer only; the sources are the official issue, with no consolidation |
| KT 7639, the two signature lines of 10 Adar II 5776 on p. 947 | encoded as one date pair; control 6; text layer only |
| the rest of KT 7639 | out-of-scope: the row cites the five lines above and the control; the other signature lines and instruments of the issue are not cited, and the row says nothing about them |
| Companies Law s 367(א)(1), the three ranges of Ordinance section numbers | encoded as three runs; defect 3; limb (a) from the page images of SH 2708 pp. 393 and 394 with the chapter placing CONSOLIDATION-ONLY; limb (b) CONSOLIDATION-ONLY |
| Companies Law s 367(א)(2) and (א)(5), the saving of Ordinance sections 33 and 115א | encoded as two runs; controls 4 and 5 |
| Companies Law s 367(ב), how the kept provisions are read | quoted for fork F3; not encoded |
| the words of s 367(א)(1) after the three ranges, and the paragraphs of s 367(א) other than (1), (2) and (5) | out-of-scope: they were not examined for this row, and the row says nothing of them |
| the rest of the Companies Law | out-of-scope: the row records one saving clause; it does not encode the Law, and it does not say what any other section requires |
| the Insolvency and Economic Rehabilitation Law, 5778-2018 | cited only for section 359 items (4) and (5), which cancel Ordinance sections 195 to 201 and chapters 11 to 17, and for section 360, read for limb (b) of defect 3 (section 5): items (1) to (9) from the deposited p. 394, and items (11) to (19) from printed pp. 405 and 406, which are not deposited; the day those cancellations began to apply is fixed by a provision of that Law that this row does not cite, so no day is stated for defect 3 |
| items (1) to (3) of section 359 of that Law | read on printed pp. 393 and 394: they change sections 1, 178(א) and 194 of the Ordinance, which are not in the cancelled runs or in the controls; not encoded |
| the Companies Ordinance [New Version], 5743-1983 | used for one purpose: the section numbers at which its chapters 11 and 17 begin and end, and the text and notes of the two saved controls; not encoded |

## 5. The defects and the controls: answer table

### The date pairs

The "computes to" column is the calendar routine's output for the printed Hebrew date (fork D1); the "agree" column compares it with the printed Gregorian day.

| pair | printed Hebrew half | printed Gregorian half | the Hebrew half computes to | days apart | agree | read from |
| --- | --- | --- | --- | --- | --- | --- |
| defect 1: Fees Regulations, regulation 8, the commencement day | 6 Shevat 5761 | 1 January 2001 (6 Tevet 5761) | 30 January 2001 | 29 | no | the page image of KT 6074 p. 231; that no later instrument touched the words is CONSOLIDATION-ONLY |
| defect 2: Compromise Regulations, regulation 66, the last day of the temporary provision | 12 Tammuz 5768 | 15 July 2007 (29 Tammuz 5767) | 15 July 2008 | 366 | no | the page image of KT 6178 p. 883; that no later instrument touched the words is CONSOLIDATION-ONLY |
| control 1: Fees Regulations, the Minister's signature line | 23 Kislev 5761 | 20 December 2000 | 20 December 2000 | 0 | yes | the page image of KT 6074 p. 232 |
| control 2: the running date line of the issue of KT 6074 | 9 Tevet 5761 | 4 January 2001 | 4 January 2001 | 0 | yes | the page image of KT 6074 p. 232, and the foot of p. 231 |
| control 3: Compromise Regulations, the Minister's signature line | 29 Sivan 5762 | 9 June 2002 | 9 June 2002 | 0 | yes | the page image of KT 6178 p. 904 |
| defect 4: KT 7639, five signature lines of the Minister of Justice (pp. 946, 948, 949) | 25 Adar I 5776 | 8 March 2016 (28 Adar I 5776) | 5 March 2016 | 3 | no | the first line (p. 946) from the page image; the other four in the text layer only |
| control 6: KT 7639, two signature lines on p. 947 | 10 Adar II 5776 | 20 March 2016 | 20 March 2016 | 0 | yes | the text layer only |

What the two halves of defects 1 and 2 say, in the printed words.
Defect 1: regulation 8 prints ו׳ בשבט התשס״א (1 בינואר 2001), as the day on which the regulations take effect.
The printed Gregorian day is three days before the issue date printed at the foot of the same pages (4 January 2001, control 2), and the Hebrew half's day is 26 days after it.
Defect 2: regulation 66 prints י״ב בתמוז התשס״ח (15 ביולי 2007) as the day until which paragraph (2) of the definition of the word for publication in regulation 1 stays in force.
As of 10 November 2026 both days of each of defects 1 and 2 have passed, so the answer to "is it in force today" is the same on both halves; the halves differ only for days between them, which the tests record as NOTHING.

Control 1: the scan prints the Gregorian month word of the signature line with a letter that reads as resh where a dalet is expected; the numerals 20 and 2000 are clear, and the consolidation prints the word with a dalet.
The routine matches the printed pair, so the row treats the line as December and records the difference here.

Defect 4 is five signature lines of one issue, Kovetz HaTakanot 7639 (24 Adar II 5776, printed 3 April 2016), each printing the same pair, 25 Adar I 5776 beside 8 March 2016.
The lines, in the order of the issue: (1) p. 946, under the Companies (Relief regarding the Duty to Set a Compensation Policy) (Amendment) Regulations, 5776-2016; (2) p. 948, under the Companies (Notice and Announcement of a General Meeting and a Class Meeting in a Public Company and Adding an Item to the Agenda) (Amendment) Regulations, 5776-2016; (3) p. 948, under the Companies (Period of Validity of a Resolution under s 121 of the Law) Regulations, 5776-2016; (4) p. 949, under the Companies (Additional Classes of Company in Which Outside Directors Who Are Not Israeli Residents May Be Appointed) Regulations, 5776-2016, whose title is on p. 948; (5) p. 949, under the Companies (Change of the First Schedule A to the Law) Order, 5776-2016.
The titles are my English renderings of the Hebrew titles printed on those pages.
Only line (1), with the title above it, was read from the page image; lines (2) to (5) and the control were read in the text layer of the PDF only.
5776 is a leap year, so Adar I is the first of two Adars: the routine gives 25 Adar I 5776 = 5 March 2016 and 28 Adar I 5776 = 8 March 2016, three days apart.
The control, 10 Adar II 5776 beside 20 March 2016, is printed twice on p. 947, under the regulation whose title is on p. 946 and under the next one, and agrees with the routine.
The sources are the official issue only; no consolidation is used.
No right or deadline in this row turns on these lines, and the row shows no effect of the difference.

### The saving clause

| | the citing words | the target | limb (a) | limb (b) |
| --- | --- | --- | --- | --- |
| defect 3 | s 367(א)(1) of the Companies Law keeps from the repeal of the Ordinance סעיפים 164 עד 201, 244 עד 367, 370 עד 382 | the Ordinance as the later law left it | read from the page image of SH 2708 p. 394: item (4) of section 359 cancels sections 195 to 201, item (5) cancels chapters 11 to 17; where those chapters begin and end (chapter 11 opens with section 244, chapter 17 closes with section 382, chapter 18 opens with section 383) is CONSOLIDATION-ONLY | CONSOLIDATION-ONLY (below) |
| control 4 | s 367(א)(2) keeps Ordinance section 33 | section 33, printed with its text and with a note that s 367(2) keeps it in force (CONSOLIDATION-ONLY) | items (1) to (5) of section 359, on printed pp. 393 and 394, name sections 1, 178(א), 194, 195 to 201 and chapters 11 to 17; none names section 33; section 33 stands in chapter 2, before chapter 11 (CONSOLIDATION-ONLY) | CONSOLIDATION-ONLY |
| control 5 | s 367(א)(5) keeps Ordinance section 115א | section 115א, printed with its text, a note that s 367(א)(5) keeps it in force, and an amendment mark of 5765 (CONSOLIDATION-ONLY) | the same page images; none names section 115א; it stands in chapter 6, before chapter 11 (CONSOLIDATION-ONLY) | CONSOLIDATION-ONLY |

What the numbers say, counted by `comp50-tests-xrefs.l4` on the printed ends of each range (the row counts NUMBERS, not sections: whether every number in a range is a section of the Ordinance is not recorded).
The first range, 164 to 201, holds 38 numbers; the 7 numbers 195 to 201 are in item (4), and the other 31 (164 to 194) are named by neither item (4) nor item (5).
The second range, 244 to 367, holds 124 numbers and the third, 370 to 382, holds 13; both lie wholly inside chapters 11 to 17 as the consolidation places them.
So 144 of the 175 numbers in the three ranges are cancelled on the page images alone for 7 of them and, for the other 137, on the page images plus the consolidation's placing of the chapters.

Limb (b) for defect 3, sorted by how strong it is.
CONSOLIDATION-ONLY: the words of s 367(א)(1) as quoted; the heading of s 367 carries the consolidation's mark "תיקון: תשס״ה" (last amended in 5765, Amendment 3), which is the only basis for the statement that nothing later touched them, and neither the Law as made nor Amendment 3 was read.
Read from the page images of SH 2708: section 360, which amends the Companies Law, has items (1) to (9) on printed p. 394, which is deposited, and items (11) to (19) on printed pp. 405 and 406, which are not deposited because they carry text outside the row's scope; none of those items names section 367.
The claim about items (11) to (19) therefore rests on my reading of pages that are not in the bundle, and cannot be checked from it.
Item (10) of section 360 runs over the pages between and was not read page by page; a search of the text layer of PDF pages 98 to 110 of the file as downloaded (not deposited) for the digits 367 found no line (`pdftotext -f 98 -l 110`, then `grep -c 367` page by page: 0 on each page), and a text layer is not the page; that search cannot be repeated from the bundle either.
So limb (b) is recorded as the consolidation only.

The day the cancellations began to apply.
It is fixed by a provision of the Insolvency and Economic Rehabilitation Law that this row does not cite, so the row states no day and `the named text is in force on` is not used for defect 3 (fork K4).
The second red assertion for defect 3 is therefore a count of shared numbers, which needs no day.

## 6. Fork register

Each fork gives the reading taken, the reading held aside, and what licenses each.

- F1, which half of a date pair governs.
  Reading taken: none. For a day between the two printed days the row's answer is NOTHING, because the printed words do not say which half governs and this row cites no rule that settles it.
  Reading held aside: that the Hebrew half governs, or that the Gregorian half governs.
  What licenses each: the printed words of regulation 8 and of regulation 66, quoted on `ext:` lines.
- F2, whether "until the day" counts the day itself.
  Reading taken: none. Each of the two printed days of defect 2, and every day between them, is NOTHING; a day before both is TRUE and a day after both is FALSE.
  What licenses it: regulation 66 says the paragraph stays in force "עד יום" a named day; this row cites no rule on whether that day is counted.
- F3, what a saving clause that keeps cancelled text means.
  Reading A: s 367(א)(1) saves what it names and the Ordinance has since lost part of it, so a court reads the clause as keeping only what remains; s 367(ב) says the kept provisions are to be read, as far as possible, in the light of the Companies Law (quoted on an `ext:[comp]` line).
  Reading B: s 367(א)(1) cites Ordinance text that the later law cancelled, so the citation is to text that no longer exists.
  The row takes neither: it records the overlap as a count (comp50-tests-xrefs.l4) and the failing assertions state what the clause needs if it is read literally.
- F4, which half governs on the five signature lines of KT 7639.
  The same question as F1, for a day of signing; the row rules neither reading and its tests record only that the halves disagree.
  Reading A: the printed Hebrew date is right, so the Minister signed on 5 March 2016, which is כ"ה באדר א' התשע"ו (as printed in the text layer).
  Reading B: the printed Gregorian date is right, so the Minister signed on 8 March 2016, which is 28 Adar I 5776, כ"ח באדר א' התשע"ו [computed, not printed].
  What licenses each: the five signature lines of KT 7639 on pp. 946, 948 and 949, quoted on `ext:` lines; the issue's own control pair, 10 Adar II 5776 beside 20 March 2016, agrees.
- D1, the Hebrew dates.
  The Gregorian day a Hebrew date computes to is typed from a calendar routine and not computed by L4; the routine reproduced 30 Kislev 5785 = 31 December 2024 before it was used.
  Each pair's output is stated beside it: 6 Shevat 5761 = 30 January 2001; 6 Tevet 5761 = 1 January 2001; 12 Tammuz 5768 = 15 July 2008; 29 Tammuz 5767 = 15 July 2007; 23 Kislev 5761 = 20 December 2000; 9 Tevet 5761 = 4 January 2001; 29 Sivan 5762 = 9 June 2002; 25 Adar I 5776 = 5 March 2016; 28 Adar I 5776 = 8 March 2016; 10 Adar II 5776 = 20 March 2016.
  A domain expert can check each in a second calendar.
- K1, the kinds.
  The three kinds of `Where a reading comes from` are my plain descriptions; the middle one names the caveat so that it is typed and not hidden in a note.
- K2, the choice of controls (assumed, not ruled).
  The controls are mine: for each date pair another pair in the same instrument or issue whose halves agree, and for the saving clause the two other paragraphs of s 367(א) that save a single numbered Ordinance section.
  A different choice would test the same functions.
- K3, numbers and not sections.
  The row counts the NUMBERS the printed ranges name; it does not say that every number is a section of the Ordinance.
- K4, no day for defect 3 (section 5).

## 7. Expected red

Eight assertions in `comp50-tests-xrefs-red.l4` fail on purpose, and the count (8) is declared in `check.sh` and in `encoding.json`.
Each defect has two, and each states what the citing words need.

- Defect 1: `the printed pair agrees` for regulation 8 of the Fees Regulations (the halves are 29 days apart), and `the regulations are in force on` 15 January 2001, expected JUST TRUE (the answer is NOTHING, because the two halves answer that day differently).
- Defect 2: `the printed pair agrees` for regulation 66 of the Compromise Regulations (the halves are 366 days apart), and `the temporary provision is in force on` 1 January 2008, expected JUST TRUE (the answer is NOTHING).
- Defect 3: `how many numbers two runs share` for the first range and the cancelled sections 195 to 201, expected 0 (the answer is 7, from the page images alone), and the same for the second and third ranges taken together against the cancelled chapters, expected 0 (the answer is 137, CONSOLIDATION-ONLY for where the chapters begin and end).
- Defect 4: `the printed pair agrees` for the first signature line of KT 7639 (the halves are 3 days apart), and the same for all five lines together, expected to hold (the answer is that it does not, for each of the five).

Nothing in either file was edited to make it pass.
Each failing assertion is paired with a green assertion in `comp50-tests-xrefs.l4` that records the actual value, so the reason it fails is itself tested.

## 8. Check numbers

Run as `L4=~/.local/bin/l4 ./check.sh`; main is the build `fetch-main-l4.sh` fetched, build 1.6.109 (main, 4c887e0, 2026-11-04).
Both binaries give the same four counts for every file.

| file | errors | satisfied | failed | refused | expected failed |
| --- | --- | --- | --- | --- | --- |
| `comp50-nouns.l4` | 0 | 0 | 0 | 0 | 0 |
| `comp50-cross-references.l4` | 0 | 0 | 0 | 0 | 0 |
| `comp50-tests-xrefs.l4` | 0 | 85 | 0 | 0 | 0 |
| `comp50-tests-xrefs-red.l4` | 8 | 0 | 8 | 0 | 8 |
| total | 8 | 85 | 8 | 0 | 8 |

The eight errors are the eight expected failures.
Mutation control, on copies of the modules in a scratch directory that were deleted afterwards: (a) giving the Fees Regulations' Hebrew half the same day as its Gregorian half (1 January 2001) left 6 of the 8 red assertions failing (the 2 about defect 1 passed) and made 7 of the 85 green assertions fail; (b) moving the cancelled chapters to section numbers 400 to 410 left 7 of the 8 red assertions failing (the one on the second and third ranges passed) and made 5 of the 85 green assertions fail; (c) giving the first signature line of KT 7639 a Hebrew half that computes to its Gregorian day (8 March 2016) left 7 of the 8 red assertions failing (the one on the first line passed, and the one on all five lines still failed) and made 3 of the 85 green assertions fail; so the tests can fail.
The check does not see a difference that no assertion exercises.

## 9. Open questions for a domain expert

- When the Hebrew half and the Gregorian half of a printed date disagree, which governs (fork F1), and does "until the day" count the day (fork F2)?
- Is s 367(א)(1), read today, a saving clause that keeps only what the Ordinance still holds, or a citation to cancelled text (fork F3)?
- What is s 367(א)(1) as the Companies Law made it, and what did Amendment 3 change in it? Neither was read.
- Does the Minister's signing day on the five lines of KT 7639 fall under reading A or B (fork F4)? The page images of pp. 947, 948 and 949 were not read, only their text layer.
- Item (10) of section 360 of SH 2708 was not read page by page; does it, or any later instrument, touch s 367? Items (11) to (19) were read from printed pp. 405 and 406, which are not in the bundle.
- Do the chapters of the Ordinance begin and end at the sections the consolidation shows (chapter 11 at section 244, chapter 17 closing at section 382)? That rests on the consolidation alone.
- Did any instrument after KT 6074 or KT 6178 touch regulation 8 of the Fees Regulations or regulation 66 of the Compromise Regulations? The consolidations' headers list later instruments for the Fees Regulations that were not opened.

No domain expert has read this against the source.
