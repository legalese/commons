# Row il-68: Families of Soldiers Killed in Action (Benefits and Rehabilitation) Law, 5710-1950, a targeted record of three references

Status on 2026-11-10: draft, version 0.1.0, target compiler main.
No domain expert has read this against the source.
Every claim below was checked against a page image named beside it or against the deposited consolidation excerpt; where it was not, it says so.
This row does not encode the Law.
The English title is a working translation of the Hebrew title (חוק משפחות חיילים שנספו במערכה (תגמולים ושיקום), תש״י–1950).

## 1. What this row is

The row records three items as typed values and tests them: a citation of a subsection letter that section 7 does not print (I1), a pointer sentence in two sections to a section whose list of updated provisions does not name them (I2), and an amending instruction of 2023 whose anchor percentage is not the percentage printed by the last Knesset-printed amendment of that paragraph that the consolidation names before 2023 (I3).
I1 and I3 are one defect each, I2 is two (sections 29A(a) and 29C), so the four references carry four expected-red assertions.
Beside each item the row keeps one sound reference as a control (two for I1, three for I2, one for I3).
Each reference says what the citing words say, what the target prints in the official text, and two limbs: limb (a), the target is repealed, missing or says something else, read from an official instrument; limb (b), the citing words still read so in the latest official instrument.
Section letters are written in Latin letters for the Hebrew letters the Law uses (1C is 1 gimel, 13B is 13 bet, 29A is 29 alef; a subsection (a) is alef, (b) bet, (c) gimel).
The row states what each page prints and records it.
It does not say which words a section should read, what a sentence means for a payment, or what any instrument does in law.

## 2. Seat

The seat is the family member of a fallen soldier, the individual to whom the Law applies.
The row asks that individual no question, because it records references; there is no input to ask for and no `@export`.

## 3. Source, and how each quotation was made

The working text is the Hebrew Wikisource consolidation of the Law, revision 2982012, last edited 2026-02-02T23:00:22Z.
Its whole page was 202183 bytes with sha256 93284b601f96f85bdd2d9f3131f73b1859d212aad5ebb30d90d214508e160914.
It is unofficial, and only an excerpt of thirteen whole lines is deposited at `../../registers/source-bundle/families-of-soldiers-killed-in-action-law-5710-1950.he.wiki.excerpt.txt` (the header lists the line numbers of the whole page).
Every statement about the Law's present words, and every statement that no later instrument touched a provision, rests on those lines and is CONSOLIDATION-ONLY unless a page image is named beside it.
The consolidation is cited by section, never by line.

The official instruments are five issues of Sefer HaChukim (SH) from the Knesset's site, and one issue of Kovetz HaTakanot (KT) from an archive of the printed issues kept by a site that is not a government site, so that copy is an aid.
Only the lines the row reads are deposited, as eight crops named by instrument and printed page (no page is deposited whole, and no PDF page extract is deposited because no page holds only lines of the row).
`SOURCES.json` gives the URL, retrieval time, sha256 and size of each whole file, and the sha256 and size of each crop and of the excerpt, recomputed with `shasum -a 256` and `stat -f %z` on 2026-11-10 (15 entries, 0 bad).
The printed-page offsets were checked by rendering each page at 100 dpi and looking at it before cropping: each footer shows the printed page that the table below gives.

| crop | printed page | PDF page of the whole file | what it holds |
| --- | --- | --- | --- |
| `sh106-p290-s14.png` | SH 106 p. 290 | 4 | item 11 (section 14 as replaced) and the footer |
| `sh1559-p53-s7.png` | SH 1559 p. 53 | 1 | the title of Amendment 19, item 1 (section 7 as replaced) and the footer |
| `sh1559-p54-s26-s30.png` | SH 1559 p. 54 | 2 | items 5 and 6 and the footer |
| `sh3072-p616-s1g.png` | SH 3072 p. 616 | 38 | the instruction that inserts after section 1B, the first paragraph of the new section 1C, and the footer |
| `sh3072-p617-items6-8.png` | SH 3072 p. 617 | 39 | items (6), (7) and (8) of section 43 and the footer |
| `sh3493-p266-s1g.png` | SH 3493 p. 266 | 2 | the title of Amendment 47, item 2 and the footer |
| `sh2216-p252-s13b.png` | SH 2216 p. 252 | 1 | the title of Amendment 30, item 4 and the footer |
| `kt10331-p4064-s3.png` | KT 10331 p. 4064 | 6 | the title and opening words of the first order on the page, its section 3 with its margin note, and the footer |

The Hebrew in a quotation line is never typed from memory.
A `src:N` line is expanded by `tools/srcquote.py` from the excerpt, and `python3 -I tools/srcquote.py --check` exits 0, so each such line equals its source line.
An `img:[instrument pPAGE]` line gives words printed on a crop: they were read from the crop, checked word by word against the text layer of the PDF page (235 Hebrew words, all found; the text layers of these pages store each word in visual order, so a word is looked up with its letters reversed), and read against the crop by eye.
That word check needs the whole PDFs, which are not in the bundle (their URLs are in `SOURCES.json`), so it cannot be re-run from the repository alone; inside the repository the `img:` lines certify themselves, and the crops are what a reader compares them with.
The order of words within an `img:` line and every numeral on it were checked by eye against the crop only, not by a tool.
`python3 -I tools/hebcheck.py <the excerpt> *.l4 NOTES.md` exits 0: it finds every run of Hebrew outside the quotation lines and requires it to occur in the excerpt or on an `img:` line.
`tools/hebcheck.py` is the il-45 tool with one change: it also reads the words of the `img:` lines as source.

## 4. Files

| file | what it holds |
| --- | --- |
| `fk68-nouns.l4` | the record of a reference with its two limbs, the typed values each item needs, and the questions asked of them |
| `fk68-cross-references.l4` | the typed values of the three items, the four references and the six control references, each beside its quotation lines |
| `fk68-tests-controls.l4` | 16 assertions that pass: the control of each item |
| `fk68-tests-readings.l4` | 31 assertions that pass: both limbs and how each was read, and the typed values the items rest on |
| `fk68-tests-red.l4` | 4 assertions that fail on purpose, declared in `check.sh` and `encoding.json` |

## 5. Coverage

| provision | status |
| --- | --- |
| section 14(2) (citing place of I1) | encoded |
| section 7 (target of I1) | encoded as the shape of the section: one paragraph, no subsection letters |
| sections 26(a) and 30(1) (places Amendment 19 changed to the bare citation; the letter of the paragraph in section 30(1) could not be read from the page) | encoded as the control of I1, by what Amendment 19 prints |
| sections 29A(a) and 29C (citing places of I2) | encoded |
| section 1C(a) (target of I2) | encoded as the list of provisions it names, as SH 3072 printed it and as SH 3493 item 2 extended it |
| sections 10(a) and 13B(1), and 9C (members of that list) | encoded as the controls of I2 |
| section 13B(1) (the words the 2023 instruction replaces) | encoded as the percentage the instruction quotes and the two percentages the pages print |
| the rest of section 1C (the later sentences of paragraph (a), paragraphs (b) onward) | out of scope: the row reads only the list of provisions in the first sentence, and does not read what the rest of the section does with them |
| the rest of the Law (the definitions, the entitlements of widows, orphans, parents and other family members, the amounts and their updating, the procedure for claims and appeals, the officers and their powers, the funds) | out of scope: this row records three citations and amending instructions and does not encode the Law; an encoding of the entitlements would have to ask the seat who the fallen soldier was, who depended on them, and which dates apply, none of which any item touches |
| the original publication of the Law, and every amending instrument other than the eight pages above | out of scope: not read; the consolidation's lists of amendments are quoted only as the lines say |

## 6. Answer tables

"Official" means read from the page image of the Sefer HaChukim named in the last column; "CO" means CONSOLIDATION-ONLY.
Pages are printed pages.

| item | the citing words say | the target prints | does the target exist | limb (a) | limb (b) | page read |
| --- | --- | --- | --- | --- | --- | --- |
| I1, section 14(2) | an entitlement of three payments that fall due "לפי סעיף 7(א)", a subsection (a) of section 7 | section 7 as replaced by SH 1559 item 1: one paragraph, no subsection letter | the section: yes; the subsection (a): no | holds, official (SH 1559 p. 53); that section 7 still has no letters is CO | holds, official for the words as printed in 1952 (SH 106 p. 290); that no later instrument touched section 14 is CO (its list of amendments names one entry) | SH 106 p. 290; SH 1559 p. 53 |
| I2, section 29A(a) | a sentence that updates of the grant follow section 1C | the list of provisions in section 1C(a), with 9C and 9D added by SH 3493: section 1 (two definitions), section 8(a) (one definition), 9C, 9D, 10(a), 13B(1) | the section: yes; the provision in the list: no | holds, official (SH 3072 p. 616; SH 3493 p. 266), for the list only | holds, official for the sentence as inserted (SH 3072 p. 617, item (7)); the present words are CO | SH 3072 pp. 616 and 617; SH 3493 p. 266 |
| I2, section 29C | the same sentence | the same list | the section: yes; the provision in the list: no | as above | holds, official for the sentence as inserted (SH 3072 p. 617, item (8)); the present words are CO | as above |
| I3, section 13B(1) | an instruction to replace the part of section 13B(1) that begins with the words "164.87% מסך" | 116.3% in the words Amendment 30 put into paragraph (1) of section 13B; 164.87% in section 3 of the order | the words in the last Knesset-printed text named before 2023: no | holds, official for what SH 2216 prints (p. 252); that it is the last Knesset-printed text named before 2023 is CO | holds, official for the instruction as printed (SH 3072 p. 617, item (6)); whether a later instrument touched the words was not read | SH 3072 p. 617; SH 2216 p. 252; KT 10331 p. 4064 |

| control | the citing words say | the target prints | limb (a) | limb (b) |
| --- | --- | --- | --- | --- |
| I1, sections 26(a) and 30(1) | the bare words "סעיף 7" (SH 1559 items 5 and 6 replace "סעיף 7(ב)" and "סעיף 7(ב)(1)") | section 7 as item 1 prints it | does not hold, official for item 1; that section 7 still exists is CO | holds for what items 5 and 6 print (official); whether a later instrument touched the words was not read |
| I2, section 1C(a) to 10(a) and to 13B(1) | the list names them | the same | does not hold, official | holds, official for the list as printed and extended; the present wording is CO |
| I2, section 1C(a) to 9C | the list names it, after SH 3493 item 2 | the same | does not hold, official | holds, official (SH 3493 p. 266); the present wording is CO |
| I3, the instruction and the order | the quoted anchor, 164.87% | section 3 of the order prints 164.87% | does not hold, official | holds for the instruction as printed (official); whether a later instrument touched the words was not read |

## 7. Fork register

- F1, what the target of I1 is.
  Taken: the subsection letters section 7 has as item 1 of Amendment 19 prints it, which are none; the section as a whole exists and the controls cite it as a whole.
  Rejected: reading the target as section 7 absent, which no page shows; and recording the percentage in section 7, because the percentage in the consolidation's line is not the one on the page of item 1 and the row does not read why.
- F2, limb (b) of I1.
  Taken: the words of section 14(2) as printed in 1952, with "no later instrument touched section 14" recorded as CONSOLIDATION-ONLY because the consolidation's list of amendments for the section names one entry (in the excerpt's heading line, the entry for 1952).
  Rejected: calling limb (b) official for the present words.
- F3, the place name of item 6 of Amendment 19.
  Taken: section 30(1), in a paragraph whose letter the row could not read from the page: the second bracket of the place name on the crop prints as a glyph that could not be told from the digit one at 400 and 800 dpi, and the text layer gives the digit.
  Rejected: naming a letter for the paragraph.
  The row does not read the present text of section 26(a) or of section 30; the controls record only what items 5 and 6 print and that item 1 printed section 7.
- F4, what "does not name these two" covers in I2.
  Taken: the list of provisions in the first sentence of section 1C(a), as SH 3072 printed it and as SH 3493 item 2 extended it.
  Rejected: reading the later sentences of paragraph (a) or the rest of section 1C, which the row does not read; the row therefore does not say that nothing else in section 1C reaches section 29A(a) or 29C.
- F5, the labels of the provisions in the list.
  The strings are this row's plain glosses ("the income needed for subsistence" and "the determining wage" for the two defined terms of section 1, "the determining grade" for the defined term of section 8(a)), not the Law's wording; the Law's words are on the `img:` line.
- F6, limb (b) of I2.
  Taken: the sentence as SH 3072 inserted it, with the present words CONSOLIDATION-ONLY.
  The consolidation's heading line for section 29A ends with an entry for the year תשפ״ו and the one for section 1C ends with the same entry; the row read only item 2 of SH 3493, so it does not say whether anything else in that year touched the pointer sentence or the list.
  The heading line for section 29C ends at the entry for 2023.
- F7, "the last Knesset-printed text before 2023" in I3.
  Taken: Amendment 30 of SH 2216 (3.12.2009), because the consolidation's list of amendments for section 13B names an entry for 2009/10 (תש״ע), then one entry in brackets for an order ([ק״ת עדכון תגמולים]), then the 2023 law (תשפ״ג) and a 2025 amendment (תשפ״ה).
  The row read the 2009 amendment and one order (KT 10331); it does not say that the bracketed entry is that order.
  That the 2009 amendment is the last Knesset-printed text named before 2023 is CONSOLIDATION-ONLY, and other orders may exist (not read).
  Rejected: saying that the instruction cannot be carried out, or that the order is not part of the Law; the row states what each page prints.
- F8, the flag on the percentages.
  The 2009 item is text the Knesset printed for the provision (true); the order is an instrument of the regulation series (false); the anchor quoted by the 2023 instruction carries no flag (NOTHING), because nothing read says in what text the Knesset printed it.
- F9, limb (b) of I3.
  The 2025 amendment is listed in the consolidation and not read, so the row states NOTHING about what section 13B(1) says today.
- F10, the footer of KT 10331.
  The footer line prints a Hebrew date and a Gregorian date whose two years disagree by a year; the Hebrew-calendar routine kept outside the repository was run on 2026-11-10 (its control date, 30 Kislev 5785, gave 31 December 2024, as it should), and the row uses neither date.
  The issue is cited by its number and printed page only, and the order by its number.
- F11, counting.
  I2 is counted as two references and one test for each, because the Law has two citing places; the expected-red count is four (section 8).

## 8. Expected red

Four assertions in `fk68-tests-red.l4` fail on purpose, and `check.sh` and `encoding.json` declare four.
One says that section 7 has the subsection the citation in section 14(2) names (I1).
Two say that the provisions section 1C(a) names, with the two SH 3493 added, include section 29A(a) and section 29C (I2).
One says that the percentage the 2023 instruction quotes equals the percentage Amendment 30 prints (I3).
If a defect is cured, its assertion turns green and the declared count must go down with it.

## 9. Check numbers

Run as `L4=~/.local/bin/l4 L4_MAIN=~/.cache/l4-main/109/l4 ./check.sh` on 2026-11-10; main is build 1.6.109 (4c887e0, 2026-11-04).
Both binaries give the same four counts for every file.

| file | errors | satisfied | failed | refused | declared failed | main errors | main satisfied | main failed | main refused |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `fk68-nouns.l4` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `fk68-cross-references.l4` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `fk68-tests-controls.l4` | 0 | 16 | 0 | 0 | 0 | 0 | 16 | 0 | 0 |
| `fk68-tests-readings.l4` | 0 | 31 | 0 | 0 | 0 | 0 | 31 | 0 | 0 |
| `fk68-tests-red.l4` | 4 | 0 | 4 | 0 | 4 | 4 | 0 | 4 | 0 |

The four errors are the four declared failed assertions.
The check does not see a different trace outcome, or any difference no assertion exercises.
Mutation control: five deliberate faults in a scratch copy (section 7 given a subsection letter, section 29C added to the extended list, Amendment 30's percentage changed to 164.87, 10(a) dropped from the list as SH 3072 printed it, a flag on the section 26(a) citation flipped) turned two assertions red in the controls module and five in the readings module, and three of the four expected-red assertions green, so those tests can fail and the red ones can turn green.

## 10. What was not done, and open questions

- The original publication of the Law and every amending instrument other than the eight pages were not read.
- The present words of sections 7, 14, 26, 29A, 29C and 30 and the later sentences of section 1C rest on the consolidation, or were not read.
- The 2025 amendment of section 13B listed in the consolidation was not read, and other orders between 2009 and 2023 may exist.
- The letter of the paragraph in section 30(1) that item 6 of Amendment 19 names could not be read from the page.
- The order of the words within each `img:` line and every numeral were checked by eye against the crop, not by a tool.
- The percentage in the consolidation's section 7 line differs from the percentage on the page of Amendment 19, item 1; the row records only the shape of section 7 and does not read why.
- Open for a domain expert: whether any instrument after SH 106 touched section 14; what the sentence added to sections 29A(a) and 29C does in the Law; what section 13B(1) says today.
