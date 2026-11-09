# Row il-52: two findings in the First Schedule of the Prohibition on Money Laundering Law, 5760-2000

Status: draft, version 0.1.0, 2026-11-10, target compiler main.
How each claim was checked: every quotation of an official instrument was typed from a page image that was looked at (the covers named under the answer table are the exception), and `tools/pdfcheck.py` then confirmed that each word of it occurs in the text layer of that page (23 quotation lines, no word missing).
The four quotation lines of Sefer HaChukim 3571 (two from p. 985, two from the cover) were checked on 2026-11-10 against the text layer of the file as downloaded, which is NOT deposited (sha256 ac4d60974667a1b0fdaae51f1b5801d38eb50b92dfbc5ef9fbe75257eae51f12, 464772 bytes, recorded in `SOURCES.json`).
Without that file `tools/pdfcheck.py` skips those four lines and says so (19 checked, 4 skipped); with `SH3571_PDF` naming a copy of it as downloaded, all 23 are checked and none has a problem.
Every quotation of a consolidation is expanded by `tools/srcquote.py` or `tools/extquote.py` from the deposited excerpt, not typed.
No domain expert has read this against the source.

## Scope

This row is NOT an encoding of the Prohibition on Money Laundering Law, 5760-2000 (Sefer HaChukim 5760 p. 293).
It records two things that the Law's First Schedule shows, as typed values with tests, and keeps each as an expected-red test.
The first is a numbering collision: an order of the Minister of Justice and an Act of 2026 each add an item after item (18ח), and both print the label (18ט).
The second is a citation: item (18ו) cites section 7ג(ב) of the Prevention of Infiltration (Offences and Jurisdiction) Law, 5714-1954, as brought in by section 1(1) of a temporary law of 2013, and the Hebrew Wikisource consolidation prints that section as lapsed.
Each finding has one sound control beside it.
A date that the sources held do not give is NOTHING; there is no REFUSE, because the target is main.

## Seat

The seat is the person whose dealings in property the Law prohibits, whose conduct is tested against the offences the First Schedule lists.
This row asks no question from the seat, because it records references and numbering, not rules.

## Coverage

This row does not encode the Law, so almost all of it is out of scope; the table says why for each part.

| Part | Status | Reason |
| --- | --- | --- |
| First Schedule: the label (18ט) of the first item of the order in Kovetz HaTakanot 12422 p. 2196א, the label (18י) of its second item, and the label (18ט) of the item added by section 27 of Sefer HaChukim 3571, p. 985 | encoded | Finding 1. Only the labels, the place (after item (18ח)), the first day and the length are recorded; the text of the added items is not quoted or discussed. |
| First Schedule: item (18ו) and its citation of section 7ג(ב) of the Infiltration Law | encoded | Finding 2. |
| First Schedule: the place of item (18ו) after item (18ה), as the order in Kovetz HaTakanot 7721 p. 38 puts it | encoded | Control for finding 2. |
| First Schedule: every other item | out-of-scope | The row records one numbering and one citation. The offences that the other items list, and the statutes they cite, are not read here, and the row says nothing about whether those citations stand. |
| The sections of the Law (definitions, the prohibition, the duties on those who deal in money, supervision, sanctions, procedure, final provisions) | out-of-scope | This row does not encode the Law. Encoding a section means encoding what it makes an offence or a duty, which needs its own brief, its own seat questions and its own tests; none of that is attempted here. |
| The other Schedules of the Law | out-of-scope | The two findings sit in the First Schedule alone; nothing is recorded about the others. |
| The Infiltration Law itself, beyond the lapse markers of sections 7ב and 7ג | out-of-scope | Only what bears on item (18ו) is deposited: the two lapse markers and the page's title line. The Law's offences, procedure and other temporary provisions are not read. |

## Fork register

D1. The day the period of section 1(1) of the 2013 temporary law ended is NOT established.
Reading taken: `the named text is in force on` answers NOTHING on every day.
Reading rejected: about 10 December 2021, which holds only if the 2020 law started on its publication day; the page of that law has four sections and none on commencement, and nothing else about its start was read.
The Hebrew that licenses the answer is the quotation of section 2 of Sefer HaChukim 2876, p. 136, in `ml52-cross-references.l4`.

D2. Whether the lapse of sections 7ב and 7ג, which the consolidation prints, is the lapse of the text item (18ו) names.
Reading taken: the consolidation's marker is recorded as CONSOLIDATION-ONLY and limb (a) of finding 2 says `the consolidation only`.
Reading rejected: treating the marker as an official finding; no official instrument that ended the period was read.
The licence is the two `ext:[infil]` lines in `ml52-cross-references.l4`, whose Hebrew word is "פקע".

D3. Whether section 1(1) of the 2013 law falls under the opening words of its section 1, which Sefer HaChukim 2876 p. 136 amends.
Reading taken: it does, as an INFERENCE from the amendment's wording ("in section 1, in the opening words"); the 2013 law's own page (Sefer HaChukim 5773 p. 78, as the footnotes of Kovetz HaTakanot 7721 p. 38 and Sefer HaChukim 2876 p. 136 cite it) was not read.
Reading rejected: that the amendment leaves section 1(1) with its old period.
The words that license the inference are on the `ext:[SH 2876 p.136 ...]` line in `ml52-cross-references.l4` that quotes section 2 ("in section 1, in the opening words" in the order they stand there).

P1. How the order's period of two years is counted.
Reading taken: the row does not make the count; it records 8 June 2028 as the first day the order's items COULD be over, a lower bound that is ASSUMED, not ruled (two years from 9 June 2026 end on 8 or 9 June 2028 by either usual count), and answers NOTHING from that day.
Reading rejected: an exact last day, because the order's start is not in the instrument (P2).
The Hebrew that licenses "two years" is the order's operative sentence, quoted in `ml52-cross-references.l4`.

P2. The day the order started.
Reading taken: 9 June 2026, the Wikisource editor's reading in the notes on lines 733 and 736 of the page (CONSOLIDATION-ONLY); the order's page has one operative section and no section on commencement.
Reading rejected: the signing day, 8 June 2026, and any later day; none is in the instrument.
The collision recorded for 1 March 2028 does not depend on the start day unless the order started after that day.

P3. The first day of the item added by section 27 of Sefer HaChukim 3571.
Reading taken: 27 January 2028, which is 18 months after the issue's date, 27 July 2026, as section 28(א) says and as the consolidation's note on line 730 agrees (CONSOLIDATION-ONLY for the note).
Reading rejected: a later day under section 28(ב), which lets a Minister postpone the start by order, with a Knesset committee's approval, by up to a year; NO postponement order was looked for, so the day is the day as enacted and is not known to be the day it started.
No Hebrew from sections 27 and 28 is quoted beyond the insertion words and the label on the `ext:[SH 3571 p.985 ...]` lines, deliberately: the two sections are paraphrased from the page image, and this row does not quote or discuss the added item's text.

P4. Whether two items printed (18ט) is a defect or a numbering the Schedule will later correct.
Reading taken: the printed labels collide on every day when all three items are certainly read, and that is the defect recorded; the row does not say how it should be corrected.
Reading rejected: ruling on the intended numbering; the consolidation's note on line 733 ("ספרור שגוי במקור") is the editor's note and is recorded as such.

## Answer table

| | Finding 1: numbering | Finding 2: citation | Control 1 | Control 2 |
| --- | --- | --- | --- | --- |
| What the citing words say | The order: for two years, after item (18ח) come items (18ט) and (18י). The Act: after item (18ח) comes a further item, printed (18ט). | Item (18ו) cites section 7ג(ב) of the Infiltration Law, as brought in by section 1(1) of the 2013 temporary law. | The order's two items are (18ט) and (18י). | The order of 2016 puts item (18ו) after item (18ה). |
| What the target says | Three items, two printed (18ט), are read on any day from 27 January 2028 as enacted, until the order's items could be over. | The consolidation prints sections 7ב and 7ג as lapsed. Sefer HaChukim 2876 p. 136 cut the period to one year from the commencement of the 2020 law. | The labels differ. | The consolidation prints (18ו) directly after (18ה). |
| Exists | Yes, as printed labels. | Not established by an official instrument; the consolidation prints a lapse marker. | Yes. | Yes (consolidation). |
| Limb (a) | Day of the Act's item: official page read, no postponement order looked for. Order's start day: the editor's reading, CONSOLIDATION-ONLY. | CONSOLIDATION-ONLY (the lapse); the cut of the period is read from the page image. | n/a | CONSOLIDATION-ONLY |
| Limb (b) | Official page read; that no later instrument touched the labels is CONSOLIDATION-ONLY. | Item as made read from the page image of Kovetz HaTakanot 7721 p. 38; the consolidation lists amending instruments of 5773 and 5774 that were not read. | n/a | As made, read from the page image; later instruments not read. |
| Page read | Kovetz HaTakanot 12422 p. 2196א (and cover); Sefer HaChukim 3571 p. 985 | Kovetz HaTakanot 7721 p. 38; Sefer HaChukim 2876 p. 136 (and cover) | as finding 1 | Kovetz HaTakanot 7721 p. 38 |

The four covers: Kovetz HaTakanot 12422 and Sefer HaChukim 2876 were read from the page image; Kovetz HaTakanot 7721 and Sefer HaChukim 3571 were read from the text layer only, and their cover images were not looked at (the issue date of Sefer HaChukim 3571 also stands in the footer of p. 985, in the deposited cropped image).
The dates on them were run through the Hebrew-calendar routine, which reproduced 30 Kislev 5785 = 31 December 2024 first: 23 Sivan 5786 = 8 June 2026, 24 Sivan 5786 = 9 June 2026, 23 Kislev 5781 = 9 December 2020, 24 Kislev 5781 = 10 December 2020, 13 Av 5786 = 27 July 2026, 24 Elul 5776 = 27 September 2016, 28 Tishrei 5777 = 30 October 2016.

## The two expected-red findings, assertion by assertion

`ml52-tests-xrefs-red.l4` holds four assertions, all failing, and `check.sh` and `encoding.json` declare that count (4).
1. `the labels are distinct on` 1 March 2028 is FALSE, because the label (18ט) names two items that are certainly read.
2. The number of recorded items bearing (18ט) and certainly read on 1 March 2028 is 2, not 1.
3. `the citation points at what it says` for item (18ו) is FALSE: the citing words describe the section as in force, and the target as the consolidation prints it is lapsed.
4. `the named text is in force on` 10 November 2026 is NOTHING, not JUST TRUE, because the end of the period was not established.

## The check

Run from this folder with `L4=~/.local/bin/l4 ./check.sh`; the main build was 1.6.109 (main, 4c887e0, 2026-11-04).

| module | errors | satisfied | failed | refused | expected failed | main: errors | satisfied | failed | refused | main verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ml52-cross-references.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| ml52-nouns.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| ml52-tests-xrefs-red.l4 | 4 | 0 | 4 | 0 | 4 | 4 | 0 | 4 | 0 | same |
| ml52-tests-xrefs.l4 | 0 | 35 | 0 | 0 | 0 | 0 | 35 | 0 | 0 | same |

The four errors are the four failed assertions; no other error, and no refusal.
`tools/hebcheck-all.sh *.l4 NOTES.md` exits 0, and `python3 -I tools/pdfcheck.py *.l4` reports 19 quotation lines checked, 4 skipped (the Sefer HaChukim 3571 lines, whose file is not deposited) and no problem; with `SH3571_PDF` naming that file as downloaded it checks all 23 with no problem.

## The deposits (UNOFFICIAL aids, both)

Hebrew Wikisource consolidation of the Law, revision 3088216 (last edited 2026-10-12T09:00:17Z): the whole page has sha256 ae7ed4166671908c9cf27eaabef098e8d2112cba4854d4715e741d65210af086 and 173044 bytes as retrieved on 2026-11-10; the excerpt deposited has sha256 a90ef078c1b392cd97197ebb08d9bb2ed3566baa059755d61c8291a421dae786 and 2254 bytes.
Hebrew Wikisource consolidation of the Infiltration Law, revision 2884065 (last edited 2024-09-23T14:40:05Z): the whole page has sha256 d75a01d1911d411f52c6033de4e1c451411a70ad65dae5e3d067462fa3933772 and 17459 bytes as retrieved on 2026-11-10; the excerpt deposited has sha256 e88ff995df59e1fa078d6326eb194259712ed2f49027272c05baed6652aa37c4 and 1120 bytes.
Each excerpt says in its first lines which lines of the whole page it copies, and each line carries its number in the whole page, so that `src:N` and `ext:[infil] N` mean the line N of the page.
Three lines of the Law's page (730, 733, 736) are deposited only as far as the editorial note that opens each, and the rest of each line is not deposited.
`registers/source-bundle/SOURCES.json` gives the URL, retrieval date, sha256 and size of every file, and says which pages were read from an image.
The other official PDFs and page images are in `registers/source-bundle/amending-laws/` and `registers/source-bundle/official/`.
Sefer HaChukim 3571 is NOT deposited: its file holds the whole amendment of another Law, outside this row's scope, and `SOURCES.json` records its URL, sha256 and size as downloaded.
What this row reads of its p. 985 is in `amending-laws/sh3571-5786-p985-cropped.png`, five bands separated by grey bars: the opening line of section 27, the label (18ט) alone, the opening line of section 28(א), section 28(ב), and the page's footer line with the issue date.
What lies between the bands is not part of this row.

## What was not done

The 2013 temporary law's own page (Sefer HaChukim 5773 p. 78) was not read.
The day the 2020 law started, and so the day the period ended, was not established.
No order postponing the item added by section 27 of Sefer HaChukim 3571 was looked for.
The 5773 and 5774 instruments that the consolidation lists for item (18ו) were not read.
The covers of Kovetz HaTakanot 7721 and Sefer HaChukim 3571 were read from the text layer, not from an image.
The text of the item added by section 27 and paragraphs (1) and (2) of section 28(א) were seen on the page but are left out of the deposited image and are no part of this row; (1) and (2) name provisions other than section 27.
