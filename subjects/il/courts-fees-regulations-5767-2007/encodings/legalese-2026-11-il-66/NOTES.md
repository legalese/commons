# Row il-66: four items about the Courts (Fees) Regulations, 5767-2007, recorded as typed values with their tests

Status: draft, version 0.1.0, 2026-11-10, target compiler main.
How each claim was checked: every quotation of an official instrument was typed from a page image that was looked at, in the 15 deposited crops of 8 issues of Kovetz HaTakanot, and the crops of printed pages 400, 401, 900, 470, 1565 and 1720, which carry the figures and the section numbers the tests depend on, were looked at a second time after the quotations were typed, line against line.
Each Hebrew or numeric word of the 102 quotation lines was then searched in the text layer of its page of the whole issue by an ad hoc search made on 2026-11-10 (the pages' text layers store the Hebrew letters and the digits in reverse order, so each word was searched in both orders, with quotation marks and brackets removed).
Of the 610 words, 553 were found as whole words of the page's text layer and 57 were not found.
47 of the 57 are tokens of the 15 footer lines, whose text layer carries the issue's name in a form the search does not match, so those words were read from the images only.
The other 10 are the numbers glued to letters or brackets in the text layer (`214יא` on printed page 720, `180(ג)` on 470, `83(3)` on 900), the prefix letter ו and the numbers 360 and 109 that follow it across a maqaf (`ו־360` on 470, `ו־109` on 900), the item numbers 8 and 22 on printed pages 400 and 401, and one word of the title of item 8 (printed page 400); each was read from the image.
No quotation line was skipped; the English notes inside the quotation lines were removed before the search.
The text layer of printed page 461 is out of order, so its lines were read from the image alone.
The text layer of the page of KT 9099 that carries item 36 does not carry the amount of its row in a form the search finds, so that amount was read from the image alone.
The search is not a tool in `tools/`: no PDF is deposited, so no `pdfcheck.py` is shipped, and the search ran against the whole issues, which are not deposited.
Every quotation of a consolidation is expanded by `tools/srcquote.py` from the deposited excerpts, not typed.
A marker carries the revision id, `--@SRC 2996639:75`, because three pages are deposited and their line numbers collide; `tools/srcquote.py` and `tools/hebcheck.py` are the versions made for that (see "The check").
A statement that names "the source notes" comes from notes made while these instruments were searched for; those notes are not deposited, and each such statement says what the builder of this row read itself.
Quoted lines that rest only on a consolidation are CONSOLIDATION-ONLY unless they are read from an official page, and each says which.
No domain expert has read this against the source.

## Scope

This row is NOT an encoding of the Courts (Fees) Regulations, 5767-2007, called "the Fees Regulations" here.
It records four things, as typed values with tests, and keeps each as expected-red tests; the files label them I1, I2, I3 and I4.
"KT" is Kovetz HaTakanot, the regulations series of Reshumot: every number after "KT" is an issue number, not a year.
Every Hebrew-letter number in a title, a tag or a date line (the 5767 of the Fees Regulations, the 5744 of the Courts Law, the 5778 of a tag) is a Hebrew year, and every other number given as a page is the number printed in the issue's footer.
No citation of the form "Sefer HaChukim 5735" occurs in this row.
I1 is a cross-reference: the definition of a pre-trial session in regulation 1 of the Fees Regulations, as made, names rule 143 of the Civil Procedure Regulations, 5744-1984 and rule 214 with a letter (214יא) of the same Regulations; the amending regulations in KT 8085 (11 October 2018) cancel regulations 1 to 131(ב), 132 to 258 and 360 to 532 of the 1984 Regulations, and their section 3 keeps the earlier regulations for proceedings opened before the commencement day of the new Regulations, unless the new Regulations apply to them under regulation 180(ג).
I2 is a citation of a subsection: the opening words of the 2021 amendment (KT 9735) cite their power as sections 83(3) and 109 of the Courts Law, and the consolidation of the Courts Law prints section 83 with the subsection labels (א) and (ב), and prints the fees in paragraph (3) of (א).
I3 is a figure printed twice: the annual notice KT 7199 prints one figure beside the word that opens the threshold in item 8 and another in item 22.
I4 is an order of dates: item 36 was added to the Schedule by regulation 4(3) of the 2017 temporary regulations (KT 7857); the suspension in KT 9089 was signed 11 January 2021 and published 12 January 2021 and treats paragraph (3) of regulation 4 as cancelled until 20 July 2021; the notice KT 9099 was signed 21 December 2020, was published 17 January 2021, and prints an amount beside item 36.
Each item has a sound control beside it, except I3, which has none (F9).
The row states what each instrument prints and what the row records; it does not say that the Fees Regulations, the Law or anyone is wrong, it does not say what a court would do, and it does not say who gains.
The row names no person who signed.
It states no commencement day of the new Civil Procedure Regulations as a fact about today's law: it records the day printed on the page as made and the day the consolidation prints today, side by side, each labelled (F4).
The row reads no annual notice later than KT 9099.
There is no REFUSE, because the target is main.

## Seat

The seat is a litigant in a civil proceeding who is charged a fee under the Fees Regulations.
This row asks no question from the seat, because it records four items, not a rule.

## Coverage

This row does not encode the Fees Regulations, so almost all of it is out of scope; the table says why for each part.

| Part | Status | Reason |
| --- | --- | --- |
| Regulation 1 of the Fees Regulations as made (title, heading, the definitions of a pre-trial session and of the 1984 Regulations), KT 6579 printed page 720, and lines 2, 16, 22 and 30 of the consolidation | encoded | I1, the citing words. The page is read from its image; the consolidation's lines are CONSOLIDATION-ONLY. |
| Regulation 5(ב)(2) and the first line of regulation 6(ב) as made, KT 6579 printed pages 722 and 723, and lines 71, 73, 75, 90 and 94 of the consolidation | encoded | I1, the places where the defined term is used. The pages are read from their images; the consolidation's lines are CONSOLIDATION-ONLY for the text now in force. |
| Sections 1 to 3 of the amending regulations, KT 8085 printed page 470 | encoded | I1, the ranges cancelled and the saving clause. Read from the official page. |
| Regulation 180(ג) of the new Regulations, KT 8085 printed page 461, and lines 1224 and 1227 of the consolidation | encoded | I1, the commencement day, as two labelled readings. |
| Rule 143 of the new Regulations, KT 8085 printed page 452 | encoded | I1, what the new Regulations print at that number. |
| The opening words of KT 9735 (printed page 900) and of KT 7980 (printed page 1748), and section 83 of the Courts Law (lines 946 to 956 of the consolidation) | encoded | I2 and its control. The pages are read from their images; section 83 is CONSOLIDATION-ONLY. |
| Items 8 and 22 of the annual notice KT 7199, printed pages 400 and 401 | encoded | I3. Read from the official pages. |
| Regulation 1 and regulation 4(3) of KT 7857 (printed pages 1718 and 1720), the whole operative part of KT 9089 (printed page 1524), and the title and item 36 of KT 9099 (printed pages 1562 and 1565) | encoded | I4. Read from the official pages. |
| Every other provision of the Fees Regulations, every other item of the Schedule, and every other instrument | out-of-scope | This row records four items and does not encode the Fees Regulations. Encoding a provision means encoding what it entitles a person to ask or obliges a person to do, which needs its own scope, seat questions and tests; none of that is attempted here, and nothing is said about any other provision. |

## Fork register

F1 (I1). What the definition cites.
Reading taken: the page of KT 6579 printed 720 defines ”ישיבת קדם משפט“ as a pre-trial session as meant in rule 143 of the Civil Procedure Regulations or a preliminary session as meant in rule 214יא of the Civil Procedure Regulations, other than a reminder session, and defines ”תקנות סדר הדין האזרחי“ as the Civil Procedure Regulations, 5744-1984.
The consolidation prints the same words at lines 22 and 30; the two definitions read the same on the page and in the consolidation.
The row compares rule 214יא by its base number 214, because the letters after a number are not a number; that is a choice of the row, not a reading of the Regulations.
Reading rejected: that the consolidation shows the definitions as made by itself; only the page does.

F2 (I1). The ranges.
Reading taken: section 2 of the amending regulations prints three ranges, 1 to 131(ב), 132 to 258 and 360 to 532; the row compares whole numbers only, so the range that ends at 131(ב) is recorded as ending at 131.
Rule 143 and rule 214 each lie inside exactly one range, 132 to 258, by that arithmetic.
Reading rejected: that the row says what it means for a rule number to be cancelled, or which rule of the 1984 Regulations 143 or 214יא is; the 1984 Regulations are not deposited and were not read.

F3 (I1). The saving clause.
Reading taken: section 3 says the earlier regulations continue to apply to proceedings opened before the commencement day of the new Regulations, as worded on the evening before that day, if the new Regulations do not apply to them under regulation 180(ג) of the new Regulations.
The row records two flags: that the earlier regulations continue for proceedings opened before the commencement day, and that the continuation is qualified by a rule of the new Regulations.
The row does not say whether any proceeding is within it.

F4 (I1). The commencement day of the new Regulations.
Two readings, each labelled: as made, read from the page: regulation 180(ג) of KT 8085 (printed page 461) prints 5 Elul 5779 (5 September 2019); as the consolidation prints it today: line 1227 of revision 3087840 prints 17 Tevet 5781 (1 January 2021).
Each printed Gregorian date is the day the Hebrew-calendar routine gives for the printed Hebrew date (table below).
The instruments between the two were NOT read.
The first 40 lines of the fetched consolidation page list these KT numbers: 8085, 8120, 8213, 8225, 8229, 8285, 8669, 8989, 8992 and 9040; that is what the page shows, and no instrument of the list was read by this row.
The tag on the heading of regulation 180 names the years "תש״ף", "תשפ״א" and "תשפ״ב" among others (Hebrew years, not issue numbers); the row states no commencement day for today's law.

F5 (I1). Rule 143 of the new Regulations.
Reading taken: the page of KT 8085 printed 452 prints rule 143 with a margin note that the row gives in English as "joining of appeals", and the rule says that regulation 40 applies to an appeal, with the changes the case needs.
The row records what the new Regulations print at that number and does not compare it with rule 143 of the 1984 Regulations.

F6 (I1). The places where the term is used.
Reading taken: the page of KT 6579 printed 722 prints, in regulation 5(ב)(2), an exemption of a litigant from the unpaid part of the fee when one of the listed things happens before the third pre-trial session in the proceeding has ended (the page's ordinal term is the one the consolidation prints); the page printed 723 prints, in regulation 6(ב), the first line of a subsection that opens with a proceeding that ends before the third pre-trial session has ended.
The consolidation prints the same words at lines 75 and 94 (CONSOLIDATION-ONLY for the text now in force); the rest of regulation 6(ב) is not deposited and was not read from the page.
The tag on the heading of regulation 1 (line 16) lists the Hebrew year תשע״ח only, so it names no instrument after KT 7980 (2018); that is a limit of what the consolidation lists, not a finding.

F7 (I2). What the citing words say and what the target prints.
Reading taken: the first line of the opening words of KT 9735 (printed page 900), quoted in the `ext:` lines of `cf66-cross-references.l4`, cites sections 83(3) and 109 of the Courts Law, so the citation gives the section number 83 and the subsection as "3", with no letter.
The consolidation of the Courts Law prints section 83 with subsection (א), which has paragraphs (1) to (4) and editorial notes between them, and subsection (ב), which refers to "סעיף קטן (א)(3)"; the labels the row lists, (א) and (ב), are typed from lines 947 and 956.
The second line of the opening words is not in the crop and was not read for this row.
The row says only what the page prints and what the consolidation prints; it does not say that the power is missing or that the amendment is invalid.
The official text of the Courts Law was not read, so the target is CONSOLIDATION-ONLY.
The title of the Courts Law's page in the Wikisource API is "חוק בתי המשפט": the source notes give it with the words for the consolidated version, in square brackets, added, and the API refuses square brackets in a title, so the page was fetched without them. The first call, made with the bracketed title, was rejected by the API as an invalid title (a 195-byte reply with no content); the excerpt comes from the one call made without the brackets, so four API calls were made in all (three that returned content and the one rejected).

F8 (I2 control). A citation without a subsection.
Reading taken: the first line of the opening words of KT 7980 (printed page 1748) cites sections 83 and 109 of the Courts Law with no subsection, and the consolidation prints a section 83, so the control resolves.
The control checks that a section 83 is printed; it does not check what its text says.

F9 (I3). The two figures.
Reading taken: the figure beside the word that opens the threshold is 23,800,859 in item 8 (printed page 400) and 23,880,859 in item 22 (printed page 401), read from the images; the text layers of both pages carry the same digits (each digit string occurs once on its page).
The difference is 80,000; the rates printed in both items are 2.5 and 1, in percent.
The cropped lines hold no other pair of items that print one threshold twice, so the row has no control of that kind; the equal rates are the sound comparison beside the unequal figure.
The row does not say which figure is intended and does not state a fee effect.

F10 (I4). The dates.
The pages print: the notice KT 9099 signed 6 Tevet 5781 (21 December 2020) and published 17 January 2021 (the footer's date); the suspension KT 9089 signed 27 Tevet 5781 (11 January 2021) and published 12 January 2021 (the footer's date), for the period up to 11 Av 5781 (20 July 2021).
The suspension prints no first day for the period; the row takes the day of its publication, 12 January 2021, as its own confinement.
The row states that the notice's publication day falls inside that period and that the notice prints an amount beside item 36, and says nothing about whether any registry charged the fee, who gains, or what happened to the 2017 regulations before or after the period.
That the item is the item that regulation 4(3) of the 2017 regulations adds rests on both pages printing the same item number and the same words ("a written motion in a civil proceeding") at item 36.
The crop of KT 9099 holds no column heading, so the amount printed at the left end of the row of item 36 (36) is recorded as a number with no unit; the page of KT 7857 prints its amount (35) under the heading "fee in new shekels".
The title line of KT 7857 on the page prints no "(No. 2)", which the source notes add to the name of the instrument; the row uses the page's title.

F11. The pages of the issues.
Printed page = PDF page + 718 for KT 6579, + 392 for KT 7199, + 1716 for KT 7857, + 420 for KT 8085, + 898 for KT 9735 and + 1558 for KT 9099; KT 7980 (printed 1748) and KT 9089 (printed 1524) are PDF page 2.
The builder confirmed each mapping by rendering the page and reading its footer.
The title of the notice KT 9099 is on PDF page 4 (printed 1562) and item 36 is on PDF page 7 (printed 1565), so the notice has two crops.

F12. The date lines in the crops.
The footer line of every crop and the signature date line of KT 8085 print a Hebrew and a Gregorian date; they are quoted as printed, and the row does not compute them or use them.
The Hebrew-calendar routine was run for the six pairs the row uses (table below).

F13. The fields in `cf66-nouns.l4`.
Reading taken: the names of the fields are mine, written from the words quoted; every field name is unique across the records, because two records with one field name make the compiler report "multiple definitions".
Reading rejected: using the Regulations' own words as field names, because the Regulations do not describe their provisions by kind.

## Answer table

| | I1 | I2 | I3 | I4 |
| --- | --- | --- | --- | --- |
| What the citing words or the page say | The definition cites rules 143 and 214יא of the 1984 Regulations; section 2 cancels 1 to 131(ב), 132 to 258 and 360 to 532. | The opening words cite sections 83(3) and 109 of the Courts Law. | Item 8 prints 23,800,859 and item 22 prints 23,880,859 beside the word that opens the threshold. | The notice, signed 21 December 2020 and published 17 January 2021, prints 36 beside item 36. |
| What the target prints | Rules 143 and 214 each lie inside the range 132 to 258; section 3 keeps the earlier regulations for earlier proceedings, qualified by regulation 180(ג). | Section 83 has the subsection labels (א) and (ב) and no subsection printed under "3". | Two items, two figures, 80,000 apart; equal rates. | The suspension, signed 11 January 2021 and published 12 January 2021, treats paragraph (3) of regulation 4 as cancelled up to 20 July 2021. |
| Limb read from a page | KT 6579, KT 8085. | KT 9735, KT 7980. | KT 7199. | KT 7857, KT 9089, KT 9099. |
| Limb read from a consolidation only | The commencement day as printed today (line 1227); the text of regulations 1, 5(ב)(2) and 6(ב) now in force. | Section 83 of the Courts Law (lines 946 to 956). | None. | None. |
| Limit | F2, F4. | F7. | F9. | F10. |
| Control | The saving clause says the earlier regulations continue for proceedings opened before the commencement day; each cited number lies outside the other two ranges. | KT 7980 cites section 83 with no subsection and resolves. | The two rates agree. | The notice was signed before the suspension was signed. |

## The six expected-red assertions, one by one

`cf66-tests-xrefs-red.l4` holds six assertions, all failing, and `check.sh` and `encoding.json` declare that count (6).
1. `the rule cited lies outside every one of the ranges` for rule 143 is FALSE: 143 lies inside 1 of the 3 ranges, 132 to 258.
2. The same for rule 214 (the base number of 214יא) is FALSE: 214 lies inside the same range.
3. `the consolidation prints a subsection under the label the citing words give` for KT 9735 is FALSE: it prints 0 subsections under "3" (it prints the labels (א) and (ב)).
4. `the citation resolves to what the consolidation prints` for KT 9735 is FALSE, for the same reason.
5. `the two items print the same figure` for items 8 and 22 is FALSE: 23,800,859 against 23,880,859.
6. `the notice prints no amount for an item treated as cancelled on its publication day` is FALSE: the notice prints 36 beside item 36, and its publication day, 17 January 2021, is inside the period 12 January to 20 July 2021.

## The Hebrew-calendar routine

Month numbers: Nisan 1, Av 5, Elul 6, Tishri 7, Kislev 9, Tevet 10; the routine is the one of Calendrical Calculations, run on 2026-11-10 as a scratch script that is not shipped.

| Hebrew date | Where printed | Routine gives | Printed Gregorian date |
| --- | --- | --- | --- |
| 30 Kislev 5785 (control) | none | 2024-12-31 | 2024-12-31 |
| 5 Elul 5779 | KT 8085 printed page 461 | 2019-09-05 | 5 September 2019 |
| 17 Tevet 5781 | consolidation, line 1227 | 2021-01-01 | 1 January 2021 |
| 6 Tevet 5781 | KT 9099 printed page 1565 | 2020-12-21 | 21 December 2020 |
| 27 Tevet 5781 | KT 9089 printed page 1524 | 2021-01-11 | 11 January 2021 |
| 11 Av 5781 | KT 9089 printed page 1524 | 2021-07-20 | 20 July 2021 |

All six agree, and so does the control.

## The check

Run from this folder with `L4=$HOME/.cache/l4-main/98/l4 ./check.sh`; the `l4` that wrote the row was 1.6.98 (main, 7689b0d, 2026-10-19) and the main build it was compared with was 1.6.109 (main, 4c887e0, 2026-11-04).

| module | errors | satisfied | failed | refused | expected failed | main: errors | satisfied | failed | refused | main verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf66-cross-references.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| cf66-nouns.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| cf66-tests-xrefs-red.l4 | 6 | 0 | 6 | 0 | 6 | 6 | 0 | 6 | 0 | same |
| cf66-tests-xrefs.l4 | 0 | 73 | 0 | 0 | 0 | 0 | 73 | 0 | 0 | same |

The six errors are the six failed assertions, each reading "assertion failed", in the red module; no other error, and no refusal.
Positive control: in a scratch copy, the figure of item 22 was changed to the figure of item 8 and the subsection cited by KT 9735 to the label (א); the three red assertions of I2 and I3 then passed (3 of 6 failed) while seven sound assertions turned red; the copy was deleted.
`tools/srcquote.py` and `tools/hebcheck.py` are copied from row il-65, unchanged (the changes are said in each file's first lines): a marker or `src:` line carries the revision id, one run of `srcquote.py` expands only the markers of the excerpt it is given, and `hebcheck.py` takes every argument ending in `.excerpt.txt` as a source.
`python3 -I tools/hebcheck.py ../../registers/source-bundle/*.excerpt.txt *.l4 NOTES.md` exits 0: every run of Hebrew outside a quotation line occurs in the deposited excerpts.
Positive control for it: a scratch copy with an absent run of Hebrew added made it print NOT IN SOURCE for that run.
It is a substring test, so a short run (a one- or two-letter label) is found inside longer words and the check cannot tell a mistyped label from a correct one.

## The deposits

UNOFFICIAL aids: three excerpts of Hebrew Wikisource consolidations, each of whole lines only, each carrying its line numbers in the whole page, so that `src:2996639:75` means line 75 of revision 2996639; each was fetched on 2026-11-10 by one API call for the then-current revision, and the revision is pinned by its id.
- `court-fees-regulations-rev2996639.he.wiki.excerpt.txt`: the Fees Regulations, revision 2996639 (last edited 2026-03-09T10:30:27Z), lines 2, 16, 22, 30, 71, 73, 75, 90, 94. The whole page content has sha256 1b431d99a934d48652a962618973e042a7df7c491de5292154b96185ad64ec7d and 83128 bytes (455 newline-terminated lines, and a last line with no newline after it); the excerpt has sha256 482649fb4b4d5b08f431142d51ee346709b621791e49097739c491d28a9a3dcd and 2977 bytes.
- `civil-procedure-regulations-2018-rev3087840.he.wiki.excerpt.txt`: the 2018 Civil Procedure Regulations, revision 3087840 (last edited 2026-10-09T07:02:12Z), lines 1224 and 1227. The whole page content has sha256 96929228c7572f930889c9d25588d78585baf5272e611979f45c45f97cfaf3e3 and 246205 bytes (1390 newline-terminated lines, and a last line with no newline after it); the excerpt has sha256 c48aa2f8adfee700cbd6ed2b3ac382d0179d5110f5c0b147b8b0be07cdbad478 and 1939 bytes.
- `courts-law-rev3082576.he.wiki.excerpt.txt`: the Courts Law, revision 3082576 (last edited 2026-09-11T05:30:22Z), lines 946 to 956. The whole page content has sha256 68ba35c5ff5f5d714a49373e6d78372c9a8dacd8e7b3a25169a65250170a204a and 286662 bytes (1500 newline-terminated lines, and a last line with no newline after it); the excerpt has sha256 cf82b832cb4fc00d7f605025dbd3db74b2ac502384e5a6f792ddba6f904163a7 and 2712 bytes.

Official pages, in `registers/source-bundle/official/`, each a crop composed of bands separated by grey bars, each viewed before it was deposited; a sliver of the issue's header logo shows under the footer of some of them:
- `kt6579-5767-p720-bands.png`, Kovetz HaTakanot 6579, printed page 720 (PDF page 2), 61724 bytes, sha256 76b46373135b58bce99fb19175d6ccd58f2401d8f7f0d2409e15583ac5daf838: the title, the heading of regulation 1, the definition of a pre-trial session, the definition of the 1984 Regulations, and the footer line.
- `kt6579-5767-p722-bands.png`, Kovetz HaTakanot 6579, printed page 722 (PDF page 4), 42410 bytes, sha256 d4147453bdff135782c2a4c59d990d9d7a07b8436efe829c5c92e958a663d0bf: the number of regulation 5, the line that opens its subsection (ב), paragraph (2) of that subsection, and the footer line.
- `kt6579-5767-p723-bands.png`, Kovetz HaTakanot 6579, printed page 723 (PDF page 5), 21839 bytes, sha256 f86545b43cfb8f1533f5e5151d2306e77643584b2fabc54ae0a7b7bb2a5e7e7b: the number of regulation 6, the first line only of its subsection (ב), and the footer line.
- `kt8085-5779-p452-bands.png`, Kovetz HaTakanot 8085, printed page 452 (PDF page 32), 8881 bytes, sha256 0f9f8968bb745ff9d6385130ac33252142b43079cad5804c0a85de0fe8db53cd: rule 143 with its margin note, and the footer line.
- `kt8085-5779-p461-bands.png`, Kovetz HaTakanot 8085, printed page 461 (PDF page 41), 19248 bytes, sha256 dbf0cb62a2d19496268a828785587e4450ffa307aa9a9fa6b812da8937e4210f: the number and margin note of regulation 180, the three lines that open its paragraph (ג), and the footer line.
- `kt8085-5779-p470-bands.png`, Kovetz HaTakanot 8085, printed page 470 (PDF page 50), 50004 bytes, sha256 00ff17b169c5cb0708954b5a995acb5089f97d3408b8901abb24759bbc3f446d: the title, sections 1 to 3 with their margin notes, the signature date line, and the footer line.
- `kt7980-5778-p1748-bands.png`, Kovetz HaTakanot 7980, printed page 1748 (PDF page 2), 14390 bytes, sha256 b6ecf60ba7a1ba84fb4987096d9583702637b1f95a842433ea188173d5804f45: the title, the first line of the opening words, and the footer line.
- `kt9735-5782-p900-bands.png`, Kovetz HaTakanot 9735, printed page 900 (PDF page 2), 34404 bytes, sha256 01dad57260339b0f452a51cd3466b7653828b046f6e4e7791d9d95087bcf944b: the title, the first line of the opening words, and the footer line.
- `kt7199-5773-p400-bands.png`, Kovetz HaTakanot 7199, printed page 400 (PDF page 8), 14935 bytes, sha256 4ba5b87763f55fbffa5ea92c9f992cc482f5ce866faf78bb833e3e0e67cb95e5: item 8 with its amount lines and threshold line, and the footer line.
- `kt7199-5773-p401-bands.png`, Kovetz HaTakanot 7199, printed page 401 (PDF page 9), 14685 bytes, sha256 c75c281a4064ef82d2b7216e9f7375f304b4e99485b7ff179bd0657d7c4473d1: item 22 with its amount lines and threshold line, and the footer line.
- `kt7857-5777-p1718-bands.png`, Kovetz HaTakanot 7857, printed page 1718 (PDF page 2), 35957 bytes, sha256 5f9848f53c940f40bc5ea2a874a4096fa6033b69ddf92c6607542135ee24ad2c: the title, regulation 1, and the footer line.
- `kt7857-5777-p1720-bands.png`, Kovetz HaTakanot 7857, printed page 1720 (PDF page 4), 14386 bytes, sha256 5b1ff842a3cb7145443ecbe072a7829b19f24338272c0a132d8d0696f692dcd2: the heading of regulation 4, its paragraph (3) with the item it adds, and the footer line.
- `kt9089-5781-p1524-bands.png`, Kovetz HaTakanot 9089, printed page 1524 (PDF page 2), 98800 bytes, sha256 0bf8ef1c42c8b74ce56bf8385a4c4f0ba5c9ba30bf3be25bd9167d9a87fc213f: the title, the opening words, section 1 with its two paragraphs, the signature date line, and the footer line.
- `kt9099-5781-p1562-bands.png`, Kovetz HaTakanot 9099, printed page 1562 (PDF page 4), 20846 bytes, sha256 965bdbc3ffcf4bf9e17131d418ad246e34b200a12332bd534e3773a6c65cc0c5: the title of the notice, and the footer line.
- `kt9099-5781-p1565-bands.png`, Kovetz HaTakanot 9099, printed page 1565 (PDF page 7), 23650 bytes, sha256 2662874221e398cdb5b09c55eed467c6e1a955b74ebb77f724c407580bab80b7: the row of item 36, the signature date line, and the footer line.

Only the pages read are deposited, as crops, and no PDF and no full-page image of any page is deposited.
`registers/source-bundle/SOURCES.json` gives each whole issue's address (olaw.org.il, a private archive of the printed issues, not a government site), size and sha256, and each crop's and excerpt's own sha256 and size; the whole issues were supplied as local copies and the addresses were not re-fetched.
The eight whole issues are KT 6579 (16 PDF pages), 7199 (12), 7857 (4), 7980 (4), 8085 (52), 9089 (2), 9099 (12) and 9735 (4).

## What was not done

No instrument other than the eight issues named was read by the builder of this row, and the statements in F4 about the instruments between the two commencement readings are what the consolidation's header shows.
The 1984 Civil Procedure Regulations were not read, so the row says nothing about what any of their rules says.
The lines of the pages printed 720, 722, 723, 900, 1718, 1720 and 1748 other than the lines deposited were seen on the rendered pages, where they share a page with the lines read, and are not deposited; nothing of them is recorded.
Regulation 6(ב) was read to its first line only, and paragraphs of regulation 4 other than (3), and the second line of the opening words of KT 9735 and KT 7980, were not read.
The Courts Law was read only at section 83 of one revision, and its official text was not read.
No annual notice later than KT 9099 was read, and no instrument that ended or extended the 2017 temporary regulations.
The addresses of the whole issues were not re-fetched.
