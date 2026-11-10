# Row il-48: four citations in the Minimum Wage Law, 5747-1987, and its Youth and Apprentices Regulations, and one printed figure (two defects, two controls, one figure)

Status: draft, version 0.1.0, target compiler main.
No domain expert has read this against the source.
Every claim below was checked against a text in the source bundle or a page image named beside it; where it was not, it says so.

## 1. Scope

This row is not an encoding of the Minimum Wage Law, 5747-1987, and not an encoding of the Minimum Wage (Working Youth and Apprentices) Regulations, 5748-1987.
It records four citations and one printed figure as typed values that tests check, and keeps the two citations that do not point at what they say as expected-red tests.
For each citation the row types two descriptions, what the citing words say they point at and what the target is, and records where each of the two readings comes from.
The seat is the employee to whom the Law is applied; for the regulations, a worker under 18 or an apprentice.
This row asks no question from that seat, because it records references and not duties, so no `@export` module is written.
No domain expert has read this against the source.

## 2. Sources

The Law is read from the Hebrew Wikisource consolidation, revision 3079167, last edited 2026-08-26T07:30:08Z (sha256 d74633b3e230f83e486642c2815a81fe98b3259450ee85f01bc6f1b972ef78f5), at `../../registers/source-bundle/minimum-wage-law-5747-1987.he.wiki.txt`; it was deposited on 2026-10-08, before this row, and is not altered.
The Youth and Apprentices Regulations are read from the Hebrew Wikisource consolidation, revision 2928721, last edited 2025-05-13T16:46:01Z (sha256 74932acab593e13c63c8230dc188f66f6664e741f2e9215910f0e4cb41f8f53e), at `../../registers/source-bundle/youth-and-apprentices-regulations-5748-1987.he.wiki.txt`; on 2026-11-10 the sha1 of the fetched file (dc7ed55a2c3d092a5aae4a4efd529f0601d1af70) was matched to the page history, which gives that revision.
The National Insurance Law [Consolidated Version], 5755-1995, is read in place from its own subject, `../../../national-insurance-law-consolidated-version-5755-1995/registers/source-bundle/national-insurance-law-consolidated-version-5755-1995.he.wiki.txt`: Hebrew Wikisource revision 3085079 (sha256 78bf47ee29a300d51c5c7646cf85992d7de78aa1380bd8460a4a18265f552a97), the revision row il-43 recorded; I did not match it to the page history again.
The Interpretation Law, 5741-1981, is read in place from `../../../interpretation-law-1981/source/law.wiki`: Hebrew Wikisource revision 2883979, last edited 2024-09-23T14:04:16Z (sha256 df3abac9015b4cd919eddece40d46565a97cdf123f78bbe925b687a5f5f0d2ab), as that subject's `source/SOURCES.md` records it.
All four are unofficial aids.
Every statement that rests only on one of them says CONSOLIDATION-ONLY.

The official instruments are in `../../registers/source-bundle/amending-laws/` and `../../registers/source-bundle/official/`, each with a 100 dpi page image of every page read from it.
Only the pages read are deposited as PDFs, and the whole issues are not in the bundle: SH 1211 printed p. 68 (page 1 of a one-page extract of a 4-page file); SH 1621 pp. 128 and 129 (the whole 2-page file, both pages read); KT 5074 printed p. 323 (page 1 of a one-page extract of a 9-page issue); KT 5942 printed p. 180 (page 1 of a one-page extract of a 33-page issue); and both pages of the extension order's copy (section 5).
SH 1211 p. 69 and every other page of the whole issues were not read and are not deposited; `SOURCES.json` keeps the URL, sha256 and size of each whole file as downloaded, and gives each extract its own entry.
On 2026-11-10 I rendered the page of each extract at 100 dpi and compared it with the same page of the whole file: the renderings are identical.
`../../registers/source-bundle/SOURCES.json` gives the URL, retrieval date, sha256 and size of every file, and the sha256 values were recomputed with `shasum -a 256` on 2026-11-10.
The two Sefer HaChukim files come from the Knesset's server; the two Kovetz HaTakanot files come from `olaw.org.il`, a website that hosts scans of Reshumot issues and is not a government site, so their origin is recorded as that and not as the Knesset's.

| instrument | pages read from the page image | what the page shows |
| --- | --- | --- |
| Sefer HaChukim 1211, 10 Nisan 5747 (9 April 1987), the Law as made | p. 68 | the definition of "השכר הממוצע" citing the 1968 National Insurance text; s 3(ב)(3); the first line of s 3(ג), which is cut off at the foot of the page and continues on p. 69, which I did not read |
| Sefer HaChukim 1621, 3 Nisan 5757 (10 April 1997), Amendment 2 | pp. 128 and 129 | p. 128: s 1(5) prints "החלק ה־186 של שכר המינימום"; s 2(1) adds words at the end of s 3(ב); s 2(2) repeals s 3(ג). p. 129: s 12 commences the Law on 23 Adar II 5757 (1 April 1997) |
| Kovetz HaTakanot 5074, 10 Tevet 5748 (31 December 1987), the regulations as made | p. 323 | regulation 7 |
| Kovetz HaTakanot 5942, 28 Kislev 5759 (17 December 1998), the amending regulations signed 10 Kislev 5759 (29 November 1998) | p. 180 | regulation 3 repealed, regulation 4 trimmed; regulation 7 is not mentioned |

The Hebrew of an official page is typed by me from the page image on a line `-- ext:[SH <issue> p.<page>, read from the page image] | ...` or `-- ext:[KT <issue> p.<page>, read from the page image] | ...` in `il48-cross-references.l4`.
`tools/pdfcheck.py` checks every Hebrew word of a Sefer HaChukim line against the text layer of that page (6 lines, 0 problems); it cannot see the order of the words, because these text layers reverse and interleave runs, so the page image is what the typing was read from.
The two Kovetz HaTakanot PDFs have no text layer, and the OCR on this machine has no Hebrew data, so none of their 4 typed lines can be checked that way.
The one typed from KT 5074 p. 323 (regulation 7) is identical to the consolidation's regulation 7 (`ext:[youth] 41`) once the wiki template marks are removed; the 3 typed from KT 5942 p. 180 have no check beyond my reading of the image.
The Hebrew of the consolidations is expanded mechanically by `tools/srcquote.py` (`src:` lines, the Law) and `tools/extquote.py` (`ext:[youth]`, `ext:[nii]` and `ext:[interp]` lines).
`tools/hebcheck-all.sh *.l4 NOTES.md` finds every other run of Hebrew in the `.l4` files and in this file in the four consolidations, and exits 0.

## 3. Files

| file | what it holds |
| --- | --- |
| `il48-nouns.l4` | the kinds of provision, the three sources of a reading, the record of a citation and of a printed figure; no rule |
| `il48-cross-references.l4` | the five functions, and one typed value per citation and for the figure, with the words of the texts quoted beside it |
| `il48-tests-xrefs.l4` | 34 assertions: the controls point at what they say, the printed figure, what was read from where, what the descriptions say, the day each named text stopped being in force, and the Interpretation Law section 25 fork |
| `il48-tests-xrefs-red.l4` | 4 assertions that fail, on purpose (section 7) |
| `check.sh`, `fetch-main-l4.sh` | the check; `check.sh` declares 4 expected failures for the file above |
| `tools/` | `srcquote.py`, `extquote.py`, `hebcheck.py`, `hebcheck-all.sh`, `pdfcheck.py` |

## 4. Coverage

| provision | status |
| --- | --- |
| regulation 7 of the Youth and Apprentices Regulations to s 3(ג) of the Law (the premium rule) | encoded; a defect; limb (a) read from the official instrument, limb (b) official with the caveat in section 5 |
| regulation 7 to s 3(ב)(3) of the Law (the fixed addition) | encoded; a sound control; both limbs official with the caveat in section 5 |
| s 1 of the Law, the definition of "השכר הממוצע", to s 1 of the National Insurance Law [Consolidated Version], 5728-1968 | encoded; a defect on the literal reading and a documented fork (P2); limb (a) CONSOLIDATION-ONLY, limb (b) official with the caveat in section 5 |
| s 14א(א) to s 6א(א)(1) to (3) of the Law | encoded; a sound control chosen by me (fork K2); both limbs CONSOLIDATION-ONLY |
| s 1 of the Law, the divisor in the definition of the hourly minimum wage | encoded as a printed figure; a control; the official figure read from the page image |
| the rest of the Law, including how the minimum wage is fixed and updated, and what each section requires of an employer | out-of-scope: this row does not encode the Law |
| every other citation in the Law and in the regulations | out-of-scope: not examined; the row records the citations that were examined and says nothing of the rest of the text |
| the rest of the Youth and Apprentices Regulations | out-of-scope: only regulation 7 and the instrument that repeals regulation 3 and trims regulation 4 were read |
| the instruments the Law's header lists after 1987 other than Amendment 2 | out-of-scope: not opened (section 9) |

## 5. The citations: answer table

"Stands" means that the target is in the official text of its law today.
Limb (a) asks whether the target is what the citing words say; limb (b) asks whether the citing words still read so in the latest official text of the citing provision.
In the last two columns "official, with the caveat" means that the page of the official instrument was read from the page image, and that no later instrument touched the words rests on the consolidation's list of amending instruments, which is CONSOLIDATION-ONLY.

| citation | the citing words say it points at | the target is | stands today | limb (a) | limb (b) |
| --- | --- | --- | --- | --- | --- |
| regulation 7 to s 3(ג) | the rule on counting a premium as a pay component, as s 3(ג) first printed it | a subsection that was repealed; the section prints no text for it | no, from 1 April 1997 | official: SH 1621 p. 128, s 2(2), and p. 129, s 12 | official, with the caveat: KT 5074 p. 323 as made; KT 5942 p. 180 leaves it alone |
| regulation 7 to s 3(ב)(3) | the fixed addition paid because of the work | the same | yes, by the consolidation | official, with the caveat: SH 1211 p. 68 as made; SH 1621 p. 128, s 2(1), touches only the closing words of s 3(ב) | official, with the caveat, same page as above |
| "השכר הממוצע" to s 1 of the National Insurance Law, 5728-1968 | the definition in the 1968 consolidated text | the definition in the 1995 consolidated text | no, from 1 October 1995, by the consolidation | CONSOLIDATION-ONLY | official, with the caveat: SH 1211 p. 68 as made; SH 1621 p. 128, s 1, does not name the definition |
| s 14א(א) to s 6א(א)(1) to (3) | the three conditions of s 6א(א) | the same | yes, by the consolidation | CONSOLIDATION-ONLY | CONSOLIDATION-ONLY |

The printed figure.
The definition of the hourly minimum wage in s 1 reads "החלק ה־186 של שכר המינימום" on Sefer HaChukim 1621 p. 128, s 1(5), which I read from the page image, and on the deposited consolidation.
Row il-32's INDEPENDENT-FINDINGS.md, finding 8, asked whether the divisor in the deposited text is stale.
This row answers that question for the words of the definition: the deposited divisor is the one the official instrument prints.
The limit is the one stated above: that no instrument after SH 1621 changed the number is CONSOLIDATION-ONLY, and this row does not say what follows from the number.

The extension order on the shortening of the work week.
The deposited copy is `../../registers/source-bundle/official/extension-order-short-week-2018-ministry-copy.pdf` (2 pages, sha256 fa27b689656194ef65d207fd6f68ec7c54c2c78d4362b2a5a2a5d3a207831a4b), with the page images `extension-order-short-week-2018-p1.png` and `extension-order-short-week-2018-p2.png` beside it.
It is the Ministry of Labour's hosted copy of the signed order (`https://www.gov.il/BlobFolder/dynamiccollectorresultitem/extention-order-short-week-2018/he/extention-order-short-week-2018.pdf`, fetched on 2026-11-10), not the Yalkut HaPirsumim publication.
I did not reach the Yalkut issue or page, so this row gives no Yalkut number, page or publication date, and the day the order took effect is not established.
Both pages were read from the page images; the text layer of the PDF has garbled digits, so `tools/pdfcheck.py` checks only the Hebrew words of the `ext:` lines against it (10 lines checked in all, 6 from Sefer HaChukim and 4 from the order, 0 problems).
The order is signed by the Minister of Labour, Welfare and Social Services on 28 Adar 5778 (15 March 2018); the calendar routine matched the Hebrew date to the Gregorian date printed beside it.
Clause 2.8 of the Schedule, on page 2, says that in line with the shortening of the work week the hourly wage is calculated on a basis of 182 hours per month of work; its Hebrew is on an `ext:` line in `il48-cross-references.l4`, beside control 3.
That clause speaks of the hourly wage generally; applying it to the minimum wage is our reading, not the clause's words.
Page 1 has three opening paragraphs without clause numbers, each on an `ext:` line in the same place.
The first says that the provisions of general collective agreement 7019/2017, signed on 2 Nisan 5777 (29 March 2017), are extended to all employees and employers in Israel.
The second says that the order takes effect on the first of the month after its publication.
The third says that the order lapses if a law sets a short work week built on a long weekend; I did not search for such a law, so whether that condition has occurred is not established.
No module value or assertion in this row depends on the order; its lines are comments.
Where I looked for the Yalkut number: a web page that summarises the order and links the copy (it gives none), and two web searches (none); a request for a Knesset document that might cite one was cancelled while it waited for the shared fetch lock.

What limb (b) of regulation 7 rests on, sorted by how strong it is.
Read from the page images: the words of regulation 7 as made, and that KT 5942 p. 180 repeals regulation 3, trims regulation 4 and does not mention regulation 7.
CONSOLIDATION-ONLY: that no other instrument touched regulation 7; the consolidation's header lists three Kovetz HaTakanot, 5074 (p. 322), 5714 (5756, p. 138) and 5942 (p. 180), and I did not open the middle one.

## 6. Fork register

Each fork gives the reading taken, the reading rejected or held aside, and the Hebrew that licenses each.

- K1, the kinds.
  The kinds in `What a provision is about` and `Where a reading comes from` are my plain descriptions, so that two descriptions of the same thing are the same kind; they are not the Law's terms.
  The middle kind of `Where a reading comes from` ("the official instruments read from their page images; that no later instrument touched the words is CONSOLIDATION-ONLY") is mine too: it names the caveat so that it is typed and not hidden in a note.
  Taken: one kind per target as its heading or first words describe it.
  Rejected: comparing the Law's words as strings, which would make every citation fail on punctuation.
- K2, the control for the second defect.
  Taken: s 14א(א) to s 6א(א)(1) to (3), a reference inside the Law to three numbered paragraphs, read from the consolidation (`src:117`, `src:62` to `src:64`).
  I chose it because it is the nearest sound citation of the same kind; it is assumed, not ruled, and nothing else depends on it.
  Both limbs are CONSOLIDATION-ONLY because neither the instrument that wrote s 14א(א) nor the one that wrote s 6א(א) was read.
- P1, how to read regulation 7's words "סעיף 3(ב)(3) ו־(ג) לחוק".
  The regulation says: "הוראות סעיף 3(ב)(3) ו־(ג) לחוק לא יחולו לגבי נער עובד וחניך" (`ext:[youth] 41`; the page image of KT 5074 p. 323 reads the same).
  Reading A, taken: the words point at the subsection as the Law reads today; the consolidation of the Law prints subsection (ג) with the note "(בוטל)" (`src:41`) and Amendment 2 says "סעיף קטן (ג) – בטל" (SH 1621 p. 128, s 2(2)); so the words point at a subsection that prints nothing.
  What licenses it: the Interpretation Law s 25 reads a reference to an enactment as "כנוסחו בשעה שנזקקים לו" (`ext:[interp] 139`), that is, as worded at the time it is turned to (CONSOLIDATION-ONLY), and regulation 7 contains no word of time.
  Reading B, held aside: the words freeze the reference to what s 3(ג) said when the regulation was made, which was a rule about counting a premium on the footing of a general collective agreement (the first line of s 3(ג), SH 1211 p. 68).
  What licenses it: regulation 7 was published on 31 December 1987 (KT 5074 p. 323), after the Law as made (SH 1211, 9 April 1987), whose s 3(ג) had that text.
  The row does not rule between A and B.
  It records the citation as a defect because under both readings the regulation still cites a subsection that has been repealed, and the 1998 amending regulations (KT 5942 p. 180) did not mention regulation 7.
  Whichever is right, the other half of the same sentence, "סעיף 3(ב)(3)", still points at a paragraph that stands (the first control).
- P2, whether the definition of "השכר הממוצע" is stale.
  The definition says: ”השכר הממוצע“ – כהגדרתו בסעיף 1 לחוק הביטוח הלאומי [נוסח משולב], התשכ״ח–1968 (`src:12`; SH 1211 p. 68 reads the same).
  The opening notice of the 1995 text says: "נוסח זה בא במקום חוק הביטוח הלאומי [נוסח משולב], התשכ״ח–1968" (`ext:[nii] 16`), and sets its commencement at 7 Tishrei 5756 (1 October 1995) (`ext:[nii] 18`) (CONSOLIDATION-ONLY).
  The 1995 text has its own definition of the same term in its s 1 (`ext:[nii] 222` to `225`).
  Reading A: the Interpretation Law s 25 reaches it, "לרבות הוראות שנוספו בו והוראות שבאו במקומו בחיקוק אחר" (`ext:[interp] 139`), so the citing words now reach the 1995 definition and nothing is stale.
  Reading B, taken as the red reading: the citing words name "התשכ״ח–1968", a particular version by its year, and the text they name stopped being the text in force on 1 October 1995, so the citation names a version that was replaced.
  Whether a consolidated version that replaces another is a provision that "came in its place" within s 25 is the question; I did not find the answer in either text, and the row does not rule.
  Why this row keeps it red: a green result would hide from a reviewer a citation whose words and target differ as printed, on a reading that rests on a consolidation; a red result states what the words need and costs a reviewer one line.
  The row records reading A as a green test (`the citation reaches its target once read through the Interpretation Law section 25`), so the choice can be reversed by editing one expected value.
  Under A the third red assertion would pass; the fourth would still fail, because the 1968 version is not in force on 10 November 2026 on either reading.
  Limb (a) of this citation, that the 1995 text replaced the 1968 text, rests on the consolidation's opening notice and is CONSOLIDATION-ONLY.
- D1, a day before the end.
  The row holds the day each named text stopped being the text in force, and no source in the bundle says whether the text was amended or replaced earlier.
  The Law's header lists an Amendment of 5755 (p. 378) that I did not open, so I cannot say what s 3(ג) read on 31 March 1997.
  Taken: for any day before the end the answer is NOTHING; for the end day and every later day it is JUST FALSE.
  Rejected: JUST TRUE for the days before, which this row does not type.
  A control has no recorded end, so its answer is NOTHING on every day; that is not a statement that its target stands.
- D2, the commencement of the repeal of s 3(ג).
  SH 1621 p. 129, s 12, commences the Law on 23 Adar II 5757 (1 April 1997); its Hebrew is typed from the page image on a line in `il48-cross-references.l4` and is not in any consolidation, so it is not repeated here.
  Taken: 1 April 1997.
  Rejected: 10 April 1997, the date of the issue, because s 12 names its own day.
- D3, the Hebrew dates.
  The calendar routine reproduced 30 Kislev 5785 = 31 December 2024 before it was used.
  Then: 23 Adar II 5757 = 1 April 1997 (SH 1621 p. 129); 3 Nisan 5757 = 10 April 1997 (SH 1621); 10 Nisan 5747 = 9 April 1987 (SH 1211); 10 Tevet 5748 = 31 December 1987 (KT 5074); 28 Kislev 5759 = 17 December 1998 and 10 Kislev 5759 = 29 November 1998 (KT 5942); 7 Tishrei 5756 = 1 October 1995 (the opening notice of the 1995 text).
  Where a page prints the Gregorian date beside the Hebrew one (SH 1621 p. 129; the opening notice of the 1995 text) the pair matches; the other Gregorian dates are the routine's output.
- E1, an enacting-formula citation.
  The consolidation's introduction to the regulations cites s 16 of the Law as the power under which they were made (CONSOLIDATION-ONLY); I did not read the enacting formula of either Kovetz HaTakanot issue.
  This row does not treat an enacting-formula citation as a defect and does not record one.

## 7. Expected red

Four assertions in `il48-tests-xrefs-red.l4` fail on purpose, and the count (4) is declared in `check.sh` and in `encoding.json`.
Each defect has two, and each states what the citing words need.

- Regulation 7 to s 3(ג): `the citation points at what it says` (the citing words say the premium rule; the target is a repealed subsection) and `the named text is in force on` 10 November 2026, expected JUST TRUE (the answer is JUST FALSE, because the repeal commenced on 1 April 1997).
- The definition of "השכר הממוצע" to the 1968 text: the same two assertions, on the literal reading in fork P2 (the answer is JUST FALSE, because the 1995 text replaced the 1968 text from 1 October 1995).

Nothing in either file was edited to make it pass.

## 8. Check numbers

Run as `L4=~/.local/bin/l4 L4_MAIN=~/.cache/l4-main/109/l4 ./check.sh`; main is build 1.6.109 (4c887e0, 2026-11-04).
Both binaries give the same four counts for every file.

| file | errors | satisfied | failed | refused | expected failed |
| --- | --- | --- | --- | --- | --- |
| `il48-nouns.l4` | 0 | 0 | 0 | 0 | 0 |
| `il48-cross-references.l4` | 0 | 0 | 0 | 0 | 0 |
| `il48-tests-xrefs.l4` | 0 | 34 | 0 | 0 | 0 |
| `il48-tests-xrefs-red.l4` | 4 | 0 | 4 | 0 | 4 |
| total | 4 | 34 | 4 | 0 | 4 |

The four errors are the four expected failures.
Mutation control, on copies of the modules that were deleted afterwards: moving the repeal day of s 3(ג) to 1 April 1998 made 2 assertions fail; that fault together with one control's target given the wrong kind made 3 fail; so the tests can fail.
The check does not see a difference that no assertion exercises.

## 9. Open questions for a domain expert

- Does regulation 7's reference to s 3(ג) fall under reading A or B (fork P1), and what, if anything, should the regulation say now?
- Does s 25 of the Interpretation Law carry the definition of "השכר הממוצע" to the 1995 text (fork P2)?
- Did Kovetz HaTakanot 5714 (5756, p. 138), which I did not open, touch regulation 7?
- In which Yalkut HaPirsumim issue and on which page was the extension order on the shortening of the work week published, and on what day did it take effect?
- What does the rest of s 3(ג) as made say? The line on SH 1211 p. 68 is cut off at the foot of the page, and p. 69 was not read.
- The Law's header lists an item as page 129 with the label "ת״ט" (Knesset file `11_lsr_ec_317833.pdf`) that I did not open, so I do not know whether it corrects any word I read from p. 68.
- The Law's header lists ten other instruments after 1987 that I did not open (Sefer HaChukim 5755 p. 378; 5762 p. 493; 5766 p. 362; 5767 p. 80; 5768 p. 63; p. 617, for which the header gives no year and which follows 5768 p. 63; 5771 p. 936; 5774 p. 604; 5775 p. 152; 5778 p. 7); that none of them touched the words read here rests on the consolidation.
- Whether the 1995 National Insurance text replaced the 1968 text on 1 October 1995 for the purpose of this definition rests on the consolidation's opening notice and was not checked against the official publication.

No domain expert has read this against the source.
