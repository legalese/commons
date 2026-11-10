# Row il-61: three items in the Compensation to Victims of Hostile Actions Law, 5730-1970, where a line of the Hebrew Wikisource consolidation and an official page print different things

Status: draft, version 0.1.0, 2026-11-10, target compiler main.
How each claim was checked: every quotation of an official instrument (the `ext:` lines of `ha61-cross-references.l4`) was typed from a page image that was looked at, in the composed band images deposited, and each Hebrew word of those lines (445 words) was then looked for in the text layer of the corresponding page of the whole file by an ad hoc search (not a tool in `tools/`).
All but 8 distinct words were found; the 8 are words of the footer date lines of printed p. 614 (2 words), p. 799 (1), p. 272 (1) and p. 273 (3), whose footers have a poor text layer, so those footer dates were read from the page image and their digits were checked by the calendar routine below, and one word of the first line of subsection (ג) on printed p. 993, which is in the image and is not in that page's text layer.
Every quotation of a consolidation is expanded by `tools/srcquote.py` from the two deposited excerpts, not typed.
A statement that names "the source notes" comes from notes made while this reference was searched for; those notes are not deposited, and each such statement says which instruments the builder of this row read itself.
`python3 -I tools/hebcheck.py <the Law's excerpt> <the Disabled Persons Law's excerpt> *.l4 NOTES.md` exits 0.
The Hebrew dates were converted with the Hebrew-calendar routine in `tools/hebcal.py`, run through `tools/datepairs.py`, which reproduces the routine's own control (30 Kislev 5785 = 31 December 2024) first and then the seven pairs the row types.
No domain expert has read this against the source.

## Scope

This row is NOT an encoding of the Compensation to Victims of Hostile Actions Law, 5730-1970 (called "the Law" here; the English titles are the row's renderings, not enacted titles).
It records three items, as typed values with tests, and keeps the three failing pairs in an expected-red module, with a control beside each.
The row records what each instrument prints and what the consolidation prints; it says nothing about whether the Law or any text is right, about what a court would do, or about who gains or loses.
A consolidation is an unofficial aid: for a line of it the row says "the consolidation prints", never "the Law says".
A day on which an instrument took effect is not typed anywhere, because none is read; there is no REFUSE, because the target is main.

**Item I1: a word in the list of s 4(א).**
Section 4(א) of the Law, as the consolidation prints it, opens a list of sections of the Disabled Persons (Compensation and Rehabilitation) Law, 5719-1959, and the list as printed includes the entry 4ב.
Section 42(1)(ב) of the instrument printed in Sefer HaChukim 3072, printed p. 614 (issued 14 Av 5783, 1 August 2023), directs that the word "4ב," be deleted from the list in section 4 of the Law, that 5א be added after 5, and that the words 7ב עד 7ו go in place of other words.
The consolidation prints 5א and 7ב עד 7ו in the list and also prints 4ב.
The consolidation of the Disabled Persons Law prints its section 4ב as "(בוטל)", with an amendment tag.
Sefer HaChukim 3549, printed p. 799, section 7, adds a subsection (ג) to section 4 of the Law after subsection (ב) and, in the words held, names no word of the list in subsection (א).

**Item I2: a number in the list of s 7(א).**
Section 7(א) of the Law, as the consolidation prints it, opens a list of sections of the Soldiers' Families Who Fell in the Campaign (Compensation and Rehabilitation) Law, 5710-1950, and the list as printed includes the entry 22.
Section 2 of the instrument printed in Sefer HaChukim 2118, printed p. 36 (issued 15 Kislev 5768, 25 November 2007), is an amendment of that law and prints that section 22 of the principal law is repealed.
Sefer HaChukim 3493, printed pp. 272 to 273 (issued 10 Shvat 5786, 28 January 2026), in its section 22 repeals section 29ה of the principal law and, in item (3)(א) of its section 26, edits the list in section 7(א) of the Law; the words of that item name no entry 22.

**Item I3: the grant of 200,000 new shekels.**
The consolidation prints, in subsection (ד1) of section 4א of the Law, a special additional grant of 200,000 new shekels to an orphan of both parents.
Section 1 of the instrument printed in Sefer HaChukim 2573, printed p. 1160 (issued 7 Av 5776, 11 August 2016), inserts a subsection (ד2) in section 4 of "the principal law", which it defines as the Compensation to Victims of Hostile Actions (Amendment 30) Law, 5771-2011, giving an orphan of both parents a grant of 200,000 new shekels.
The two texts put an amount of 200,000 in different places: the consolidation in section 4א of the Law, the instrument in section 4 of the 2011 instrument.

## Seat

The seat is the injured person, or the relative of a person who died, to whom the Law gives compensation.
This row asks no question from the seat, because it records three items and their controls, not rules.

## Coverage

This row does not encode the Law, so almost all of it is out of scope; the table says why for each part.

| Part | Status | Reason |
| --- | --- | --- |
| Item I1: the entry 4ב of the list in s 4(א), the instruction in s 42(1)(ב) of Sefer HaChukim 3072 that deletes it, and the entries 5א and 7ב עד 7ו as the control | encoded | A finding about what a consolidation prints beside what an official instruction directs. Only the entries named are typed; the rest of the list is quoted as the consolidation prints it and is not discussed. |
| Item I2: the entry 22 of the list in s 7(א), the repeal in s 2 of Sefer HaChukim 2118, and the entries 10, 9ג and 29ה as controls | encoded | A finding about a list that names a section an official instrument repeals. Only the entries named are typed. |
| Item I3: the grant of 200,000 new shekels in s 4א(ד1) as the consolidation prints it, the insertion of (ד2) in s 4 of the 2011 instrument by s 1 of Sefer HaChukim 2573, and the 550,000-shekel grant in s 4(ג) of the 2011 instrument as the control | encoded | A finding about where two texts put one amount. The row records the amount and the place, not the conditions of the grant. |
| The conditions of the grants (who is an orphan of both parents, the age limits, the dates before which a death must have happened) | out-of-scope | Encoding a condition means encoding what it requires, which needs its own brief, its own seat questions and its own tests; the row quotes the lines and types only the amount and the place, and says nothing about the conditions. |
| The other entries of the two lists, and the sections of the Disabled Persons Law and of the Soldiers' Families Law that they cite | out-of-scope | The row types the entries named above. What a cited section says was not read, except that the consolidation prints section 4ב of the Disabled Persons Law as cancelled. |
| Every other provision of the Law, including what compensation is, who is entitled and how it is paid | out-of-scope | This row records three items and does not encode the Law; the row says nothing about those provisions. |
| The day each instrument took effect, and any other revision of either consolidation | out-of-scope | Not read: the row holds the issue date of each instrument and the current revision of each consolidation, and rests on nothing else. |

## Fork register

F1. What the note "(בוטל)" printed for section 4ב in the consolidation of the Disabled Persons Law means for the list entry.
Reading taken: that the consolidation prints that section as cancelled, which is limb (a) for item I1 and is CONSOLIDATION-ONLY.
Reading rejected: that the instrument of Sefer HaChukim 3072 is the instrument that cancelled section 4ב of that law; the band says nothing about it and the row does not tie the consolidation's tag to an instrument.

F2. The day on which each instrument took effect.
Reading taken: not read; the row records the issue date of each instrument, which is the footer date, and no day of effect, and never says "since".
Reading rejected: treating the issue date as the day of effect; the sections on commencement are not among the lines deposited.
The source notes say that section 4 of Sefer HaChukim 2118 sets 1 January 2008; the row did not deposit that section and does not type that day.

F3. Whether the list in section 4(א) reads today, in the latest official text, without the entry 4ב.
Reading taken: Sefer HaChukim 3072 directs the deletion, and Sefer HaChukim 3549, section 7, adds a subsection to section 4 and names no word of the list in subsection (א); what the consolidation prints today is CONSOLIDATION-ONLY.
Reading rejected: saying that no later instrument re-adds the word; of Sefer HaChukim 3493 the row holds only the opening of section 26 and its item (3)(א), which edits the list in section 7(א), so it does not say whether that instrument touches the list in section 4(א).

F4. Which law "the principal law" is in section 22 of Sefer HaChukim 3493.
The band of printed p. 272 does not name the law.
Reading taken: the Soldiers' Families Law, because the text layer of PDF pages 1 and 2 of the file (not deposited) gives, as the title of the instrument, an amendment of the Soldiers' Families Law (Amendment 47) and defines "the principal law" as that law, and section 26, which follows section 22, opens by naming the Law (the Hostile Actions Law) in the band.
Reading rejected: reading that title from the deposited band; it is not on it.

F5. What section 22 of the Soldiers' Families Law said before it was repealed.
Not read; the row types no content for it, and no page held shows the text of any section of that law.

F6. Whether the consolidation's subsection (ד1) and the 2016 instrument's subsection (ד2) are one grant.
Reading taken: the row does not decide; it records that both print an amount of 200,000 new shekels for an orphan of both parents, that the wording differs (the consolidation adds words about a death before the commencement of "this law" and a figure 37, and does not say "in addition to the grants under (ג) and (ד1)"), and that the places differ.
Reading rejected: calling either text the wrong one.
The instrument that inserted subsection (ד1) into section 4 of the 2011 instrument was not found among the pages held, and the row does not say which it is.

F7. Which pages of the 2011 instrument are read.
Reading taken: subsection (ג) of section 4, whole, and the heading of section 4 with the first two lines of its subsection (א), to show that (ג) is in section 4 of that instrument; subsection (ד) is not quoted and not read.

## Answer table

| | Item I1 | Item I2 | Item I3 |
| --- | --- | --- | --- |
| What the citing words say | The list in s 4(א) includes the entry 4ב (consolidation). | The list in s 7(א) includes the entry 22 (consolidation). | Subsection (ד1) of section 4א prints a grant of 200,000 new shekels (consolidation). |
| What the target says | Section 4ב of the Disabled Persons Law is printed as cancelled (consolidation); the official instruction in section 42(1)(ב) of Sefer HaChukim 3072 deletes the word from the list. | Section 2 of Sefer HaChukim 2118 prints that section 22 of the principal law is repealed (read from the page image). | Section 1 of Sefer HaChukim 2573 inserts (ד2), a grant of 200,000 new shekels, in section 4 of the 2011 instrument (read from the page image). |
| Exists | No (consolidation of the Disabled Persons Law); an instruction deletes the word. | No (an official instrument repeals it). | The grant is printed in two places; the places differ. |
| Limb (a) | CONSOLIDATION-ONLY for the target; the instruction was read from the page image. | Read from the page image of Sefer HaChukim 2118. | The 2016 instrument was read from its page image; the consolidation's line is CONSOLIDATION-ONLY. |
| Limb (b) | The instruction was read from the page image; Sefer HaChukim 3549, section 7, names no list word; what the consolidation prints today is CONSOLIDATION-ONLY. | The list as printed is CONSOLIDATION-ONLY; the item (3)(א) of Sefer HaChukim 3493, read from the page image, edits the list and names no entry 22. | What the consolidation prints today is CONSOLIDATION-ONLY. |
| Control | The entries 5א and 7ב עד 7ו: added by the same instruction and printed by the consolidation. | The entries 10 (amended by the same instrument as the repeal), 9ג (added to the list in 2026 and printed) and 29ה (repealed and deleted from the list in 2026, and not printed). | The 550,000-shekel grant in section 4(ג) of the 2011 instrument and the 2016 insertion are put in the same law and section. |
| Pages read | Sefer HaChukim 3072, printed p. 614; Sefer HaChukim 3549, printed p. 799 | Sefer HaChukim 2118, printed p. 36; Sefer HaChukim 3493, printed pp. 272 and 273 | Sefer HaChukim 2573, printed p. 1160; Sefer HaChukim 2307, printed pp. 992 and 993 |

The consolidation lines are lines 50 and 153 to 154 (I1), 104 (I2) and 69 and 84 (I3) of the whole pages; the current revision of the Law is the revision the source notes name, so its line numbers held without re-reading.

## The expected-red finding, assertion by assertion

`ha61-tests-xrefs-red.l4` holds six assertions, all failing, and `check.sh` and `encoding.json` declare that count (6).
1. Every entry the consolidation prints in the list of s 4(א) is one that no official instruction read by this row deletes: it is FALSE, because the entry 4ב is printed and deleted.
2. The number of entries of that list that the consolidation prints and an official instruction deletes is 0: it is 1.
3. Every entry the consolidation prints in the list of s 7(א) names a section that no official instrument read by this row repeals: it is FALSE, because the entry 22 is printed and its section repealed.
4. The number of entries of that list that the consolidation prints and whose section an official instrument repeals is 0: it is 1.
5. The consolidation and the 2016 instrument put the grant of 200,000 new shekels in the same law: it is FALSE.
6. The consolidation and the 2016 instrument put the grant in the same section: it is FALSE.
The row records this and says nothing about what the citing words are for or whether anyone should change them.

## The check

Run from this folder with `L4=$HOME/.cache/l4-main/98/l4 ./check.sh`; the main build was 1.6.109 (main, 4c887e0, 2026-11-04).

| module | errors | satisfied | failed | refused | expected failed | main: errors | satisfied | failed | refused | main verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ha61-cross-references.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| ha61-nouns.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| ha61-tests-xrefs-red.l4 | 6 | 0 | 6 | 0 | 6 | 6 | 0 | 6 | 0 | same |
| ha61-tests-xrefs.l4 | 0 | 72 | 0 | 0 | 0 | 0 | 72 | 0 | 0 | same |

The six errors are the six failed assertions; no other error, and no refusal.

## The deposits

Hebrew Wikisource consolidation of the Law, revision 3037611 (timestamp 2026-08-02T11:00:21Z), an UNOFFICIAL aid: the whole page has sha256 b06466bb9bd24172efe0897e3e2bb5b259917f14c9e6dbbe225db8b3cc006d3c and 120261 bytes (444 lines) as retrieved on 2026-11-10 through the MediaWiki API (the current revision at that time); the excerpt deposited has sha256 eaec70142ea148540b96726b624a785bbef1bb85f544f8bc38bcfefa45f1c751 and 9486 bytes.
Hebrew Wikisource consolidation of the Disabled Persons Law, revision 3037613 (timestamp 2026-08-02T11:00:30Z), an UNOFFICIAL aid: the whole page has sha256 e4ec9c7370e92367d5915c3ec6d93179f14a8257045888610f7e000f58f39048 and 235485 bytes (1212 lines); the excerpt deposited has sha256 3dc04438f3be59d0089c72616e06be9f3b4c8b3098813e2b65470e27ced44166 and 1064 bytes.
Each excerpt says in its first lines which lines of the whole page it copies, and each line carries its number in the whole page, so that `src:N` means line N of the Law's page and `src:dis:N` means line N of the Disabled Persons Law's page.
The official pages are eight composed images of cropped bands, each with its bands separated by a grey bar, each viewed after it was composed, in `registers/source-bundle/official/`:

| image | instrument | printed page | PDF page | bytes | sha256 |
| --- | --- | --- | --- | --- | --- |
| `official/sh3072-5783-p614-bands.png` | Sefer HaChukim 3072 | 614 | 36 of 44 | 35725 | 17320000399248d71d71d160c53c2ede45b421cb5287ea9b8613f009769d2b25 |
| `official/sh3549-5786-p799-bands.png` | Sefer HaChukim 3549 | 799 | 3 of 4 | 29809 | 9c5fd1173860525cde14cb1f704257a8659fa00eafa5f1668f83e3fa9ad130c0 |
| `official/sh2118-5768-p36-bands.png` | Sefer HaChukim 2118 | 36 | 1 of 1 | 24968 | 0d08573d24df8cf3b79271a8872c95bcc75b9adf89589e9f12d41b8721b6e5c6 |
| `official/sh3493-5786-p272-bands.png` | Sefer HaChukim 3493 | 272 | 8 of 12 | 18136 | 918007898e6fb95a1bb5bdc2e508b08820950705f6dc5a0852e36ee30e291be0 |
| `official/sh3493-5786-p273-bands.png` | Sefer HaChukim 3493 | 273 | 9 of 12 | 14601 | 1e340972caf7a38752ec3b486183ee15f55c20e323fe322abd1795dfb988dfa9 |
| `official/sh2573-5776-p1160-bands.png` | Sefer HaChukim 2573 | 1160 | 8 of 8 | 46829 | adf69b3938e2f93b928c5e44d80727f08769cad8c31940075dad1624cda737c4 |
| `official/sh2307-5771-p992-bands.png` | Sefer HaChukim 2307 | 992 | 1 of 2 | 23090 | 21aa9d19bbfe2314fe57cd6ba8f4d3bdf194e16eedb5bc77cbe881663b930714 |
| `official/sh2307-5771-p993-bands.png` | Sefer HaChukim 2307 | 993 | 2 of 2 | 30092 | 195623c4410e2ecf18eb33156bfbd67d17275f15dc7e1cc6446a0d8978eb6128 |

The six whole files are not deposited; `registers/source-bundle/SOURCES.json` records their sha256 and sizes as supplied, and the Knesset address of the file for Sefer HaChukim 2573 (https://fs.knesset.gov.il/20/law/20_lsr_348525.pdf); for the other five files the address was not recorded.

| whole file | pages | bytes | sha256 |
| --- | --- | --- | --- |
| Sefer HaChukim 3072 | 44 pages | 608521 | cbe786e55487b8ecde65cdda9c996bf29f6ee2113f87f8f42d220959c9df1bef |
| Sefer HaChukim 3549 | 4 pages | 98087 | b8acfe349e334efd80399a32e4aae90254a26cc461fcab002681f47a65d5926b |
| Sefer HaChukim 2118 | 1 page | 84949 | 1bfafa925cd3ee0334bde962b64dd99ccd1250b74324df37b577c20908118c8d |
| Sefer HaChukim 3493 | 12 pages | 173974 | 1f09dd46de2685d07d1e7483e47fe12a83ce7632bc10fbfd7332ef3937db799f |
| Sefer HaChukim 2573 | 8 pages | 130913 | cbe1bc999859ff5a51320d44842e95d8a45d871f31b8ed9e42d534090d6aa97b |
| Sefer HaChukim 2307 | 2 pages | 84448 | af9c70ca7b29d40adfeaa1569dd6226ee0d8c8a360d36871a70e4b5733b15509 |

The page of Sefer HaChukim 2573, printed p. 1160, is a crop and not a page extract: besides sections 1 and 2 of the amending instrument the page carries the signature block, a footnote and the imprint line with the price, none of which belongs to the item, so the rule that a page is extracted only when every line of it belongs to the item sent it to a crop.
No page extract is deposited, so the row ships no page-checking tool.
No full page of any file is deposited.

## What was not done

The sections on commencement of the instruments were not deposited and are not read for a day of effect.
Of Sefer HaChukim 3493 only two bands are deposited; the rest of section 26 is not read.
The instrument that inserted subsection (ד1) into section 4 of the 2011 instrument was not found.
The row does not read the Disabled Persons Law or the Soldiers' Families Law beyond what the consolidation prints for section 4ב.
The amendment tag that the consolidation of the Disabled Persons Law prints beside section 4ב is not tied to an instrument.
