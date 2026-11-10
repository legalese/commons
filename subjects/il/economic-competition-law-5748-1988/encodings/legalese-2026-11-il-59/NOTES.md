# Row il-59: five items in the Economic Competition Law, 5748-1988, and the instruments under it

Status: draft, version 0.1.0, 2026-11-10, target compiler main.
No domain expert has read this against the source.
How each claim was checked: every quotation of an official instrument was typed from a cropped page image that was looked at, and `tools/pdfcheck.py` then confirmed, for the ten lines whose pages have a usable text layer, that each Hebrew word of two or more letters occurs in the text layer of the page (10 lines checked, 0 problems, when the four whole files are named in `SH2781_PDF`, `KT11002_PDF`, `KT10454_PDF` and `KT12149_PDF`).
Ten other quotation lines cannot be checked that way: the five of Kovetz HaTakanot 5164 (a scan with no text layer) and the five footer lines (whose text layer is reversed and garbled); they rest on the cropped images alone.
Every quotation of a consolidation is expanded by `tools/srcquote.py` or `tools/extquote.py` from the deposited excerpt, not typed.
The Hebrew-calendar routine reproduced 30 Kislev 5785 = 31 December 2024 first, and then each footer date and each effective date that the crops print (listed under the answer table).

## Scope

This row is NOT an encoding of the Economic Competition Law, 5748-1988 (Sefer HaChukim 5748 p. 128).
It records five items as typed values with tests, and keeps four of them as expected-red tests.
Item 1 is a record, not a defect of the Law: since the Amendment of 2019 the Law has a new name, and the old name is still the one in the printed titles of some instruments under it.
Item 2 is a citation in the fee schedule to a section that the consolidation prints as repealed.
Item 3 is a citation in the same schedule to a section whose printed text no longer holds the application the item names.
Item 4 is the recital of one fee notice, which prints two index years two years apart.
Item 5 is a citation in a set of regulations of 1964 to a power in a Law that the consolidation prints as repealed.
Each of items 2 to 5 has one sound control beside it.
A date that the sources held do not give is NOTHING; there is no REFUSE, because the target is main.

## Seat

The seat is the applicant who files a request or an appeal with the Competition Tribunal and pays the fee that the regulations set.
This row asks no question from the seat, because it records references, titles and a recital, not rules.

## Coverage

This row does not encode the Law, so almost all of it is out of scope; the table says why for each part.

| Part | Status | Reason |
| --- | --- | --- |
| Item 1: section 1 of Sefer HaChukim 2781 p. 246, and the titles of the Law, the annual notice of Kovetz HaTakanot 12149 p. 482, the fee regulations of 1989, the police-station order of 2000 and the 1964 regulations | encoded | A record of which name each printed title carries. It is not a defect of the Law, and no test of it is red. Only the titles are recorded; the order's operative sentence is deposited only as far as its opening words. |
| Item 2: fee item (a)(3) of regulation 2, section 28, and section 11 of Sefer HaChukim 2781 p. 247 | encoded | A citation whose target the consolidation prints as repealed. |
| Item 3: fee item (b)(5) of regulation 2 and section 30 | encoded | A citation whose target is in force but holds no application of the kind the item names. |
| Item 4: the recitals of Kovetz HaTakanot 11002 p. 948 and, as the control, Kovetz HaTakanot 10454 p. 598 | encoded | Two printed years and the difference between them. The amounts that follow the recitals were looked at and are not deposited or asserted (see the last section). |
| Item 5: the 1964 regulations and section 10א of the 1959 Law, and section 53 of the Law | encoded | A citation to a power in a Law the consolidation prints as repealed. Whether the regulations continue in force is not decided (fork F3). |
| Controls: fee item (a)(1) and section 7; the note under the heading of the Schedule of the 1964 regulations and its regulation 2 | encoded | One sound reference beside the defects. |
| Every other section of the Law, its Schedule and its Chapters | out-of-scope | This row records five items and does not encode the Law. Encoding a section means encoding what it makes a duty, a power or an offence, which needs its own brief, its own seat questions and its own tests; none of that is attempted here. |
| Every other item of the fee schedule, the other regulations of the fee regulations, and every other notice | out-of-scope | The row records items (a)(1), (a)(3) and (b)(5) of regulation 2 and the recitals of two notices. The other items and regulations were not read for this row. |
| The Amendment of 2019 beyond sections 1 and 11, and every other amending instrument of the Law | out-of-scope | Only the two sections that items 1 and 2 read are in the row; the rest of the Amendment is not read here. |

## Fork register

F1. The day the repeal of section 28 took effect, and the day the 1959 Law ceased to be in force, are NOT established.
Reading taken: `the named text is in force on` answers NOTHING on every day, for every recorded citation.
Reading rejected: the publication day of Sefer HaChukim 2781 (10 January 2019) as the day of the repeal, because the cropped pages hold no section on commencement.
The licence is the quotation of section 11 in `ec59-cross-references.l4`.

F2. Whether fee item (b)(5) can be read as applying to the objection of section 30(ו).
Reading taken: the row records only that the item names an application under section 30 and that section 30 as the consolidation prints it holds the Commissioner's instructions and, as its one proceeding before the Tribunal, an objection of subsection (ו); the record says the target does not hold the kind of proceeding named.
Reading rejected: that the item is dead, and that the item covers the objection; the row does not choose.
The heading of section 30 prints the same words as the item (the lines are quoted in `ec59-cross-references.l4`), which is why the item can be read as the nearest proceeding.
The amending instruments that the heading line of section 30 lists were not read, so limb (a) is CONSOLIDATION-ONLY.

F3. Whether the 1964 regulations continue in force.
Reading taken: not decided.
The row records that they name section 10א of the 1959 Law as the source of the power to make them, that the consolidation prints the 1959 Law as repealed (section 53), and that the consolidation's section after section 10 is section 11.
The rules that bear on the question are sections 22 and 23 of the Interpretation Law, 5741-1981, which this row does not apply: section 23 says that when an enactment is repealed the regulations made under it lapse with it, unless the repealing enactment provides provisions in place of the repealed ones, in which case the regulations stand until revoked under the repealing enactment; section 22(2) and (3) say that a repeal does not affect what was done under the repealed law or the rights and duties arising under it.
Those two sections are at lines 126 to 133 of `subjects/il/interpretation-law-1981/source/law.wiki` in this repository (sha256 df3abac9015b4cd919eddece40d46565a97cdf123f78bbe925b687a5f5f0d2ab); they are paraphrased here, not deposited again, and whether the Law provides provisions in place of the repealed ones for section 10א was not read.
Reading rejected: that the regulations are in force, and that they have lapsed.
The hyperlink that the consolidation's 1964 text carries for the words about section 10א points at a section of the current Law whose text this row does not read; the excerpt replaces that link target by a sign, and says so in its first lines.

F4. What the recital of Kovetz HaTakanot 11002 p. 948 should print.
Reading taken: the row records the two years as printed (2023 and 2021) and tests that they are one year apart, as the notice of Kovetz HaTakanot 10454 p. 598 prints them (2022 and 2021); the test for the 2023 notice is red.
Reading rejected: saying why the years stand as they do, and stating that a series of notices exists beyond the two recorded; the notices before Kovetz HaTakanot 10454 were not read.

F5. Whether the old name in a printed title is a defect.
Reading taken: it is a record; the row says what each title prints, and the Law itself is not said to be at fault.
Reading rejected: a red test for item 1.

F6. Whether any instrument other than a notice amends regulation 2 of the fee regulations.
Reading taken: the consolidation's header, which names the 1989 regulations and then lists notices only, is the licence for treating the 1989 page as the latest official text of items (a)(3) and (b)(5); this is CONSOLIDATION-ONLY.
The header is line 5 of the page and is deposited whole.
Reading rejected: searching the official gazette for others; that was not done.

## Answer table

| | Item 2 | Item 3 | Item 4 | Item 5 |
| --- | --- | --- | --- | --- |
| What the citing words say | Fee item (a)(3): an appeal against a requirement of the Commissioner, under section 28. | Fee item (b)(5): an application to regulate monopoly actions, under section 30. | The notice compares the index of November 2023 with the index of November 2021. | The 1964 regulations are made under section 10א of the 1959 Law. |
| What the target says | Section 28 is repealed (section 11 of Sefer HaChukim 2781 p. 247 repeals it; the consolidation prints a repeal marker). | Section 30 is in force; it holds the Commissioner's instructions and an objection to the Tribunal, and no application of the kind. | The notice before it, Kovetz HaTakanot 10454, compares November 2022 with November 2021. | Section 53 of the Law repeals the 1959 Law; the Law has no section 10א. |
| Exists | No (repealed). | Yes, but not as an application. | Both notices exist. | The 1959 Law is repealed, as the consolidation prints it. |
| Limb (a) | Official page read from a crop; that no later instrument touched it is CONSOLIDATION-ONLY. | CONSOLIDATION-ONLY. | n/a | CONSOLIDATION-ONLY. |
| Limb (b) | Official page read from a crop (Kovetz HaTakanot 5164 p. 473); later instruments: CONSOLIDATION-ONLY. | The same page. | The crop of Kovetz HaTakanot 11002 p. 948. | CONSOLIDATION-ONLY: the 1964 gazette issue was not read. |
| Control | Fee item (a)(1) and section 7: same words, same application. | The same control. | Kovetz HaTakanot 10454 p. 598: one year apart. | The Schedule's note and regulation 2: both printed. |
| Page read | Kovetz HaTakanot 5164 p. 473; Sefer HaChukim 2781 p. 247 | Kovetz HaTakanot 5164 p. 473 | Kovetz HaTakanot 11002 p. 948; 10454 p. 598 | none (consolidation only) |

Footer dates printed on the crops, each run through the Hebrew-calendar routine: Sefer HaChukim 2781, 4 Shevat 5779 = 10 January 2019; Kovetz HaTakanot 5164, 9 Adar I 5749 = 14 February 1989; Kovetz HaTakanot 10454, 2 Tevet 5783 = 26 December 2022; Kovetz HaTakanot 11002, 9 Tevet 5784 = 21 December 2023; Kovetz HaTakanot 12149, 5 Tevet 5786 = 25 December 2025.
The effective dates the two recitals print: 20 Tevet 5784 = 1 January 2024 (Kovetz HaTakanot 11002) and 8 Tevet 5783 = 1 January 2023 (Kovetz HaTakanot 10454).
No test depends on these dates.
The notice printed on p. 482 of Kovetz HaTakanot 12149 is in an issue whose footer is dated 25 December 2025; its own signature line is not in the crop and is not stated here.

## The expected-red tests, assertion by assertion

`ec59-tests-xrefs-red.l4` holds eight assertions, all failing; `check.sh` and `encoding.json` declare that count (8).
1. `the citation points at what it says` for fee item (a)(3) is FALSE: the citing words describe a live appeal, and the target is printed as repealed.
2. `the consolidation prints the named text as in force` for fee item (a)(3) is FALSE.
3. `the citation points at what it says` for fee item (b)(5) is FALSE: the item names an application, and the target holds instructions and an objection.
4. `the target holds the kind of proceeding the citing words name` for fee item (b)(5) is FALSE.
5. `the earlier index is the one of the year before the later index` for Kovetz HaTakanot 11002 p. 948 is FALSE.
6. `years between the two indexes printed` for the same recital is 2, not 1.
7. `the citation points at what it says` for the 1964 regulations' power line is FALSE: the citing words name a section of a Law that the consolidation prints as repealed.
8. `the consolidation prints the named text as in force` for the same line is FALSE.

## The check

Run from this folder with `L4=$HOME/.cache/l4-main/98/l4 ./check.sh` (the cached stable binary, 1.6.98); the main build the script ran was 1.6.109 (main, 4c887e0, 2026-11-04).

| module | errors | satisfied | failed | refused | expected failed | main: errors | satisfied | failed | refused | main verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ec59-cross-references.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| ec59-nouns.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| ec59-tests-xrefs-red.l4 | 8 | 0 | 8 | 0 | 8 | 8 | 0 | 8 | 0 | same |
| ec59-tests-xrefs.l4 | 0 | 55 | 0 | 0 | 0 | 0 | 55 | 0 | 0 | same |

The eight errors are the eight failed assertions; no other error, and no refusal.

## The deposits (UNOFFICIAL aids first, then the official crops)

Hebrew Wikisource consolidation of the Law, page "חוק התחרות הכלכלית", revision 3022230 (last edited 2026-07-01T11:00:27Z), fetched by revision id on 2026-11-10: the whole page has sha256 4ded892b7325a0d173a4cb0302dc34236edebe48cc3596974fe3644afcd7418c and 150758 bytes; the excerpt has sha256 5d7b633922accd5f27b004bec650e009e70cd837312fbcb43df384f709917f9e and 5139 bytes.
Hebrew Wikisource consolidation of the fee regulations, revision 2970452 (last edited 2025-12-25T16:00:20Z), the newest at retrieval: whole page sha256 09e09524f97cd10fec82d3cb82c75e9f703985c28183e604e0a7237c2affaf37, 7548 bytes; excerpt sha256 2136c89178e56bb6593263c8039155afe887c7436b0abc049fa3725313300c9b, 5413 bytes.
Hebrew Wikisource consolidation of the police-station order, revision 2925158 (last edited 2025-05-13T09:40:53Z), the newest at retrieval: whole page sha256 140f0d7f227aa2e434f469ca86d4f74711a47426c25d123f383c12e402fe8a7a, 1895 bytes; excerpt sha256 482380ea39041d2917d59349d6f54723bc78752ddebbc8f0b8af857c3c6ec011, 815 bytes.
Hebrew Wikisource consolidation of the 1964 regulations, revision 2926407 (last edited 2025-05-13T11:57:46Z), the newest at retrieval: whole page sha256 f7d67f2d93ba8b12ff0c4670bd3832bd9f7eb3274cc99f7423c8bfd76eb47b99, 3097 bytes; excerpt sha256 74d6a5a6b52496754790b190d1a5b817498787d9066929e5a207d453a3738477, 1671 bytes.
Each excerpt says in its first lines which lines of the whole page it copies; each line carries its number in the whole page, so that `src:N` and `ext:[tag] N` mean the line N of the page.
Three lines of the fee regulations' page and one line of the police-station order's page are deposited only as far as shown, and the rest of each line is not deposited.
Every reading that rests only on a consolidation is CONSOLIDATION-ONLY.
The official pages are six cropped images, each of the lines read and the page's footer line, and nothing else: in `registers/source-bundle/amending-laws/` the crops of Sefer HaChukim 2781 pp. 246 and 247, and in `registers/source-bundle/official/` the crops of Kovetz HaTakanot 5164 p. 473, 10454 p. 598, 11002 p. 948 and 12149 p. 482.
No PDF and no full page is deposited; `registers/source-bundle/SOURCES.json` records, for each of the five whole files, its address, sha256 and size as it was supplied for this row, and gives each crop its own sha256 and size.
The crop of Kovetz HaTakanot 5164 p. 473 is five bands separated by grey bars: the opening line of group (א) of regulation 2, item (3), the opening line of group (ב), item (5), and the footer line.
The crops of the three notices are separated by grey bars into the notice's title, the first operative sentence (for the two recitals) and the footer; the crop of Kovetz HaTakanot 12149 p. 482 holds the title and the footer.
The crops of Sefer HaChukim 2781 hold the title and section 1 and the footer (p. 246), and section 11 with its margin note and the footer (p. 247).

## What was not done

The Kovetz HaTakanot issue of 1964 (printed p. 562) that the consolidation cites for the 1964 regulations was not read.
The official gazette was not searched for an instrument other than a notice that amends regulation 2 of the fee regulations.
The amending instruments that the heading line of section 30 lists were not read.
The day on which Sefer HaChukim 2781 took effect was not established.
The original text of the Law (Sefer HaChukim 5748 p. 128) was not read; section 53 and the heading lines of sections 10 and 11 are the consolidation's.
The Interpretation Law's sections 22 and 23 are paraphrased and not applied.
Looked at and not deposited or asserted: the two amounts that each of the notices of Kovetz HaTakanot 10454 and 11002 prints below its recital, read from the text layer of the page (2,508 and 999 in the first, 2,602 and 1,036 in the second), whose ratios are about 1.037 in both cases; and the text layer of the notice of Kovetz HaTakanot 12149, which prints the index of November 2025 against the index of November 2024.
No test depends on those figures.
