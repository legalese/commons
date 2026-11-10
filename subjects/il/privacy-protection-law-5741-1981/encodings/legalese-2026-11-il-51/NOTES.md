# Row il-51: ten recorded defects in the cross-references of the Privacy Protection Law, 5741-1981, and of five sets of regulations made under it, with seven sound controls

Status: draft, version 0.1.0, target compiler main.
No domain expert has read this against the source.
Every claim below was checked against a text in the source bundle or a page image named beside it; where it was not, it says so.
The Hebrew typed from a page image is not machine-checked against the image: only the Sefer HaChukim lines are checked, and only word by word against a text layer (section 2).

## 1. Scope

This row is not an encoding of the Privacy Protection Law, 5741-1981, and not an encoding of any regulation made under it.
It records ten defects, seven sound controls and one rounding rule as typed values that tests check, and keeps each defect as an expected-red test.
For each citation the row types two descriptions, what the citing words say they point at and what the target is, and records where each of the two readings comes from.
Nine of the ten defects are citations whose two descriptions differ; the tenth (P6) is a rounding rule set against the per-person rates a notice prints.
The seat is the individual to whom the Law is applied: the individual about whom personal information is held in a database.
This row asks no question from that seat, because it records references and not duties, so no `@export` module is written.
"Amendment 13" is the Privacy Protection Law (Amendment 13), 5784-2024, Sefer HaChukim 3287 of 14 August 2024.

## 2. Sources

The Law is read from the Hebrew Wikisource consolidation of the page "חוק הגנת הפרטיות", revision 3088217, last edited 2026-10-12T09:00:24Z, fetched on 2026-11-10.
The revision id was not returned with the page; I took it from the revision list fetched about two minutes after the page, so it is inferred.
The revisions of the five regulation pages come from one batch revision query on 2026-11-10; they are in the table.
All are unofficial aids, and every statement that rests only on one of them says CONSOLIDATION-ONLY.
The Interpretation Law, 5741-1981, is read in place from `../../../interpretation-law-1981/source/law.wiki` (sha256 df3abac9015b4cd919eddece40d46565a97cdf123f78bbe925b687a5f5f0d2ab); its revision was not matched again here.

| consolidation | deposit | Wikisource revision (last edited) | sha256 of the whole page | sha256 of the deposit |
| --- | --- | --- | --- | --- |
| the Law | excerpt, 40 of 1267 lines (one of them blank) + 5 lines of header | 3088217 (2026-10-12T09:00:24Z) | 9a80db7fd85ce5bf02159e7f8ecc5de60f966618abcc4c71fdc02a2673540451, 274480 bytes | 6dc3b9ff9cb25b4af4a096fbe37423b3d219b774b8fb288d7e3de6644f4a195b |
| 2023 regulations (information from the European Economic Area) | excerpt | 2926316 (2025-05-13T11:46:27Z) | c025664dcd43cf637c21e14f5d7077a516404bfaa3840547f18012ac87a355d7, 12343 bytes | 41ad280040028c59dd6371115fe15e00f39bdf49c5c46c16279566781de144f5 |
| 1986 regulations (public bodies) | excerpt | 2998985 (2026-03-18T09:30:27Z) | 98c40b014f081e89e7c3396489b0c3f61b13dec3e47d12127c6744e94d4ff46a, 11312 bytes | 15b010a1bee6a5c4f9ff634a798e15dc7abfca54d6d4b913be8f25ab74877e84 |
| 1981 regulations (inspection) | whole page | 2998986 (2026-03-18T09:30:34Z) | 064b13a89f07c36edb369a8b46431c7812bf7b06a204ee83bf9d3fd7737775f6 (the whole page is the deposit) | 064b13a89f07c36edb369a8b46431c7812bf7b06a204ee83bf9d3fd7737775f6 |
| 2001 regulations (transfer abroad) | whole page | 2926317 (2025-05-13T11:46:32Z) | aacc899f50bdeddf3cb0fbe3982217926a69186f9d89c82ae88016dc8f847c55 (the whole page is the deposit) | aacc899f50bdeddf3cb0fbe3982217926a69186f9d89c82ae88016dc8f847c55 |
| 2004 regulations (fixed administrative fine) | whole page | 2927009 (2025-05-13T13:20:38Z) | cbb4d34e22ebab196abc20ca203095d06cfa8250a58bd0dc0e05e854a088f1e6 (the whole page is the deposit) | cbb4d34e22ebab196abc20ca203095d06cfa8250a58bd0dc0e05e854a088f1e6 |

An excerpt carries a header giving the revision, the whole-page sha256 and the original line numbers, and a tag in an `ext:[law] N` line cites the ORIGINAL line number of the whole page.
`../../registers/source-bundle/SOURCES.json` gives the URL, retrieval date, sha256 and size of every file; the sha256 values were recomputed on 2026-11-10 (Python hashlib, SHA-256).
The official pages are in `../../registers/source-bundle/amending-laws/` and `../../registers/source-bundle/official/`.
Sefer HaChukim 3287 comes from the Knesset's server.
Only the pages the row reads are deposited, and the whole files are not in the bundle: the url, retrieval date, sha256 and size of each whole file as downloaded are kept in `SOURCES.json`, and each extract has its own entry.
The Sefer HaChukim extract holds printed pp. 1430, 1433, 1461, 1472 and 1495 (PDF pages 2, 5, 33, 44 and 67 of the whole file; extract pages 1 to 5 in that order), with a page image of each beside it.
Printed pp. 1438 and 1474 are deposited only as cropped images, with no PDF page: the crop of p. 1438 shows the line of s 16 and the footer, and the crop of p. 1474 shows item 4 of the First Schedule with its paragraph (א), the definition paragraph (3) of the Third Schedule, and the footer, because the rest of each page is text the row does not read.
Kovetz HaTakanot 6299 and 6913 come from `olaw.org.il`, a non-official archive that hosts scans of Reshumot issues and is not a government site; the extract of 6299 holds printed pp. 323 and 324 (PDF pages 7 and 8 of 17; the scan has no text layer; the two pages are not quoted), and the extract of 6913 holds printed p. 1430 (PDF page 2 of 8).
Kovetz HaTakanot 10637 (p. 1722) and Yalkut HaPirsumim 15000 (p. 654) are deposited as deliberate CROPS of the page image, with no PDF: the crop of 10637 starts at regulation 7, and the crop of 15000 shows the opening of the notice and its footnotes.
The crop of 15000 also shows other amounts of the same section of the Law; no figure of them is quoted or used by this row.

| instrument | pages read from the page image | what the page shows |
| --- | --- | --- |
| Sefer HaChukim 3287, 14.8.2024 (10 Av 5784), Amendment 13 | pp. 1430, 1433, 1438, 1461, 1472, 1474, 1495 (p. 1495 is rendered at 80 dpi, a lower resolution than the others) | p. 1430: s 1 (replacement of terms, in every place in the Law) and the new definition of בעל שליטה; p. 1433: the definition of הרשות and s 3 (repeal of s 7); p. 1438 (cropped image): s 16 (repeal of s 17א); p. 1461: the rounding words of s 23לב(ב); p. 1472: s 34 (repeal of ss 26 and 31א); p. 1474 (cropped image): First Schedule item 4(א) and the Third Schedule definition paragraph (3); p. 1495: ss 74 and 75 (commencement and application) |
| Kovetz HaTakanot 6913, 17 Av 5770 (28 July 2010) | p. 1430 | the Schedule of the 2004 regulations as replaced: the section numbers listed in column A |
| Kovetz HaTakanot 10637, 16 Iyar 5783 (7 May 2023) | p. 1722 (crop) | regulation 7 of the 2023 regulations |
| Yalkut HaPirsumim 15000, 26 Tishrei 5787 (7 October 2026) | p. 654 (crop) | the notice's updated per-person rates and its rounding footnote |

The Hebrew of an official page is typed by me from the page image on a line `-- ext:[SH 3287 p.<page>, read from the page image] | ...`, `-- ext:[KT <issue> p.<page>, ...] | ...` or `-- ext:[YP 15000 p.654, ...] | ...` in `priv51-cross-references.l4`.
`tools/pdfcheck.py` checks every Hebrew word of a Sefer HaChukim line against the text layer of that page in the extract; it cannot see the order of the words, because these text layers reverse and interleave runs, so the page image is what the typing was read from.
The lines typed from pp. 1438 and 1474, which are deposited only as cropped images, are not checked by it (its output counts them).
The Kovetz HaTakanot and Yalkut HaPirsumim lines are not checked by any tool: those pages are images.
The Hebrew of the consolidations is expanded mechanically by `tools/extquote.py` (`ext:[law]`, `ext:[eea]`, `ext:[pb]`, `ext:[inspect]`, `ext:[abroad]`, `ext:[fine]` and `ext:[interp]` lines).
`tools/hebcheck-all.sh *.l4 NOTES.md` finds every other run of Hebrew in the `.l4` files and in this file in the seven consolidations, and exits 0.
The dates that carry a Hebrew date on an instrument were checked with the calendar routine, after it reproduced the control date 30 Kislev 5785 = 31 December 2024: 10 Av 5784 = 14 August 2024, 16 Iyar 5783 = 7 May 2023 (and the signature date, 12 Iyar 5783 = 3 May 2023), 17 Av 5770 = 28 July 2010 (and 16 Tammuz 5770 = 28 June 2010), 26 Tishrei 5787 = 7 October 2026.

## 3. Files

| file | what it holds |
| --- | --- |
| `priv51-nouns.l4` | the kinds of provision, the three sources of a reading, the record of a citation and of a per-person rate; no rule |
| `priv51-cross-references.l4` | the four functions, the rounding function, and one typed value per citation and per rate, with the words of the texts quoted beside it |
| `priv51-tests-xrefs.l4` | 66 assertions: the controls point at what they say, the rounding arithmetic, the rates, what was read from where, what the descriptions say, the day each named text stopped being in force, and the Interpretation Law section 25 readings |
| `priv51-tests-xrefs-red.l4` | 20 assertions that fail, on purpose (section 7) |
| `check.sh`, `fetch-main-l4.sh` | the check; `check.sh` declares 20 expected failures for the file above |
| `tools/` | `extquote.py`, `hebcheck.py`, `hebcheck-all.sh`, `pdfcheck.py` |

## 4. Coverage

| item | status |
| --- | --- |
| P1: First Schedule item 4(א) to s 7 | encoded; a defect; control: the same item's words "ראש הרשות" to the definition in s 3 |
| P2: Third Schedule definition paragraph (3), the person called בעל המאגר | encoded; a defect; control: s 12(ג) to s 12(א) and (ב) |
| P3(a): 1986 regulation 1, terms "כהגדרתם בסעיף 7 לחוק" | encoded; a defect; control: regulation 7(ג) to s 23ג |
| P3(b): 1986 regulation 1, "פנקס" "כמשמעותו בסעיף 12 לחוק" | encoded; a defect on the literal reading, with a documented fork; same control as P3(a) |
| P4: 1981 inspection regulations 2(א), 5(א), 7(ב), "הרשם רשאי להאריך" | encoded; a defect; control: regulation 8 to regulation 5 |
| P5: 2023 regulation 7, "מידע רגיש לפי סעיף 7 לחוק" | encoded; a defect, with a documented fork; control: regulation 7 to regulation 2 |
| P6: s 23לב(ב) rounding against the per-person rates | encoded as a rounding function and three typed rates; two failing assertions; controls: the rate of 50 as enacted, and the notice's own reading |
| P7: 2001 regulations 2 and 3, "בעל מאגר מידע" and "בעל מאגר המידע" | encoded; a defect; control: regulation 3 to regulation 1 |
| P8: 2004 schedule, column A, to s 31א(א)(1) to (7) and to s 17א(א) and (ב) | encoded; two defects; control: the schedule's s 17ד |
| the rest of the Law, every section other than those named above | out-of-scope: this row records cross-references and one rounding rule, and writes no rule of the Law; encoding the Law's own duties and powers is a different task, and nothing here should be read as a statement about them |
| every other citation in the Law, its Schedules and the five sets of regulations | out-of-scope: not examined; the row records the citations that were examined and says nothing about the rest of the text, so the absence of a row is no finding that a citation is sound |
| other regulations and notices made under the Law, and the other instruments that amend the five sets of regulations | out-of-scope: not read for this row, so the row makes no statement about them or about whether they were conformed to Amendment 13 |
| the other items of the First Schedule and the other paragraphs of the Third Schedule definition | out-of-scope: only the words listed above were examined; the other words of the same Schedules were not read for defects |
| the Interpretation Law other than ss 22 and 25 | out-of-scope: read only for the two sections the forks need |

## 5. The citations: answer table

"Stands today" means that the target is in the official text today as far as the sources read show; for every defect that is a statement about Amendment 13 as published, and that no later instrument changed it is CONSOLIDATION-ONLY.
Limb (a) asks whether the target is what the citing words say; limb (b) asks whether the citing words still read so in the latest official text of the citing provision.
"Official, with the caveat" means the page of the official instrument was read from the page image, and that no later instrument touched the words rests on the consolidation's list of amending instruments, which is CONSOLIDATION-ONLY.

| item | citing words | target | stands today | limb (a) | limb (b) | page read |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | First Schedule item 4(א): "כרשם לעניין סעיף 7 לחוק הגנת הפרטיות" | s 7, repealed by s 3 of Amendment 13 | no | official, with the caveat | official, with the caveat | SH 3287 pp. 1433, 1474, 1495 |
| P1 control | the same item: "את ראש הרשות" | the definition of ראש הרשות in s 3 | yes (consolidation) | consolidation only | official, with the caveat | SH 3287 p. 1474 |
| P2 | Third Schedule definition (3): "שבעל המאגר כפוף בשלו" | no definition of בעל המאגר; the Law's person is בעל שליטה | no | official, with the caveat | official, with the caveat | SH 3287 pp. 1430, 1474 |
| P2 control | s 12(ג): "סעיפים קטנים (א) ו־(ב)" | subsections (א) and (ב) of s 12 | yes | consolidation only | consolidation only | none |
| P3(a) | 1986 regulation 1: "כהגדרתם בסעיף 7 לחוק" | s 7, repealed | no | official, with the caveat | consolidation only | SH 3287 pp. 1433, 1495 |
| P3(b) | 1986 regulation 1: "כמשמעותו בסעיף 12 לחוק" | s 12 as it reads now: the register called מרשם | the section yes; the word פנקס no | official, with the caveat | consolidation only | SH 3287 p. 1430 |
| P3 control | 1986 regulation 7(ג): "בהתאם לסעיף 23ג לחוק" | s 23ג, headed סייג לאיסור | yes (consolidation) | consolidation only | consolidation only | none |
| P4 | 1981 regulations 2(א), 5(א), 7(ב): "הרשם רשאי להאריך" | ראש הרשות, which Amendment 13 puts in the place of הרשם in the Law | the office called הרשם: no | official, with the caveat | consolidation only | SH 3287 p. 1430 |
| P4 control | 1981 regulation 8: "כאמור בתקנה 5" | regulation 5 | yes | consolidation only | consolidation only | none |
| P5 | 2023 regulation 7: "מידע רגיש לפי סעיף 7 לחוק" | s 7, repealed | no | official, with the caveat | official, with the caveat | KT 10637 p. 1722; SH 3287 pp. 1433, 1495 |
| P5 control | 2023 regulation 7: "כאמור בתקנה 2" | regulation 2 | yes | consolidation only | consolidation only | none |
| P7 | 2001 regulations 2 and 3: "בעל מאגר מידע", "בעל מאגר המידע" | בעל שליטה, which Amendment 13 puts in the place of בעל מאגר | the person called בעל מאגר: no | official, with the caveat | consolidation only | SH 3287 p. 1430 |
| P7 control | 2001 regulation 3: "לפי תקנה 1" | regulation 1 | yes | consolidation only | consolidation only | none |
| P8(a) | 2004 schedule column A: "סעיף 31א(א)(1)" to "(7)" | s 31א, repealed by s 34 of Amendment 13 | no | official, with the caveat | official, with the caveat | SH 3287 pp. 1472, 1495; KT 6913 p. 1430 |
| P8(b) | 2004 schedule paragraph (5): "סעיף 17א(א)" and "(ב)" | s 17א, repealed by s 16 of Amendment 13 | no | official, with the caveat | official, with the caveat | SH 3287 pp. 1438, 1495; KT 6913 p. 1430 |
| P8 control | 2004 schedule paragraph (7): "סעיף 17ד" | s 17ד, headed דיוור ישיר | yes (consolidation) | consolidation only | official, with the caveat | KT 6913 p. 1430 |

P6 is not a citation. The notice of 7 October 2026 (YP 15000 p. 654, read from a crop of the page image) prints 51.18 for 50, 102.36 for 100, 2.05 for 2, 4.09 for 4 and 8.19 for 8 shekels, and a footnote that the rounding is done on the final amount of the sanction after the multiplication; the first words of s 23לב(ב) were read from SH 3287 p. 1461.
The rates as enacted are 50, 100, 2, 4 and 8: 50 and 100 are multiples of ten shekels, and 2, 4 and 8 are not; of the printed rates none is a multiple of ten.
(The enacted figures 100 and 8 are the words the notice replaces; 50, 2 and 4 are also in the consolidation, CONSOLIDATION-ONLY.)

## 6. Fork register

Each fork records the reading taken and the reading rejected or left open, with the Hebrew.
The red assertions follow the LITERAL reading of the citing words in every case; the row does not rule between readings and does not call any citation something to be fixed.

**D0. The day Amendment 13 took effect.**
Taken: the later day, 15 August 2025.
Rejected, not excluded: 14 August 2025.
Section 74(א) says the Law takes effect one year from the day of its publication; the Law was published on 14 August 2024.
Which of the two days is first depends on how the days of a period are counted, and I did not look that up.
```
-- ext:[SH 3287 p.1495, read from the page image] | (א) תחילתו של חוק זה שנה מיום פרסומו (להלן – יום התחילה).
```
The effect on the row is only that `the named text is in force on` says NOTHING for 14 August 2025 and before, and JUST FALSE from 15 August 2025.
Section 74(ב), read from the page image, defers one other section's commencement; none of the repeals this row cites is deferred on p. 1495, which I read.
Page 1496 was not opened.

**D1. NOTHING for a day before the end of the named text.**
Taken: NOTHING.
Rejected: JUST TRUE.
No source read says whether the named text was amended between its enactment and its repeal or replacement, so a day before the end is not answered.

**P1. The First Schedule item 4(א) and the historical text of a decision.**
Reading A (taken by the red tests): the Schedule is part of the Law, so its words cite s 7, which prints no text.
Reading B (recorded, not rejected): the Schedule gives itself as the wording of a Government decision, so item 4(א) is the historical text of that decision and cites s 7 as it stood in 2022, not a live provision.
The words of the definition that give the Schedule that role, on p. 1433 and in the consolidation:
```
-- ext:[SH 3287 p.1433, read from the page image] | "הרשות", "הרשות להגנת הפרטיות" – הרשות להגנת הפרטיות שהוקמה ופועלת על פי החלטות הממשלה מס' 4660 מיום 19 בינואר 2006, מס' 4820 מיום 28 ביוני 2012, מס' 3019 מיום 7 בספטמבר 2017 והחלטת הממשלה מס' 1890 מיום 2 באוקטובר 2022 שנוסחה מובא בתוספת הראשונה;
-- ext:[law] 997 | ⟦ח:קטע4||[note: (ההגדרה ””הרשות“, ”הרשות להגנת הפרטיות““, בסעיף 3)]⟧
-- ext:[law] 998 | ⟦ח:קטע3||נוסח החלטת הממשלה מס׳ 1890⟧
```

**P2. The Third Schedule uses a person the same Amendment replaced.**
Reading A (taken): the paragraph names בעל המאגר, which section 1 of Amendment 13 replaces in the Law with the בעל שליטה forms; a search of the whole consolidation on 2026-11-10 finds the words "בעל המאגר" or "בעל מאגר" once, in this paragraph, and the section 3 definition of the person is בעל שליטה.
Reading B (recorded, not rejected): section 1 replaces words that stood in the Law when the Amendment took effect, and the Schedule was written by the same Amendment, so the replacement does not reach it; the paragraph is then read in the ordinary sense of the words as the person the definition of בעל שליטה describes, and there is no gap.
Whether the Schedules are "the Law" for section 1 was not decided.
```
-- ext:[SH 3287 p.1430, read from the page image] | (8) במקום "בעל המאגר" יבוא "בעל השליטה במאגר";
-- ext:[law] 1050 | (3) מאגר מידע הכולל מידע אישי שבעל המאגר כפוף בשלו לחובת סודיות מקצועית לפי דין או לפי עקרונות של אתיקה מקצועית;
```

**P3. The 1986 regulations and the Interpretation Law section 25.**
The section 25 text:
```
-- ext:[interp] 138 | סעיף 25 – פירושם של אזכורים
-- ext:[interp] 139 | אזכור של חיקוק בחיקוק אחר – כוונתו לחיקוק המאוזכר כנוסחו בשעה שנזקקים לו, לרבות הוראות שנוספו בו והוראות שבאו במקומו בחיקוק אחר.
```
(a) Section 7. Taken: the regulations name s 7, which prints no text.
Recorded and not ruled: whether the definitions now in s 3 "came in the place of" s 7, and whether a replacement within the same Law is a replacement "in another enactment"; the word מידע alone is not among the definitions I saw.
The row says NOTHING for what section 25 reaches here.
(b) Section 12. Taken: on the literal words the regulations name a book called פנקס, and section 12 now speaks of a register called מרשם (section 1(1) of Amendment 13, p. 1430).
Reading A (recorded as a green test, not ruled): read through section 25 the words reach section 12 as it now reads, which is the target.
```
-- ext:[SH 3287 p.1430, read from the page image] | (1) במקום "פנקס" יבוא "מרשם", במקום "בפנקס" יבוא "במרשם" ובמקום "מהפנקס" יבוא "מהמרשם";
-- ext:[pb] 35 | ”פנקס“ – כמשמעותו בסעיף 12 לחוק;
-- ext:[law] 204 | סעיף 12 – מרשם מאגרי מידע [תיקון: תשנ״ו, תשפ״ד]
-- ext:[law] 205 | (א) ראש הרשות ינהל מרשם מאגרי מידע אשר יהיה פתוח לעיונו של הציבור ויאפשר חיפוש בפרטיו.
```
The same sentence of regulation 7(ג), which the control cites, also says "לרשם"; that word is a case of P4 and is not part of the control's citation.

**P4. The 1981 regulations and the office called הרשם.**
Taken: the regulations name an office the Law, after section 1(2) of Amendment 13, no longer names.
Rejected, not excluded: read through the Law's replacement the office is ראש הרשות; the row says NOTHING for what section 25 reaches, because a bare word is not a citation of an enactment.
The three places are regulation 2(א) (line 21 of the deposited page), regulation 5(א) (line 38) and regulation 7(ב) (line 46); regulation 3 has no subsection (א) that says these words.
```
-- ext:[inspect] 21 | (א) ניתן לעיין במידע, בתדפיס או במצג, במקום הישוב שבו נמצא המאגר ובשעה משעות היום שקבע לכך הבעל או המחזיק של מאגר המידע, ובלבד שהמועד יחול תוך 30 ימים מיום שנתקבלה הבקשה לעיון; הרשם רשאי להאריך תקופה זו לענין מסויים או למאגר מסויים ב־15 ימים נוספים.
-- ext:[inspect] 38 | (א) סירב בעל או מחזיק של מאגר מידע להתיר עיון במידע, יודיע על כך למבקש תוך 21 ימים מיום קבלת הבקשה, בטופס המפורט בתוספת השניה; הרשם רשאי להאריך תקופה זו לענין מסויים או למאגר מסויים ב־15 ימים נוספים.
-- ext:[inspect] 46 | (ב) סירב בעל מאגר המידע או מחזיקו, לפי הענין, לתקן או למחוק את המידע כמבוקש, יודיע על כך למבקש תוך 30 ימים מיום קבלת הבקשה; הרשם רשאי להאריך תקופה זו לענין מסויים או למאגר מסויים ב־15 ימים נוספים.
```

**P5. The 2023 regulations and the definition of מידע בעל רגישות מיוחדת.**
Reading A (taken by the red tests): regulation 7 names s 7, which prints no text.
Reading B (recorded as a green test, not ruled): read through section 25 the citing words reach the definition of מידע בעל רגישות מיוחדת in s 3, whose paragraph (12), as the Second Schedule sets it out, names regulation 7 of these regulations.
```
-- ext:[law] 1033 | ⟦ח:קטע2|תוספת 2|תוספת שנייה|תיקון: תשפ״ד⟧
-- ext:[law] 1034 | ⟦ח:קטע4||[note: (פסקה (12) להגדרה ”מידע בעל רגישות מיוחדת“, בסעיף 3)]⟧
-- ext:[law] 1037 | מידע על חברות בארגון עובדים כאמור בתקנה 7 לתקנות הגנת הפרטיות (הוראות לעניין מידע שהועבר לישראל מהאזור הכלכלי האירופי), התשפ״ג–2023.
-- ext:[KT 10637 p.1722, read from the page image] | מידע שהועבר למאגר מידע בישראל כאמור בתקנה 2 בעניינים המפורטים להלן, הוא מידע רגיש לפי סעיף 7 לחוק:
-- ext:[eea] 77 | מידע שהועבר למאגר מידע בישראל כאמור בתקנה 2 בעניינים המפורטים להלן, הוא מידע רגיש לפי סעיף 7 לחוק:
-- ext:[eea] 78 | (1) מידע על מוצאו של אדם;
-- ext:[eea] 79 | (2) מידע על חברות בארגון עובדים.
```
The consolidation's regulation 7 (lines 76 to 79 of the page, quoted above) reads as the crop of the page image reads, word for word; I compared them by eye.
The enacting formula of these regulations (line 10 of the page) also cites s 7; an enacting-formula citation is not recorded as a defect by itself.

**P6. The rounding words of s 23לב(ב) and the per-person rates.**
Reading A (taken by the red tests): the amount to be rounded is the updated per-person rate itself, so a printed rate of 2.05 or 4.09 shekels is not what rounding it to the nearest ten shekels gives (nothing).
Reading B (recorded as green tests): the notice's footnote, that the rounding is done on the final sanction after the multiplication.
```
-- ext:[SH 3287 p.1461, read from the page image] | הסכום האמור יעוגל לסכום הקרוב שהוא מכפלה של 10 שקלים חדשים
-- ext:[YP 15000 p.654, read from the page image] | העיגול יתבצע לגבי סכום העיצום הכספי הסופי המתקבל לאחר ביצוע המכפלה לפי החוק.
```
Whether a notice's footnote binds a court on the question was not decided.
The row computes in whole agorot, so no figure is a fraction; the rounding function rounds a remainder of 500 agorot or more up.

**P8. The 2004 schedule lists repealed sections.**
Taken: the schedule's column A names s 31א(א)(1) to (7) and s 17א(א) and (ב), and Amendment 13 repeals both sections.
Recorded: conduct before the repeal is saved by the Interpretation Law section 22, so the listing is not without effect on conduct from before the repeal.
Section 75 of Amendment 13 speaks of s 26 only.
This row makes no claim about any fine imposed.
```
-- ext:[interp] 126 | סעיף 22 – סייגים לכוחו של ביטול [תיקון: תשנ״ד]
-- ext:[interp] 127 | ביטולו של דין אין כוחו יפה –
-- ext:[interp] 128 | (1) להחיות דבר שלא היה לו תוקף בשעה שהביטול נכנס לתקפו;
-- ext:[interp] 129 | (2) להשפיע על פעולה קודמת של הדין המבוטל או על מה שנעשה לפיו;
-- ext:[interp] 130 | (3) להשפיע על זכות או חיוב שלפי הדין המבוטל.
-- ext:[SH 3287 p.1472, read from the page image] | סעיפים 26 ו־31א לחוק העיקרי – בטלים.
-- ext:[SH 3287 p.1438, read from the page image] | סעיף 17א לחוק העיקרי – בטל.
```
The original schedule (KT 6299, pp. 323 and 324) is deposited as images and is not quoted; the schedule quoted is the one KT 6913 replaced it with.

**K1 to K7. The controls.**
Assumed, not ruled: I chose each sound control as the nearest citation I could check, in the same instrument where the deposit allowed it, so that a test of a defect has a citation of the same kind that passes; the control of P2 is in s 12 of the Law.
P3(a) and P3(b) share one control, and so do P8(a) and P8(b).

## 7. Expected-red declaration

`priv51-tests-xrefs-red.l4` holds 20 assertions that fail, on purpose: two for each of ten defects (P1, P2, P3(a), P3(b), P4, P5, P6, P7, P8(a), P8(b)).
For the nine citations the first assertion fails because what the citing words say they point at is not what the target is, and the second because the text the citing words name is not in force on 10 November 2026.
For P6 both assertions fail because the printed rate is not what rounding it to the nearest ten shekels gives.
The count is declared in `check.sh` (`expected_failed`) and in `encoding.json` (`expected_red`).

## 8. check.sh numbers

Run on 2026-11-10 with `L4=~/.local/bin/l4 ./check.sh`; the main build is 1.6.109 (main, 4c887e0, 2026-11-04).

| module | errors | satisfied | failed | refused | expected failed | main: errors | main: satisfied | main: failed | main: refused | main |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `priv51-nouns.l4` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| `priv51-cross-references.l4` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| `priv51-tests-xrefs.l4` | 0 | 66 | 0 | 0 | 0 | 0 | 66 | 0 | 0 | same |
| `priv51-tests-xrefs-red.l4` | 20 | 0 | 20 | 0 | 20 | 20 | 0 | 20 | 0 | same |

A failed assertion is also counted as an error, so the 20 errors of the red module are its 20 failures.

## 9. What was not read

Page 1496 of Sefer HaChukim 3287 and every page of it not named in section 2 were not read for this row.
No instrument later than those named was opened; that none touched the cited words is CONSOLIDATION-ONLY wherever a limb says so.
The images of Kovetz HaTakanot 6299 pp. 323 and 324 were looked at and are not quoted.
Of Kovetz HaTakanot 10637 and Yalkut HaPirsumim 15000 only the deposited crops were read.
Whether any of the ten defects matters to a court, to a regulator or to anyone who relies on the text was not examined.
No domain expert has read this against the source.
