# Attorney General Law (Opinions, Representation and Supervision), 5786-2026, in L4 (row IL-41, draft)

Status: draft.
No domain expert has read this encoding against the source, and no independent tester has run.
Target compiler: `main`.
Written 2026-11-09.

## 1. Seat

The first seat is the individual to whom the Law is applied: a party to a court proceeding in which the State takes a side, or a person whose matter an official decides.
The Law's duties fall on officials (the Attorney General, the Government, ministers, courts), so each question in `il41-seat.l4` asks what the text provides for that person.
The commons rulings of 2026-10-18 and 2026-10-21 give officials no seat, and the encoding follows them (fork F1).
`il41-seat-recipient.l4` is a second layer, the recipient of an opinion of the Attorney General.
It was asked for in the brief and is not a commons seat.
It adds no rule: each question calls the rules in the Chapter modules.
Every exported question has `@export` and `@desc`.
Where the text does not decide a case, the rule returns `NOTHING`, following the commons rulings of 2026-11-04 and 2026-11-05: a flat negative and a "means" definition answer `FALSE`; an unclosed list, silence and a scope limit with no "only" answer `NOTHING`.

## 2. Edition and sources

The official text is Sefer HaChukim 5786 no. 3550, 5 Av 5786 (19 July 2026), pp. 802 to 804, the Knesset's PDF `fs.knesset.gov.il/25/law/25_lsr_14184818.pdf` (sha256 in `registers/source-bundle/SOURCES.json`).
It was read from the page images (`official/sefer-hachukim-5786-no-3550-*.page-image.png`).
The PDF's text layer is in visual order, and the text layer of page 3 (p. 803) carries every word twice (953 words on that page against 429 and 410 on the other two text pages); the page image shows each word once.
The footnote on p. 802 (read from the text layer) says the Law was passed in the Knesset on 1 Av 5786 (15 July 2026), in a sitting that began on 28 Tammuz 5786 (13 July 2026), and that the bill and its explanatory notes were published in Hatza'ot Chok HaKnesset 1192 of 9 Sivan 5786 (25 May 2026), p. 217.
The Law has twenty sections in three chapters and one indirect amendment (s 16).
Footnotes 1 to 4 cite Dinei Medinat Yisrael New Version 11 p. 282 (the Ordinance in s 10(a)); Sefer HaChukim 5718 p. 118 and 5777 p. 920 (the State as Litigant Law, s 16); Sefer HaChukim 5786 p. 802 (the Law itself); and Sefer HaChukim 5719 p. 86 (the Civil Service (Appointments) Law, s 20).
The Knesset's database lists an unofficial text (`25_lsh_14184774.docx`), converted with `textutil` to `aids/knesset-unofficial-text-25_lsh_14184774.he.txt`.
Every `-- lsh:N |` comment quotes line N of that file.
The comments headed `cp:`, `ord:`, `app:` and `com:` quote lines of Hebrew Wikisource consolidations of the cited laws, which are aids and not official versions.
A Hebrew Wikisource page for the Law itself also exists (revisions 3024924 of 17 July 2026 to 3037609 of 2 August 2026 were listed); it was used only for comparison.
Anything stated here that rests only on a consolidation is labelled CONSOLIDATION-ONLY.

## 3. The texts compared

`tools/compare-texts.py` compares, as multisets of words, the Knesset's unofficial text, the official PDF's text layer (raw mode, page 3 counted at half), and the text of the Law in the second and third reading bill dated 13 July 2026 (pages 2 to 6 of that document are deposited).
Unofficial text against official pages: 1005 words against 1013.
Every word that appears on one side only is a text-layer artefact: seven ordinary words that the layer prints with their letters scrambled or glued to a digit, three running heads, and three section references glued together.
Unofficial text against the 13 July text: 1005 words against 1007; the differences are digits glued to words by the extraction, the running date, and one word split in two.
No word differs in substance in either comparison.
The word order of the official pages was compared by eye against the unofficial text at 130 dpi, section by section.
A multiset cannot see a word moved, and an eye at that resolution can miss a letter, so that is the limit of the claim.
`tools/compare-wiki.py` compares the Wikisource page of the Law with the unofficial text: the differences are the table of contents markup and s 16, which the page replaces by a note that the text was integrated into the amended law.
The Knesset's plenum-vote list for the bill holds 95 records; the reservation votes among them were not read.
Where the texts differ, the Sefer HaChukim text is the one followed; none differ.

## 4. What the Law refers to

The Law makes thirty cross-references: twenty-four to a provision of itself and six to something outside it.
They are typed in `il41-references.l4` as a record of the subject the citing text says the target has and the subject the target has, and `il41-tests-references.l4` counts them and checks that every one is sound (the target exists and the two subjects agree).
All thirty pass.
The subjects are a classification made from the headings and words read in the sources (fork F5).

The six outside references and what was read:

- **s 10(a), the Ordinance (Appearance of the Attorney General) [New Version].**
  Footnote 1 cites Dinei Medinat Yisrael New Version 11 p. 282, read from its page image.
  Its s 1 lets the Attorney General appear and be heard in a proceeding in which a right of the State or a public right or interest is or may be affected; its s 2 lets him or his representative represent a public employee or a public body that is a party.
- **s 16, the Civil Procedure Amendment (State as Litigant) Law 5718-1958, s 4.**
  The text of s 4 as originally published was read from the page image of Sefer HaChukim 251 p. 119 (6 April 1958).
  Sefer HaChukim 1695 p. 34 (18 December 1998; repeals s 5 and strikes five words from s 7) and Sefer HaChukim 2635 p. 920 (29 Nisan 5777; adds s 6A) were read from their page images; neither touches s 4.
  The heading of s 16 says "No. 3"; two amendments precede it.
- **s 20, the Civil Service (Appointments) Law 5719-1959, s 5.**
  Read from the page image of Sefer HaChukim 279 p. 86 (15 April 1959): the Government may fix the ways and conditions for the appointment of the Attorney General, and to the extent it has not, the Law's provisions apply.
- **s 15(c)(3)(b), the Commissioner for Complaints against State Representatives in the Courts.**
  The office has the same title in s 2(a) of the Complaints Commissioner Law 5776-2016, read from the page image of Sefer HaChukim 2574 p. 1162 (11 August 2016); the rest of that Law, and any amendment after 2016, was not read for this row.
- **s 5(b), two committees of the Knesset.**
  Both are main committees of the 25th Knesset in the Knesset's database (Ids 4191 and 4190; deposited).

## 5. Section 16, the indirect amendment

Section 16 amends the State as Litigant Law by an instruction in these words: in s 4, "at its end shall come" the words "subject to the provisions of the Attorney General Law (Opinions, Representation and Supervision), 5786-2026".
`il41-amendment.l4` types the record: the law amended, the section, the words of s 4 as published in 1958, the instruction, and the words it adds.
Section 4 as published in 1958 ends with a full stop (Sefer HaChukim 251 p. 119, page image), and the instruction names no change to that punctuation.
The Hebrew Wikisource consolidation of the State as Litigant Law prints a comma where the full stop was (CONSOLIDATION-ONLY).
The publications are typed with their years and pages: 5718 p. 118, 5759 p. 34 (1998), 5777 p. 920.
Footnote 2 of the Law cites 5718 p. 118 and 5777 p. 920.

## 6. Coverage

| provision | heading | disposition |
| --- | --- | --- |
| title, footnote * | the Law's name; the stage dates | quoted in section 2 |
| 1 | definitions | encoded: "executive authority", "court", "the Minister" (`il41-opinions.l4`) |
| 2 | legal advice to the Government | quoted only: states tasks of the Attorney General; typed as the target of references from s 14(a) |
| 3(a) | opinions of the Attorney General | quoted only; typed as a reference target |
| 3(b) | form | encoded: `s 3(b) permits an opinion to be given orally` |
| 4 | force of a written opinion | encoded with s 5 |
| 5(a)(1), (a)(2) | exceptions | encoded (the Government's decision is an input) |
| 5(b) | laying the decision | encoded: which committee (fork F4) |
| 5(c)(1), (c)(2) | criminal-law domain; statutory powers | encoded in the s 4 rule |
| 6 | the Attorney General presents the position | encoded with ss 8 and 9 |
| 7 | who fixes the position | encoded |
| 8 | notice that the position cannot be presented | encoded as an input of the s 9 rule |
| 9 | external representation | encoded; the body that decides how the lawyer is paid is typed |
| 10(a), (b) | appearance of the Attorney General | encoded |
| 11 | other bodies of the State | encoded |
| 12(a), (b) | what Chapter B does not apply to | encoded (fork F6) |
| 13 | validity of a law | encoded |
| 14(a), (b) | independence | encoded through s 15(d); s 14(a) typed as a reference source |
| 15(a) | supervision | encoded: the Minister of Justice supervises |
| 15(b) | the Government's decisions and policy | quoted only: states a duty of the Attorney General; no input or output for the seat |
| 15(c)(1) to (3) | accounts | encoded |
| 15(d) | no direction in a criminal proceeding | encoded |
| 16 | amendment of the State as Litigant Law | encoded as a typed record (section 5) |
| 17 | regulations | encoded: the power |
| 18 | commencement | encoded: the day as an input with the text's own rule; the Hebrew and Gregorian days agree |
| 19 | saving | encoded: `JUST FALSE` |
| 20 | transition | encoded: the 30 days (fork F3) |

## 7. Forks

- **F1** seat: the individual first; the recipient of an opinion as a second layer at the brief's suggestion.
- **F2** the quoted words are the Knesset's unofficial text, compared with the official pages (section 3).
- **F3** s 20 says "within 30 days from the day of its commencement": whether the commencement day is day one.
  Two readings are kept by name; the third value declines to choose and returns `NOTHING`.
- **F4** s 5(b): the Foreign Affairs and Defense Committee is the committee for an opinion on the security of the State or its foreign relations, and the Constitution, Law and Justice Committee otherwise.
- **F5** the subjects of the citing sides of the references in ss 16 and 20 are inferred, because those sections describe their targets in no words.
- **F6** s 12(a): the three exclusions are taken as alternatives (any one takes the matter out of Chapter B).
- **F7** s 9: the Government's power to choose another lawyer is read as given where the Attorney General has given notice under s 8 or the minister concerned considers that the position is not or will not be properly presented through him; a decision without either is not within it, so the Attorney General presents.
  Rejected: a power with no such condition.
- **F8** s 15(c)(3): where the Attorney General considers that the step might harm an important public interest, the account the Minister asked for under (2) goes to the Commissioner and not to the Minister.
  Rejected: to both.

## 8. Dates and statuses

| claim | value | source | how verified |
| --- | --- | --- | --- |
| issue and page | Sefer HaChukim 3550, 5 Av 5786 = 19 July 2026, pp. 802 to 804 | the PDF; `knesset-odata/bill.json` (MagazineNumber 3550, PageNumber 802, PublicationDate 2026-07-19) | page images; OData |
| Knesset record | bill Id 2197909, private bill 877, StatusID 118 ("passed third reading"), committee 4191 (Constitution, Law and Justice) | `bill.json`, `status118.json`, `committee4191.json` | OData |
| passed | 1 Av 5786 = 15 July 2026, in a sitting begun 28 Tammuz 5786 = 13 July 2026 | the footnote on p. 802 | PDF text layer; the third-reading vote is stamped 2026-07-15 20:42 (+03:00) in `plenumvote.json` (Id 46462) |
| first reading | discussed 16 Sivan 5786 = 1 June 2026; the vote is stamped 2026-06-02 04:12 | the second and third reading document, page 1 (text layer; page 1 is not deposited); `plenumvote.json` Id 46009 | text layer; OData; the stamp falls after midnight, the sitting before it |
| committee decision | the Knesset approved the committee's decision to split the bill on 21 Tammuz 5786 = 6 July 2026; the vote is stamped 2026-07-07 00:02 | the same document; `plenumvote.json` Id 46185 | text layer; OData |
| second and third readings | submitted for 28 Tammuz 5786 = 13 July 2026; the document is dated 13/7/2026 | the same document | text layer |
| bill published | Hatza'ot Chok HaKnesset 1192, 9 Sivan 5786 = 25 May 2026, p. 217 | the footnote on p. 802; page 217 | text layer; page image of p. 217 |
| earlier bills | P/877/25, 2785, 3198, 3825, 4625, 5262, 5287, 5289, 5808 passed to the committee on 7 Heshvan 5786 = 29 October 2025; P/5782/25 on 18 Tevet 5786 = 7 January 2026; nine have StatusID 122 ("merged with another bill") | page 217; `unionbills.json`, `union-main.json` | page image; OData |
| preliminary reading | vote stamped 2025-10-29 | `plenumvote.json` Id 44619 | OData |
| commencement | 22 Tevet 5787 = 1 January 2027 | s 18 | page image; `tools/hebdate.py` computes the pair |
| other pairs | 5 Av = 19 July; 1 Av = 15 July; 28 Tammuz = 13 July; 9 Sivan = 25 May; 16 Sivan = 1 June; 21 Tammuz = 6 July; 7 Heshvan 5786 = 29 October 2025; 18 Tevet 5786 = 7 January 2026 | the sources above | computed with `tools/hebdate.py`; each agrees |

The Knesset's website `main.knesset.gov.il` answers with a script-based bot challenge and was not used; the records above come from its public OData service.

## 9. What `check.sh` prints

Run on 2026-11-09 with `~/.local/bin/l4` (its version prints as "dev") and the main build 1.6.109 (main, 4c887e0, 2026-11-04), fetched by `fetch-main-l4.sh`.
Fourteen modules; total errors 0, satisfied 117, failed 0, refused 0; the main columns are the same for every module.
Per module: `il41-tests-opinions.l4` 27 satisfied, `il41-tests-representation.l4` 35, `il41-tests-general.l4` 20, `il41-tests-amendment.l4` 7, `il41-tests-references.l4` 9, `il41-tests-seat.l4` 19; the eight rule and noun modules carry no assertions.
`tools/hebcheck.py` is run by hand (`python3 -I tools/hebcheck.py il41-*.l4`; `check.sh` does not run it) and checks that every Hebrew string literal occurs verbatim in a deposited aid: 4 literals, none missing.
It checks against the aids, not against the official page images.
A mutation check was run on three rules (the s 4 default answer, the s 10(a) bar, the s 20 count); each mutation made at least one test fail.
No wider mutation check was run.

## 10. Not reached

- `main.knesset.gov.il` (bot challenge, not circumvented).
- Sefer HaChukim 2574 pp. 1163-1172 as page images (the Complaints Commissioner Law as made: only p. 1162, s 1 and s 2(a), was read for this row), and any amendment of that Law after 2016.
- The notice in Yalkut HaPirsumim 5760 p. 4894 that the Wikisource consolidation of the Appointments Law records.
- The explanatory notes of the bills and the committee's protocols.
- The stage dates of the second and third reading document were read from its text layer, not from a page image.
