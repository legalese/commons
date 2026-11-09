# Row il-49: two cross-references in the Securities Law, 5728-1968, that name a repealed section (two defects, two controls)

Status: draft, version 0.1.0, target compiler main.
No domain expert has read this against the source.
Every claim below was checked against a text in the source bundle or a page image named beside it; where it was not, it says so.

## 1. Scope

This row is not an encoding of the Securities Law, 5728-1968.
It records two cross-references as typed values that tests check, and keeps the two that name a repealed section as expected-red tests.
Defect A is item (2) of Part C of the Seventh Schedule, which still cites "35ד(ב)(2)" although section 35ד was repealed by the Securities Law (Amendment 50), 5772-2012.
Defect B is subsection (ב) of section 56, which lists "14א" although section 14א was repealed by the Courts Law (Amendment 59), 5770-2010.
For each cross-reference the row types two descriptions, what the citing words say they point at and what the target is, and records where each of the two readings comes from.
The control for defect A is an amending instruction and not a citation: the same Amendment 50 deleted the words "35ד(ב)(2)," from item (3), paragraph (א), of the Fifth Schedule, a parallel place, and left Part C of the Seventh Schedule alone.
The control for defect B is a sound citation in the same subsection: section 56(ב) also lists section 38, which the same instrument that repealed 14א amended and left standing.
The row does not say what the repealed provisions required, because their wording is in none of the deposited pages (forks F1 and F4).

## 2. The seat

The seat is the person to whom the Law is applied: a corporation to which the Law's duties apply, or an interested party or senior officer of one (the words of section 38(ב), whole-page line 1251 of the consolidation excerpt).
This row asks no question from that seat, because it records references and not duties, so no `@export` module is written.

## 3. Sources

The Law is read from the Hebrew Wikisource consolidation, page "חוק ניירות ערך", revision 3088555, last edited 2026-10-13T11:30:12Z, retrieved on 2026-11-10; it is an UNOFFICIAL aid.
Only an excerpt is deposited, at `../../registers/source-bundle/securities-law-5728-1968.he.wiki.excerpt.txt` (5939 bytes, sha256 02f3bdccef9d0973c63ee1bc7d7509ca13e2103f4e76f5edaf3f486e7b114ff9): ten blocks of whole-page lines copied unaltered, with the whole page's size and sha256 and the line numbers copied in its first lines.
The whole page as retrieved is 717048 bytes, 3494 lines counted by splitting at newlines, sha256 da34949b62ced32e4ff7b559edff5c6d8a46f49195e9598a40cd468a7e829767; the whole page is not deposited.
A `src:N` line in the `.l4` files is whole-page line N, expanded mechanically from the excerpt by `tools/srcquote.py`, which maps N through the excerpt's `#### whole-page lines A-B` marker lines.
The revision id came from a page-history query made in the same session, not from matching the fetched file to a history row, so it is the current revision only if the page was not edited between the two requests (fork F7).
Every statement that rests only on the consolidation says CONSOLIDATION-ONLY.

The official pages are in `../../registers/source-bundle/amending-laws/`, each with a 100 dpi page image of every page read from it; `../../registers/source-bundle/SOURCES.json` gives the URL, retrieval date, sha256 and size of every file, and the sha256 values were recomputed with `shasum -a 256` on 2026-11-10.
All three come from the Knesset's file server.
Sefer HaChukim 2380 is deposited whole (18 pages).
For Sefer HaChukim 2274 and 2253 the Knesset's file holds more than the pages this row reads from, so only those pages are deposited, cut out with qpdf; the sha256 and size of each whole file as downloaded are in `SOURCES.json`.

| instrument | pages read from the page image | what the page shows |
| --- | --- | --- |
| Sefer HaChukim 2380, 20 Av 5772 (8 August 2012), Securities Law (Amendment 50) | p. 681 | s 7: section 35ד of the principal Law is repealed |
| the same | p. 694 | s 27(1): the words "35ד(ב)(2)," are deleted from item (3), paragraph (א), of the Fifth Schedule; s 28: Part B item (7) of the Seventh Schedule is amended; s 29(א): the Law commences three months after publication; the opening words of s 29(ב) |
| Sefer HaChukim 2274, 22 Shevat 5771 (27 January 2011) | p. 238 | an item (2) as enacted, citing "35ד(ב)(2)"; the page has no Schedule or Part heading |
| Sefer HaChukim 2253, 16 Av 5770 (27 July 2010), Courts Law (Amendment 59) | p. 617 | s 9(1) to (4), amendments of the Securities Law: 14א repealed; 36ג(ב), 38 and 47 amended; footnote 12 gives the Law's own publication as Sefer HaChukim 5728, p. 234 |
| the same | p. 619 | s 13: the Law commences on 8 Tevet 5771 (15 December 2010) and applies to proceedings filed in court from that day |

The Hebrew of an official page is typed by me from the page image on a line `-- ext:[SH <issue> p.<page>, read from the page image] | ...` in `sec49-cross-references.l4`.
`tools/pdfcheck.py` checks every Hebrew word of such a line against the text layer of that page (9 lines, 0 problems); it cannot see the order of the words, because these text layers reverse and interleave runs, so the page image is what the typing was read from.
Two more pages were looked at through their text layer only, without a page image, and are not deposited: p. 695 of Sefer HaChukim 2380 and p. 618 of Sefer HaChukim 2253 (fork F3 and fork F5).
`tools/hebcheck-all.sh *.l4 NOTES.md` finds every other run of Hebrew in the `.l4` files and in this file in the excerpt, and exits 0.
The calendar routine reproduced 30 Kislev 5785 = 31 December 2024 before it was used; then 20 Av 5772 = 8 August 2012, 22 Shevat 5771 = 27 January 2011, 16 Av 5770 = 27 July 2010 and 8 Tevet 5771 = 15 December 2010, each of which matches the Gregorian date the page prints beside it.

## 4. Files

| file | what it holds |
| --- | --- |
| `sec49-nouns.l4` | the kinds of provision, the four sources of a reading, the record of a cross-reference and of an amending instruction; no rule |
| `sec49-cross-references.l4` | the four functions, and one typed value per cross-reference and per instruction, with the words of the texts quoted beside it |
| `sec49-tests-xrefs.l4` | 33 assertions: the controls, what was read from where, what the descriptions say, and the day each named text stopped being in force |
| `sec49-tests-xrefs-red.l4` | 4 assertions that fail, on purpose (section 7) |
| `check.sh`, `fetch-main-l4.sh` | the check; `check.sh` declares 4 expected failures for the file above |
| `tools/` | `srcquote.py`, `hebcheck.py`, `hebcheck-all.sh`, `pdfcheck.py` |

## 5. Coverage

| provision | status |
| --- | --- |
| Seventh Schedule, Part C, item (2), the words "35ד(ב)(2)", to section 35ד | encoded; defect A; limb (a) from the official pages with the caveat in section 6, limb (b) from the page image of the words as enacted with the wider caveat |
| Fifth Schedule, item (3), paragraph (א), as conformed by Amendment 50 s 27(1) | encoded as an amending instruction; control A1 |
| Amendment 50 s 28, Seventh Schedule, Part B, item (7) | encoded as an amending instruction; control A2 |
| section 56(ב), the words "14א", to section 14א | encoded; defect B; limb (a) from the official pages with the caveat, limb (b) CONSOLIDATION-ONLY |
| section 56(ב), the words "38", to section 38 | encoded; a sound control chosen by me (fork F4); limb (a) from the official page with the caveat, limb (b) CONSOLIDATION-ONLY |
| the other sections that section 56(ב) lists (35יד(ז), 36ג(ב), 47 and 56א) | out-of-scope: they sit in the same list and were not checked for repeal; the official page shows that 36ג(ב) and 47 were amended by the same instrument as 38 and not repealed, and the row records nothing more about them |
| the other sections that item (2) cites (25(ד), 26(ג), 30, 35יד(ו), 35טו(א), 35כד, 36, 44ד, 52כז(ב), 52ס(ד), 54ג(ג), 54ו, 56(ג)(3) and (ד)) | out-of-scope: the row was made to test one citation in the item and did not open the sections the others name, so it says nothing about whether they stand |
| the other items of the Fifth and Seventh Schedules | out-of-scope: only the three items named above were read; the row says nothing about what any other item says or requires |
| the rest of the Law: what each section requires, allows or forbids, and the procedures it sets | out-of-scope: this row does not encode the Law; it records two cross-references and their controls, and whatever it does not name it did not read |
| the Law's other amending instruments | out-of-scope: the row opened only the three instruments that the two defects and their controls need, and does not list the others |

## 6. The cross-references: answer table

"Stands" means that the target is in the official text of its law today.
Limb (a) asks whether the target is what the citing words say; limb (b) asks whether the citing words still read so in the latest official text of the citing provision.
"Official, with the caveat" means that the repeal and its commencement were read from page images of the official instruments, and that nothing later brought the section back or touched the same words rests on the consolidation, which is CONSOLIDATION-ONLY.

| item | the citing words say it points at | the target is | stands today | limb (a) | limb (b) | pages read |
| --- | --- | --- | --- | --- | --- | --- |
| A: Seventh Schedule Part C item (2) to 35ד(ב)(2) | paragraph (2) of subsection (ב) of section 35ד, whose wording was not read | a section that was repealed, so that it prints no text | no, from 9 November 2012 on the counting in fork F2 | official, with the caveat: SH 2380 p. 681 s 7 and p. 694 s 29(א) | the words as enacted, from the page image of SH 2274 p. 238; that this list is Part C, and that nothing later changed the words, are CONSOLIDATION-ONLY | SH 2380 pp. 681, 694; SH 2274 p. 238 |
| A1: Fifth Schedule item (3)(א), conformed | not a citation: an instruction that deletes the words naming 35ד(ב)(2) | the instruction is s 27(1) of Amendment 50 | not applicable | official: SH 2380 p. 694 | not applicable | SH 2380 p. 694 |
| A2: Seventh Schedule Part B item (7) | not a citation: an instruction that does not delete those words | the instruction is s 28 of Amendment 50 | not applicable | official: SH 2380 p. 694 | not applicable | SH 2380 p. 694 |
| B: section 56(ב) to 14א | section 14א, whose wording was not read | a section that was repealed, so that it prints no text | no, from 15 December 2010 | official, with the caveat: SH 2253 p. 617 s 9(1) and p. 619 s 13 | CONSOLIDATION-ONLY: no official page that prints section 56(ב) was read | SH 2253 pp. 617, 619 |
| B control: section 56(ב) to 38 | section 38, the section on a court order | the same | yes, by the consolidation; the official page shows it existed and was amended on 27 July 2010 | official, with the caveat: SH 2253 p. 617 s 9(3) | CONSOLIDATION-ONLY | SH 2253 p. 617 |

What limb (b) of defect A rests on, sorted by how strong it is.
Read from the page image: SH 2274 p. 238 prints an item (2) citing "35ד(ב)(2)", with the words as enacted.
CONSOLIDATION-ONLY: that this item (2) is item (2) of Part C of the Seventh Schedule, because the heading of the list is on an earlier page of that issue, which was not read, and the consolidation prints Part C item (2) (whole-page line 3429) with the same words; and that no instrument after SH 2274 touched those words.
The consolidation's heading line of the Seventh Schedule (whole-page line 3309) carries one amendment tag; I did not read the list that maps a tag to an issue (fork F6).
What limb (a) of defect A rests on, sorted by how strong it is.
Read from the page image: SH 2380 p. 681, s 7, repeals section 35ד; p. 694, s 29(א), fixes commencement three months after publication; s 29(ב) names two other provisions and not s 7.
CONSOLIDATION-ONLY: that nothing later brought section 35ד back, because the consolidation prints it with the note "(בוטל)" (whole-page lines 676 and 677).
The text layer of p. 695 shows no mention of s 7, section 35ד or the Seventh Schedule, but it is garbled and was not read from an image (fork F3).
Control A1: the same Amendment that repealed 35ד also deleted the words "35ד(ב)(2)," from item (3)(א) of the Fifth Schedule (SH 2380 p. 694, s 27(1)), and the consolidation's item (3)(א) lists no section 35ד (whole-page line 3101, CONSOLIDATION-ONLY).
Section 28 of the same Amendment amends Part B item (7) of the Seventh Schedule and names no other item, so on p. 694, which was read from the image, no instruction touches Part C item (2).
A search of the text layer of all 18 pages of Sefer HaChukim 2380 for the Hebrew words for "the Fifth Schedule" and "the Seventh Schedule" finds them on p. 694 only; the text layers are garbled, so that is a search and not a reading of the other 17 pages.

What limb (b) of defect B rests on.
Only the consolidation: section 56(ב) lists "14א" (whole-page line 2760), and the heading line of section 56 (whole-page line 2758) carries amendment tags of which the last is of the year 5764 and none is of the year 5770, the year of SH 2253; that is the only evidence that the subsection was not conformed, and it is CONSOLIDATION-ONLY (fork F6).
I did not read the instrument that last amended subsection (ב).
The text layer of p. 618 of SH 2253, which is not deposited, shows that s 9 continues there with a paragraph (5) on section 56ד, which is a different section from 56; that text layer is garbled and I did not read the page as an image (fork F5).

## 7. Fork register

Each fork gives the reading taken, the reading rejected or held aside, and the Hebrew that licenses each.
The Hebrew of an official page is on the `ext:` lines of `sec49-cross-references.l4`, which this file points at and does not repeat.

- F1, the wording of the repealed paragraph.
  The wording of paragraph (2) of subsection (ב) of section 35ד, before its repeal, is in none of the deposited pages, and I did not read it.
  Reading A, taken as the row's statement: item (2) cites a paragraph that no longer exists, so the words "35ד(ב)(2)" cite nothing, whether or not a successor duty exists.
  What licenses it: s 7 of Amendment 50 repeals the whole section (SH 2380 p. 681), and the consolidation prints the section with the note "(בוטל)" (whole-page line 677).
  Reading B, held aside: a successor duty exists, in the new text of Amendment 50 or elsewhere, which item (2) should now cite; then the defect is stale words and a gap.
  What would license it: Amendment 50 adds new sections in the same place (the pages show new sections 35ג to 35ג3 and 35ה1 in ss 6 and 8), and I did not read what they say.
  Reading C, held aside: no successor duty exists, so the words should simply go; what licenses it is that s 27(1) deletes "35ד(ב)(2)," from the Fifth Schedule and the page prints no words in their place, whereas s 27(2) on the same page inserts words in item (5) of the same Schedule (I did not type s 27(2)).
  The row does not rule between B and C.
  It records the item as a defect because under both the words as they stand cite a repealed paragraph, and the Fifth Schedule's parallel place was conformed.
- F2, how three months from 8 August 2012 are counted.
  SH 2380 p. 694, s 29(א), commences the Law three months after publication, and the issue is dated 20 Av 5772 = 8 August 2012.
  Taken: the first day certain on either counting is 9 November 2012, so the value is JUST (Date 9 11 2012) and 8 November 2012 and every earlier day answer NOTHING.
  Rejected: 8 November 2012 as the commencement day, because the rule that counts a period of months was not read, so I do not choose between the same-numbered day and the day after the period ends.
  The two red assertions and the day tests on 10 November 2012 and 10 November 2026 do not depend on the choice.
- F3, the rest of the commencement section.
  The opening words of s 29(ב) set s 29(א) aside for two provisions (their Hebrew is on an `ext:` line of `sec49-cross-references.l4`): its two limbs name sections 35ג to 35ג3 as worded in s 6 and section 35ה1 as worded in s 8, and they do not name s 7.
  The rest of s 29 is on p. 695, which I looked at only through its garbled text layer; it concerns a person who served as a trustee before the commencement and I found no mention of s 7 or section 35ד there.
  Taken: s 7 commences three months after publication.
  Held aside: that a transitional provision on p. 695 postpones or limits the repeal; nothing I read says so, and I did not read the page as an image.
- F4, the controls.
  Control A1 is chosen by the nature of the defect: a parallel place in the neighbouring Schedule, conformed by the same instruction; control A2 is the sibling instruction on the same page that does not touch Part C.
  Control B is section 38, chosen by me among 36ג(ב), 38 and 47, all of which s 9 of SH 2253 amends and leaves standing and all of which section 56(ב) lists; it is assumed, not ruled, and nothing else depends on it.
  What the page shows for section 38 is that it existed on 27 July 2010 and was amended by deleting a word (SH 2253 p. 617, s 9(3)); that it stands today rests on the consolidation (whole-page lines 1249 to 1251).
  The wording of section 14א and of section 35ד before their repeal was not read, so neither control tests a reading of what those sections said.
- F5, the commencement of the repeal of section 14א.
  SH 2253 p. 619, s 13, commences the Courts Law (Amendment 59) on 8 Tevet 5771 = 15 December 2010 and says that it applies to proceedings filed in court from that day on.
  Taken: 15 December 2010, so the value is JUST (Date 15 12 2010) and earlier days answer NOTHING.
  Held aside: that section 14א went on applying to proceedings filed before that day; I did not read how the amendment's application clause bears on a repealed section, and the answers for 10 November 2026 do not depend on it.
  Section 9 has a fifth paragraph, on section 56ד, at the top of p. 618, which I saw only in its garbled text layer; the row says nothing more about it.
- F6, the amendment tags.
  The consolidation's own header lists the amending instruments and their Sefer HaChukim pages; that header is not deposited.
  Taken: the amendment tags on the heading lines of the sections and Schedules the row cites, which are in the excerpt (whole-page lines 291, 676, 1249, 2758 and 3309), and a tag of the form `תש״ע־5` read as the fifth law of the year 5770.
  The match between a tag and an issue is mine, by the year and the order, and I did not check it against the header's list.
  Consequence: every statement that no later instrument touched the same words is CONSOLIDATION-ONLY, and the row does not call it official.
- F7, the revision id.
  The revision id 3088555 comes from a page-history query, as section 3 says; it was not matched to the fetched file.
- F8, an enacting-formula citation.
  This row does not treat an enacting-formula citation as a defect and records none.
  Section 56(ב) is a power-conferring subsection; I did not read any regulation made under it, so I do not know what such a regulation's enacting formula cites.

## 8. Expected red

Four assertions in `sec49-tests-xrefs-red.l4` fail on purpose, and the count (4) is declared in `check.sh` and in `encoding.json`.
Each defect has two, and each states what the citing words need.

- Defect A: `the citation points at what it says` (the citing words say a paragraph of a section; the target is a repealed section) and `the named text is in force on` 10 November 2026, expected JUST TRUE (the answer is JUST FALSE, because the repeal has commenced on either counting in fork F2).
- Defect B: the same two assertions for section 56(ב) and section 14א (the answer is JUST FALSE, because the repeal commenced on 15 December 2010).

Nothing in either file was edited to make it pass.

## 9. Check numbers

Run as `L4=~/.local/bin/l4 ./check.sh`; main is build 1.6.109 (4c887e0, 2026-11-04), and the installed `l4` reports its version as `dev`.
Both binaries give the same four counts for every file.

| file | errors | satisfied | failed | refused | expected failed | main: errors, satisfied, failed, refused |
| --- | --- | --- | --- | --- | --- | --- |
| `sec49-nouns.l4` | 0 | 0 | 0 | 0 | 0 | 0, 0, 0, 0 (same) |
| `sec49-cross-references.l4` | 0 | 0 | 0 | 0 | 0 | 0, 0, 0, 0 (same) |
| `sec49-tests-xrefs.l4` | 0 | 33 | 0 | 0 | 0 | 0, 33, 0, 0 (same) |
| `sec49-tests-xrefs-red.l4` | 4 | 0 | 4 | 0 | 4 | 4, 0, 4, 0 (same) |
| total | 4 | 33 | 4 | 0 | 4 | 4, 33, 4, 0 |

The four errors are the four expected failures; `l4 run` on the red module reports an `assertion failed` at the four assertions on lines 17, 19, 24 and 26.
Mutation control, on copies of the modules that were deleted afterwards: moving defect A's end day to 9 November 2013 made 2 assertions fail; giving control B's target the repealed kind made 2 fail; setting control A1's deletion flag to FALSE made 1 fail; the unmutated copy made none fail.
So the tests can fail; the check does not see a difference that no assertion exercises.

## 10. Open questions for a domain expert

- What did paragraph (2) of subsection (ב) of section 35ד say, and is there a successor duty that item (2) of Part C should cite (fork F1)?
- Is the list on SH 2274 p. 238 that cites "35ד(ב)(2)" Part C of the Seventh Schedule? The heading is on an earlier page that I did not read, and the identification rests on the consolidation.
- How does the Law count "three months from publication" for a commencement (fork F2)?
- Does anything on p. 695 of SH 2380, which I did not read as an image, postpone or limit the repeal of section 35ד (fork F3)?
- Which instrument last amended subsection (ב) of section 56, and has any regulation made under it cited section 14א?
- Did section 14א go on applying to proceedings filed before 15 December 2010 (fork F5)?
- What does the amendment tag `תשע״א־2` on the Seventh Schedule's heading line stand for in the consolidation's own header (fork F6)?

No domain expert has read this against the source.
