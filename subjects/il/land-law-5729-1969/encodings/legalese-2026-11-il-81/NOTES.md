# Row il-81: Land Law, 5729-1969, a targeted record of four references

Status on 2026-11-11: draft, version 0.1.0, target compiler main.
No domain expert has read this against the source.
Every claim below was checked against a deposited page image or the deposited excerpt named beside it; where it rests on neither, it says so.
This row does not encode the Law.
The English title "Land Law, 5729-1969" is a working translation of the Hebrew title the Law's own first page prints; it is not an enacted title.
The later instruments the row reads print the year of that title with the letter he before it.

## 1. What this row is

The row records four references in the Land Law, 5729-1969 ("the Law"), as typed values, and tests them.
Each item has two limbs.
Limb (a): the target, read from an official instrument.
Limb (b): the citing words as they stand in the latest official instrument the row reads.
The items are labelled I1 to I4, in this order.

- I1: section 77(d) of the Law cites "section 19(b)" of the Courts Law, 1957, by its printed title.
  SH 1123 (issue dated 31.8.1984), the Courts Law [Consolidated Version], prints on printed page 218 a table headed with the words for "comparison table", with a sub-heading for the 1957 law and two columns, "new section" and "previous section".
  In the middle block of that table the row whose new-section cell is 41 has 19 in the previous-section cell; section 41(a), on printed page 205, carries the mark "[ב/19]" under its margin note.
  The page prints no key to the letter of the mark, and the row says nothing about it.
- I2: section 129 of the Law cites "section 20" of the ordinance it names by its printed title.
  NH 18, the new version of the Evidence Ordinance, prints on printed page 434 a table whose right-hand pair of columns opens with the heading for the ordinance the citing words name and whose left-hand pair continues it (that the left-hand pair continues the right-hand pair is positional); the left-hand pair prints 29 against two previous cells, (2)18 and 20.
  Printed page 425 prints section 29 with the margin note "הגדרות", and a footnote on printed page 421 says what the new version is in place of.
  The issue date of NH 18 is NOTHING: the pages read print none.
- I3: section 160 of the Law names siman 46 of an instrument by its printed title, and says it does not apply to land matters.
  SH 978 (issue dated 31.7.1980) prints in its section 2(a) the word "בטל" after the same words.
  Section 2(b) of SH 978 is typed as a string and is not evaluated; the commencement of SH 978 is NOTHING; a day printed in the footnote on its title is not typed.
- I4: SH 1634 (issue dated 5.8.1997) prints in its section 5 an instruction that inserts into section 72(a) a clause ending with the words "לחוק הבזק, התשמ״ב–1982".
  SH 1807 (issue dated 9.8.2001) prints in its section 1 an instruction that gives this title before the instruction and a different title after it.
  The row types the three printed instructions that wrote and edited the clause (SH 1634 section 5, SH 1807 section 97, SH 3238 section 2) as data, and the clause after each step as the concatenation of its parts, so each step is checked against its instruction without a replace function.
  The 1969 page of section 72(a) contains none of these words, and the row does not call them enacted in 1969.

The row types each instrument as Printed, and every date it takes from a footer as an issue date; it does not say what follows from the dates.
Dates the pages print for the commencement of an instrument are typed only where a commencement section was read (SH 1807 section 102); every other commencement is NOTHING.
The row says nothing about the subject of any instrument beyond its printed title, and nothing about what a court would do.
It also types sections 1 and 25 of the Interpretation Law, 5741-1981 (SH 1030, issue dated 15.6.1981, printed pages 302 and 305), as printed, as one string and as a list of words; the row does not say whether any of these provisions bears on the citing words.

Quotations, as the modules carry them (the lines are in the format of the modules' quotation lines, which `tools/hebcheck.py` skips):

I1

```text
-- ext:[sh575-p268] | (ד) פסק־הדין של בית המשפט בערעור לפי סעיף קטן (א) ניתן לערעור ברשות כאמור בסעיף 19(ב) לחוק בתי המשפט, תשי״ז–1957.
-- ext:[sh1123-p205] | 41. (א) פסק דין של בית משפט מחוזי בערכאה ראשונה ניתן לערעור לפני בית המשפט העליון.
-- ext:[sh1123-p205] | ערעור
-- ext:[sh1123-p205] | [ב/19]
-- ext:[sh1123-p218] | לוח השוואה
-- ext:[sh1123-p218] | ב. חוק בתי המשפט, התשי״ז–1957:
-- ext:[sh1123-p218] | הסעיף החדש | הסעיף הקודם
-- ext:[sh1123-p218] | right-hand block, last row: 34 | 12
-- ext:[sh1123-p218] | middle block, rows: 35 | 13 ; 40 | 18 ; 41 | 19 ; 42 | 20
```

I2

```text
-- ext:[sh575-p275] | 129. הוכח לרשם בצו של בית משפט או בתעודה ציבורית כמשמעותה בסעיף 20 לפקודת העדות, כי כשרותו המשפטית של בעל מקרקעין או של בעל זכות במקרקעין נשללה או הוגבלה על פי חוק, ירשום הרשם, לפי בקשת צד מעונין או לפי בקשת היועץ המשפטי לממשלה, הערה על כך.
-- ext:[sh575-p275] | הערה על הגבלת כשרות
-- ext:[sh575-p275] | חוקי א״י, כרך א׳, ... עמ׳ 650.
-- ext:[nh18-p421] | נוסח חדש זה בא במקום שתי אלה:
-- ext:[nh18-p421] | (1) פקודת העדות: חוקי א״י, כרך א׳, ... עמ׳ 650; ...
-- ext:[nh18-p434] | לוח השוואה
-- ext:[nh18-p434] | פקודת העדות :
-- ext:[nh18-p434] | הסעיף החדש | הסעיף הקודם
-- ext:[nh18-p434] | left pair, rows: 30 | (1)18 ; 29 | (2)18 ; 31 | 19 ; 29 | 20 ; 33 | 21
-- ext:[nh18-p425] | סימן ד׳: תעודות ציבוריות ונכריות
-- ext:[nh18-p425] | 29. בסימן זה —
-- ext:[nh18-p425] | הגדרות
-- ext:[nh18-p425] | ״תעודה ציבורית״ – תעודה של אחד הגופים המנויים להלן
```

I3

```text
-- ext:[sh575-p279] | 160. בעניני מקרקעין לא יחול סימן 46 לדבר המלך במועצתו לארץ־ישראל, 1922–1947.
-- ext:[sh575-p279] | עצמאות החוק
-- ext:[sh575-p279] | חוקי א״י, כרך ג׳, עמ׳ 2738.
-- ext:[sh978-p163] | 2. (א) סימן 46 לדבר המלך במועצתו לארץ־ישראל, 1922–1947 – בטל.
-- ext:[sh978-p163] | (ב) אין בהוראות סעיף קטן (א) כדי לפגוע במשפט שנקלט בארץ לפני תחילת חוק זה.
-- ext:[sh978-p163] | ביטול סימן 46 לדבר המלך במועצתו ושמירת דינים
-- ext:[sh978-p163] | חוקי א״י, כרך ג׳, עמ׳ 2738.
```

I4

```text
-- ext:[sh575-p268] | 72. (א) סכסוך בין בעלי דירות בבית משותף בדבר זכויותיהם או חובותיהם לפי התקנון או לפי סעיף 58, יכריע בו המפקח.
-- ext:[sh575-p268] | סמכות להכריע בסכסוכים
-- ext:[sh1634-p216] | 5. בחוק המקרקעין, התשכ״ט–1969, בסעיף 72(א), אחרי ״עד 59ו״ יבוא ״או לפי סעיף 6כט לחוק הבזק, התשמ״ב–1982״.
-- ext:[sh1634-p216] | תיקון חוק המקרקעין – מס׳ 20
-- ext:[sh1807-p560] | 97. בחוק המקרקעין, התשכ״ט–1969, בסעיף 72(א), במקום ״לפי סעיף 6כט״ יבוא ״לפי סעיפים 6נט עד 6סא, 21ב ו־27ג״.
-- ext:[sh1807-p560] | תיקון חוק המקרקעין – מס׳ 22
-- ext:[sh1807-p530] | 1. חוק הבזק, התשמ״ב–1982, ייקרא חוק התקשורת (בזק ושידורים), התשמ״ב–1982 (להלן – החוק העיקרי).
-- ext:[sh1807-p530] | החלפת שם החוק
-- ext:[sh3238-p1044] | 2. בחוק המקרקעין, התשכ״ט–1969, בסעיף 72(א), במקום ״21ב״ יבוא ״21ב, 21ד״.
-- ext:[sh3238-p1044] | תיקון חוק המקרקעין – מס׳ 38
```

The Law's title and the Interpretation Law's two sections:

```text
-- ext:[sh575-p259] | חוק המקרקעין, תשכ״ט–1969
-- ext:[sh1030-p302] | 1. תחולת החוק וסייגיה
-- ext:[sh1030-p305] | 25. פירושם של אזכורים
-- ext:[sh1030-p305] | אזכור של חיקוק בחיקוק אחר — כוונתו לחיקוק המאוזכר כנוסחו בשעה שנזקקים לו, לרבות הוראות שנוספו בו והוראות שבאו במקומו בחיקוק אחר.
```

## 2. Seat

The seat is the reader of the Law who follows one of the four references to the instrument the reference names.
The row asks that reader no question, because it records references: there is no input to ask for and no `@export`.

## 3. Source, and how each quotation was made

The working text is the Hebrew Wikisource consolidation of the Law, revision 2962167, last edited 2025-10-28T10:30:27Z (UNOFFICIAL aid).
Only an excerpt of it is deposited, `../../registers/source-bundle/land-law-5729-1969.he.wiki.excerpt.txt`: 8 whole lines of the page (the heading line of section 72 with its tag list and its subsection (a) line; the heading and (d) lines of section 77; the heading and text lines of sections 129 and 160), with a header that gives the revision id, its timestamp, the line numbers copied, the whole page's size and sha256.
The whole page is 185693 bytes and its sha256 is 9618fdac28a52679ac72d350e72521e3814f35139f1bb0b224d0e95dacc397b7; the excerpt is 3084 bytes and its sha256 is afbdd66923fedce66f99932b9cdabcfd73f45451b7b197f556429537f40a16db (the excerpt recomputed with `shasum -a 256` and `stat -f %z` on 2026-11-11).
The consolidation is unofficial, so every statement about the Law's present words that rests only on it is labelled CONSOLIDATION-ONLY.
That covers the claim, in I1, I2 and I3, that the cited words still stand: the row reads the words from the 1969 page, and the untagged heading lines of sections 77, 129 and 160 in the consolidation are the only thing the row has on whether a later instrument touched them (CONSOLIDATION-ONLY).

The official instruments are 11 files from the Knesset's site: ten issues of Sefer HaChukim (SH) and one volume of Dinei Medinat Yisrael (NH 18), which prints new versions and is not Sefer HaChukim.
Only the lines the row reads are deposited, as 26 cropped images in `../../registers/source-bundle/pages/`; no full page is deposited, and the whole files are not in the bundle.
`SOURCES.json` there gives the URL, retrieval time, sha256 and size of each whole file and of each deposit, recomputed on 2026-11-11 (39 entries, 0 differ).
No PDF is deposited.

| deposit | instrument | printed page (PDF page of the whole file) | what is on it |
| --- | --- | --- | --- |
| `sh575-p259-title.png` | SH 575, 27.7.1969 | 259 (1) | the title line of the Law, with its asterisk; the footer line |
| `sh575-p268-s72a-s77d.png` | SH 575 | 268 (10) | section 72, paragraph (a), with its margin note; paragraph (d) of section 77; the footer line |
| `sh575-p275-s129.png` | SH 575 | 275 (17) | section 129 with its margin note; the footnote line printed under it; the footer line |
| `sh575-p279-s160.png` | SH 575 | 279 (21) | section 160 with its margin note; the last footnote line; the footer line |
| `sh978-p163-s2.png` | SH 978, 31.7.1980 | 163 (1) | the title line; section 2 with its margin note and its paragraphs (a) and (b); the last footnote line; the footer line, printed below another law |
| `sh1030-p302-s1.png` | SH 1030, 15.6.1981 | 302 (1) | the title line; section 1 with its margin note; the footer line |
| `sh1030-p305-s25.png` | SH 1030 | 305 (4) | section 25 with its margin note; the footer line |
| `sh1123-p198-title.png` | SH 1123, 31.8.1984 | 198 (1) | the title line; the footer line |
| `sh1123-p205-s41.png` | SH 1123 | 205 (8) | paragraph (a) of section 41 with its margin note and the mark printed beneath it; the footer line |
| `sh1123-p218-table.png` | SH 1123 | 218 (21) | four bands: the heading of the table; the right-hand block's sub-heading, column heads and rows through new 34 against previous 12; the middle block's column heads and rows from new 35 against previous 13 to new 43 against previous 21; the footer line |
| `nh18-p421-title-fn.png` | NH 18 | 421 (1) | the title line; the asterisk footnote from its first line through item (2); the footer line (the volume and the page number; no date) |
| `nh18-p425-s29.png` | NH 18 | 425 (5) | the chapter heading; section 29 with its margin note; the entries through the first line of the one the row types; the footer line |
| `nh18-p434-table.png` | NH 18 | 434 (14) | the heading of the table; the column heads and rows of both pairs of columns through the row whose previous-section cell is 21 in the left pair; the footer line |
| `sh1634-p214-title.png` | SH 1634, 5.8.1997 | 214 (1) | the title line; the footer line |
| `sh1634-p216-s5.png` | SH 1634 | 216 (3) | section 5 with its margin note; the footer line; the signatures, which print below it, are not on it |
| `sh1807-p530-s1.png` | SH 1807, 9.8.2001 | 530 (1) | the title line and section 1 with its margin note; the footer line |
| `sh1807-p560-s97.png` | SH 1807 | 560 (31) | section 97 with its margin note; the footer line |
| `sh1807-p561-s102.png` | SH 1807 | 561 (32) | section 102, paragraphs (a) and (b), with its margin note; the footer line |
| `sh2129-p154-title.png` | SH 2129, 24.1.2008 | 154 (1) | the title (two lines); the footer line |
| `sh2129-p156-s14.png` | SH 2129 | 156 (3) | section 14 with its margin note; the footer line |
| `sh2591-p49-title.png` | SH 2591, 29.12.2016 | 49 (3) | the title (two lines); the footer line |
| `sh2591-p79-s12-3.png` | SH 2591 | 79 (33) | the heading line of section 12 with its margin note; item (3) of section 12; the footer line |
| `sh2888-cover.png` | SH 2888, 27.12.2020 | the issue cover (1) | the line with the date and the issue number; the contents line of the amending instrument, with its page number |
| `sh2888-p247-i9.png` | SH 2888 | 247 (5) | item 9 with its margin note; the footer line |
| `sh3238-cover.png` | SH 3238, 4.7.2024 | the issue cover (1) | the line with the date and the issue number; the contents line of the amending instrument; the indirect-amendment heading; the Land Law's entry |
| `sh3238-p1044-s2.png` | SH 3238 | 1044 (4) | section 2 with its margin note; the footer line; the signatures, which print below it, are not on it |

The page offsets were checked by the footer of each crop, which prints the issue number, the date and the printed page number; the covers of SH 2888 and SH 3238 print the date and the issue number, and NH 18 prints the volume and the page number and no date.
Each crop was cut afresh from a 300 dpi render of its PDF page, in whole text rows found by a row projection of the render and the text layer's word boxes, and was viewed with the Read tool after it was composed.
Crops of several bands are stacked with a grey bar between bands; the two tables are cut as narrow bands over the columns the row reads.
No crop carries a signer's name or title: each lower edge sits above any signature block, and each of the 26 crops was viewed for this.
The Knesset copy of SH 1123 begins at printed page 198 and has no cover page.
NH 18 prints no date on any page read.
The body title page of the Amendment in SH 2888 (PDF page 2) is not viewed; its title is read from the issue cover.
The row reads printed pages 214 and 216 of SH 1634 and types no commencement for its section 5.
Four whole pages were viewed beyond the crops: printed page 218 of SH 1123, printed page 434 of NH 18 and printed page 79 of SH 2591, each as a copy at 40% of the 300 dpi render, and printed page 268 of SH 575 at about 100 dpi.
The number and margin note of section 77 are not on the crop of SH 575 printed page 268; they were read from that whole page at about 100 dpi.
Page identity otherwise rests on the footer of each crop.

Quotation lines in the modules are of two kinds.
A `src:N` line is expanded by `tools/srcquote.py` from the excerpt, and N is the line number in the whole page, which the excerpt's header lists; `python3 -I tools/srcquote.py --check <excerpt> *.l4` exits 0.
An `ext:[shNNNN-pPPP]` line quotes the Hebrew read from the deposited image of issue NNNN (or `nh18` for the volume), printed page PPP, and may be skipped by `tools/hebcheck.py` only because it is a quotation line.
Hebrew is typed in code only where the same words are on an `ext:` or `src:` line; the replay clauses of I4 are built with CONCAT of parts for that reason, so that every typed string is on a quotation line; `python3 -I tools/hebcheck.py <excerpt> *.l4 NOTES.md` exits 0.
`tools/hebcheck.py` is copied unchanged from row il-71 and `tools/srcquote.py` from row il-74.

The Hebrew of every `ext:` line was read from the deposited image, and then compared with the text layer of the PDF page as a bag of words (the word order of the 1969 to 2002 layers is reversed or scrambled, so only the words and the numbers could be compared, and a word counts as matched if the page's layer holds it in either direction).
76 `ext:` lines that carry Hebrew were compared, 664 words in all; 622 words matched, and 61 lines matched word for word and number for number.
Words of one character, and the lines that carry only numbers and English, were not compared.
The 15 lines that did not match fully, each for a reason seen in the layer:

- 10 footer lines (those of SH 575 printed page 259, SH 978, SH 1030, SH 1123, NH 18, SH 1634, SH 1807, SH 2591, SH 2888 and SH 3238): the layer lacks the footer's words, holds them with the letters reversed and glued, or holds the day number only; these were read from the image only, and the Hebrew-calendar comparison below checks the pairs of dates.
- the word for "in the provisions" in paragraph (b) of section 2 of SH 978: the layer reads its first letter as a kaf where the image prints a bet; the image decides, and the `ext:` line follows the image.
- the two footnote lines that cite the collection of the laws of the Land of Israel (SH 978 printed page 163 and NH 18 printed page 421): the layer holds no word of the citation in either direction.
- the year 1947 in section 160 of SH 575: the layer glues the footnote number to it (24 and 1947 read as one token).
- the abbreviation for "number" in the margin note of section 97 of SH 1807: the layer reads its geresh as the letter yod.

Where the layer and the image or the consolidation differ in a word that a test reads, the row types the page (forks F1 and F2).

Hebrew calendar: each Hebrew date printed beside a Gregorian date on a footer, and the day printed in section 102 of SH 1807, was entered by hand as day, month name and year number from its `ext:` line and converted with a Hebrew-calendar routine on 2026-11-11, after the control 30 Kislev 5785 = 31.12.2024 passed: 12 Av 5729 = 27.7.1969 (SH 575); 18 Av 5740 = 31.7.1980 (SH 978); 13 Sivan 5741 = 15.6.1981 (SH 1030); 3 Elul 5744 = 31.8.1984 (SH 1123); 2 Av 5757 = 5.8.1997 (SH 1634); 20 Av 5761 = 9.8.2001 (SH 1807); 17 Shevat 5768 = 24.1.2008 (SH 2129); 29 Kislev 5777 = 29.12.2016 (SH 2591); 12 Tevet 5781 = 27.12.2020 (SH 2888); 28 Sivan 5784 = 4.7.2024 (SH 3238); 17 Tevet 5762 = 1.1.2002 (section 102 of SH 1807).
All eleven pairs agree with the Gregorian date the page prints.
The routine checks the page's own pair of dates and does not check the transcription of the Hebrew letters.
The days printed in the footnotes on the titles of SH 978 and NH 18, and the first sentence of the footnote of NH 18, are not typed.

Text-layer leg, over each crop's band rectangle in the whole PDF pages: 64 bands, 1005 words in the layers.
The eye check of each crop decides for what the layers cannot show; all 26 crops were viewed.

Code points: the typed strings follow the code points of the consolidation (the gershayim sign, the maqaf, the en dash); the pages print a double quote, a hyphen or a long dash in those places, and the eye cannot tell them apart.
Only the words and the numbers were compared with the layers, not the code points.

## 4. Files

| file | what it holds |
| --- | --- |
| `ll81-nouns.l4` | the types (an instrument as the row types it, a status in the instruments read, how a limb was read, a reference in the Law, a table of section numbers and its rows, a section as a page prints it, an instruction that prints a status word, the three kinds of instruction of I4, a commencement clause, a provision of another law, a provision of the Interpretation Law, an item of the row) and the questions asked of them (the lookups in a table in both directions, the red tests of I1 to I4, the title comparisons, the word counts, the CONCAT checks of a replay step) |
| `ll81-cross-references.l4` | the 11 instruments, the Interpretation Law's sections 1 and 25, the citing words and the targets of I1 to I4, the instructions of I4 with the clause after each step, the six numbers typed NotChecked, and the four items, each beside its quotation lines |
| `ll81-tests-controls.l4` | 168 assertions that pass: the pairs of the two tables read by the same test as the red ones, the agreement of the two printed places in I1, the printed sections as typed, the replay steps, the limb (b) probes of the instructions after 1997, the commencement clause of SH 1807 section 102, the Interpretation Law's sections |
| `ll81-tests-red.l4` | 4 assertions that fail on purpose, one per item, declared in `check.sh` and `encoding.json` |
| `check.sh`, `fetch-main-l4.sh` | copied from row il-74 with the expected-red module name changed |
| `tools/` | `hebcheck.py` copied unchanged from row il-71, `srcquote.py` copied from row il-74 |

## 5. Coverage

| provision | status |
| --- | --- |
| section 77(d) of the Law (cites section 19(b) of the 1957 law) | encoded as item I1 |
| section 129 of the Law (cites section 20 of the ordinance it names) | encoded as item I2 |
| section 160 of the Law (names siman 46 of an instrument by its printed title) | encoded as item I3 |
| section 72(a) of the Law, the clause with the Bezeq Law's short title | encoded as item I4: the 1969 page typed as printed; the instructions of SH 1634 section 5, SH 1807 section 97 and SH 3238 section 2 typed as data with the clause after each step; the instructions of SH 2129, SH 2591 and SH 2888 typed as data for limb (b) |
| SH 1807 section 1 (the instruction that gives a title before it and a title after it) and section 102 (commencement clause) | encoded: section 1 as the instruction of I4, section 102 as printed with the section numbers it names |
| section 41(a) of SH 1123 and the comparison table of printed page 218 | typed as printed: the rows 34 against 12, 35 against 13, 40 against 18, 41 against 19, 42 against 20 |
| the footnote on the title of NH 18, section 29, and the comparison table of printed page 434 | typed as printed: the sentence of the footnote, section 29 with its margin note and the opening of one entry, the five rows of the left pair |
| section 2 of SH 978 | typed as printed: paragraph (a) with its status word, paragraph (b) as a string, commencement NOTHING |
| the numbers the clause of I4 names in the other law (`6כט`, `6נט`, `6סא`, `21ב`, `21ד` and `27ג`) | typed NotChecked: the row does not read the pages of that law |
| sections 1 and 25 of the Interpretation Law | typed as printed, as one string and as a list of words |
| SH 1228, SH 1350, SH 1380, SH 1584, SH 1805 and SH 1856 | read, logged in section 7, not deposited and not typed |
| the other provisions of the Law | out of scope: this row records four references and does not encode the Law; its operative provisions would need their own coverage table, a seat layer with questions put to the individual, and tests written from the whole text, none of which this row has |
| the rest of the 1957 law, the Evidence Ordinance, the instrument of siman 46, the Bezeq Law and the Interpretation Law | out of scope: each is read only where an item cites it, through the pages named in section 3 |

## 6. Answer table

"Official" means read from a deposited page image; "CO" means CONSOLIDATION-ONLY.
Pages are printed pages.

| item | the citing words say | the target page prints | limb (a) | limb (b) | pages read |
| --- | --- | --- | --- | --- | --- |
| I1, section 77(d) | section 19(b) of the 1957 law, by its printed title (SH 575 p. 268, official) | SH 1123 p. 218: the middle block prints new 41 against previous 19; p. 205: section 41(a) carries the mark "[ב/19]" (official) | the number cited, 19, is not the new-section cell the table prints against the previous cell 19, which is 41: the red assertion fails | the words stand as SH 575 prints them; no instruction on section 77 is read, and the consolidation's heading line of section 77 carries no tag (CO) | SH 575 p. 268; SH 1123 p. 198, 205, 218 |
| I2, section 129 | section 20 of the ordinance it names (SH 575 p. 275, official) | NH 18 p. 434: the left pair prints new 29 against previous (2)18 and against previous 20; p. 425: section 29 with the margin note "הגדרות"; p. 421: a footnote sentence that says the new version is in place of the ordinance the citing words name and one other (official) | the number cited, 20, is not the new-section cell the table prints against the previous cell 20, which is 29: the red assertion fails | the words stand as SH 575 prints them; no instruction on section 129 is read, and the consolidation's heading line of section 129 carries no tag (CO) | SH 575 p. 275; NH 18 p. 421, 425, 434 |
| I3, section 160 | siman 46 of an instrument named by its printed title does not apply to land matters (SH 575 p. 279, official) | SH 978 p. 163, section 2(a): the same number and title tail, then the word "בטל"; section 2(b) is a string (official) | an instruction deposited here prints a status word for the number and title tail the citing words name: the red assertion, that none does, fails | the words stand as SH 575 prints them; no instruction on section 160 is read, and the consolidation's heading line of section 160 carries no tag (CO) | SH 575 p. 279; SH 978 p. 163 |
| I4, section 72(a) | the clause "לחוק הבזק, התשמ״ב–1982", written by SH 1634 section 5 (p. 216, official) | SH 1807 p. 530, section 1: the instruction that gives this title before it and "חוק התקשורת (בזק ושידורים), התשמ״ב–1982" after it (official) | the short title in the citing words equals the title SH 1807 section 1 prints before the instruction, and not the one it prints after it: the red assertion, that it equals the one after, fails | none of the instructions on section 72(a) after SH 1634 that are deposited replaces, deletes or names these words; the log of section 7 covers the rest; the consolidation's line for section 72(a) still ends with the words (CO) | SH 1634 p. 214, 216; SH 1807 p. 530, 560, 561; SH 2129 p. 154, 156; SH 2591 p. 49, 79; SH 2888 cover, p. 247; SH 3238 cover, p. 1044 |

Dates in the answer table are the issue dates the footers print; no date is typed as a day of effect except the one printed in section 102 of SH 1807, which names a day for a different section.
The row says nothing about whether the old title still names the law, about what section 19(b), section 20 or siman 46 provided, or about how any citation should read.

## 7. Limb (b), the tag list of section 72, and the Interpretation Law

For I1, I2 and I3 the row types the 1969 words and the one later fact the pages give, and nothing about whether a later instrument touched the cited words.
The heading lines of sections 77, 129 and 160 in the consolidation carry no tag (CONSOLIDATION-ONLY), and the row reads no instruction on any of the three sections after SH 575; the untagged heading lines are the only thing the row has on that question.
The consolidation's lines for sections 77(d) and 160 read the same as the pages once its markup is removed and the dash and quotation glyphs are normalised (compared by script on 2026-11-11); its line for section 129 differs from the page in one letter (fork F1).

For I4 the heading line of section 72 in the consolidation carries 12 tags, typed here from the excerpt line.
A tag names the Hebrew year and, after a dash, the ordinal of the instrument among those the consolidation's header box lists for that year; a bare tag is taken as the first entry.
The header box lists both `תשס״א` and `תשס״א־2`, which supports that reading.
Each tag was matched to the box (CONSOLIDATION-ONLY for the matching); the box, read in the pinned copy on 2026-11-11, lists three instruments for the year of the first tag and its last entry has the page number 1044, which is the page of SH 3238.
The six instruments that are not deposited are logged by issue number, issue date, printed page and what the instruction does to section 72; no crop of them is in the bundle, nothing in the modules rests on them, and they are log entries.

| tag | instrument, issue date, printed page | what the page prints about section 72 | deposit |
| --- | --- | --- | --- |
| `תשמ״ח` | SH 1228, 19.11.1987, page 7 | an instruction on section 72(a) that puts the plural of the word for "section", the number 58 and further words in place of the singular of the word and the number 58 (the words after 58 were read at about 90 dpi only); the tag's year is earlier than that of SH 1634 | not deposited |
| `תשנ״א` | SH 1350, 26.3.1991, page 117 | an instruction on section 72(a) that puts other words in place of a list of section numbers beginning with 59; the tag's year is earlier than that of SH 1634 | not deposited |
| `תשנ״ב` | SH 1380, 23.1.1992, page 58 | an instruction on section 72(a) that inserts a section number beginning with 59; the tag's year is earlier than that of SH 1634 | not deposited |
| `תשנ״ו` | SH 1584, 21.3.1996, page 248 | an instruction on section 72(a) that puts other words, ending in a section number beginning with 59, in place of words; the tag's year is earlier than that of SH 1634 | not deposited |
| `תשנ״ז` | SH 1634, 5.8.1997, page 216 | section 5 inserts the clause that ends with the Bezeq Law's short title (the ext line tagged sh1634-p216) | `sh1634-p216-s5.png` |
| `תשס״א` | SH 1805, 7.8.2001, page 520 | an instruction on section 72 that replaces one number by another and does not name the clause with the Bezeq words | not deposited |
| `תשס״א־2` | SH 1807, 9.8.2001, page 560 | section 97 puts "לפי סעיפים 6נט עד 6סא, 21ב ו־27ג" in place of "לפי סעיף 6כט"; section 1 of the same instrument is the instruction of I4 | `sh1807-p560-s97.png`, `sh1807-p530-s1.png` |
| `תשס״ב־2` | SH 1856, 10.7.2002, page 474 | an instruction on subsection (c) of section 72, and not on subsection (a) | not deposited |
| `תשס״ח־2` | SH 2129, 24.1.2008, page 156 | section 14 puts other words in place of "59א עד 59ז" (the ext line tagged sh2129-p156) | `sh2129-p156-s14.png` |
| `תשע״ז` | SH 2591, 29.12.2016, page 79 | item (3) of section 12 puts other words in place of "59א עד 59ח" (the ext line tagged sh2591-p79) | `sh2591-p79-s12-3.png` |
| `תשפ״א` | SH 2888, 27.12.2020, page 247 | item 9 puts "59י" in place of "59ח" | `sh2888-p247-i9.png` |
| `תשפ״ד־2` | SH 3238, 4.7.2024, page 1044 | section 2 puts "21ב, 21ד" in place of "21ב" | `sh3238-p1044-s2.png` |

The Hebrew day of SH 1228 is not typed.
The consolidation's header box ends with SH 3238 (CONSOLIDATION-ONLY), so the row names no instrument later than 4.7.2024 and says nothing about any later one.
SH 1634 is the instrument that wrote the words "לחוק הבזק, התשמ״ב–1982" into section 72(a); the instruments after it that print an instruction on section 72(a) are SH 1805, SH 1807, SH 2129, SH 2591, SH 2888 and SH 3238.
The controls probe each of the five deposited ones through the word the cited title contains: the string each replaces does not hold it.
The instruction of SH 1807 section 97 puts words in place of the words that stand before the cited title, and the instruction of SH 3238 section 2 replaces "21ב" only.
The clause after each of the three steps that touch it, as the row types it, still ends with the cited title; these clause strings are the row's own application of the printed instructions, built with CONCAT from the parts of the 1997 clause and the printed strings, and each step is checked against its instruction in the controls.
The consolidation reads "סעיף 6נט עד 6סא" in the singular where the page of SH 1807 section 97 prints "סעיפים 6נט עד 6סא"; this is a difference between two texts, and the row types the page.
The commencement of SH 1634 section 5, SH 1807 sections 1 and 97 and SH 3238 section 2 is NOTHING: the pages read print none.
Section 102 of SH 1807 is typed as printed with the section numbers it names (`6כ2(ג)(5)(ג)(2)`, `33(2)(ב)` and 69); the controls assert that neither 1 nor 97 is among them, and that 69 is.
Section 101 of SH 1807 was read and names neither section 1 nor section 97 of that instrument; it is not deposited.
The text layer of SH 1807 has no clause on references to the old title, and the row says nothing about whether such a clause exists.

The Interpretation Law's sections 1 and 25 are typed as printed (SH 1030, issue dated 15.6.1981, printed pages 302 and 305): section 1 as one string and as a list of 55 words, section 25 as one string and as a list of 22 words, each list generated from its string by splitting on spaces.
The row does not compare the words of these sections with any other page.

## 8. Fork register

- F1, the word for "interested" in section 129.
  SH 575 printed page 275 prints it with one yod, and the page's text layer holds it so; the consolidation's line for section 129 prints it with two.
  Taken: the page's spelling, on the `ext:` line tagged `sh575-p275` and in the typed citing words; the consolidation's line stays as a `src:` line, CONSOLIDATION-ONLY.
  Rejected: the consolidation's spelling, which is not on the page.
  The controls pin the page's spelling and the absence of the other.
- F2, the year word of the sub-heading of the table of SH 1123.
  SH 1123 prints the year word of the 1957 law's title with the letter he before it, and the text layer holds it so; the citing words of section 77(d) in SH 575 print it without.
  Taken: each string as its page prints it, so the two titles are not equal strings; the controls assert that, that each holds the words of the title and the year, and that the 1984 string is the 1969 string with the letter he put before the year word.
  Rejected: typing the sub-heading as the 1969 string, which is not what SH 1123 prints.
- F3, the glyphs.
  The eye cannot tell the gershayim sign from an ASCII quotation mark, or the long dash from a hyphen; the layers compared use the ASCII forms in places, and the consolidation uses the Hebrew gershayim, the maqaf and the en dash.
  Taken: the typed strings follow the consolidation's code points, and the equality tests compare typed strings.
  Rejected: claiming that the pages' own code points were compared; only the words and numbers were (section 3).
- F4, the cells "(1)18" and "(2)18" of NH 18.
  The previous-section cells of the first two rows of the left pair print a bracketed numeral and 18 side by side.
  Taken: typed as the left-to-right reading of the image, "(1)18" and "(2)18", without the text layer.
  Rejected: a reading that puts 18 first, which is not the order the eye reads from left to right.
- F5, the continuity of the tables.
  That the middle block of SH 1123 continues the right-hand block, and that the left pair of NH 18 continues the right pair, is positional: nothing else on the page says so.
  Taken: the two bands of each table are deposited together, and the rows 34 against 12 and 35 against 13 (SH 1123) are typed as the join.
- F6, the mark "[ב/19]".
  Taken: typed as printed, in its own field; the number inside it is read by the same test as the table's cell.
  Rejected: saying what its letter stands for; the page prints no key.
- F7, the 1969 words of section 72(a).
  The 1969 page prints none of the words with the Bezeq Law's short title, and the row does not call them enacted in 1969; the earliest page read that prints them is SH 1634 section 5.
- F8, the days printed in two footnotes.
  The footnote on the title of SH 978 (it is not on the crop; the text layer of the page shows that it prints a day of adoption) and the first sentence of the footnote on the title of NH 18 (on the crop) each print a day; neither is typed as an issue date or as a commencement date.
- F9, the commencement of the instruments.
  Taken: NOTHING for NH 18's issue date, for SH 978, SH 1634 section 5, SH 1807 sections 1 and 97 and SH 3238 section 2; the issue dates are the footers' dates and are never days of effect.
- F10, section 2(b) of SH 978.
  Taken: typed as a string, not evaluated; the row does not say what it does to paragraph (a) or to section 160.
- F11, what is typed as the citing words.
  Taken: the words of the section or paragraph between its label and its closing full stop, with the label in its own field where the module has one.
  Rejected: typing footnote numbers or quotation marks the pages print around inserted texts; the `ext:` lines leave both out.
- F12, the Law's Hebrew title.
  The form in `subject.json` is the one SH 575 printed page 259 prints, read from the crop; the later instruments read print the year with the letter he before it.
- F13, the number of red assertions.
  Taken: four, one per item, so that each limb (a) is one typed fact.
- F14, the other law's numbers.
  Taken: the six numbers the clause names (`6כט`, `6נט`, `6סא`, `21ב`, `21ד` and `27ג`) typed NotChecked; the row does not read that law's pages.
- F15, the section 77 crop.
  The crop holds paragraph (d) only; section 77's number and margin note were read from the whole page viewed at about 100 dpi (section 3).

## 9. Expected red

Four assertions in `ll81-tests-red.l4` fail on purpose, and `check.sh` and `encoding.json` declare four.
I1: the number section 77(d) cites for the 1957 law is the new-section number that the table of SH 1123 prints against that previous number; false: the citing words give 19, and the table prints 41 against the previous cell 19.
I2: the number section 129 cites for the ordinance is the new-section number that the table of NH 18 prints against that previous number; false: the citing words give 20, and the table prints 29 against the previous cell 20.
I3: no section named in the citing words of section 160 has a status word printed for it by an instrument deposited here; false: SH 978 section 2(a) prints the status word for siman 46, which the citing words name.
I4: the short title in the citing words of section 72(a) is the title SH 1807 section 1 prints after the instruction; false: it is the title the section prints before the instruction.
If a later instrument is read that changes any of these, or if a typed value is corrected against its page, the assertion it changes turns green and the declared count must go down with it.

## 10. Check numbers

Run as `L4=~/.local/bin/l4 L4_MAIN=~/.cache/l4-main/109/l4 ./check.sh`; main is build 1.6.109 (4c887e0, 2026-11-04).
Both binaries give the same four counts for every file.

| file | errors | satisfied | failed | refused | declared failed |
| --- | --- | --- | --- | --- | --- |
| `ll81-nouns.l4` | 0 | 0 | 0 | 0 | 0 |
| `ll81-cross-references.l4` | 0 | 0 | 0 | 0 | 0 |
| `ll81-tests-controls.l4` | 0 | 168 | 0 | 0 | 0 |
| `ll81-tests-red.l4` | 4 | 0 | 4 | 0 | 4 |

The four errors are the four declared failed assertions.
The check does not see a different trace outcome, or any difference no assertion exercises; there are no traces here.
The number of `#ASSERT` lines in each test file (168 and 4) equals the satisfied or failed count, so no assertion was swallowed.
Mutation controls, on scratch copies run with the main build (controls satisfied and failed, then red satisfied and failed):
M1, the SH 1123 row 41 against 19 typed as 19 against 19: 163 and 5, then 1 and 3, so the red assertion of I1 turns green.
M2, the NH 18 row 29 against 20 typed as 20 against 20: 164 and 4, then 1 and 3, so the red assertion of I2 turns green.
M3, the status word of SH 978 section 2(a) typed as a different word: 166 and 2, then 1 and 3, so the red assertion of I3 turns green.
M4, the cited title of I4 typed as the title after the rename: 163 and 5, then 1 and 3, so the red assertion of I4 turns green.
M5, the issue date of SH 575 typed as 27.7.1985: 162 and 6, then 0 and 4.
M6, the SH 1123 row 41 against 19 typed as 41 against 91: 163 and 5, then 0 and 4, so the red assertion of I1 stays false because no row prints a new-section cell against the previous cell 19.
The baseline is 168 and 0, then 0 and 4.
A sweep of the whole subject folder for absolute paths on 2026-11-11 printed no hit.

## 11. What was not done, and open questions

- No instrument after SH 3238 that touches section 72 was read; no instruction on section 77, 129 or 160 was read after SH 575.
- The pages the row does not read are not read: the Courts Law's and the Evidence Ordinance's own sections 19 and 20, the instrument of siman 46, and the Bezeq Law's and the Communications Law's sections; the row types the six numbers the clause names NotChecked.
- No day of effect is typed for any provision or instrument except the one section 102 of SH 1807 prints.
- Open for a domain expert: what the references are read to mean in practice, and whether any later text changes what the cited words name; this row does not say.
