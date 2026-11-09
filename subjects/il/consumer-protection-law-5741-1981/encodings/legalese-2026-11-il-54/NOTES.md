# Row il-54: six citations in the Consumer Protection Law, 5741-1981, recorded as typed values

Status: draft.
Target compiler: main.
Written on 2026-11-10 by one Sonnet builder, from a written brief; the page images named below were read by the builder.
No domain expert has read this against the source.
This row records references and tests them; it is not an encoding of the Law.

## Scope

The row records six citations in the Consumer Protection Law, 5741-1981, as typed values, and tests them.
Three are defects and three are controls that sit next to a defect.
Section 31א(א)(7) cites "סעיף 18א(5)", and section 31א(א)(8) cites "סעיף 18א(1)", each with no letter for the subsection; since 2008 section 18א has had lettered subsections, and the bare numbers find more than one paragraph.
The Ninth Schedule, item 6, uses the short name "חוק התקשורת", which item 1 of the Second Schedule defines; section 105 of the Communications (Broadcasts) Law, 5786-2026, rewrites that definition and the use in the Third Schedule and does not name the Ninth Schedule.
Each defect is one typed value with two descriptions, what the citing words are about and what the words they use find, and two assertions that fail; the six failing assertions are the expected-red module.
The controls are sound citations whose descriptions agree.
The row says what the texts say and what they do not say, and rules on nothing.

## Seat

The seat is the individual to whom the Law is applied: the consumer, and for the Ninth Schedule the consumer who makes a transaction for telephony, internet access or broadcasts with a provider.
This row asks no question from that seat, because it records references.

## Coverage

| item | status | reason |
| --- | --- | --- |
| section 31א(א)(7), the words "סעיף 18א(5)" | encoded | defect 1; the reference record `reference: s 31א(א)(7) to 18א(5), the warranty certificate`, with two failing assertions |
| section 31א(א)(8), the words "סעיף 18א(1)" | encoded | defect 2; `reference: s 31א(א)(8) to 18א(1), the repair and replacement`, with two failing assertions |
| section 31א(א)(7), the words "סעיף 18א(א1)" | encoded | control 1, the lettered citation in the same sentence as defect 1 |
| section 31א(א)(5), the words "סעיף 17ב(ד)" | encoded | control 2, a citation in the same list that resolves to one provision |
| Ninth Schedule item 6, the short name "חוק התקשורת" | encoded | defect 3; `reference: Ninth Schedule item 6 to the short name the Second Schedule defines`, with two failing assertions |
| Third Schedule item 1, the words "בחוק התקשורת" | encoded | control 3, the use that section 105(2) rewrites together with the definition |
| every other citation in the Law | out-of-scope | this row does not encode the Law and does not claim that these six are the only citations that matter; a citation not listed here has not been recorded, which says nothing about whether it is sound |
| the Law's duties, rights and remedies, section by section | out-of-scope | this row does not encode the Law; the six citations are taken out of the places they stand in and say nothing about what the sections around them require of a trader or give a consumer |
| the other schedules and the regulations made under the Law | out-of-scope | not read for this row beyond the Second, Third and Ninth Schedule lines quoted |
| what item 6 of the Ninth Schedule requires of a trader, and when | out-of-scope | the row records one name used in it and the days on which the instruments say it starts and the name stops being defined |
| where the definition of broadcasts will sit once the Communications (Broadcasts) Law starts | out-of-scope | not read; item 6(ב) refers to broadcasts "as defined" and the row does not say where that definition will be |

## Answer tables

### Defect 1: section 31א(א)(7) to "סעיף 18א(5)"

| question | answer |
| --- | --- |
| what the citing words say | paragraph (5) of section 18א; read with the words around it ("תעודת אחריות") it is the paragraph on warranty certificates, paragraph (5) of subsection (א) |
| what the target says | section 18א has lettered subsections; two paragraphs carry the number 5, (א)(5) on warranty certificates and (א1)(5) on the Minister's power over the sticker exemption; the section has no paragraph (5) at its top level |
| exists | no, as one provision at that address; the paragraph meant exists at (א)(5) |
| limb (a) | the lettering is read from the official instruments: Sefer HaChukim 2159 p. 576 (section 1, the old text is marked as subsection (א)) and p. 577 (section 2, in force three months from publication), and Sefer HaChukim 2310 p. 1022 (section 1 adds subsection (א1) with paragraphs (1) to (5)); that (א) holds paragraphs (1) to (5) and the section's present structure are CONSOLIDATION-ONLY |
| limb (b) | the words as they stood in 2011 are read from Sefer HaChukim 2310 p. 1023 (section 3 quotes "סעיף 18א(5)" as words already in 31א(א)(7)); that they are unchanged today rests on the consolidation alone (CONSOLIDATION-ONLY), no instrument after Sefer HaChukim 2310 having been read for them |
| pages read from the image | Sefer HaChukim 2159 pp. 576 and 577; Sefer HaChukim 2310 pp. 1022 and 1023 |

### Defect 2: section 31א(א)(8) to "סעיף 18א(1)"

| question | answer |
| --- | --- |
| what the citing words say | paragraph (1) of section 18א; read with the words around it ("שיתקן קלקול", the warranty period) it is the paragraph on repair and replacement, paragraph (1) of subsection (א) |
| what the target says | at least three paragraphs carry the number 1, in subsections (א), (א1) and (ג) (a search of the whole consolidated section found a fourth, in a later subsection that is not quoted); the section has no paragraph (1) at its top level |
| exists | no, as one provision at that address; the paragraph meant exists at (א)(1) |
| limb (a) | as for defect 1 |
| limb (b) | CONSOLIDATION-ONLY entirely: no official instrument was read for the words of 31א(א)(8) |
| pages read from the image | Sefer HaChukim 2159 pp. 576 and 577; Sefer HaChukim 2310 p. 1022 |

### Defect 3: the Ninth Schedule, item 6, to the short name "חוק התקשורת"

| question | answer |
| --- | --- |
| what the citing words say | the Communications Law (Bezeq and Broadcasts), 5742-1982, under the short name that item 1 of the Second Schedule defines |
| what the target says | once section 105 has taken effect, item 1 of the Second Schedule defines a short name for the Bezeq Law and defines no short name for the Communications Law, and the Third Schedule uses the new name; the Ninth Schedule is not named by section 105 |
| exists | yes until 28 July 2028 (computed, fork D2), no from then on |
| limb (a) | section 105(1)(א) and (2) are read from Sefer HaChukim 3572 p. 1029; the day is read from section 138(א) on p. 1035, and the lists of (ב) to (ז) on pp. 1035 and 1036 do not mention section 105; that the short name is defined once, in item 1, is CONSOLIDATION-ONLY (a search of the whole consolidated page, which is not deposited, found the defining words in one place); no commencement order or postponement under the Communications (Broadcasts) Law was looked for |
| limb (b) | the words are read from Sefer HaChukim 3569 p. 907 (item 6, opening words and (א) and (ב)); that they are unchanged today rests on the consolidation alone (CONSOLIDATION-ONLY), no instrument after Sefer HaChukim 3569 having been read apart from Sefer HaChukim 3572 pp. 1029, 1035 and 1036 |
| the Ninth Schedule's own start | eight months from 22 July 2026, that is 22 March 2027 (computed, fork D2), Sefer HaChukim 3569 p. 913, section 10(א); section 10(ב)(1) lets the Minister postpone it by further periods of at most four months together, so 22 July 2027 at the latest (computed); whether the power was used is not known |
| pages read from the image | Sefer HaChukim 3569 pp. 907 and 913; Sefer HaChukim 3572 pp. 1029, 1035 and 1036 |

### Controls

| control | citing words say | target says | exists | limb (a) | limb (b) |
| --- | --- | --- | --- | --- | --- |
| 31א(א)(7) to "סעיף 18א(א1)" | subsection (א1) of section 18א, the warranty sticker | the same | yes | Sefer HaChukim 2310 p. 1022, section 1, adds it (image); that nothing later touched it is CONSOLIDATION-ONLY | Sefer HaChukim 2310 p. 1023, section 3 (image); later: CONSOLIDATION-ONLY |
| 31א(א)(5) to "סעיף 17ב(ד)" | subsection (ד) of section 17ב, the binding price of goods | the same | yes | CONSOLIDATION-ONLY | CONSOLIDATION-ONLY |
| Third Schedule item 1, as section 105(2) rewrites it | the Bezeq Law's short name as the Second Schedule defines it after section 105 | the same | yes from 28 July 2028 (computed) | Sefer HaChukim 3572 p. 1029, section 105(1)(א) (image) | Sefer HaChukim 3572 p. 1029, section 105(2) (image) |

## Forks

Every ambiguity the row met, the reading taken, the reading rejected, and the Hebrew that licenses each.

**F1. What the bare numbers in 31א(א)(7) and (8) mean.**
Reading A (the literal one, checked by the failing assertions): "סעיף 18א(5)" and "סעיף 18א(1)" name a paragraph of the section itself, and the section has none at its top level; the numbers find two and at least three paragraphs.
Reading B (taken as the context reading, recorded as a green test, not ruled on): the words around each citation say which paragraph is meant, the warranty-certificate paragraph for (7) and the repair-and-replacement paragraph for (8).
The Hebrew that licenses B, from the consolidation excerpt (CONSOLIDATION-ONLY): the words around the citation in 31א(א)(7) and (8), and the two paragraphs of 18א(א):

```
-- src:12 | (7) ביקש צרכן מיצרן טובין או מעוסק לקבל תעודת אחריות, כפי שנדרש לפי סעיף 18א(5) או ביקש צרכן מעוסק לקבל מדבקת אחריות, כפי שנדרש לפי סעיף 18א(א1) – והיצרן או העוסק, לפי העניין, לא מסר תעודה או מדבקה כאמור;
-- src:7 | (5) מתן תעודות אחריות, תוכנן, ואיסור התנאה בתעודות כאמור על זכויות הצרכן לפי דין.
-- src:13 | (8) ביקש צרכן מיצרן טובין או מעוסק, שיתקן קלקול שנתגלה בטובין שנמכרו לו או שיספק חלקי חילוף לשם תיקון הטובין, כפי שנדרש לפי סעיף 18א(1) – והיצרן או העוסק, לפי העניין, לא תיקן כל קלקול כאמור במהלך תקופת האחריות בלא תמורה או לא סיפק חלקי חילוף כאמור עד תום תקופת האחריות, בתוך התקופה שנקבעה לכך לפי אותו סעיף.
-- src:3 | (1) תיקון ליקויים ופגמים והחלפת טובין, בשלמותם או בחלקם, בלי תשלום, במשך תקופה שיקבע;
```

**F2. Whether item 6 of the Ninth Schedule needs a definition of "חוק התקשורת".**
Reading A (taken in the failing assertions): the short name is the one item 1 of the Second Schedule defines, so once section 105 rewrites item 1 the name is no longer defined in the Law.
Reading B (not ruled on; the context reading is NOTHING): the Ninth Schedule uses the name as the plain short name of the Bezeq Law and needs no definition.
The defining words, from the consolidation excerpt (CONSOLIDATION-ONLY), and the Ninth Schedule's opening words:

```
-- src:14 | ספק מורשה כהגדרתו בחוק התקשורת (בזק ושידורים), התשמ״ב–1982 (בחוק זה – חוק התקשורת) המספק לפי החוק האמור אחד או יותר מהשירותים האלה:
-- src:17 | כל אחת מהעסקאות המפורטות להלן, לרבות מכירה של ציוד או ציוד קצה כהגדרתו בחוק התקשורת, לפי העניין, שנעשית במסגרת אותה עסקה, בהמשך לה או בעקבותיה, ולעניין העסקאות כאמור בפסקאות משנה (ב) ו־(ג) – ובלבד שהציוד משמש לקבלת השירות בהתאם לתנאי אותן עסקאות:
```

**D1. Days before the stopping day.**
For a day before the day the words stop reaching their text, and for a citation with no stopping day, the answer is NOTHING; it is not "yes".
No source held says what the words found before.

**D2. The four computed days.**
The row computed 26 September 2008 (three months from 26 June 2008), 22 March 2027 (eight months from 22 July 2026), 22 July 2027 (four more months) and 28 July 2028 (two years from 28 July 2026).
Whether a month is Gregorian and whether the day of publication counts was not checked against the Interpretation Law.
The tests ask only about days well clear of these days, and the one assertion that compares two computed days compares 22 July 2027 with 28 July 2028.

**D3. What the replacement in item 1 of the Second Schedule reaches.**
Section 105(1)(א) puts the Bezeq Law's short name in place of "חוק התקשורת" in item 1; the words also occur inside the full title in that item.
Reading A: only the defined short name is replaced.
Reading B: every occurrence is replaced.
Defect 3 holds on both: on either, item 1 no longer defines the short name "חוק התקשורת".

**D4. Whether the postponement power of section 10(ב)(1) of Amendment 74 was used.**
Not known; the row records the latest day the start can reach (22 July 2027) and nothing more.

## What was and was not read

Read from the page image: Sefer HaChukim 2159 pp. 576 and 577; Sefer HaChukim 2310 pp. 1022 and 1023; Sefer HaChukim 3569 pp. 907 and 913; Sefer HaChukim 3572 pp. 1029, 1035 and 1036.
Typed from those images on `ext:[SH ...]` lines and checked word by word against the text layer of the page by `tools/pdfcheck.py`; the two footer lines (the footer of p. 907, which carries the date of Sefer HaChukim 3569, and that of p. 1035) are tagged differently because those footers are not in the text layer, so `pdfcheck.py` does not guard them.
The deposited images of Sefer HaChukim 3569 are crops: p. 913 is cropped to section 10, and p. 907 to the heading of the Ninth Schedule with items 1 to 6, plus a strip with the printed footer; the row relies only on those parts, and the whole pages were read before they were cropped.
Of Sefer HaChukim 3569 no PDF is deposited, so the quotations from pp. 907 and 913 carry the tag `SH 3569, p.907 image only` or `SH 3569, p.913 image only`, which `tools/pdfcheck.py` does not match; every word of them was checked against the text layer of the whole PDF as downloaded (sha256 79212abfbf0871f2eae88eb19bca791cc3675dbfa09ad424392e1de91891e738, 12 pages) before it was removed, in one run of 19 quotation lines with 0 problems.
Of Sefer HaChukim 3572 only a three-page extract (printed pp. 1029, 1035 and 1036) is deposited, and `pdfcheck.py` checks its quotations against that extract.
Not read: any instrument after Sefer HaChukim 2310 for the words of 31א(א)(7) and (8); the instrument that wrote paragraphs (1) and (5) of section 18א(א); the other pages of Sefer HaChukim 3569 and 3572; any commencement order under either; the Interpretation Law.
A text-layer search of the 52 PDF pages of Sefer HaChukim 3572, as downloaded (that whole file is not deposited), for the title of the Consumer Protection Law finds it on PDF page 1 and on PDF page 39 (printed p. 1029) only.
PDF page 1 was not read as an image, and a text layer can miss a mention, so the row does not say that section 105 is the only place where that Law amends the Consumer Protection Law.

## Check numbers

Command: `L4=~/.local/bin/l4 L4_MAIN=~/.cache/l4-main/109/l4 ./check.sh`, run from this folder on 2026-11-10; main build 1.6.109 (main, 4c887e0, 2026-11-04).

| module | errors | satisfied | failed | refused | expected | main: errors | satisfied | failed | refused | main verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cons54-cross-references.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| cons54-nouns.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| cons54-tests-xrefs-red.l4 | 6 | 0 | 6 | 0 | 6 | 6 | 0 | 6 | 0 | same |
| cons54-tests-xrefs.l4 | 0 | 49 | 0 | 0 | 0 | 0 | 49 | 0 | 0 | same |

A mutation probe was run once on a scratch copy: three edits (a day, a description, a limb label) turned three satisfied assertions into three failed ones, so the green tests do detect a change of a recorded value.
`python3 -I tools/hebcheck.py <excerpt> *.l4 NOTES.md` exits 0.

## Expected red

Six assertions fail, two for each defect, in `cons54-tests-xrefs-red.l4`; the count is declared in `check.sh` (`expected_failed`) and in `encoding.json` (`expected_red`).
Each states what the citing words need: that the description of what they are about is the description of what the words find, and that the words still reach their text on a day after the day computed for the stop.
Nothing is edited to make them pass.

## Deposits

All under `registers/source-bundle/` of this subject, with one entry for each file in `SOURCES.json`.
The Hebrew Wikisource consolidation is deposited as an EXCERPT, an UNOFFICIAL aid: revision 3099046, last edited 2026-10-29, retrieved 2026-11-10, file `consumer-protection-law-5741-1981.he.wiki.excerpt.txt`, sha256 29a1c13d0e2cccccaf09a03bc9ccc17149dc43be0e776d52d20e70c5d5fa0b3f.
The whole page text it was cut from was 344005 bytes with sha256 90ce2b9a0feafbabdc072856a733d0e9e87477e16d36359cbb1a39b6e953861e; the rest of that text is not deposited.
In this row's files, `src:N` is line N of the excerpt, not of the whole page; `SOURCES.json` lists the whole-page line each excerpt line was taken from.
Only the pages read are deposited, in `amending-laws/`.
Sefer HaChukim 2159 and 2310 are deposited whole (two pages each, the amending laws themselves); of Sefer HaChukim 3572 a three-page extract is deposited (PDF pages 39, 45 and 46 of the file as downloaded); of Sefer HaChukim 3569 no PDF is deposited, only three cropped images (p. 907 heading and items 1 to 6, the p. 907 footer strip, and p. 913 section 10).
With the full-page images of the other pages read, that makes ten page images.
For each file not deposited whole, `SOURCES.json` keeps the URL, the retrieval date and the sha256 and size of the whole file as downloaded (Sefer HaChukim 3569: sha256 79212abfbf0871f2eae88eb19bca791cc3675dbfa09ad424392e1de91891e738, 229542 bytes; Sefer HaChukim 3572: sha256 df1e818b9ff7920e20b33191b9174cd71d1834ea72c1d2156107cf8e92dc9691, 699669 bytes), and says that only the pages read are deposited.
