# Row il-53: two printed figures that an instruction of the Insolvency and Economic Rehabilitation Law, 5778-2018, wrote into the Execution Law, 5727-1967 (two defects, two controls)

Status: draft, built 2026-11-10 from the sources named in section 2.
No domain expert has read this against the source.
Every reading below says where it comes from: a page image of the official instrument, the Hebrew Wikisource consolidation (UNOFFICIAL), or the text layer of the PDF.
Where nothing was read, the row says `not read`.

## 1. Scope

This row does not encode the Insolvency and Economic Rehabilitation Law, and it does not encode the Execution Law.
It records references: two printed figures that section 361 of the Insolvency Law wrote into the Execution Law, and what stands beside each.
- Defect 1: Execution Law section 7א2, as section 361 inserted it (Sefer HaChukim 2708 p. 407).
  Paragraph (1) says "אינו עולה על 150,000 שקלים חדשים" and paragraph (2) says "הוא 150,000 שקלים חדשים לפחות", so a total debt of exactly 150,000 shekels is inside both paragraphs.
- Defect 2: Execution Law section 76(ג), as section 361 wrote it (p. 407).
  The instruction fixes "תחול עד לסכום של 26,000 שקלים חדשים", and the Insolvency Law's own section 234(א)(1)(א) as enacted (p. 366) fixes 25,630 shekels for wages and 39,945 shekels for severance pay together with wages.
- Control 1, for defect 1: instruction (10) of section 361, to Execution Law section 77א, read from the same page image.
  Control 2, for defect 2: instruction (8) of section 361, to Execution Law section 69י1, read from the same page image.

The seat is the individual to whom the Law is applied: the individual debtor whose total debt is compared with the figure in section 7א2, and the employee whose claim for unpaid wages is limited by the figure in section 76(ג).
The row asks no question from the seat because it records references.

What the row does not say: it does not say what the Execution Office should do at exactly 150,000, which of the two wage figures governs a given claim, or what any figure is today.
It states no figure other than those printed on the two pages read.

## 2. Sources

- **The official instrument.** Sefer HaChukim 2708, 28 Adar 5778 (15 March 2018), fetched from `https://fs.knesset.gov.il/20/law/20_lsr_491934.pdf` on 2026-11-10.
  The whole file as downloaded has 128 pages (sha256 f6c352653ced3bf709ef5805474648405aa26c5d4b2da0934732d2d204d6a98b, 2,081,294 bytes); only the pages read are deposited, as a three-page extract, `../../registers/source-bundle/amending-laws/sh2708-5778-pages-310-366-407-page-extract.pdf` (sha256 0d0a96774db61f71c31092259863f1a11798a105d65c77a0e390b6e8d4ab4124, 54,146 bytes).
  Extract page 1 is printed page 310, the page that opens the Law's text; extract page 2 is printed page 366 (section 234) and extract page 3 is printed page 407 (the Execution Law instructions of section 361).
  Printed pages 366 and 407 were read from page images, `sh2708-5778-p366.png` and `sh2708-5778-p407.png` beside the extract, at 100 dpi, rendered for this row from the extract.
  No other page is quoted from or imaged.
- **The first printed page of the Law.** The subject's citation says p. 310.
  The running header of the page that opens the Law's text prints 310 above section 1; that was read from the text layer of extract page 1, not from an image, and the page is deposited so that it can be checked.
  It is not an image reading, and nothing else on that page is used.
- **The consolidation (UNOFFICIAL aid).** Hebrew Wikisource page of the Execution Law, revision 3099076, last edited 2026-10-29T14:03:51Z, raw wikitext retrieved 2026-11-10.
  Whole page as retrieved: sha256 c18dfd4c5e13de6d372353b142cb12e8f725cc56bbcf9e85715347e43c325b2f, 440,529 bytes.
  Deposited as an EXCERPT only, `../../registers/source-bundle/execution-law-5727-1967-excerpt-rev3099076.he.wiki.txt` (sha256 8baf902da9747729eba8ec4244c40ac331fd32e129f8152f412e48bf45865fd5, 5,318 bytes).
  Its first four lines give the revision, the whole page's sha256 and size, and the page line numbers copied (2; 253 to 256; 1169 to 1170; 1542; 1548; 1553 to 1554).
  `src:N` in the `.l4` files is line N of the EXCERPT; the excerpt's `page line` markers give the line in the whole page.
  The Wikisource consolidation of the Insolvency Law itself was not deposited and was not used for any quotation in this row.
- **Text layer of the whole issue only, pages not deposited.** Two statements rest on the text layer of pages of the issue as downloaded that are not in the extract, so they cannot be checked from the bundle: that the amending section is section 361 and that items (1) and (2) of it come before (4), and that section 352(א) of the Insolvency Law says the amounts fixed in that Law are updated each 1 January by the change in the consumer price index.
  The text layer of the odd pages of this PDF is reversed and doubled in places, so nothing here is quoted from it.
- **Not read.** The instrument that wrote the old end of section 76(ג), from the words "תחול עד לסכום"; any instrument after the Insolvency Law that touched sections 7א2 or 69י1 or 76(ג) or 77א; the Insolvency Law's present words; the page of the PDF that holds the opening words of the instruction that inserts section 7א2, as an image.
  The number (3) of that instruction is inferred from the sequence of the items; it is not read from an image.

## 3. Files

| file | what it is |
| --- | --- |
| `insolv53-nouns.l4` | the kinds: where a reading comes from, a paragraph with a debt figure, a figure fixed by a provision, an amending instruction and its target |
| `insolv53-cross-references.l4` | the typed values with every quotation beside them (`src:` lines from the excerpt, `ext:[SH 2708 ...]` lines typed from the page images), and the functions that compare them |
| `insolv53-tests-xrefs.l4` | 29 assertions that pass: the recorded facts, the controls, the printed figures, and what was read from where |
| `insolv53-tests-xrefs-red.l4` | 4 assertions that fail, two for each defect (section 7) |
| `check.sh`, `fetch-main-l4.sh` | the self-check and the fetcher of the main build, copied from row il-48; `check.sh` declares the 4 expected failures |
| `tools/hebcheck.py`, `tools/hebcheck-all.sh` | every run of Hebrew outside a `src:` or `ext:` line must occur in the excerpt; `hebcheck-all.sh` names the one deposit |
| `tools/srcquote.py` | expands `--@SRC n` markers into `src:` lines from the excerpt |
| `tools/pdfcheck.py` | checks each Hebrew word of an `ext:[SH 2708 p.366 ...]` or `ext:[SH 2708 p.407 ...]` line against the text layer of its page |

There is no `extquote.py`: this row quotes no consolidation other than the excerpt.

## 4. Coverage

"Encoded" means a typed value and tests; "stated" means a comment only.
Everything else is out of scope, with the reason.

| item | status | reason |
| --- | --- | --- |
| Execution Law s 7א2(1) and (2): the figure and which paragraph covers which debts | encoded | defect 1 |
| Execution Law s 76(ג): the fixed figure | encoded | defect 2 |
| Insolvency Law s 234(א)(1)(א): the two figures as enacted | encoded | the figures beside which s 76(ג) stands |
| Insolvency Law s 234(ב): the enacted figures are updated each 1 January | encoded as one boolean field, with a passing test | it is on the same page as the figures, p. 366 |
| Insolvency Law s 352(א): the amounts fixed in that Law are updated each 1 January by the consumer price index | stated | read from the text layer of the whole issue as downloaded only; its page is not deposited and was not imaged, so it is not typed, no page of it is cited, and it cannot be checked from the bundle |
| Instruction (10) of s 361, to Execution Law s 77א | encoded | control 1 |
| Instruction (8) of s 361, to Execution Law s 69י1 | encoded | control 2 |
| The other instructions of s 361 that are on p. 407: (4) to (7), (11) and (12) | out-of-scope | they stand on the page that was read, but no value in this row depends on any of them, and none was checked against its target |
| The rest of s 234 and every other section of the Insolvency Law | out-of-scope | the row does not encode the Law; each further section would need its own reading of the page and its own check against the amended text |
| The other instructions of the amending chapter, which amend other laws | out-of-scope | not examined by this row; each amended law needs its own consolidation and its own page |
| The rest of the Execution Law | out-of-scope | only four sections are touched, and only through the excerpt of the consolidation; the other sections were not read |
| The present wording of the Insolvency Law | out-of-scope | not read; the Insolvency Law figures are recorded as enacted only |
| Any figure as updated since enactment | out-of-scope | the row records printed figures; it states no updated figure for any provision |

## 5. The figures: answer table

"Exists" asks whether the figure or words are on the page read.
Limb (a) asks whether the amending instruction wrote what the row says; limb (b) asks whether the Execution Law's present words are those words.
"CONSOLIDATION-ONLY" means the present text rests on the excerpt of revision 3099076 and that no later instrument was read.

| item | citing words | target | exists | limb (a) | limb (b) | page read |
| --- | --- | --- | --- | --- | --- | --- |
| defect 1: s 7א2(1) | "אינו עולה על 150,000 שקלים חדשים" | a total debt of exactly 150,000 | yes: covered by paragraph (1) | official | CONSOLIDATION-ONLY (`src:10`) | SH 2708 p. 407 |
| defect 1: s 7א2(2) | "הוא 150,000 שקלים חדשים לפחות" | a total debt of exactly 150,000 | yes: covered by paragraph (2) as well | official | CONSOLIDATION-ONLY (`src:11`) | SH 2708 p. 407 |
| control 1: instruction (10), s 77א | the first replacement: "בפנייה להליכי חדלות פירעון לפי חוק חדלות פירעון ושיקום כלכלי" | the same words in s 77א | yes | official | CONSOLIDATION-ONLY (`src:21`) | SH 2708 p. 407 |
| defect 2: s 76(ג) | "תחול עד לסכום של 26,000 שקלים חדשים" | s 234(א)(1)(א) of the Insolvency Law: 25,630 (wages) and 39,945 (severance with wages) | the words and both figures are on the pages; the figures differ from 26,000 | official (p. 407 and p. 366) | CONSOLIDATION-ONLY (`src:18`) for s 76(ג); `not read` for s 234 | SH 2708 p. 407 and p. 366 |
| control 2: instruction (8), s 69י1 | "מיום התחילה של חוק חדלות פירעון ושיקום כלכלי" | the same words in s 69י1 | yes | official | CONSOLIDATION-ONLY (`src:14`) | SH 2708 p. 407 |

No row has both limbs read from the official instruments; the tests assert that (`NOT ... were read from the official instruments`).

## 6. Fork register

Each fork gives the ambiguity, the reading taken, the reading rejected or held aside, and the Hebrew that licenses each.

- F1, the kinds.
  The kinds in `Where a reading comes from` and `How a paragraph meets its figure` are my plain descriptions, so that two descriptions of the same thing are the same kind; they are not the Law's terms.
  Taken: three sources of a reading (a page image, the consolidation only, not read).
  Rejected: comparing the Law's words as strings throughout, which would turn every difference of punctuation into a defect.
- F2, whether two different figures for the priority of a wage claim are a defect.
  Taken: record the two figures as they are printed (26,000, and 25,630 with 39,945), and state in the expected-red file the reading under which one figure serves both; the Law does not say that they must be the same.
  Rejected, held aside: that the figures are meant to differ, because section 76(ג) governs the ranking of creditors in an execution and section 234 the ranking in an insolvency, each applied in its own proceeding.
  What licenses the taken reading: section 76(ג) speaks of "זכות קדימה לעניין חוב בשל אי־תשלום שכר עבודה", the same kind of claim as the first group in section 234(א)(1)(א), and no word of instruction (9) or of section 76(ג) refers to section 234.
  What licenses the held-aside reading: the words "אין בהוראות סעיף זה כדי לגרוע מזכות קדימה או מעדיפותו של זוכה או נושה על פי כל דין אחר" confine the subsection to the execution.
  The row does not rule between them.
- F3, the overlap in section 7א2.
  Taken: paragraph (1) covers every total debt up to and including 150,000, and paragraph (2) every total debt from 150,000 upward, 150,000 included, so both apply at exactly 150,000.
  What licenses it: "אינו עולה על 150,000 שקלים חדשים" for paragraph (1) and "הוא 150,000 שקלים חדשים לפחות" for paragraph (2).
  Rejected, held aside: reading "לפחות" as meaning more than 150,000, or reading the first paragraph as taking precedence because it comes first.
  What licenses them: nothing in the two paragraphs gives an order between them or excludes the figure from the second.
- F4, whether the update of the Insolvency Law's own 150,000 reaches the figure in section 7א2.
  The Insolvency Law's section 352(א) updates the amounts fixed in that Law; it is stated in a comment only (text layer, no page cited).
  The words of paragraphs (1) and (2) of section 7א2 contain no reference to section 352 or to a figure of the Insolvency Law.
  Taken: the question is not answered by the words read, and the row states no updated figure.
  Rejected: reading the figure in section 7א2 as the Insolvency Law's figure, because no word says so.
- F5, limb (b) for section 76(ג).
  The consolidation's tags carry the label תשע״ח־5 on sections 7א2 and 69י1 and 77א (excerpt lines 8, 13 and 20), which instructions of section 361 amend, and do not carry it on section 76 (excerpt line 16), which instruction (9) of the same section amends.
  So the tag is not a complete record of what amended section 76, and that no later instrument touched section 76(ג) rests on nothing better than the consolidation's text.
  Taken: limb (b) is CONSOLIDATION-ONLY for all four sections.
- F6, the number of the instruction that inserts section 7א2.
  Taken: item (3) of section 361, by the sequence; items (1) and (2) are on the text layer of the preceding page, which is not deposited, and (4) opens p. 407.
  Not read from an image: the opening words of that instruction.
- F7, the controls.
  Taken: instruction (10) for defect 1 and instruction (8) for defect 2, because each is on p. 407 beside the defect and its target is in the excerpt; they are assumed, not ruled, and nothing else depends on them.
  The two strings compared in each control were typed by me twice, once from the page image and once from the excerpt, so the control tests a transcription and not the Law.
  The marginal heading of section 77א is not touched by instruction (10) and is not used.

## 7. Expected red

Four assertions in `insolv53-tests-xrefs-red.l4`, all failing.
Each states what the printed words need if one reading is to hold.

1. Defect 1: exactly one paragraph of section 7א2 applies to a total debt of exactly 150,000.
   It fails: two apply.
2. Defect 1: the two paragraphs do not both apply to a total debt of exactly 150,000.
   It fails: both apply.
3. Defect 2: the figure written into section 76(ג) is the figure the Insolvency Law fixes for wages in section 234(א)(1)(א).
   It fails: 26,000 is not 25,630.
4. Defect 2: the figure written into section 76(ג) is one of the two figures the Insolvency Law fixes in section 234(א)(1)(א).
   It fails: 26,000 is neither 25,630 nor 39,945.

The count (4) is declared in `check.sh` (`expected_failed`) and in `encoding.json` (`expected_red`).
The first two assertions are the same fact stated as a count and as a negation; the last two differ in the set of figures compared.

## 8. Check numbers

Run from the row folder with `L4=~/.local/bin/l4 L4_MAIN=~/.cache/l4-main/109/l4 ./check.sh` on 2026-11-10; the main build is 1.6.109 (main, 4c887e0, 2026-11-04).

| module | errors | satisfied | failed | refused | expected failed | main: errors, satisfied, failed, refused |
| --- | --- | --- | --- | --- | --- | --- |
| `insolv53-cross-references.l4` | 0 | 0 | 0 | 0 | 0 | 0, 0, 0, 0 (same) |
| `insolv53-nouns.l4` | 0 | 0 | 0 | 0 | 0 | 0, 0, 0, 0 (same) |
| `insolv53-tests-xrefs-red.l4` | 4 | 0 | 4 | 0 | 4 | 4, 0, 4, 0 (same) |
| `insolv53-tests-xrefs.l4` | 0 | 29 | 0 | 0 | 0 | 0, 29, 0, 0 (same) |
| total, 4 modules | 4 | 29 | 4 | 0 | | 4, 29, 4, 0 |

Each failed assertion is also an error diagnostic, so the 4 errors are the 4 expected failures and no other error was reported.
No module refuses, and no module uses REFUSE.
`tools/hebcheck-all.sh *.l4 NOTES.md` exits 0, and `tools/pdfcheck.py *.l4` checks 10 quotation lines with 0 problems; that check is weak, since it looks for each Hebrew word anywhere on the page's text layer and not for the words in order.
A one-number mutation of the second paragraph's figure, made in a scratch copy of the modules, turned 4 of the 29 passing assertions red and was then discarded, so the tests respond to the figures they quote.

## 9. Open questions for a domain expert

- Whether a total debt of exactly 150,000 shekels should fall in paragraph (1) or paragraph (2) of section 7א2, and whether the Execution Office is meant to treat the overlap as a choice.
- Whether the figure in section 76(ג) is meant to follow the figure in section 234(א)(1)(א), or whether the two are meant to differ.
- What the 26,000 in section 76(ג) replaced: the instrument that wrote the old end of the subsection was not read.
- Whether any instrument after the Insolvency Law amended sections 7א2 or 69י1 or 76(ג) or 77א; none was read.
- No domain expert has read this against the source.
