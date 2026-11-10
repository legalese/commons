# Row il-62: one reference in the Criminal Procedure (Enforcement Powers - Arrests) Law, 5756-1996, whose range ends at a paragraph printed as deleted

Status: draft, version 0.1.0, 2026-11-10, target compiler main.
How each claim was checked: every quotation of an official instrument was typed from a page image that was looked at, and each Hebrew word of 10 of the 11 quotation lines (printed p. 89 of Sefer HaChukim 1973 and printed p. 927 of Sefer HaChukim 2556) was then found in the text layer of the corresponding page of the whole file (PDF page 14 and PDF page 31) by an ad hoc search; the eleventh, the footer line of printed p. 89, was read from the page image only, because the page has no text layer for its footer (this search is not a tool in `tools/`).
Every quotation of the consolidation is expanded by `tools/srcquote.py` from the deposited excerpt, not typed.
The Hebrew dates were converted with the Hebrew-calendar routine in `tools/hebcal.py`, run through `tools/datepairs.py`, which reproduces the routine's own control (30 Kislev 5785 = 31 December 2024) first.
No domain expert has read this against the source.

## Scope

This row is NOT an encoding of the Criminal Procedure (Enforcement Powers - Arrests) Law, 5756-1996.
It records one reference, as typed values with tests, and keeps it as an expected-red test, with the neighbouring paragraphs as the sound control.
The reference is the tail of section 35(b): the words "בפסקאות (1) עד (5)".
Section 35(b) is the paragraph that lists the offences for which a person is a "security-offence suspect" ("חשוד בעבירת בטחון") in that Law, and the tail cites its paragraphs (1) to (5).
The consolidation prints paragraph (5) as "(נמחקה)", that is, as deleted, in place of text.
Section 51(2) of the instrument printed in Sefer HaChukim 1973 (29 Tevet 5765, 10 January 2005, printed p. 89) adds paragraph (5), and section 86(3) of the instrument printed in Sefer HaChukim 2556 (17 Sivan 5776, 23 June 2016, printed p. 927) directs that paragraph (5) be deleted.
Those two instruments are the Terror Financing Law, 5765-2005, and the Counter-Terrorism Law, 5776-2016, as the first pages of the two files give them; those first pages are not deposited, and the English titles are the row's renderings, not enacted titles.
The row records what each instrument prints and says nothing about any other section of the Law, any other amendment, or what the citing words are for.
A date that the sources held do not give is NOTHING; there is no REFUSE, because the target is main.

## Seat

The seat is a person who is arrested or suspected of an offence under the Law's procedure, to whom the Law is applied.
This row asks no question from the seat, because it records one reference and its control, not rules.

## Coverage

This row does not encode the Law, so almost all of it is out of scope; the table says why for each part.

| Part | Status | Reason |
| --- | --- | --- |
| Section 35(b): the tail words "בפסקאות (1) עד (5)" and the range they name | encoded | The finding. Only the range the words name (paragraphs 1 to 5) is recorded; the rest of the tail line is quoted as the consolidation prints it and is not discussed. |
| Section 35(b), paragraph (5): printed as deleted by the consolidation, added by section 51(2) of Sefer HaChukim 1973, directed deleted by section 86(3) of Sefer HaChukim 2556 | encoded | The target of the finding. |
| Section 35(b), paragraphs (1) to (4) | encoded | Control: each is printed with text by the consolidation and none is directed deleted by an instrument read here. What each of them says is quoted and not discussed. |
| The footers of printed p. 89 of Sefer HaChukim 1973 and printed p. 927 of Sefer HaChukim 2556: the issue dates with their Hebrew dates | encoded | Date pairs, each checked with the Hebrew-calendar routine; the row records the two issue dates and no day on which a change took effect. |
| Every other provision of the Law, including the other subsections of section 35 | out-of-scope | This row records one reference and its control and does not encode the Law. Encoding a provision means encoding what it requires, allows or forbids, which needs its own brief, its own seat questions and its own tests; none of that is attempted here, and the row says nothing about those provisions. |
| Later official instruments that touch section 35 | out-of-scope | Opened, not deposited: the row rests on none of them, and what the tail reads today rests on the consolidation alone, which is CONSOLIDATION-ONLY. |

## Fork register

F1. What "(נמחקה)" in place of paragraph (5) means.
Reading taken: that the paragraph is deleted, because the consolidation prints the note in place of text and section 86(3) of Sefer HaChukim 2556 directs that paragraph (5) be deleted.
Reading rejected: that the note stands in place of text still to come; nothing read says so.

F2. The day on which the deletion took effect.
Reading taken: not read; the row records the issue date of the instrument, 23 June 2016, and no day of effect, and never says "since".
Reading rejected: treating the issue date as the day of effect; the instrument's section on commencement is not among the pages read.

F3. Whether the tail still reads "(1) עד (5)" today.
Reading taken: it does, as the consolidation prints it (line 476 of the whole page, CONSOLIDATION-ONLY); section 86 of Sefer HaChukim 2556 has no item that names those words, and later official instruments were opened and are not deposited.
Reading rejected: treating the consolidation's print as an official finding about the current text.

F4. How the numbering of the instrument of 2005 maps onto the consolidation's.
Section 51(1) of Sefer HaChukim 1973 replaces "(1) עד (4)" by "(1) עד (5)" in a passage it calls paragraph (4), and section 51(2) adds paragraph (5) after paragraph (4).
Reading taken: the row does not map that numbering onto today's; it records only that paragraph (5) was added by section 51(2) and that the consolidation prints the tail after paragraph (5) as an unnumbered line.
Reading rejected: identifying the passage the instrument calls paragraph (4) with the tail line; the row has no basis for it.

F5. Which paragraphs are the control.
Reading taken: paragraphs (1) to (4) of the same list, each of which the consolidation prints with text and none of which an instrument read here directs be deleted; the brief of the row names paragraph (4).
Reading rejected: a control from another section, which would not sit beside the finding.

## Answer table

| | Finding | Control |
| --- | --- | --- |
| What the citing words say | "בפסקאות (1) עד (5)" names paragraphs (1), (2), (3), (4) and (5) of the list in section 35(b). | The same words name paragraph (4) among them. |
| What the target says | Paragraph (5) is printed by the consolidation as "(נמחקה)"; section 86(3) of Sefer HaChukim 2556 directs that it be deleted. | Paragraph (4) is printed with text by the consolidation. |
| Exists | No (consolidation); an instrument directs its deletion (read from the page image). | Yes (consolidation). |
| Limb (a) | The two instruments were read from page images; that no later instrument touched the paragraph is CONSOLIDATION-ONLY. | CONSOLIDATION-ONLY. |
| Limb (b) | Section 86 of Sefer HaChukim 2556, read from the page image, has no item that names the words "(1) עד (5)"; that the tail still reads so today is CONSOLIDATION-ONLY. | The same. |
| Page read | Sefer HaChukim 1973, printed p. 89; Sefer HaChukim 2556, printed p. 927 | Section 35(b) of the consolidation, lines 470 to 476 of the whole page |

The footer of printed p. 89 has no text layer, so its Hebrew date and Gregorian date were read from the page image only.
The footer of printed p. 927 was also found in the text layer by the ad hoc search.
Both pairs match the routine: 29 Tevet 5765 = 10 January 2005 and 17 Sivan 5776 = 23 June 2016.

## The expected-red finding, assertion by assertion

`ar62-tests-xrefs-red.l4` holds three assertions, all failing, and `check.sh` and `encoding.json` declare that count (3).
1. Every paragraph the range names is printed with text by the consolidation: it is FALSE, because paragraph (5) is printed as deleted.
2. The number of named paragraphs that the consolidation prints as deleted is 0: it is 1.
3. The number of named paragraphs that an instrument read by this row directs be deleted is 0: it is 1.
The row records this and says nothing about what the citing words are for or whether anyone should change them.

## The check

Run from this folder with `L4=$HOME/.cache/l4-main/98/l4 ./check.sh`; the main build was 1.6.109 (main, 4c887e0, 2026-11-04).

| module | errors | satisfied | failed | refused | expected failed | main: errors | satisfied | failed | refused | main verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ar62-cross-references.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| ar62-nouns.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| ar62-tests-xrefs-red.l4 | 3 | 0 | 3 | 0 | 3 | 3 | 0 | 3 | 0 | same |
| ar62-tests-xrefs.l4 | 0 | 38 | 0 | 0 | 0 | 0 | 38 | 0 | 0 | same |

The three errors are the three failed assertions; no other error, and no refusal.
`python3 -I tools/hebcheck.py <the deposited excerpt> *.l4 NOTES.md` exits 0, the ad hoc search of the text layers (not a tool in `tools/`) checked 10 quotation lines with no word missing and skipped 1 (the footer of printed p. 89), and `python3 -I tools/datepairs.py` reproduces the routine's control and both pairs.

## The deposits

Hebrew Wikisource consolidation of the Law, revision 3079198 (timestamp 2026-08-26T09:30:10Z), an UNOFFICIAL aid: the whole page has sha256 1227597f5bebd812746f054df3d667bea89b2e4fdb0293b8b1941b4fd28eb867 and 175393 bytes as retrieved on 2026-11-10 through the MediaWiki API; the excerpt deposited has sha256 2d7a5701bd682ca2cff405412aee833880384d3de6f952fde5aba06e842ba6aa and 3036 bytes.
The excerpt says in its first lines which lines of the whole page it copies (the title line and lines 470 to 476, which are section 35(b) up to and including its tail), and each line carries its number in the whole page, so that `src:N` means the line N of the page.
The official pages are two composed images of cropped bands, each with its bands separated by a grey bar: `registers/source-bundle/official/sh1973-5765-p89-bands.png` (printed p. 89 of Sefer HaChukim 1973, PDF page 14 of the 15-page file) and `registers/source-bundle/official/sh2556-5776-p927-bands.png` (printed p. 927 of Sefer HaChukim 2556, PDF page 31 of the 36-page file).
The first holds section 51 alone, with its marginal note, and the footer line; the second holds section 86 alone, with its marginal note, and the footer line.
Nothing else of either page is deposited, and both images were viewed after they were composed.
The two whole files are not deposited; `registers/source-bundle/SOURCES.json` records their URLs, sha256 and sizes as supplied, and the sha256 and size of the two images and of the excerpt.
No full page of either file is deposited.

## What was not done

The later official instruments that touch section 35 were opened, not deposited, and are not re-read here: the statement that none of them changed the words "(1) עד (5)" is not made by this row, and what the tail reads today rests on the consolidation alone.
The day on which the deletion took effect was not read.
The first pages of the two files, which carry the titles of the instruments, are not deposited; their titles were read from the text layer only.
The text layer of the footer of printed p. 89 does not exist, so that footer was read from the page image only.
