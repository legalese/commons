# Broadcasting Act 1994 (Singapore): an L4 encoding with a seat layer

Row `legalese-sonnet-5.5` of the subject `sg/broadcasting-act-1994`.
Status: **draft**.
Not reviewed: no domain expert has read this encoding against the text.
One independent review by a second Claude session (Opus 5.5) was made after the encoders finished; it is not a domain expert's review, and "Independent review" below says what it did and did not cover.
Written by Claude Sonnet 5.5 (`claude-sonnet-5-5`) in one run by a single encoder ("Encoder BA"), from the texts named under "Inputs" below.
The encoder had no subagents.
The earlier naive encoding in `../naive-2026-10/` was not opened for writing and is not edited.
The sister encoding of the Telecommunications Act 1999 (`../../../telecommunications-act-1999/encodings/legalese-sonnet-5.5/`, modules `sgta-`) was written at the same time by another encoder; nothing here is imported from it or copied from it (see "Cross-folder links").

**Quarantine.**
This file, the layer-1 modules and their tests do not state any conclusion about the question the two encodings were commissioned to help answer.
Every conclusion about it is in `TV-QUESTION-BA.md` and in the files named `sgba-tv-*.l4`; nothing outside those files imports them.
Where this file has to mention a reading that matters to that question, it says what the readings are and sends the reader to `TV-QUESTION-BA.md`.

## The text, and what it is not

The only source for the Act is `../../registers/source-bundle/BA1994.txt`, a **plain-text rendering** of the *informal consolidation, version in force from 25/9/2024* (every page footer says so), taken from Singapore Statutes Online on 2026-10-01 (`BA1994.meta.json`: "Current version as at 01 Oct 2026").
Its cover says "2020 Revised Edition", but the body is the consolidation as amended since, up to G.N. S 738/2024 (item 30 of the legislative history).
It is **not the official text**, and nothing here is "verified against the official text".
The file has 4,774 newlines and 4,775 lines, 192,067 bytes and 190,635 characters; `BA1994.meta.json` records `char_count` 190,635, which matches.
Provenance caveat, the same one the Interpretation Act row records: `shasum -a 256` of the file gives `ffc14d37...2625b0d`, while the `text_sha256` in `BA1994.meta.json` is `47fd1d48...8b0d`.
The cause is unknown, so every quotation in the L4 files is a line copied out of that file by script (`qx.py`) and re-checked by `srcrefs.py`, and neither tool can say whether the converter dropped or changed a word.
The licence terms of the quoted text are in `../../SOURCE-LICENSE.md`; `SOURCE-LICENSE.md` here points at it and does not repeat it.

### Editions encoded, and where each text could not be had

- **The Act: one consolidation for everything but the schedules.**
  Every rule of layer 1 outside `sgba-versions.l4` states the consolidation in force from 25 September 2024.
  A rule that depends on the text takes the date as an input and answers `NOTHING` outside the window in which the deposited text is the text in force (`sgba-vintage.l4`: 25 September 2024 to 4 November 2026, `the day the sources were last checked`).
  **Assumed, not ruled:** that last day is 4 November 2026.
  The consolidation was retrieved on 1 October 2026; the lawplain instruments on 3 November 2026; the Gazette texts on 3 and 4 November 2026; and the e-Gazette index was searched on 4 November 2026 as follows.
  On 4 November 2026 the orchestrating session searched the e-Gazette index for 'Broadcasting Act' (year 2026: 22 results; 'Broadcasting Act amendment', 2025 to 2026: 7 results; first page of each) and read the three results that name the Act: Act 13 of 2026 (it amends the Info-communications Media Development Authority Act 2016 and the Telecommunications Act 1999, and refers to the Broadcasting Act's licences under sections 8 and 21 without amending any provision of it; first published 5 June 2026, in operation on a date to be appointed by notification, which was not found), the Digital Infrastructure Bill (Bill 20/2026, first published 8 September 2026; a Bill, not law; it names the Broadcasting Act once, in its explanatory statement; https://assets.egazette.gov.sg/2026/Legislative%20Supplements/Bills%20Supplement/26bills20.pdf, sha256 e74a98b41a04a54bb1a97ce9cd25dd7966f42f3ff087c216286528bc05a55408), and S 700/2026 (Info-communications Media Development Authority (Regulated Persons) Notification 2026, in operation 2 October 2026, made under the IMDA Act; https://assets.egazette.gov.sg/2026/Legislative%20Supplements/Subsidiary%20Legislation%20Supplement/26sls700.pdf, sha256 70f1358cb250167422af6f10cbc5ad5cde53ad8abe4dee2f9acff17be8c04bf5). The other results are titles under other Acts and were not read. None of the three amends a provision of the Broadcasting Act. That is what a first-page index search and three readings show; it is not a finding that nothing exists.
  To revert to the earlier cutoff, change the one line `` `the day the sources were last checked` MEANS Date 4 11 2026`` in `sgba-vintage.l4` to `Date 1 10 2026`: every window and the three version tables read that constant, and no module has the date typed in.
  The tests that name a reading day of 2 October to 4 November 2026 and expect an answer would then fail and are set back by hand; `grep -n 'Date [0-9]* 11 2026' sgba-tests-*.l4 sgba-tv-*.l4 sgba-cases-seat.l4` finds them.
  Build 98 of `main` has no `EVAL UNDER RULES EFFECTIVE AT`, so the windows are explicit.
  For the First and Third Schedules, and the definition of "broadcasting apparatus" and s 20(1) that depend on the First, there are four versions on two dates each: see "Point in time" below.
- **Three past texts of the Act, from the e-Gazette: the first two deposited 2026-11-03, the third 2026-11-04:** `../../registers/source-bundle/BA1994.20030731.txt` (Revised Edition 2003, title page "31st July 2003") and `BA1994.20120831.txt` (Revised Edition 2012, "31st August 2012"), each with a `.meta.json` beside it (URL, retrieval date, sha256 of the PDF and of the text, how obtained, `"ocr": false`).
  The e-Gazette serves them as static PDFs with a text layer; the text is `pdftotext -layout`, unedited.
  The terms and the reliance are in `../../registers/source-bundle/SOURCE-LICENSE-GAZETTE.md`: the e-Gazette's Terms of Use clause 11 permits reproduction with the copyright and permission statement; its FAQ says that before 9 March 2025 only copies printed by the Government Printer are prima facie evidence, so these texts are an aid for quotation and the PDF is the source; that is reliance, not a clearance.
  The third is `../../registers/source-bundle/BA1994.20211231.txt`, the 2020 Revised Edition as printed (`incorporates all amendments up to and including 1 December 2021 and comes into operation on 31 December 2021`), from `https://assets.egazette.gov.sg/2021/Legislative%20Supplements/Revised%20Acts/21rs8040.pdf`.
  **Compared by script with the 2024 consolidation on the receiver chain** (after removing page furniture and amendment notes; `cmp-reved2020.py` in this folder, run as `python3 -I cmp-reved2020.py`): the s 2(1) definition of "broadcasting apparatus" (24 words), s 20(1) to (4) (185 words) and s 47 (62 words) are word for word identical, and so is the First Schedule except that the consolidation prints its running head "FIRST SCHEDULE - continued" at a page break (4 words of page furniture).
  Nothing earlier than 31 July 2003 was obtained.
- **The consolidations between the two editions were not obtained** (2010-10-01, 2011-01-01 and 2011-01-02 are among the 24 SSO version dates `BA1994.meta.json` lists; the list does not say what changed on them).
  lawplain serves one vintage of everything: its `as_at` and `version` parameters made no difference (identical bytes), and `kind` accepts only `act_current` and `act_revised`.
  The legal-data-hunter server holds `SG/SSOStatutes` as the 2020 Revised Edition "up to and including 1 December 2021", one document per Act, with no historical versions (another encoder's probe, recorded in the Telecommunications Act row's `PROGRESS.md`).
  SSO's own historical pages were not tried by this encoder: the brief allows one attempt, inside 03:00 to 07:00 Singapore time, and two earlier probes by others were refused with 403.
  The attempt is for what the Gazette does not give, the consolidated texts of 2010-10-01 and 2011-01-01 as a cross-check; its result, or the reason it was not made, is recorded under "The single SSO attempt" below.
  For any date before 25 September 2024 outside the schedules' versions the encoding answers "the Act, as deposited, does not say".
  No past text was rebuilt from the present one.
- **The instruments: twelve from lawplain and eighteen from the e-Gazette.**
  The twelve were served by lawplain on 2026-11-03, one vintage each; lawplain is a secondary source whose operator and terms are unrecorded (see each deposit's `SOURCE-LICENSE.md`), and each deposit's `meta.json` records the retrieval date, the joined-text sha256 and "SSO not attempted".
  A lawplain `get_document` result carries these fields and no others: `sl_id`, `parent_act_id`, `sl_number`, `short_title`, `doc_date`, `url`, `body_text`, `body_length`, `body_offset`; there is no terms, licence or provenance field (checked 2026-11-04 on S 121/2008).
  The Class Licence Notification (N 1) and S 523/2010 are served **without their Schedules** (the conditions of the class licence; the list of exempt services).
  The eighteen from the e-Gazette are static PDFs with a text layer (`pdftotext -layout`, unedited, `"ocr": false`), each with a `.meta.json` beside it: the Television and Radio Licensing Regulations (Rg 1, 2004 Revised Edition), S 333/2004 (its amendment), S 548/2012 (its revocation), S 212/1999 (an earlier amendment), S 549/2012 and S 559/2010 (the Schedule notifications), S 354/2001 (TVRO), S 600/2014 and the Exemption Order of the 2004 Revised Edition, S 523/2010 as made (with its Schedule), S 212/2022 (the Order that deleted a sub-paragraph of O 2 paragraph 2), and the Class Licence amendments S 496/2001, S 555/2003, S 196/2004, S 70/2012, S 330/2013, S 674/2016 and S 478/2020.
  The orchestrating session read each URL it passed to the encoder off a result in the e-Gazette index; the encoder downloaded each file, and no URL was guessed.
  No instrument deposit came from the reviewer's retrievals; the twelve lawplain deposits were read through the lawplain server by the encoder.
  Six more deposits, the three amending Acts of 2004, 2005 and 2010 and their commencement notifications, came the same way on 2026-11-04 (the 2004 Act was downloaded on 2026-11-03); they are in their own table under the coverage table.
  Sixteen are their own subjects under `../../../broadcasting-*/` or `../../../singapore-broadcasting-authority-*/`; the as-made S 523/2010 and the Exemption Order of the 2004 Revised Edition are further deposits in the subjects of the lawplain rows for the same instruments.
- **Not obtained at all** (rows in the coverage table, disposition `source not obtained`): the Singapore Broadcasting Authority Act Second Schedule notification S 308/1996, the earlier history of Rg 1 (S 21/80 and eleven amendments before S 212/99), the original Schedule to N 1, the Codes of Practice under ss 6 and 45L, any Part 10A regulations (none was found), and any s 20(4) exemption (none found; on 4 November 2026 the orchestrating session searched the e-Gazette index for 'Broadcasting Act section 20(4) exemption', 63 results, read the first page by title only and opened nothing, and no title on that page names an exemption under section 20(4); that is a first-page title search and not a finding that none exists; the lawplain search recorded in the table row is the other place looked).

## Point in time: the First and Third Schedules, version by version

Design instruction (2026-11-03): model a retrospective notification on two explicit time axes, not as a fork.
Every version of a Schedule has TWO dates: **the day it takes effect** (valid time, the day it is the law for conduct) and **the day it was published** (rule-version time, the day it was made known to a reader).
A question has two days: **the day of the conduct** and **the day the law is read as at**.
The answer is the latest version published on or before the reading day whose effective day is on or before the conduct day; where no version qualifies the answer is `NOTHING`.
Both days are ordinary `GIVEN` inputs of type `DATE` and the versions are a table (`sgba-versions.l4`, tested in `sgba-tests-versions.l4`).

| version | takes effect | published | text and source |
| --- | --- | --- | --- |
| Revised Edition 2003 | 31 July 2003 | 31 July 2003 | First Schedule `BA1994.20030731.txt:2134-2154`; Third Schedule 2214-2220 |
| S 559/2010 (Third Schedule only) | 1 October 2010 | 30 September 2010 | `BA1994-S559-2010.txt`: made 28 September 2010, first published 30 September 2010 at 5:00 pm, "shall come into operation on 1st October 2010" |
| Revised Edition 2012 | 31 August 2012 | 31 August 2012 | First Schedule `BA1994.20120831.txt:2163-2178`; Third Schedule 2210-2226 |
| S 549/2012 (First Schedule only) | 1 January 2011 | 31 October 2012 | `BA1994-S549-2012.txt`: made 30 October 2012, first published 31 October 2012 at 5.00 pm, "deemed to have come into operation on 1st January 2011" |
| consolidation in force from 25 September 2024 | 25 September 2024 | 25 September 2024 | First Schedule `BA1994.txt:4342-4357`; Third Schedule 4391-4402 |

Notes on the table:

- The Revised Editions' effective and publication days are taken as their printed dates; the 2024 consolidation says only that it is the version in force from 25/9/2024, so its publication day is taken as the same day.
  The 5.00 pm of a Gazette publication is not kept, because the reading day is a date.
- A reading day after `the day the sources were last checked` (4 November 2026, assumed, not ruled) answers `NOTHING`: nothing is known of later versions.
  A reading day from 2 October to that day is answered from the latest version deposited, and the First Schedule and Third Schedule version functions carry the caveat in their comments: on 4 November 2026 the orchestrating session searched the e-Gazette index (first page of each of two searches) and read the three results that name the Act; none amends a provision of the Broadcasting Act (detail in sgba-vintage.l4). That is what a first-page index search and three readings show; it is not a finding that nothing exists.
  A conduct or reading day before 31 July 2003 answers `NOTHING`.
  A conduct day later than the reading day is not rejected.
- S 549/2012 is retrospective: its effective day (1 January 2011) is earlier than its publication day (31 October 2012).
  The table encodes the deeming as the text states it.
  **Whether a retrospective notification is valid, and what a court would do with conduct already past, is not addressed.**
- On an `unstable` build, the same table would be read with the built-ins: `EVAL UNDER VALID TIME` or `RULES EFFECTIVE DATE` for the conduct day, the rule-version axis (`tcRuleVersionTime`) for the reading day, and system time for "today".
  Build 98 of `main` rejects those, so this row takes the two days as inputs.
  (An `unstable`-only row, `../unstable-multitemporal-2026-11/`, is another session's and is not edited here.)
- **The same section across the editions** (compared by script, `tools/cmp_sections.py` in the encoder's scratch, after removing page furniture): ss 8, 9, 20, 51, 57, 60 and 65 are identical in the 2003 and 2012 editions, and s 47 differs only in the spacing of "20 (1)".
  The 2024 text differs from the 2012 text in ss 20, 51, 57, 60 and 65 only in drafting style ("no person shall" becomes "a person must not", "he" and "his" become "the person" and "the person's", s 57(1) drops "in its discretion", s 60 drops "published" before "in the Gazette", and s 65(1) loses the amendment note "[18/2001]"), and s 47 is identical; the one difference of substance is that the 2012 s 57(3), "All sums collected under this section shall be paid to the Authority", is not in the 2024 text.
  Only ss 2(1) (the definition) and 20(1) are encoded on two dates in `sgba-versions.l4`; the others are encoded once, on the 2024 text, and this comparison is the reason that is enough for the sections named; the deletion of s 57(3) is read on two days in `sgba-versions-later.l4`.
- **Two nouns for the same thing, and why both are kept.**
  `Apparatus` (in `sgba-nouns.l4`, used by `sgba-sched.l4`, `sgba-p5-apparatus.l4` and their tests) has two facts, "capable of reception of a broadcasting service" and "capable of direct reception from a satellite", because the 2024 First Schedule needs only those.
  `Receiving equipment` (same file, used by `sgba-versions.l4`) adds "designed or constructed for", "used for the aural reception" and "used for the visual and aural reception in monochrome or colour", which the older Schedules' items 1 and 2 are defined by.
  Both were kept because the 2024 modules and their assertions were written and tested against `Apparatus`, and changing its fields would have changed every one of those rules after they were tested.
  The cost is that "capable of reception" is stated in both nouns; a later merge would change `sgba-p5-apparatus.l4` and `sgba-sched.l4` and their tests together.
- **What amended the First Schedule between the editions.**
  The 2012 edition's own legislative history lists, between the two editions, Act 55 of 2004 (Broadcasting (Amendment) Act 2004), Act 10 of 2005 (Telecommunications (Amendment) Act 2005), Act 21 of 2005 (Companies (Amendment) Act 2005), S 559/2010 and Act 15 of 2010 (Criminal Procedure Code 2010).
  I read all five in the Gazette (Act 10 of 2005 from my own download of Acts Supplement No. 3 of 2005 on 2026-11-03, which the Telecommunications Act subject also deposits as `TA1999.ACT10-2005.txt`): the 2004 Act touches only ss 48 and 48A, Act 10 of 2005 only s 26 of the Broadcasting Act (its s 32), the Companies (Amendment) Act 2005 only s 35(3) (item (3) of its Schedule), S 559/2010 only the Third Schedule, and the Criminal Procedure Code 2010 only s 55 (item 8 of its Sixth Schedule).
  The Acts' numbers were read off the texts' own headings: Act 55 of 2004 is Acts Supplement No. 58 of 2004, Act 21 of 2005 is Acts Supplement No. 18 of 2005, Act 15 of 2010 is Acts Supplement No. 13 of 2010.
  The three Acts that name the Broadcasting Act, with S 750/2004, S 878/2005 and S 776/2010 that brought them into operation, are deposited, and the wording each changed is a two-day version in `sgba-versions-acts.l4` (below); none of those sections is on the chain of s 2(1), s 20, s 47 and the First Schedule.
  Act 10 of 2005's s 26 is encoded as a version too, in `sgba-versions-later.l4`, with the later amendments listed in "The legislative history, item by item".
  The Bill for the 2004 Act (Bill 50/2004, extrinsic) was not fetched.
  The First Schedule is identical in the 2003 and 2012 editions, which is the evidence that nothing changed it between them.

### The Television and Radio Licensing Regulations (Rg 1), on the same two axes

The same design applies to the Regulations that set the licences under s 20: three versions, each with a valid-time date and a rule-version-time date (`sgba-versions.l4`, `the Rg 1 versions`; tests in `sgba-tests-rg1.l4`).

| version | takes effect | published | text and source |
| --- | --- | --- | --- |
| Revised Edition 2004 ("RevEd 2004") | 29 February 2004 | 29 February 2004 | `BA1994-RG1.txt` (e-Gazette, Revised Subsidiary Legislation 2004, "REVISED EDITION 2004 (29.2.2004)"); the PDF prints no separate publication line, so the Edition's date is used for both |
| as amended by S 333/2004 | 21 June 2004 | 15 June 2004 | `BA1994-S333-2004.txt`: made 11 June 2004, first published 15 June 2004 at 5:00 pm, "shall come into operation on 21st June 2004" |
| revoked by S 548/2012 | 1 January 2011 | 31 October 2012 | `BA1994-S548-2012.txt`: made 30 October 2012, first published 31 October 2012 at 5.00 pm, "shall be deemed to have come into operation on 1st January 2011" |

- The version read is chosen as for the Schedules.
  A conduct or reading day before 29 February 2004 answers `NOTHING`: the history line of the Revised Edition names S 21/80 and eleven amendments before it (S 46/83 to S 291/96), none of which was obtained, and S 212/99, which was (`sgba-i-s212-1999.l4`, one amended word-group of reg 8).
  A reading day after 4 November 2026 answers `NOTHING`; a reading day up to that day is answered from the latest version, the revoked S 548/2012 version for conduct from 1 January 2011.
- The amended Regulations are not printed whole anywhere I have: S 333/2004 prints only the replacement and new text.
  The encoding therefore holds the Revised Edition's regulations as printed (`sgba-i-rg1.l4`, functions marked "(RevEd 2004)") and the substituted or new text of S 333/2004 (`sgba-i-s333-2004.l4`, functions marked "(S 333/2004)"), and does not assemble a third, whole text.
  A regulation S 333/2004 left alone is read from the Revised Edition's function; the dispatchers of `sgba-versions.l4` take the helper for the version read.
  **Each dispatcher answers what Rg 1 states in terms, and its name says so** (`Rg 1 reg 23 states in terms that a licence is required for a broadcast sound receiver installed in a vehicle or in a vessel, …`, `Rg 1 reg 28(2) states in terms …`, `Rg 1 reg 29A(1) states in terms …`, `Rg 1 regs 24 and 29 state in terms …`).
  FALSE from one of them means that regulation says nothing of the kind, not that no licence was needed: for a sound receiver kept at home, the reg 23 dispatcher answers FALSE because reg 23 names a vehicle or a vessel, while s 20(1)(c) of the Act, stated by `s 20(1) the person contravenes section 20(1)(a), (b) or (c), …`, is a separate question (F-BA-12).
- S 548/2012's savings (reg 2(2)) and refund (reg 2(3)) are rules in `sgba-i-s548-2012.l4`.
  The savings agree with the version table: a matter before 1 January 2011 is read under the version in force on that day, even on a reading day after 31 October 2012.
- S 548/2012 and S 549/2012 carry the same publication day and hour (31 October 2012, 5.00 pm) and the same deemed commencement (1 January 2011).
  Whether either retrospective instrument is valid, and what a court would do with conduct already past, is not addressed.

### What the amending Acts and Orders after 2003 changed, on two days

None of these is on the chain of s 2(1), s 20, s 47 and the First Schedule; each has the same two days (`sgba-versions-acts.l4`, tests in `sgba-tests-versions-acts.l4`).
The text before is the Revised Edition 2003 (31 July 2003); the text after is the amending Act or Order, whose words the 2012 Revised Edition prints and the 2024 consolidation re-styles ("shall" to "must", "he" to "the person", "referred to" to "mentioned"; compared by script on 2026-11-04).

| provision | before | after | takes effect | published (assumed) | amending text, and what appoints its day |
| --- | --- | --- | --- | --- | --- |
| s 48 and new s 48A | five acts, in the course of trade or business, no knowledge element; no civil action | s 48 as substituted, with the knowledge element and s 48A | 1 January 2005 | 17 December 2004 | Act 55 of 2004 s 2; S 750/2004 para 2 |
| s 35(3) | 5% of the nominal amount of all voting shares | 5% of the total votes attached to all voting shares | 30 January 2006 | 30 December 2005 | Act 21 of 2005 s 58 and Schedule item (3); S 878/2005 para 2 |
| s 55 | proceedings conducted by an officer | the same, with the authorisation of the Public Prosecutor | 2 January 2011 | 20 December 2010 | Act 15 of 2010 s 430 and Sixth Schedule item 8; S 776/2010 para 2 |
| O 2 para 2 | not held (sub-paragraph (a) existed) | sub-paragraph (a) deleted | 25 March 2022 | 25 March 2022 | S 212/2022 para 2; no commencement clause, so its publication day (Interpretation Act, "Commencement of subsidiary legislation") |

- **Assumed, not ruled: the published day.**
  For an amendment made by an Act the published day is the day the commencement notification was first published, because until then a reader of the Act could not tell from the Act when it takes effect.
  The Acts were first published on 14 December 2004, 6 June 2005 and 21 June 2010; to use those days instead, change the three `... was first published on` constants in `sgba-versions-acts.l4`.
  The 5.00 pm of a Gazette publication is not kept, as for the Schedules.
- **S 212/2022 takes effect on its publication day.**
  The Order says "Made on 22 March 2022" and "First published ... on 25 March 2022 at 5 pm" and has no commencement clause; the "wef 25/03/2022" against sub-paragraph (a) in O 2 is the consolidation's note.
  The Interpretation Act 1965 (the consolidation in force from 5 December 2025; the text in force in March 2022 was not deposited), under "Commencement of subsidiary legislation", says that subsidiary legislation, "unless it is otherwise provided in the subsidiary legislation, takes effect and comes into operation on the date of its publication".
  The text of O 2 before the Order is not held, so a conduct day before 25 March 2022 answers `NOTHING` for O 2, as the single-text rule always did.
  O 2 exempts four named broadcasting holding companies from s 33; no receiver is within it.
- **The conduct day for s 55.**
  The first day of a question on s 55 is the day the proceedings are conducted; section 429(2) of the Criminal Procedure Code 2010 keeps proceedings begun before the appointed day (2 January 2011) under the repealed Code, and the encoding does not apply it (F-BA-13).

The later amendments are in `sgba-versions-later.l4` (tests in `sgba-tests-versions-later.l4`), on the same two days, and all are off the receiver chain:

| provision | before | after | takes effect | published (assumed to be the day the notification or Order was first published) | amending text, and what appoints its day |
| --- | --- | --- | --- | --- | --- |
| s 26 (sharing of facilities) | subsection (2) leaves a telecommunication system licensed under s 5 of the Telecommunications Act out; no power to direct co-operation with a telecommunication licensee | subsection (1) excludes such a system; new subsection (2), a power to direct co-operation with a telecommunication licensee | 16 February 2005 | 16 February 2005 | Act 10 of 2005 s 32; S 76/2005 para 2 |
| s 2(1) "Authority"; "Chairman" and "chief executive"; the Info-communications Development Authority of Singapore definition; s 12(3); s 22(f); s 23; ss 52(1) and 55; s 57(3); s 67 | the Revised Edition 2012 wording | nine amendments (the Media Development Authority of Singapore becomes the Info-communications Media Development Authority; s 23 and s 67 repealed; s 57(3), "All sums collected under this section shall be paid to the Authority", deleted) | 1 October 2016 | 29 September 2016 | Act 22 of 2016 s 93(a) to (i); S 461/2016 para 2 |
| s 61(1) | "taken in execution" | "taken under or pursuant to an enforcement order" | 1 April 2022 | 31 March 2022 | Act 25 of 2021 s 84; S 250/2022 para 2 (s 84 is not among the sections it excepts) |
| s 38 | the Minister's power to make further transitional provisions | deleted | 1 November 2022 | 31 October 2022 | Act 31 of 2022 s 23(1); S 850/2022 para 2 |
| ss 32(2), 34(2) and (3), 35(3A) and (6), 36(3A) and (4A), 37(3), 40(3), 44(1A) and (4) | the Act without the variable capital company provisions | S 26/2022 para 3 limbs (a) to (l) insert them | 13 January 2022 | 12 January 2022 | S 26/2022 para 1(1) and para 3 |
| s 8(5) and (6) | not in the Act | the late-payment charge, and the deeming of amounts collected before the Act's commencement | 1 April 2024 | 28 March 2024 | Act 4 of 2008 s 3; S 244/2024 para 2 (the Act except ss 9 and 12); S 128/2008 (18 March 2008) was cancelled by S 129/2008 |
| long title; s 2(1) definitions; ss 2A to 2D; Part 10A; s 59(1) and (5); s 64 and s 64A | the 2020 Revised Edition wording, or not in the Act | online communication services regulated | 1 February 2023 | 31 January 2023 | Act 38 of 2022 ss 2 to 7; S 29/2023 para 2 |
| the Fourth Schedule | item 1, social media service (Act 38 of 2022 s 8) | Part 1 items 1 and 2 (social media service; app distribution service) and Part 2 definitions | 25 September 2024 | 24 September 2024 | S 738/2024 paras 1 and 2; the Order states its own day |

- **Wording or presence, not a second encoding of the rule.**
  For all but s 26 these tables return the wording read (a STRING), or whether a provision is part of the Act (a BOOLEAN); the rules themselves are encoded once, on the 2024 text, as before.
  Their base is the Revised Edition 2012 (the 2020 Revised Edition for Act 38 of 2022); a conduct day before 31 August 2012 (31 December 2021) answers `NOTHING` for them, because the earlier wording of these provisions was not compared.
  Section 8(6) has a rule that computes the date: an amount collected before 1 April 2024 is deemed validly collected, and the rule says nothing about one collected on or after it.
  Section 26 has real rules on both sides: subsection (1) gives the same answer in both texts, and subsection (2) is `FALSE` before 16 February 2005 and the 2024 rule from then.

### The legislative history, item by item

The Act's legislative history (`BA1994.txt:4432-4745`) numbers 30 items.
Items 1 to 14 (1963 to 2002) precede the Revised Edition 2003, which restates the law at 31 July 2003 and is the earliest text held; nothing before it is encoded.
Status words: **deposited and encoded** (the text is a deposit and a module reads it), **source not obtained** (no text; a row in the coverage table says where I looked); every item from 15 to 30 is the first of these.
"Telecommunications subject" means a deposit of the Telecommunications Act encoder, used from where it is and cited from there, not copied.

| item | instrument | in operation | what it changes | status | module, or where looked |
| --- | --- | --- | --- | --- | --- |
| 15 | 2003 Revised Edition | 31 July 2003 | restates the Act | deposited | `BA1994.20030731.txt`; base of the two-day tables |
| 16 | Act 55 of 2004 | 1 January 2005 (S 750/2004) | s 48 repealed and re-enacted, new s 48A | deposited and encoded, with S 750/2004 | `sgba-versions-acts.l4` |
| 17 | Act 10 of 2005 | 16 February 2005 (S 76/2005) | s 26 (its s 32) | deposited and encoded (Telecommunications subject) | `sgba-versions-later.l4` |
| 18 | Act 21 of 2005 | 30 January 2006 (S 878/2005) | s 35(3) | deposited and encoded, with S 878/2005 | `sgba-versions-acts.l4` |
| 19 | S 559/2010 | 1 October 2010 | Third Schedule | deposited and encoded | `sgba-i-s559-2010.l4`, `sgba-versions.l4` |
| 20 | S 549/2012 | 1 January 2011 (published 31 October 2012) | First Schedule | deposited and encoded | `sgba-i-s549-2012.l4`, `sgba-versions.l4` |
| 21 | Act 15 of 2010 | 2 January 2011 (S 776/2010) | s 55 | deposited and encoded, with S 776/2010; fork F-BA-13 | `sgba-versions-acts.l4` |
| 22 | 2012 Revised Edition | 31 August 2012 | restates the Act | deposited | `BA1994.20120831.txt`; base of the later tables |
| 23 | Act 22 of 2016 | 1 October 2016 (S 461/2016) | nine amendments (its s 93) | deposited and encoded (Telecommunications subject) | `sgba-versions-later.l4` |
| 24 | 2020 Revised Edition | 31 December 2021 | restates the Act | deposited (2026-11-04) | `BA1994.20211231.txt`; compared with the 2024 consolidation on ss 2(1), 20, 47 and the First Schedule: identical; base of the Act 38 of 2022 tables |
| 25 | S 26/2022 | 13 January 2022 | variable capital company provisions in Part 10 | deposited and encoded (Telecommunications subject) | `sgba-versions-later.l4`; the inserted provisions in `sgba-p10-ownership.l4` |
| 26 | Act 25 of 2021 | 1 April 2022 (S 250/2022) | s 61(1) (its s 84) | deposited and encoded (Telecommunications subject), with S 250/2022 (deposited here) | `sgba-versions-later.l4` |
| 27 | Act 31 of 2022 | 1 November 2022 (S 850/2022) | s 38 deleted (its s 23(1)) | deposited and encoded (Telecommunications subject) | `sgba-versions-later.l4` |
| 28 | Act 38 of 2022 | 1 February 2023 (S 29/2023) | long title, s 2(1) definitions, ss 2A to 2D, Part 10A (ss 45A to 45T), s 59, s 64 and new s 64A, the Fourth Schedule | deposited and encoded, with S 29/2023 | `sgba-versions-later.l4` |
| 29 | Act 4 of 2008 | 1 April 2024 (S 244/2024; S 128/2008 was cancelled by S 129/2008) | s 8(5) and (6) | deposited and encoded, with S 244/2024, S 128/2008 and S 129/2008; fork F-BA-09 answered | `sgba-versions-later.l4` |
| 30 | S 738/2024 | 25 September 2024 (the Order says so) | the Fourth Schedule (s 2B(1)) | deposited and encoded | `sgba-versions-later.l4` |

- **Nothing in items 15 to 30 is source not obtained any more.**
  The 2024 consolidation is still the single text of every rule outside the two-day tables, and it contains these amendments (it marks them "[Act 38 of 2022 wef 01/02/2023]" and so on); where a notification states a day, the table says the notification says it, and "wef" is SSO's annotation; where the consolidation's wording before an amendment is held (the 2003, 2012 and 2020 Revised Editions and the amending texts), the two-day tables read it, and elsewhere a rule on the 2024 text answers `NOTHING` for a day before 25 September 2024, as it always did.
- **The consolidation's "wef" annotations agree with the days the notifications state.**
  Counted in `BA1994.txt` on 2026-11-04: "Act 38 of 2022 wef 01/02/2023" 51 times (S 29/2023 says 1 February 2023), "Act 4 of 2008 wef 01/04/2024" twice (S 244/2024 says 1 April 2024), "Act 25 of 2021 wef 01/04/2022" once (S 250/2022 says 1 April 2022 at 12.00 a.m.), "S 738/2024 wef 25/09/2024" once (the Order says 25 September 2024).
  In the tables the day comes from the notification or the Order, and the annotation is SSO's own and is not relied on.
  The Act number in each heading is the number the history gives: "No. 38 of 2022." and "No. 4 of 2008." are printed under the assent; the supplement numbers differ for Act 38 of 2022 (Acts Supplement No. 37).
  S 250/2022 names the Act by title only (the Courts (Civil and Criminal Justice) Reform Act 2021), so the number 25 of 2021 rests on the Telecommunications Act encoder's deposit of the Act, `TA1999.ACT25-2021.txt`.
- **After the consolidation**: nothing amending the Act has been found; `sgba-vintage.l4` says what the orchestrating session's index search of 4 November 2026 did and did not show.
- **Why no row is on the receiver chain**: items 16, 17, 18, 21, 23, 25, 26, 27, 28, 29 and 30 touch only ss 48 and 48A; s 26; s 35(3); s 55; four definitions of bodies and offices in s 2(1) and ss 12(3), 22(f), 23, 52(1), 55, 57(3) and 67; the variable capital company provisions in ss 32 to 44; s 61(1); s 38; ss 2A to 2D, 45 to 45T, 59, 64 and 64A; s 8(5) and (6); and the Fourth Schedule; none of those is the s 2(1) definition of "broadcasting apparatus", s 20, s 47 or the First Schedule. Items 19 and 20 are the Schedules, which `sgba-versions.l4` reads on two days, and items 15, 22 and 24 are restatements.
  Act 38 of 2022 mentions "broadcasting apparatus" once, in the words after which it inserts new words in the long title, and never names s 20, s 47 or the First Schedule (searched in the deposit); it adds definitions to s 2(1) but leaves the definition of "broadcasting apparatus" alone.

## Search for receivers

A mechanical search of every deposited Broadcasting Act text for words that would show a rule about receiving equipment, run on 2026-11-04 over the deposited `.txt` files (the lawplain rows, the three Act texts and the seventeen Gazette deposits).
Whole words, case-insensitive, singular and plural together ("receiver" counts "receivers", "sound" counts "sounds", "licence fee" counts "licence fees", "car" counts "cars"); the counts are of occurrences, not of lines.

| document | receiver(s) | sound(s) | radio(s) | television(s) | apparatus | licence fee(s) | vehicle(s) | car(s) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Act, Revised Edition 2003 | 4 | 4 | 8 | 12 | 63 | 1 | 1 | 0 |
| Act, Revised Edition 2012 | 4 | 4 | 8 | 12 | 63 | 1 | 1 | 0 |
| Act, consolidation 2024 | 0 | 5 | 8 | 15 | 60 | 1 | 1 | 0 |
| Rg 1 (Television and Radio Licensing Regulations, RevEd 2004) | 104 | 36 | 23 | 87 | 42 | 2 | 20 | 0 |
| S 333/2004 | 25 | 8 | 3 | 20 | 4 | 0 | 4 | 0 |
| S 548/2012 | 6 | 3 | 3 | 6 | 0 | 0 | 0 | 0 |
| S 549/2012 | 0 | 0 | 0 | 2 | 3 | 0 | 0 | 0 |
| S 559/2010 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| RG3 (TVRO System Regulations) | 5 | 1 | 0 | 5 | 6 | 1 | 0 | 0 |
| S 354/2001 | 2 | 0 | 0 | 2 | 1 | 1 | 0 | 0 |
| S 212/1999 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 |
| S 477/2020 | 0 | 4 | 0 | 1 | 0 | 0 | 7 | 1 |
| S 523/2010 as made (Gazette) | 0 | 0 | 3 | 2 | 0 | 0 | 0 | 0 |
| S 523/2010 (lawplain, no Schedule) | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| S 555/2003 | 0 | 0 | 2 | 2 | 0 | 1 | 0 | 0 |
| S 70/2012 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| S 674/2016 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| O 1 (RevEd 2004, Gazette) and O 1 (lawplain) | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| the other thirteen deposits (N 1, RG2, OR2, OR3, S 121/2008, S 211/2022, S 47/2023, S 30/2023, S 600/2014, S 196/2004, S 330/2013, S 478/2020, S 496/2001) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Contexts, instruments only (the Act's own hits are its sections and Schedules, which the coverage table reads):

- Rg 1 is the instrument about receivers: "receiver(s)" 104 times, "television" 87, "sound" 36, "vehicle(s)" 20 (including the table of contents and the regulation headings), "radio" 23; Part IV is headed "BROADCAST SOUND RECEIVERS" (regs 23 to 26) and Part V "BROADCAST TELEVISION RECEIVERS" (regs 27 to 35); "vehicle" appears in regs 5, 10, 13, 23 and 28 and in their headings and the table of contents.
  "car" does not appear in it.
- S 333/2004 and S 548/2012 repeat those terms because they amend and revoke Rg 1.
- "receiver(s)" (RG3, 5; S 354/2001, 2): reg 2's definition of "broadcast television receiver" ("any apparatus used for the visual and aural reception of any broadcasting service"), reg 10 (the diagram of the TVRO system and the cable system connecting it to receivers, and the location of every receiver connected to it) and reg 13(2) (a change in the number of such receivers).
- "radio" in S 523/2010 (3 in the Gazette text, 1 in the lawplain text that lacks the Schedule): para 4(c)(i) and Schedule items 2 and 3 ("special interest radio services transmitted through an educational institution's closed Internet protocol network" and "... public address system").
  "radio" in S 555/2003: "a radio frequency"; in S 70/2012 and S 674/2016: "radio-communication" (Internet access).
- "television": S 549/2012 and RG3 as above; S 559/2010 (the Third Schedule's "Subscription nationwide television service"); OR1 ("close circuit television surveillance services"); S 523/2010; S 477/2020 ("subscription nationwide television service"); S 555/2003 (teletext and television channels); S 212/1999 (the title "Broadcasting and Television").
- "licence fee(s)": the heading above reg 4 of RG3 and of S 354/2001; "annual licence fee of $2,000" for a teletext service (S 555/2003); in Rg 1, reg 5(1)(b) ("the appropriate annual licence fee set out in the First Schedule") and reg 37(2) ("licence fees payable for the block licence").
  In the Act the one hit in each text is in a list of fees and charges ("royalties, licence fees, spectrum utilisation fees and other fees"; 2003 edition line 450, 2012 edition 441, consolidation 1075), which says nothing of receivers.
- "sound(s)" (S 477/2020, 4) and "vehicle(s)" and "car(s)" (S 477/2020): digital display panels, public passenger transport vehicles and "Taxi or chauffeured private hire car"; none is about receiving equipment.
- The words "FM", "AM", "VHF", "UHF", "medium wave", "frequency modulation" and "amplitude" occur in no deposited text.
- In the Act, "receiver" occurs only in the First Schedule of the two Revised Editions (items 1 and 2 and their two definitions: 2003 edition lines 2139, 2141, 2146, 2148; 2012 edition 2167, 2168, 2171, 2173) and nowhere in the 2024 consolidation.
  "sound(s)" in the Act is two hits in the definition of "programme" (2003 edition lines 214 and 216; 2012 edition 206 and 208; consolidation 300 and 303) plus, in the Revised Editions, item 2 and its definition, and, in the consolidation, lines 339, 725 and 730 (the definitions of "content", of "MMS message" and of "one-to-one live aural communications": "speech, music or other sounds", "by any sound or images", "speech or other sounds conveyed in real time").

## Seat

The seat is **a person who owns or uses broadcasting equipment or provides a broadcasting service, or who handles a decoder or an online communication service, and who asks whether the Broadcasting Act requires a licence of them, whether they are committing an offence, and how much they can be punished.**
Why this seat: the Act addresses the Authority, the Minister and licensees at least as much as it addresses the public, and the person on the other side of every one of those provisions is someone holding a licence, equipment or a service who wants to know where they stand.
`sgba-seat.l4` is the **neutral** seat: 18 questions, each with `@export` and an `@desc` on every input, covering the licensing of services (s 8 and the Second Schedule), class licences and exemption orders, decoders (s 48 and the civil action of s 48A), corporate officers (s 56), jurisdiction (s 58), other laws (s 54), information notices (s 50), obstruction (s 49) and the appeal and representation periods of ss 12 and 10.
`sgba-cases-seat.l4` has 57 cases that assert the words of the answers.
The questions about apparatus, the First Schedule, the TVRO Regulations, compounding and seizure are in `sgba-tv-seat.l4` (12 questions; the questions on apparatus, the First Schedule, section 20(1) on each reading of its premises phrase, and Rg 1 take the day of the conduct, the day the law is read as at, and the kind of equipment) with `sgba-tv-cases-seat.l4` (178 cases) and `sgba-tv-s9a.l4` (14 assertions), because their answers are conclusions about the question and so are quarantined.
Every input of every question is plain: yes or no, a number, a date or a choice written out in words.
No question asks the person which reading of a fork to take.
Where the Act does not say, the answer is the sentence "The Act, as deposited, does not say for that date.", which is the explicit not-covered value (`NOTHING` in layer 1) turned into words, and the cases assert it.
The quarantined equipment questions, which take two days, answer "The texts deposited do not say for those two days." when no version of the First Schedule qualifies, and, for a kind of equipment they do not know, "Say television, FM radio, AM radio or satellite dish: those are the kinds this question knows."
`sgba-seat.l4` restates no rule; it only words the answer.

## Inputs

`../../registers/source-bundle/BA1994.txt`; the fourteen instrument deposits listed in the coverage table (each under `../../../broadcasting-*/registers/source-bundle/`); the two Gazette editions `BA1994.20030731.txt` and `BA1994.20120831.txt`; `BRIEF.md` (a copy of the commissioning brief, kept here); `docs/ENCODING-GUIDE.md` and `docs/directory-conventions.md` of the commons repository; the two skills `encoding-a-subject` and `writing-l4-rules`; the existing Interpretation Act row `../../../interpretation-act/encodings/legalese-sonnet-5.5/` (read for its section 9A and its time rules, cited and never imported).

## What is encoded, and in which file

Every section, subsection, paragraph, defined term, Schedule item and table row of the Act has a row in the coverage table below, and every row has one disposition.
Each Part has its own modules, in the Act's own order.

| file | what it holds |
| --- | --- |
| `sgba-nouns.l4` | nouns only: `Punishment`, `Imprisonment`, `Daily fine`, `Forfeiture`, `Kind of person`, `Apparatus`, the Second Schedule services, the acts with a decoder, the ways to serve a document |
| `sgba-vintage.l4` | the date windows in which each deposited text is the text in force |
| `sgba-versions-later.l4` | the later amendments (Act 10 of 2005 s 26; Act 22 of 2016 s 93; Act 25 of 2021 s 84; Act 31 of 2022 s 23(1); S 26/2022 para 3; Act 4 of 2008 s 3, which inserts s 8(5) and (6); Act 38 of 2022; S 738/2024) on two days |
| `sgba-versions-acts.l4` | the wording of ss 35(3), 48, 48A and 55 before and after Acts 21 of 2005, 55 of 2004 and 15 of 2010, and of the Exemption (No. 2) Order O 2 after S 212/2022, on two days each |
| `sgba-versions.l4` | the First and Third Schedules and the Television and Radio Licensing Regulations (Rg 1) version by version on two dates (valid time, publication time), the selection of the version read, s 2(1) and s 20(1) on two dates on each reading of F-BA-01, the Rg 1 dispatchers, and the TVRO institution-only rule from 1 August 2001 |
| `sgba-p1-defs.l4`, `sgba-p1-other.l4`, `sgba-p1-online.l4` | Part 1: s 1, s 2(1) (every definition), s 2(2) to (6), ss 2A to 2D (online communication services, the Fourth Schedule, transitional arrangements, "provider") |
| `sgba-p2-authority.l4` | Part 2: directions by the Minister (s 3) and the exclusion of the Authority's liability (s 4) |
| `sgba-p4-services.l4` | Parts 3 and 4: licensing powers (ss 5 to 7), licensing of services, class licences, modification, suspension, Codes of Practice, free-to-air and public-service provisions (ss 8 to 19) |
| `sgba-p5-apparatus.l4` | Part 5: licensing of broadcasting apparatus (ss 20 and 21) |
| `sgba-p6-p7.l4` | Parts 6 and 7: frequency planning, sharing of facilities, inspection and testing, building space (ss 22 to 28) |
| `sgba-p8-p9-foreign.l4` | Parts 8 and 9: proscribed and declared foreign broadcasting services (ss 29 to 31) |
| `sgba-p10-ownership.l4` | Part 10: ownership and control of broadcasting companies (ss 32 to 45) |
| `sgba-p10a-d1-d2.l4`, `sgba-p10a-d3.l4`, `sgba-p10a-d4.l4` | Part 10A, Divisions 1 to 4: online communication service regulation (ss 45A to 45T) |
| `sgba-p11-offences.l4` | Part 11: offences, penalties, powers of officers, composition, jurisdiction (ss 46 to 58) |
| `sgba-p12-misc.l4` | Part 12: appeals, exemption, service of documents, financial penalties, regulations, transitional provisions (ss 59 to 68) |
| `sgba-sched.l4` | the First, Second, Third and Fourth Schedules |
| `sgba-i-*.l4` (30 files) | the instrument deposits (twelve from lawplain; eighteen from the e-Gazette, among them `sgba-i-s212-2022.l4`, `sgba-i-rg1.l4`, `sgba-i-s333-2004.l4`, `sgba-i-s548-2012.l4`, `sgba-i-s549-2012.l4`, `sgba-i-s559-2010.l4`, `sgba-i-s354-2001.l4` and the Class Licence amendments) |
| `sgba-seat.l4`, `sgba-cases-seat.l4` | the neutral seat and its cases |
| `sgba-tv-seat.l4`, `sgba-tv-cases-seat.l4`, `sgba-tv-s9a.l4` | the quarantined seat questions, their cases and the Interpretation Act section 9A marker |
| `sgba-tests-*.l4` | the layer-1 tests; every expected value is written from the text of the provision it tests, not from what the code returned |
| `gen-coverage.py`, `qx.py`, `srcrefs.py`, `check.sh`, `fetch-main-l4.sh` | the tools named under "Generators and checkers" |
| `srcrefs-all.py` | runs `srcrefs.py --strict` over every module that quotes a source, against the texts deposited in this repository, in three groups (the Act's modules; the three modules that quote more than one deposit; each other instrument module); exits 0 only when there are 0 problems; added by the orchestrating session after the independent review, see "What `check.sh` prints" |
| `dispositions.tsv` | the disposition of every row, read by `gen-coverage.py` |
| `graph/` | the reference graph for a lay reader's diagram: `nodes.tsv`, `edges.tsv`, `edges-uncited.tsv`, `tv-path.tsv`, `renumbering.tsv`, `check-graph.py` and a `README.md` that says what each arrow means and where the graph is deliberately silent |
| `TV-QUESTION-BA.md` | the quarantined conclusions for the question the two encodings were commissioned to help answer |

### How a rule is shaped

- Facts a witness of ordinary competence could state are `GIVEN` inputs, typed `BOOLEAN`, `NUMBER`, `DATE` or a noun of `sgba-nouns.l4`.
- The Authority's and the Minister's judgments ("is satisfied", "thinks fit", "may approve") are asked as plain facts: whether the Authority is satisfied is the Authority's, and the encoding takes it as given.
- Meanings borrowed from another Act (the Companies Act 1967, the Variable Capital Companies Act 2018, the Penal Code 1871 and others) are asked as facts, with the section cited; they are never re-encoded.
- A definition that says "means" returns `BOOLEAN`; one that says "includes" returns `MAYBE BOOLEAN`, `JUST TRUE` for a listed thing and `NOTHING` otherwise, because an inclusive definition never says no.
- A penalty is a `Punishment` record holding the ceilings: a fine, a term in months, a daily fine for a continuing offence and a forfeiture.
  Where the Act says "a fine not exceeding $X or imprisonment not exceeding Y or both", each figure is a ceiling the court may use alone or together, and the record holds the ceilings, not a sentence.
- A rule that depends on the text of a Schedule or of an instrument takes a date and answers `NOTHING` outside the deposited text's window.

## Fork register

**Bench rulings of 2026-11-04** (full text in `docs/ENCODING-GUIDE.md` section 5; they apply to every entry below).
These rulings set this corpus's drafting conventions, which each row follows and flags; L4 itself takes no position on them.

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23


Each entry gives the readings, the text that licenses each, which one the encoding takes, and where.
"No ambiguities found" would not be believed, and the entries below are everything the encoder noticed, including those where no reading was preferred.
The encoder's reading is a choice, not a ruling; every entry waits for one.

**F-BA-01.
Section 2(1) "broadcasting apparatus" (BA1994.txt:277-279).**
The text: "any apparatus capable of or designed or constructed for the reception of any broadcasting service and specified in the First Schedule".
Reading A: "specified in the First Schedule" qualifies the whole phrase, so an apparatus is broadcasting apparatus only if it is capable of, or designed or constructed for, reception *and* is specified in the First Schedule.
Reading B: it qualifies only "designed or constructed for", so an apparatus *capable of* reception is broadcasting apparatus whether or not it is listed, and one *designed or constructed for* reception is so only if listed.
For A: one noun phrase with two post-modifiers; the First Schedule is headed "Broadcasting apparatus" with the cross-reference "Sections 2(1) and 65(1)" (BA1994.txt:4342-4346), and s 65(1) lets the Minister amend it at any time; a listing that the definition did not require would have no work to do for apparatus that is capable of reception.
For B: the double "or" before "reception", and no comma before "and specified".
Taken: A, in `sgba-p1-defs.l4` (`s 2(1) the apparatus is broadcasting apparatus on`).
Not encoded: B, because `Apparatus` has no field for "designed or constructed for"; the input `capable of reception of a broadcasting service` stands for "capable of, or designed or constructed for, the reception of any broadcasting service".
Where the readings differ is an apparatus that can receive but is not in the First Schedule; what that means for the question is in `TV-QUESTION-BA.md`.

**F-BA-02.
Section 7(2), void transfer (BA1994.txt:1024-1025).**
The text: "Any purported transfer of any licence is for all purposes void and of no effect."
Reading A (literal): every purported transfer is void.
Reading B: only a purported transfer made without the prior written consent that s 7(1) requires is void, because s 7(1) contemplates a transfer *with* consent.
For A: the words say "any".
For B: the heading "Restriction on transfer of licences" and the consent in (1).
Taken: both are encoded, as two functions in `sgba-p4-services.l4` (the first named "read literally", the second "on the reading that only a transfer without consent is"); no choice is made between them.

**F-BA-03.
Section 20(1)(c), premises (BA1994.txt:1434-1436).**
The text: "operate or have on any premises in Singapore owned or occupied by the person broadcasting apparatus on or by which broadcasting services are received".
Reading A: "on any premises in Singapore owned or occupied by the person" qualifies both "operate" and "have".
Reading B: it qualifies only "have", so operating the apparatus elsewhere is also within (c).
For A: one verb phrase with a single place phrase.
For B: the place phrase sits after both verbs and "operate" can take a place of its own.
The Regulations also say "A licence shall not be required for the temporary use of a broadcast sound receiver in a public place or at an official or social function or a function organised for charitable purposes" (reg 24, `BA1994-RG1.txt:460-462`; reg 29 says the same of a television receiver, `521-523`), which has work to do only if operating a receiver reaches such places, and, for a television receiver before S 333/2004, reg 27(1) "No person shall operate a broadcast television receiver without a licence" was not limited to premises (`BA1994-RG1.txt:481-482`).
Taken: A is the default, and B is encoded beside it.
The `Dealing with apparatus` noun holds the premises phrase as three facts (`operates it`, `has it`, `the place is premises in Singapore owned or occupied by the person`), so that either reading can be written (`sgba-nouns.l4`).
Reading A is `(operates it OR has it) AND the place is premises in Singapore owned or occupied by the person`; reading B is `operates it OR (has it AND the place is premises in Singapore owned or occupied by the person)`.
The functions on reading A are unchanged in name: `sgba-p5-apparatus.l4` (`s 20(1)(c) …, on`) and the `reading A` and `reading B` (of F-BA-01) functions of `sgba-versions.l4`.
The functions on reading B of F-BA-03 carry `reading B of F-BA-03` in their names, in `sgba-p5-apparatus.l4` and, combined with each reading of F-BA-01, in `sgba-versions.l4`.

**F-BA-04.
Section 48A(3), six years (BA1994.txt:3772-3774).**
The text: "after the expiry of 6 years from the time the relevant act ... took place".
Reading A: counted on dates, the action is in time up to and including the sixth anniversary of the day of the act.
Reading B: "time" is the moment of the act, so the period ends at that clock time on the anniversary and an action brought later that day is late.
Reading C: the day of the act counts as the first day, so the last day is the day before the anniversary.
Taken: A, in `sgba-p11-offences.l4` (`s 48A(3) the action is not barred`), which cannot see hours.
The Interpretation Act's rules for counting periods are encoded in the Interpretation Act row and are not applied here; whoever needs the exact last day should ask that row.

**F-BA-05.
TVRO System Regulations, reg 2 "institution" and reg 3(2) (`BA1994-RG3.txt:7` and `:16`).**
The text: "institution" means "any body of persons, corporate or unincorporate, and includes any undertaking"; "No person other than an institution may be granted with a licence."
Reading A: an individual who carries on an undertaking is, for that reason, an institution.
Reading B: "undertaking" extends the meaning to a body that is an undertaking, and an individual acting alone is not an institution.
For A: "includes any undertaking" is added to "body of persons" and an undertaking can be one person's.
For B: the definition begins "body of persons" and the regulation says "person other than an institution", which distinguishes a person from an institution.
Taken: neither; the limbs are `OR` and each is a plain fact the person states (`reg 2 the person is an institution` in `sgba-i-tvro-regs.l4`).

**F-BA-06.
Section 43(9) "foreign source", paragraph (d) (BA1994.txt:2588-2611).**
The text, as printed: "(d) any — (i) body corporate formed or incorporated in Singapore, one or more of whose members or directors are not citizens of Singapore ...; or (ii) unincorporated association or body constituted under any law in force in Singapore, one or more of whose members or directors are not citizens of Singapore ..., (d) as the Minister may, by notification in the Gazette, declare to be a foreign source; or (e) any other source outside Singapore that the Minister may ... declare to be a foreign source".
The consolidation prints the closing words of (d) with the letter (d) again.
Reading A: the closing words end paragraph (d), so a Singapore body with a non-citizen member or director is a foreign source only if the Minister declares it.
Reading B: they are a separate paragraph, so such a body is a foreign source outright, and the Minister's declaration is an extra route.
Taken: neither.
`s 43(9) foreign source includes this Singapore body` answers `JUST TRUE` for a declared body and `NOTHING` for an undeclared one, which is the one case where the readings differ.

**F-BA-07.
Section 45H(1)(c), the closing words (BA1994.txt:3064-3071).**
The consolidation prints "(ii) so as to stop or reduce the communication, provision or access, or further communication, provision or access, by Singapore end-users of egregious content on the online communication service" with the letter (ii) a second time, after (c)(ii)(A) and (B).
Reading A: the words end paragraph (c)(ii) only.
Reading B: they end the whole of paragraph (c), so disabling access under (c)(i) must also be "so as to stop or reduce" the same communication and access.
Taken: A, in `sgba-p10a-d1-d2.l4` (`s 45H(1) the direction is of a kind the subsection allows`: the purpose is on the second limb only).

**F-BA-08.
The legislative history, items 19 and 20 (BA1994.txt:4640-4648). Resolved 2026-11-03 by the e-Gazette text of S 549/2012.**
The history prints "G.N. No. S 559/2010 - Broadcasting Act (Amendment of Third Schedule) Notification 2010, commencement 1 October 2010" and "G.N. No. S 549/2012 - Broadcasting Act (Amendment of First Schedule) Notification 2012, commencement 1 January 2011".
A notification numbered and titled 2012 with a commencement in 2011 looked odd on its face.
Reading A: a 2012 notification with a retrospective commencement.
Reading B: the year or the number is misprinted for 2010 or 2011.
Reading C: the commencement date is misprinted.
The Gazette text of S 549/2012 settles it for reading A: "Made this 30th day of October 2012", "First published in the Government Gazette, Electronic Edition, on 31st October 2012 at 5.00 pm", and paragraph 1, "shall be deemed to have come into operation on 1st January 2011" (`BA1994-S549-2012.txt` lines 3, 20-22, 37).
The notification is retrospective, which is why the table above has two dates.
What remains open is not the date but the validity and effect of a retrospective notification, which the encoding does not address (see "Point in time").

**F-BA-09.
Act 4 of 2008, commencement (BA1994.txt:1094, 1104 and, in item 29 of the history, 4729-4737).**
The consolidation prints "[Act 4 of 2008 wef 01/04/2024]" on s 8(5) and on s 8(6), and prints "Commencement: 1 April 2024" for the Statutes (Miscellaneous Amendments) Act 2008 in item 29 of the history.
That is odd for a 2008 Act, but SSO's own list of version dates includes 2024-04-01, so the date is not obviously a misprint.
Section 8(6) deems valid every amount collected "before the date of commencement of the Statutes (Miscellaneous Amendments) Act 2008" as a late-payment charge.
Reading A: that date is 1 April 2024, as printed.
Reading B: it is an earlier date in 2008, for which no source in hand gives a date.
**Answered 2026-11-04 by the texts, reading A:** S 244/2024 (made 27 March 2024, published 28 March 2024) says "The Statutes (Miscellaneous Amendments) Act 2008, except sections 9 and 12, comes into operation on 1 April 2024", and s 3 (the amendment of s 8) is not among the excepted sections.
The only earlier appointment, S 128/2008 (published 18 March 2008 at 5.00 pm), said 18 March 2008; S 129/2008 (published 18 March 2008 at 8.00 pm) notified that it "has been published in error is to be treated as cancelled".
Taken: reading A. `sgba-versions-later.l4` computes the date; the rule on the 2024 text (`sgba-p4-services.l4`) still asks whether the amount was collected before that commencement as a plain fact.

**F-BA-10.
Rg 1: "broadcast matter transmitted by radio waves, wire or cable" (BA1994-RG1.txt:139-156).**
Reg 2(1) of the Revised Edition defines "broadcast sound receiver" as "any apparatus used for the aural reception of broadcast matter transmitted by radio waves, wire or cable" and "broadcast television receiver" as one used for the aural and the visual reception of the same, excluding a TVRO system.
The Act's definition of "broadcasting apparatus" and the First Schedule speak of "any broadcasting service".
Reading A: the receiving facts are the same facts (what a witness says the equipment receives).
Reading B: "broadcast matter transmitted by radio waves, wire or cable" is narrower or wider than "any broadcasting service" and the two can differ for some equipment.
Taken: A; the encoding asks the same receiving facts for both (`sgba-i-rg1.l4`, `sgba-nouns.l4` `Receiving equipment`).
No outcome in the tests differs.

**F-BA-11.
S 333/2004 deletes the definitions of "broadcast sound receiver" and "broadcast television receiver" (BA1994-S333-2004.txt:25-54).**
Para 2(a) deletes both definitions and substitutes "broadcasting apparatus" (any broadcast sound receiver or broadcast television receiver), "commercial property" and "hospital"; para 2(c) deletes paragraph (2).
After 21 June 2004 the Regulations use "broadcast sound receiver" and "broadcast television receiver" without defining them.
Reading A: they take the meaning the Act's First Schedule gives "for the purposes of this Schedule" ("any apparatus used for the aural reception of any broadcasting service"; "... for the visual and aural reception in monochrome or colour of any broadcasting service").
Reading B: they keep their ordinary meaning, or the meaning the deleted definitions gave.
Taken: neither is decided; the amended rules take the receiver kind as a fact (`Rg 1 reg 2(1) the apparatus is broadcasting apparatus (S 333/2004)` has two inputs, one for each receiver).

**F-BA-12.
Rg 1: the provisions that name a licence for a broadcast sound receiver (BA1994-RG1.txt:170, 215-223, 276-289, 441-444, 460-472, 485-488, 629, 657-660).**
Reg 23(1) says in terms that "a licence shall be required" for a sound receiver installed in a vehicle or vessel (as the Revised Edition prints it) and reg 23(2) for one in a vessel (as S 333/2004 substitutes it).
Regs 5(2) and (3), 8(b), 24, 25, 26 and 27(3), reg 2(2)(b), the First Schedule (item 2) and the Second Schedule (item 1) speak of a licence for a broadcast sound receiver without that limit.
The texts allow more than one reading of how these fit together and with s 20(1)(c) of the Act; the readings and what each gives by date are in `TV-QUESTION-BA.md`, "Household radios".
Taken: none; the encoding says what each regulation says, and `sgba-tv-seat.l4` answers "Yes." only where a regulation states a requirement in terms.

**F-BA-13.
Section 55, the Criminal Procedure Code 2010 and proceedings begun before 2 January 2011 (BA1994-ACT15-2010.txt:9697-9709, 13743-13747).**
The text: item 8 of the Sixth Schedule inserts ", with the authorisation of the Public Prosecutor," after "this Act may" in s 55 (conduct of proceedings in respect of any offence under the Act, including the offence in s 47); s 429(2)(a) says the Code "shall not affect ... any inquiry, trial or other proceeding commenced or pending under the repealed Code before the appointed day".
Reading A: the amendment applies by the day the proceedings are conducted, so that from 2 January 2011 an officer needs the Public Prosecutor's authorisation, whenever the offence was committed and the proceedings begun.
Reading B: proceedings begun before 2 January 2011 continue under the Revised Edition 2003 wording of s 55 even after that day.
For A: the amendment is made by s 430 and the Sixth Schedule, which are about the text of other Acts, not about proceedings.
For B: item 8 is a part of "this Code", and s 429(2) preserves what was begun before the appointed day "as if this Code had not been enacted".
Taken: A, as an assumption; `sgba-versions-acts.l4` reads s 55 by the day given and does not encode s 429(2).
No question of the seat turns on it: the seat's questions do not ask who may conduct a prosecution.

### Reading notes (no outcome differs)

**R-1.
Section 37(4), a stray letter (BA1994.txt:2258-2264).**
After the sub-paragraphs (c)(i) and (c)(ii) the words "as the case may be" are printed as "(c) as the case may be".
They are read as the closing words of s 37(4) as a whole, which is how `sgba-p10-ownership.l4` states them.
No other reading was found.

**R-2.
Section 44(1)(b), a stray letter (BA1994.txt:2638-2649).**
After (b)(ii) the words "any foreign source, whether acting alone or together with one or more other foreign sources" are printed as "(b) any foreign source ...".
They are read as the object of "appointed by" and of "accustomed or under an obligation ... to act in accordance with the directions, instructions or wishes of".
No other reading was found.

**R-3.
Rg 1 reg 23(1) and reg 28(2), "in respect of which a ship station licence has not been granted" (BA1994-RG1.txt:440-445, 495-512).**
The relative clause follows "a vehicle or in a vessel".
A ship station licence is granted for a vessel, so the clause is read as qualifying "vessel" only.
If it qualified both, a vehicle could never be licensed under the regulation, which makes no sense of reg 23(1).
No outcome differs.

**R-4.
The Second Schedule of Rg 1 before and after S 333/2004.**
The Revised Edition's Second Schedule prints, for each of its two items, "(if the application is made after 21 days following the expiration of the licence)".
The Schedule S 333/2004 substitutes prints four items and no such condition.
The encoding states each as printed: the Revised Edition's function has the 21-day condition and the amended function does not.
Whether the 21 days survives is not a question the amended text answers.

## What the Act turns out to say

Facts of the text, stated without applying them to anyone.

- The Act has twelve Parts and a Part 10A, four Schedules and 842 coverage rows; Part 10A (online communication service regulation, ss 45A to 45T) entered on 1 February 2023, and the Fourth Schedule (the "social media service" and "app distribution service" items) can be revoked, replaced or added to by order (s 2B).
- It has **no general penalty section**: section 66 (regulations) carries no penalty clause and section 67 is repealed (Act 22 of 2016).
  Each offence section carries its own penalty; ss 54 and 56 to 58 carry the rest of the penal machinery (other laws, corporate and unincorporated offenders, composition, jurisdiction).
- Penalty ceilings in the encoding (fine; imprisonment; further daily fine; forfeiture):
  s 28(4) $10,000; s 30(3) $40,000, 3 years; s 31(5) $100,000; s 33(5) $50,000 and $5,000 a day; s 41(1) $50,000 and $5,000 a day; s 41(2) $50,000, 3 years and $5,000 a day; s 42(3) the same as s 41(2); s 43(8) $50,000, 3 years, and the fund forfeited; s 45E(2) $1 million and $100,000 a day; s 45F(2) $20,000 a day up to $500,000 in all; s 45N(2) $1 million and $100,000 a day; s 45S(1) $1 million; s 46 $200,000, 3 years and $10,000 a day; s 47 $40,000, 3 years and forfeiture of the apparatus installed or found; s 48(3) $40,000, 3 years and forfeiture of the decoder; s 49 $5,000; s 50(4) $5,000 and 12 months.
- Section 57(1) lets the Authority compound a prescribed offence for a sum not exceeding $1,000; the Composition of Offences Regulations (reg 2) prescribe one offence.
- Two powers to exempt run through the Act: the Minister's, by order, from "all or any of the provisions of this Act" (s 60(b)), and the Authority's from the licensing of apparatus (s 20(4)).
  The deposited exemption orders use only the first.
- The Second Schedule lists 20 services in a single column, the Third Schedule one row, and the First Schedule one item with an interpretation paragraph.
- Part 10 (ownership and control) turns on three percentage thresholds: more than 5% in an agreement to act together (s 35(3)), 12% for a controller (s 36(3)) and 49% for foreign sources (s 44(1)).

## Reading a result: FALSE and NOTHING

A function answers `JUST FALSE` or `FALSE` only where the text itself says no to the case in its own words: a definition that says "means", a condition introduced by "if", "only if" or "unless", or an express negation.
Where the text lists things without closing the list, says "includes", leaves a term undefined, is silent or points to someone's judgment outside the Act, the function answers `NOTHING`.
In plain words: `FALSE` is the Act's own "no"; `NOTHING` is "the Act does not say".
The seat renders them "No." and "The Act, as deposited, does not say for that date."
A date outside the window of a deposited text always answers `NOTHING`, never `FALSE`.

## Known limits

What the encoding cannot answer, stated so that nobody looks for it.
They are limits of the encoding, not findings about the Act.

1. **Past texts.** Outside the First and Third Schedules, every answer about a date before 25 September 2024 is "the Act does not say"; within them, the versions of "Point in time" answer from 31 July 2003, and nothing earlier was obtained (see "Editions encoded").
2. **The Authority and the Minister.** What they are satisfied of, what they think fit, what they approve and what they declare are plain inputs; the encoding cannot say whether they would.
3. **Borrowed meanings.** The Companies Act, the Variable Capital Companies Act, the Penal Code, the Children and Young Persons Act and the other Acts the text points to are not encoded here; the facts they decide are inputs.
4. **Instruments without Schedules and instruments after the served vintage.** The class licence conditions and the list of services exempted by S 523/2010 are not in the text served; whether the served instruments were amended or revoked after the vintage served is not shown by the served text.
5. **Codes of Practice.** The Codes of Practice under ss 6 and 45L are not obtained and have no function; what they require would enter as plain inputs.
6. **"Designed or constructed for".** See F-BA-01.
7. **Retrospective instruments.** S 549/2012 and S 548/2012 are each deemed in operation from 1 January 2011, a day before their publication on 31 October 2012; the encoding reads them as the text states them and does not say whether they are valid or what a court would do with conduct already past.
8. **Rg 1 and TVRO before the editions.** Nothing of Rg 1 before 29 February 2004 and nothing of the TVRO Regulations' regulation 3 before 1 August 2001 was obtained; those days answer `NOTHING`.
9. **Rg 1 amended is not printed whole.** The amended Regulations are held as the Revised Edition's functions plus S 333/2004's replacement text, not as a third assembled text.
10. **Counting periods.** Where the Act counts days or years, the encoding compares dates or whole numbers as the rule says and does not apply the Interpretation Act's rules for counting periods, which are in the Interpretation Act row.

## What the stable binary does not accept

The binary is `1.6.98 (main, 7689b0d, 2026-10-19)`, the `main` build `check.sh` fetches.
Sorted by how the failure shows up.

**Loud (an error or a warning, so you learn at once):**

- `AND` and `OR` on lines at the same indentation give a warning ("may indicate a precedence error"); put each `OR` group in a line that starts with `AND`, or on one line.
- A one-line `CONSIDER ... WHEN ... WHEN ...` with several `WHEN` arms does not parse; use `EQUALS` or lay the arms out on lines.
- Two `GIVEN` lines in a row do not parse; use one `GIVEN` with several names.
- A `@ref` at the end of a file, with nothing after it, gives a warning.
- A record field cannot be matched as `WHEN ctor WITH field`; write `WHEN ctor var` and use `var`.
- A pattern variable named like a record field (`months`, `dollars`) clashes with it; rename the variable.
- A type with a space in its name needs backticks wherever it is used (``k IS A `Kind of person` ``).
- `REFUSE`, `#ASSERT REFUSED`, `@lang` and `YMD` do not exist in this build; dates are `Date day month year`, and "not covered" is `NOTHING` in a `MAYBE`.
- `sed -i` on macOS needs an argument; the tools here edit with Python.

**Silent (a wrong answer, exit code 0):**

- `NOT a AND b` parses as `NOT (a AND b)`; every `NOT` in this encoding is parenthesised.
- `l4 check` prints `Check succeeded.` and says nothing about assertions; `check.sh` reads the counts.
- `l4 run` of `sgba-tv-cases-seat.l4` takes about two minutes; `check.sh` is run with `L4_MAIN_TIMEOUT=900`.

## Cross-folder links

Stable `l4` cannot `IMPORT` across folders, so every link below is a citation and a plain input.

| link | where it is used | how it is handled |
| --- | --- | --- |
| Interpretation Act 1965, s 9A and the time rules | `sgba-tv-s9a.l4` (quarantined) and F-BA-04 | cited from `../../../interpretation-act/encodings/legalese-sonnet-5.5/` (the `sgia-` modules); never re-encoded; the marker never changes the literal answer |
| Telecommunications Act 1999 | s 2(1) "internet access service" (BA1994.txt:434-457), s 24 (1493-1507), s 26(3) (1551-1553); N 1 para 2 (Internet Access Service Provider and VAN licences "under section 5 of the Telecommunications Act"); TVRO Regs reg 2 "telecommunications" | the licence or system status is a plain fact; the Telecommunications Act row (`sgta-`) answers what it means |
| Companies Act 1967, VCC Act 2018 | Part 10 | facts asked, with the section cited |
| Penal Code 1871, Children and Young Persons Act 1993, the terrorism Acts | s 45D(3) | facts asked, with the section cited |
| Criminal Procedure Code | ss 51 to 52 (arrest, search), s 58 (jurisdiction) | facts asked |

## The single SSO attempt

The single SSO attempt was made at 03:07:48 Singapore time on 2026-11-04, inside the 03:00 to 07:00 window.
The first request, for `https://sso.agc.gov.sg/robots.txt` with the brief's User-Agent, answered 403 (919 bytes).
The body is an HTML page headed "403 ERROR / The request could not be satisfied. / Request blocked.", served by CloudFront from a Singapore edge (`x-cache: Error from cloudfront`), so it is a block page and not a robots.txt.
The script and the brief both end the attempt at a 403, so no page of the Act was requested.
Nothing was deposited from SSO, no mirror was used, and no meta.json of a deposited text records an SSO text.
Two earlier 403s from SSO were recorded by other sessions on 2026-10-20 and 2026-11-03.
The attempt was for the consolidations of 2010-10-01 and 2011-01-01 as a cross-check; the Gazette texts (the Revised Editions 2003 and 2012, S 549/2012, S 559/2010 and the Television and Radio Licensing Regulations) supply the First Schedule, the Third Schedule and Rg 1 at those dates without it.
The consolidated text of the Act between the two Revised Editions remains unobtained.

## What `check.sh` prints

**Target: `main`.**
`check.sh` ran every module with both builds: the one it was written with and the `main` build it fetched, `1.6.98 (main, 7689b0d, 2026-10-19)`; both are the same build here, so the comparison shows that no module reads differently on `main` and says nothing about a newer `main`.
Command, from this folder: `L4=$HOME/.cache/l4-main/98/l4 L4_MAIN_BUILD=98 L4_MAIN_TIMEOUT=900 ./check.sh`.

The run below was made on 2026-11-04 10:46:41 to 2026-11-04 11:08:59 (Singapore time) after the last change to any module or test; later changes are to prose files only.
Columns: errors, assertions satisfied, failed, refused, the number expected to fail; then the same four counts on the `main` build, and `same` when they agree.

```
main build: 1.6.98 (main, 7689b0d, 2026-10-19)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
sgba-cases-seat.l4                             0        57       0        0         0 |      0        57       0        0  same
sgba-i-class-licence.l4                        0         0       0        0         0 |      0         0       0        0  same
sgba-i-composition.l4                          0         0       0        0         0 |      0         0       0        0  same
sgba-i-digital-panels.l4                       0         0       0        0         0 |      0         0       0        0  same
sgba-i-exempt-1996.l4                          0         0       0        0         0 |      0         0       0        0  same
sgba-i-exempt-2008.l4                          0         0       0        0         0 |      0         0       0        0  same
sgba-i-exempt-2022.l4                          0         0       0        0         0 |      0         0       0        0  same
sgba-i-exempt-educ.l4                          0         0       0        0         0 |      0         0       0        0  same
sgba-i-exempt-no2.l4                           0         0       0        0         0 |      0         0       0        0  same
sgba-i-exempt-no3.l4                           0         0       0        0         0 |      0         0       0        0  same
sgba-i-online-cop-rules.l4                     0         0       0        0         0 |      0         0       0        0  same
sgba-i-or1-2004.l4                             0         0       0        0         0 |      0         0       0        0  same
sgba-i-rg1.l4                                  0         0       0        0         0 |      0         0       0        0  same
sgba-i-s196-2004.l4                            0         0       0        0         0 |      0         0       0        0  same
sgba-i-s212-1999.l4                            0         0       0        0         0 |      0         0       0        0  same
sgba-i-s212-2022.l4                            0         0       0        0         0 |      0         0       0        0  same
sgba-i-s330-2013.l4                            0         0       0        0         0 |      0         0       0        0  same
sgba-i-s333-2004.l4                            0         0       0        0         0 |      0         0       0        0  same
sgba-i-s354-2001.l4                            0         0       0        0         0 |      0         0       0        0  same
sgba-i-s478-2020.l4                            0         0       0        0         0 |      0         0       0        0  same
sgba-i-s496-2001.l4                            0         0       0        0         0 |      0         0       0        0  same
sgba-i-s523-2010-schedule.l4                   0         0       0        0         0 |      0         0       0        0  same
sgba-i-s548-2012.l4                            0         0       0        0         0 |      0         0       0        0  same
sgba-i-s549-2012.l4                            0         0       0        0         0 |      0         0       0        0  same
sgba-i-s555-2003.l4                            0         0       0        0         0 |      0         0       0        0  same
sgba-i-s559-2010.l4                            0         0       0        0         0 |      0         0       0        0  same
sgba-i-s600-2014.l4                            0         0       0        0         0 |      0         0       0        0  same
sgba-i-s674-2016.l4                            0         0       0        0         0 |      0         0       0        0  same
sgba-i-s70-2012.l4                             0         0       0        0         0 |      0         0       0        0  same
sgba-i-service-website.l4                      0         0       0        0         0 |      0         0       0        0  same
sgba-i-tvro-regs.l4                            0         0       0        0         0 |      0         0       0        0  same
sgba-nouns.l4                                  0         0       0        0         0 |      0         0       0        0  same
sgba-p1-defs.l4                                0         0       0        0         0 |      0         0       0        0  same
sgba-p1-online.l4                              0         0       0        0         0 |      0         0       0        0  same
sgba-p1-other.l4                               0         0       0        0         0 |      0         0       0        0  same
sgba-p10-ownership.l4                          0         0       0        0         0 |      0         0       0        0  same
sgba-p10a-d1-d2.l4                             0         0       0        0         0 |      0         0       0        0  same
sgba-p10a-d3.l4                                0         0       0        0         0 |      0         0       0        0  same
sgba-p10a-d4.l4                                0         0       0        0         0 |      0         0       0        0  same
sgba-p11-offences.l4                           0         0       0        0         0 |      0         0       0        0  same
sgba-p12-misc.l4                               0         0       0        0         0 |      0         0       0        0  same
sgba-p2-authority.l4                           0         0       0        0         0 |      0         0       0        0  same
sgba-p4-services.l4                            0         0       0        0         0 |      0         0       0        0  same
sgba-p5-apparatus.l4                           0         0       0        0         0 |      0         0       0        0  same
sgba-p6-p7.l4                                  0         0       0        0         0 |      0         0       0        0  same
sgba-p8-p9-foreign.l4                          0         0       0        0         0 |      0         0       0        0  same
sgba-sched.l4                                  0         0       0        0         0 |      0         0       0        0  same
sgba-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
sgba-tests-amendments.l4                       0        95       0        0         0 |      0        95       0        0  same
sgba-tests-defs.l4                             0       112       0        0         0 |      0       112       0        0  same
sgba-tests-instruments-licensing.l4            0       183       0        0         0 |      0       183       0        0  same
sgba-tests-instruments-tv.l4                   0        73       0        0         0 |      0        73       0        0  same
sgba-tests-online.l4                           0        84       0        0         0 |      0        84       0        0  same
sgba-tests-p1-p9.l4                            0       136       0        0         0 |      0       136       0        0  same
sgba-tests-p10.l4                              0       253       0        0         0 |      0       253       0        0  same
sgba-tests-p10a.l4                             0       200       0        0         0 |      0       200       0        0  same
sgba-tests-p11.l4                              0       128       0        0         0 |      0       128       0        0  same
sgba-tests-p12.l4                              0        86       0        0         0 |      0        86       0        0  same
sgba-tests-p4.l4                               0       130       0        0         0 |      0       130       0        0  same
sgba-tests-p5.l4                               0        76       0        0         0 |      0        76       0        0  same
sgba-tests-rg1.l4                              0       353       0        0         0 |      0       353       0        0  same
sgba-tests-sched.l4                            0        50       0        0         0 |      0        50       0        0  same
sgba-tests-versions-acts.l4                    0       108       0        0         0 |      0       108       0        0  same
sgba-tests-versions-later.l4                   0       233       0        0         0 |      0       233       0        0  same
sgba-tests-versions.l4                         0       149       0        0         0 |      0       149       0        0  same
sgba-tv-cases-seat.l4                          0       178       0        0         0 |      0       178       0        0  same
sgba-tv-s9a.l4                                 0        14       0        0         0 |      0        14       0        0  same
sgba-tv-seat.l4                                0         0       0        0         0 |      0         0       0        0  same
sgba-versions-acts.l4                          0         0       0        0         0 |      0         0       0        0  same
sgba-versions-later.l4                         0         0       0        0         0 |      0         0       0        0  same
sgba-versions.l4                               0         0       0        0         0 |      0         0       0        0  same
sgba-vintage.l4                                0         0       0        0         0 |      0         0       0        0  same
TOTAL (72 modules)                             0      2698       0        0           |      0      2698       0        0
```

**72 modules, 0 errors, 2698 assertions satisfied, 0 failed, 0 refused; every one of the 72 modules reads the same on the `main` build (72 lines say `same`).**
Assertions written (`grep -c '^#ASSERT'` over the `sgba-*.l4` files): 2698; assertions satisfied: 2698.
No assertion is expected to fail, so `check.sh` has no `expected_failed` entry.

`srcrefs.py` over the Act's modules: `srcrefs check: 2896 src: lines, 443 runs, 443 locators, 0 problems`
The run includes `sgba-tv-seat.l4`, `sgba-tv-cases-seat.l4` and `sgba-tv-s9a.l4`; they quote no source text (0 `src:` lines of their own), so it has nothing to check in them.

`srcrefs.py` over the two modules that quote more than one deposit (`sgba-versions-acts.l4` quotes the 2003 Revised Edition, three amending Acts, three commencement notifications and S 212/2022, and `sgba-versions-later.l4` quotes the Revised Editions of 2003, 2012 and 2020, six more amending Acts (10/2005, 22/2016, 25/2021, 31/2022, 38/2022 and 4/2008), eight notifications (S 76/2005, S 461/2016, S 850/2022, S 29/2023, S 128/2008, S 129/2008, S 244/2024 and S 250/2022), S 26/2022 and S 738/2024; `sgba-i-s212-2022.l4` quotes S 212/2022 and the Interpretation Act), each against its deposits side by side (a `src:ID:N` locator names a file beside the first one):

- `sgba-versions-acts.l4`: `srcrefs check: 104 src: lines, 21 runs, 21 locators, 0 problems`
- `sgba-versions-later.l4`: `srcrefs check: 447 src: lines, 60 runs, 60 locators, 0 problems`
- `sgba-i-s212-2022.l4`: `srcrefs check: 13 src: lines, 4 runs, 4 locators, 0 problems`

`srcrefs.py` over each other instrument module, against its own deposit:

- `sgba-i-tvro-regs.l4`: `srcrefs check: 31 src: lines, 24 runs, 24 locators, 0 problems`
- `sgba-i-composition.l4`: `srcrefs check: 1 src: lines, 1 runs, 1 locators, 0 problems`
- `sgba-i-class-licence.l4`: `srcrefs check: 36 src: lines, 14 runs, 14 locators, 0 problems`
- `sgba-i-digital-panels.l4`: `srcrefs check: 42 src: lines, 14 runs, 14 locators, 0 problems`
- `sgba-i-exempt-1996.l4`: `srcrefs check: 10 src: lines, 1 runs, 1 locators, 0 problems`
- `sgba-i-exempt-no2.l4`: `srcrefs check: 6 src: lines, 1 runs, 1 locators, 0 problems`
- `sgba-i-exempt-no3.l4`: `srcrefs check: 1 src: lines, 1 runs, 1 locators, 0 problems`
- `sgba-i-exempt-2008.l4`: `srcrefs check: 2 src: lines, 2 runs, 2 locators, 0 problems`
- `sgba-i-exempt-2022.l4`: `srcrefs check: 4 src: lines, 1 runs, 1 locators, 0 problems`
- `sgba-i-exempt-educ.l4`: `srcrefs check: 22 src: lines, 4 runs, 4 locators, 0 problems`
- `sgba-i-service-website.l4`: `srcrefs check: 1 src: lines, 1 runs, 1 locators, 0 problems`
- `sgba-i-online-cop-rules.l4`: `srcrefs check: 40 src: lines, 13 runs, 13 locators, 0 problems`
- `sgba-i-s549-2012.l4`: `srcrefs check: 17 src: lines, 1 runs, 1 locators, 0 problems`
- `sgba-i-s559-2010.l4`: `srcrefs check: 16 src: lines, 1 runs, 1 locators, 0 problems`
- `sgba-i-rg1.l4`: `srcrefs check: 424 src: lines, 41 runs, 41 locators, 0 problems`
- `sgba-i-s333-2004.l4`: `srcrefs check: 170 src: lines, 16 runs, 16 locators, 0 problems`
- `sgba-i-s548-2012.l4`: `srcrefs check: 29 src: lines, 6 runs, 6 locators, 0 problems`
- `sgba-i-s212-1999.l4`: `srcrefs check: 11 src: lines, 1 runs, 1 locators, 0 problems`
- `sgba-i-s354-2001.l4`: `srcrefs check: 51 src: lines, 7 runs, 7 locators, 0 problems`
- `sgba-i-s600-2014.l4`: `srcrefs check: 9 src: lines, 3 runs, 3 locators, 0 problems`
- `sgba-i-or1-2004.l4`: `srcrefs check: 7 src: lines, 2 runs, 2 locators, 0 problems`
- `sgba-i-s523-2010-schedule.l4`: `srcrefs check: 10 src: lines, 1 runs, 1 locators, 0 problems`
- `sgba-i-s478-2020.l4`: `srcrefs check: 11 src: lines, 2 runs, 2 locators, 0 problems`
- `sgba-i-s196-2004.l4`: `srcrefs check: 10 src: lines, 2 runs, 2 locators, 0 problems`
- `sgba-i-s555-2003.l4`: `srcrefs check: 40 src: lines, 4 runs, 4 locators, 0 problems`
- `sgba-i-s496-2001.l4`: `srcrefs check: 29 src: lines, 3 runs, 3 locators, 0 problems`
- `sgba-i-s70-2012.l4`: `srcrefs check: 44 src: lines, 2 runs, 2 locators, 0 problems`
- `sgba-i-s330-2013.l4`: `srcrefs check: 50 src: lines, 5 runs, 5 locators, 0 problems`
- `sgba-i-s674-2016.l4`: `srcrefs check: 102 src: lines, 2 runs, 2 locators, 0 problems`

`gen-coverage.py audit`: `audit: 842 rows, 435 @refs in layer-1 modules, 179 @refs in instrument modules, 807 rule heads checked, 0 findings`

`python3 -I srcrefs-all.py` runs all the groups above in one command and prints `TOTAL: 4686 src lines, 704 runs, 704 locators, 0 problems; groups with a problem: 0` (exit 0).
It is the check that `sgba-tv-seat.l4`, `sgba-tv-cases-seat.l4` and `sgba-tv-s9a.l4` are included in, though they quote no source text and so it checks nothing in them.
The Act's group is 21 files, the three multi-deposit modules are checked one by one through a temporary directory of symlinks, and the other 29 instrument modules total `1226 src lines, 176 runs, 176 locators, 0 problems`.

## Independent review

After both encoders had finished, one separate Claude session (Opus 5.5) reviewed this encoding and the Telecommunications Act encoding.
It is not a domain expert, so the status at the top of this file stands.
The record is in `../../../telecommunications-act-1999/encodings/legalese-sonnet-5.5/review/`.
Its `README.md` says who reviewed, what the reviewer was shown, what leaked, and the numbers; `REVIEW.md`, `DISAGREEMENTS.md`, `MISSED-INSTRUMENTS.md`, `CITATION-CHECK.md` and `REQUESTS.md` are the reviewer's own files, unedited; `DISPOSITIONS.md` says what each encoder did about each item.
Those files contain the reviewer's own answers to the question; this file does not, in keeping with the quarantine above.

**What was independent.**
The method, set by the project owner, was Sonnet 5.5 encoders and then one independent Opus 5.5 reviewer who is not shown the encoders' conclusion.
The reviewer worked in a read-only copy of the repository without `TV-QUESTION-BA.md`, the `sgba-tv-*` modules, any `PROGRESS.md` and the forward-looking row `unstable-multitemporal-2026-11`.
It was told to re-derive its answer from the deposited texts before it opened any encoding file.

**What was not.**
When the reviewer's context was compacted, at 2026-11-03T19:53:49Z, the harness attached four files to it.
One was its own brief, which it had read once; the other three it had not opened, and one of those stated both encoders' preliminary answers.
The reviewer reported this itself and opened none of the three.
Only section 1 of `REVIEW.md`, last written 14 minutes before the compaction (sha256 `dd6325a0943dd1744ecb76027edca414c6e32b2884d876fd5ad8d5a9b8d36176`), is blind.
Everything after it is not, and should not be counted as a further independent confirmation of it.

**What it found about this encoding.**
Eleven items of difference between the reviewer and an encoding (D1 to D11; 6 marked B, identified in the blind section, and 5 marked P, noticed later), of which five concern this encoding.
- D1: whether "operate" in s 20(1)(c) is read against the premises phrase. The default reading (A) is kept; reading B is now encoded as separate functions and the seat asks a new question for it (fork F-BA-03). The encoder's own words: the balance is close and the text does not settle it.
- D3: TVRO licences and individuals. No change; the encoding already treats "is an institution" as a plain fact (fork F-BA-05).
- D5: the Rg 1 dispatchers answered reg 23 only. They are renamed to say what Rg 1 states in terms, and a comment says that FALSE from a dispatcher means the regulation says nothing of the kind (fork F-BA-12).
- D6: "today" lay beyond the version model. The cutoff is now one constant, `the day the sources were last checked` MEANS Date 4 11 2026, labelled "assumed, not ruled" with a one-line revert. The last reading day that gets an answer moved from 2 October to 4 November 2026; no answer for a reading day up to 2 October moved.
- D10: citation defects. M1 to M4 and G2 are fixed in `sgba-i-rg1.l4`, and `srcrefs-all.py` was added so that every quoting module is run.

For the quotations the reviewer found all 15,530 quote lines of the 97 quoting modules it checked, in both folders, to be verbatim substrings of the lines they name.
By hand it found 17 locator-level mismatches of 8 kinds and 2 coverage gaps in the two folders together; none is in a quotation's words, and a random sample of 64 had 1.
The reviewer's own run of this folder's `check.sh` on its copy gave 64 modules and 2,108 assertions satisfied; its copy lacked the `sgba-tv-*` modules, so that is lower than the figures under "What `check.sh` prints", which are for the whole folder.

**What the project owner ruled that touches this file.**
- Scope: the whole Acts and every instrument found, encoded; an instrument that could not be obtained is a row marked `source not obtained`.
- A text from an unofficial mirror could be used for the First Schedule before 2011 only if the Singapore Statutes Online route, the Gazette, the Bills and Hansard all failed; none was used (see "The single SSO attempt").
- A second blind review was permitted if a point first noticed after the leak could change a headline answer; none could, so it was not run.

## Before the encoding is worth relying on

- A domain expert should read the modules against the text, section by section.
- The thirteen forks are waiting for a ruling.
- The texts of the Act and of the instruments are converter and lawplain renderings, not the official text.
- The First and Third Schedules are known from 31 July 2003; nothing earlier was obtained, and the consolidations between the two Revised Editions were not seen (the single SSO attempt, below, is for those).

## Generators and checkers used and not shipped

Shipped in this folder: `qx.py` (expands `--@Q` macros into quotation lines and `@ref`s copied out of a deposited text, so a quotation cannot be misspelled), `srcrefs.py` (re-checks every quotation and locator against the text), `gen-coverage.py` (makes the coverage rows from the text, proves every non-blank line is in exactly one row, makes the table from `dispositions.tsv`, and audits the table against the modules), `check.sh` and `fetch-main-l4.sh`.
Used and not shipped (in the encoder's scratch space): a deposit script that line-breaks each instrument's text, `mkdisp2.py` (writes `dispositions.tsv` from the `@ref`s of the layer-1 modules), `tx.py` (expands a function-name prefix in a test file into the backticked name).
A quotation in the instrument modules is checked against the instrument's own deposit, with plain `src:N` locators (`srcrefs.py check --strict <deposit>.txt sgba-i-<name>.l4`).
Two reviewing steps found real defects and are worth repeating: the audit that every rule with an `@ref` is named in a test, and a read of each instrument's `@ref` against its deposit; the second found that the S 121/2008 module cited the wrong lines for paragraphs 2(1) and 2(2) (the lines of the date and of the signature), which `srcrefs.py` accepts because the quotation exists.

## Coverage

The table below is generated, not typed: `gen-coverage.py` makes the rows from the text of `BA1994.txt` and proves that every non-blank line of the text falls in exactly one row, and `dispositions.tsv` (written from the `@ref`s of the layer-1 modules) gives each row its disposition.
`python3 -I gen-coverage.py audit ../../registers/source-bundle/BA1994.txt dispositions.tsv .` found 0 problems: no row is `deferred`, every `encoded` row has an `@ref` over its text, every `fork` row names an F-BA entry, and every rule head (807 of them) in the Act's modules and in the instrument modules is named in a tests or cases file.
Dispositions are the brief's: `encoded` (a rule with a test and an `@ref`), `inert (1)` not operative (title, contents list, long title, headings, a purpose clause), `inert (2)` machinery (the Act's own commencement), `inert (3)` repealed text, `fork`, `repealed or blank in this text`, `source not obtained` (instruments only).
Section rows are named as the text numbers them; a row such as `s8(6)` is the subsection that starts on that line, and the section row of a section whose first line carries `(1)` is named `sN(1)`.
`dispositions.tsv` has no `inert (3)` row: the three repealed sections (23, 38 and 67) are `repealed or blank in this text`, and the repealed items inside encoded rows are noted in the row.

### The Act, row by row

| row | lines | text (first words) | disposition | module | note |
| --- | --- | --- | --- | --- | --- |
| front:cover | 1-19 | title page and 2020 Revised Edition notice | inert (1) not operative |  | title page, contents list or long title: not operative |
| front:arrangement | 20-229 | Arrangement of Sections (contents list) | inert (1) not operative |  | title page, contents list or long title: not operative |
| front:long-title | 230-236 | long title | inert (1) not operative |  | title page, contents list or long title: not operative |
| front:commencement | 237-238 | commencement note [1 October 1994] | inert (2) machinery |  | the Act's own commencement |
| part:1 | 239-240 | Part heading | inert (1) not operative |  | heading, not operative |
| s1:heading | 241-241 | PART 1 PRELIMINARY Short title | inert (1) not operative |  | heading, not operative |
| s1 | 242-246 | 1. This Act is the Broadcasting Act 1994. | encoded | sgba-p1-other |  |
| s2:heading | 247-248 | Interpretation | inert (1) not operative |  | heading, not operative |
| s2(1) | 249-250 | 2.—(1) In this Act, unless the context otherwise requires — | encoded | sgba-p1-other |  |
| s2(1)-def:a point | 251-256 | a point | encoded | sgba-p1-defs |  |
| s2(1)-def:access | 257-271 | access | encoded | sgba-p1-defs |  |
| s2(1)-def:Authority | 272-276 | Authority | encoded | sgba-p1-defs |  |
| s2(1)-def:broadcasting apparatus | 277-280 | broadcasting apparatus | fork | sgba-p1-defs | F-BA-01: whether 'specified in the First Schedule' qualifies all of 'capable of or designed or constructed for the reception' (reading A, encoded) or only 'designed or constructed for' (reading B, not encoded) |
| s2(1)-def:broadcasting apparatus licence | 281-285 | broadcasting apparatus licence | encoded | sgba-p1-defs |  |
| s2(1)-def:broadcasting licence | 286-289 | broadcasting licence | encoded | sgba-p1-defs |  |
| s2(1)-def:broadcasting service | 290-309 | broadcasting service | encoded | sgba-p1-defs |  |
| s2(1)-def:Chief Executive | 310-314 | Chief Executive | encoded | sgba-p1-defs |  |
| s2(1)-def:class licence | 315-318 | class licence | encoded | sgba-p1-defs |  |
| s2(1)-def:Code of Practice | 319-321 | Code of Practice | encoded | sgba-p1-defs |  |
| s2(1)-def:communicate | 322-332 | communicate | encoded | sgba-p1-defs |  |
| s2(1)-def:content | 333-353 | content | encoded | sgba-p1-defs |  |
| s2(1)-def:debenture | 354-355 | debenture | encoded | sgba-p1-defs |  |
| s2(1)-def:dwelling house | 356-358 | dwelling house | encoded | sgba-p1-defs |  |
| s2(1)-def:electronic service | 359-362 | electronic service | encoded | sgba-p1-defs |  |
| s2(1)-def:encrypted | 363-365 | encrypted | encoded | sgba-p1-defs |  |
| s2(1)-def:end-user | 366-381 | end-user | encoded | sgba-p1-defs |  |
| s2(1)-def:engage in conduct | 382-401 | engage in conduct | encoded | sgba-p1-defs |  |
| s2(1)-def:entity | 402-418 | entity | encoded | sgba-p1-defs |  |
| s2(1)-def:excluded electronic service | 419-423 | excluded electronic service | encoded | sgba-p1-defs |  |
| s2(1)-def:free-to-air broadcasting service | 424-428 | free-to-air broadcasting service | encoded | sgba-p1-defs |  |
| s2(1)-def:free-to-air licence | 429-433 | free-to-air licence | encoded | sgba-p1-defs |  |
| s2(1)-def:internet access service | 434-460 | internet access service | encoded | sgba-p1-defs |  |
| s2(1)-def:licence | 461-463 | licence | encoded | sgba-p1-defs |  |
| s2(1)-def:licensable broadcasting service | 464-469 | licensable broadcasting service | encoded | sgba-p1-defs |  |
| s2(1)-def:member | 470-471 | member | encoded | sgba-p1-defs |  |
| s2(1)-def:online Code of Practice | 472-477 | online Code of Practice | encoded | sgba-p1-defs |  |
| s2(1)-def:online communication service | 478-482 | online communication service | encoded | sgba-p1-defs |  |
| s2(1)-def:Part 10A regulations | 483-487 | Part 10A regulations | encoded | sgba-p1-defs |  |
| s2(1)-def:programme | 488-514 | programme | encoded | sgba-p1-defs |  |
| s2(1)-def:provider | 515-519 | provider | encoded | sgba-p1-defs |  |
| s2(1)-def:regulated online communication service | 520-525 | regulated online communication service | encoded | sgba-p1-defs |  |
| s2(1)-def:regulations | 526-527 | regulations | encoded | sgba-p1-defs |  |
| s2(1)-def:securities | 528-532 | securities | encoded | sgba-p1-defs |  |
| s2(1)-def:shares | 533-535 | shares | encoded | sgba-p1-defs |  |
| s2(1)-def:Singapore end-user | 536-550 | Singapore end-user | encoded | sgba-p1-defs |  |
| s2(1)-def:social media service | 551-554 | social media service | encoded | sgba-p1-defs |  |
| s2(1)-def:subscription broadcasting service | 555-562 | subscription broadcasting service | encoded | sgba-p1-defs |  |
| s2(1)-def:subscription fee | 563-566 | subscription fee | encoded | sgba-p1-defs |  |
| s2(2) | 567-569 | (2) In this Act, unless the context otherwise requires, “par | encoded | sgba-p1-other |  |
| s2(2)(a) | 570-571 | (a) residents in a particular place; | encoded | sgba-p1-other |  |
| s2(2)(b) | 572-573 | (b) employees of any firm, company or organisation; | encoded | sgba-p1-other |  |
| s2(2)(c) | 574-576 | (c) occupiers of a particular building or part of the buildi | encoded | sgba-p1-other |  |
| s2(2)(d) | 577-578 | (d) members of any profession, club or society. | encoded | sgba-p1-other |  |
| s2(3) | 579-582 | (3) For the purposes of this Act, a company is regarded as w | encoded | sgba-p1-other |  |
| s2(4) | 583-588 | (4) For the purposes of this Act, whether any communication  | encoded | sgba-p1-other |  |
| s2(4)(a) | 589-591 | (a) the number of individuals in Singapore who are able to | encoded | sgba-p1-other |  |
| s2(4)(b) | 592-595 | (b) any restrictions on who may access the content by means | encoded | sgba-p1-other |  |
| s2(4)(c) | 596-598 | (c) the relationship between the persons that the content is | encoded | sgba-p1-other |  |
| s2(4)(d) | 599-602 | (d) any other relevant factor. | encoded | sgba-p1-other |  |
| s2(5) | 603-607 | (5) However, for the purposes of subsection (4), the followi | encoded | sgba-p1-other |  |
| s2(5)(a) | 608-614 | (a) a requirement to log in to or register with the broadcas | encoded | sgba-p1-other |  |
| s2(5)(b) | 615-620 | (b) a requirement to make a payment or take out a subscripti | encoded | sgba-p1-other |  |
| s2(5)(c) | 621-629 | (c) inability to access a broadcasting service or an online | encoded | sgba-p1-other |  |
| s2(6) | 630-635 | (6) In determining for the purposes of this Act whether an e | encoded | sgba-p1-other |  |
| s2A:heading | 636-638 | Meanings of “online communication service” and associated te | inert (1) not operative |  | heading, not operative |
| s2A(1) | 639-642 | 2A.—(1) In this Act, an online communication service means a | encoded | sgba-p1-online |  |
| s2A(2) | 643-645 | (2) For the purposes of subsection (1), an electronic servic | encoded | sgba-p1-online |  |
| s2A(2)(a) | 646-656 | (a) that — | encoded | sgba-p1-online |  |
| s2A(2)(b) | 657-668 | (b) that is a service — | encoded | sgba-p1-online |  |
| s2A(2)(c) | 669-670 | (c) that is not an excluded electronic service. | encoded | sgba-p1-online |  |
| s2A(3) | 671-673 | (3) For the purposes of subsection (2)(c), an excluded elect | encoded | sgba-p1-online |  |
| s2A(3)(a) | 674-675 | (a) an SMS service; | encoded | sgba-p1-online |  |
| s2A(3)(b) | 676-677 | (b) an MMS service; | encoded | sgba-p1-online |  |
| s2A(3)(c) | 678-679 | (c) an internet access service; | encoded | sgba-p1-online |  |
| s2A(3)(d) | 680-683 | (d) an electronic service where the only user-generated cont | encoded | sgba-p1-online |  |
| s2A(3)(e) | 684-687 | (e) an electronic service where the only user-generated cont | encoded | sgba-p1-online |  |
| s2A(3)(f) | 688-693 | (f) an electronic service where the user-generated content | encoded | sgba-p1-online |  |
| s2A(3)(g) | 694-699 | (g) an electronic service that is prescribed by the Minister | encoded | sgba-p1-online |  |
| s2A(4) | 700-703 | (4) References in this Act to an online communication servic | encoded | sgba-p1-online |  |
| s2A(5) | 704-707 | (5) In this section — | encoded | sgba-p1-online |  |
| s2A(5)(a) | 708-713 | (a) any feature that enables interactions of any | encoded | sgba-p1-online |  |
| s2A(5)(b) | 714-735 | (b) any feature that enables end-users to search online | encoded | sgba-p1-online |  |
| s2A(5)(c) | 736-769 | (c) that is not accompanied by user-generated content of | encoded | sgba-p1-online |  |
| s2B:heading | 770-771 | Amendment of Fourth Schedule | inert (1) not operative |  | heading, not operative |
| s2B(1) | 772-774 | 2B.—(1) The Minister may, by order in the Gazette, revoke or | encoded | sgba-p1-online |  |
| s2B(2) | 775-779 | (2) Every order made under subsection (1) must be presented  | encoded | sgba-p1-online |  |
| s2C:heading | 780-782 | Transitional arrangements for former licensable broadcasting | inert (1) not operative |  | heading, not operative |
| s2C(1) | 783-786 | 2C.—(1) With effect from the date that a licensable broadcas | encoded | sgba-p1-online |  |
| s2C(1)(a) | 787-793 | (a) this Act ceases to apply to — | encoded | sgba-p1-online |  |
| s2C(1)(b) | 794-799 | (b) this Act then continues to apply to that service as an o | encoded | sgba-p1-online |  |
| s2C(1)(c) | 800-802 | (c) the enforcement by any person of any right or claim agai | encoded | sgba-p1-online |  |
| s2C(1)(d) | 803-805 | (d) the enforcement by the former broadcasting licensee of a | encoded | sgba-p1-online |  |
| s2C(1)(e) | 806-812 | (e) any proceeding under section 12(1) with respect to the | encoded | sgba-p1-online |  |
| s2C(1)(f) | 813-816 | (f) any appeal under section 12(2) or 59(1) with respect to  | encoded | sgba-p1-online |  |
| s2C(2) | 817-822 | (2) Any proceeding and appeal mentioned in subsection (1)(e) | encoded | sgba-p1-online |  |
| s2D:heading | 823-824 | Meaning of “provider” of online communication service | inert (1) not operative |  | heading, not operative |
| s2D(1) | 825-827 | 2D.—(1) Subject to this section, in this Act, the provider o | encoded | sgba-p1-online |  |
| s2D(1)(a) | 828-830 | (a) who can use the online communication service that is | encoded | sgba-p1-online |  |
| s2D(1)(b) | 831-834 | (b) the operations of the characteristics of the electronic | encoded | sgba-p1-online |  |
| s2D(1)(c) | 835-837 | (c) which content is communicated or provided on the online | encoded | sgba-p1-online |  |
| s2D(2) | 838-842 | (2) Where an online communication service is generated by a | encoded | sgba-p1-online |  |
| s2D(3) | 843-847 | (3) However, if no entity controls the machine mentioned in | encoded | sgba-p1-online |  |
| s2D(4) | 848-849 | (4) If no entity has control over — | encoded | sgba-p1-online |  |
| s2D(4)(a) | 850-852 | (a) who can use the online communication service that is | encoded | sgba-p1-online |  |
| s2D(4)(b) | 853-856 | (b) the operations of the characteristics of the electronic | encoded | sgba-p1-online |  |
| s2D(4)(c) | 857-866 | (c) which content is communicated or provided on the online | encoded | sgba-p1-online |  |
| s2D(5) | 867-872 | (5) Despite subsection (1), a person that provides an intern | encoded | sgba-p1-online |  |
| s2D(6) | 873-878 | (6) Part 10A regulations may be made to specify who is to be | encoded | sgba-p1-online |  |
| part:2 | 879-882 | Part heading | inert (1) not operative |  | heading, not operative |
| s3:heading | 883-884 | Directions by Minister | inert (1) not operative |  | heading, not operative |
| s3(1) | 885-889 | 3.—(1) The Minister may, after consultation with a person to | encoded | sgba-p2-authority |  |
| s3(2) | 890-892 | (2) Without limiting subsection (1), if it appears to the Mi | encoded | sgba-p2-authority |  |
| s3(2)(a) | 893-896 | (a) when any public emergency occurs, in the public interest | encoded | sgba-p2-authority |  |
| s3(2)(b) | 897-920 | (b) in order — | encoded | sgba-p2-authority |  |
| s3(3) | 921-923 | (3) Any directions given under subsection (1) or (2) may inc | encoded | sgba-p2-authority |  |
| s3(3)(a) | 924-925 | (a) the prohibition or regulation of any broadcasting servic | encoded | sgba-p2-authority |  |
| s3(3)(b) | 926-929 | (b) the taking of, the control of or the use for official pu | encoded | sgba-p2-authority |  |
| s3(3)(c) | 930-933 | (c) the stopping, delaying and censoring of messages and the | encoded | sgba-p2-authority |  |
| s3(4) | 934-937 | (4) A person to whom this section applies must give immediat | encoded | sgba-p2-authority |  |
| s3(5) | 938-942 | (5) A person to whom this section applies must not disclose  | encoded | sgba-p2-authority |  |
| s3(6) | 943-944 | (6) The Minister may — | encoded | sgba-p2-authority |  |
| s3(6)(a) | 945-948 | (a) pay compensation for any damage caused to a licensee by | encoded | sgba-p2-authority |  |
| s3(6)(b) | 949-956 | (b) make grants to licensees for defraying or contributing | encoded | sgba-p2-authority |  |
| s3(7) | 957-960 | (7) Any sums required by the Minister for paying compensatio | encoded | sgba-p2-authority |  |
| s3(8) | 961-963 | (8) This section applies to the Authority and to any person  | encoded | sgba-p2-authority |  |
| s3(9) | 964-965 | (9) If any doubt arises as to — | encoded | sgba-p2-authority |  |
| s3(9)(a) | 966-967 | (a) the existence of a public emergency; or | encoded | sgba-p2-authority |  |
| s3(9)(b) | 968-975 | (b) whether any act done under this section was in the publi | encoded | sgba-p2-authority |  |
| s4:heading | 976-977 | Exclusion of liability of Authority for act or default of li | inert (1) not operative |  | heading, not operative |
| s4 | 978-982 | 4. The Authority shall not be liable in respect of any injur | encoded | sgba-p2-authority |  |
| part:3 | 983-984 | Part heading | inert (1) not operative |  | heading, not operative |
| s5:heading | 985-985 | PART 3 LICENSING SCHEME Power of Authority to grant licences | inert (1) not operative |  | heading, not operative |
| s5(1) | 986-986 | 5.—(1) The Authority may grant the following licences: | encoded | sgba-p4-services |  |
| s5(1)(a) | 987-987 | (a) broadcasting licences; | encoded | sgba-p4-services |  |
| s5(1)(b) | 988-988 | (b) broadcasting apparatus licences. | encoded | sgba-p4-services |  |
| s5(2) | 989-995 | (2) The Authority may grant licences under subsection (1) in | encoded | sgba-p4-services |  |
| s6:heading | 996-997 | Codes of Practice | inert (1) not operative |  | heading, not operative |
| s6(1) | 998-999 | 6.—(1) The Authority may issue and from time to time review  | encoded | sgba-p4-services |  |
| s6(1)(a) | 1000-1002 | (a) Codes of Practice relating to standards of programmes an | encoded | sgba-p4-services |  |
| s6(1)(b) | 1003-1005 | (b) Codes of Practice relating to broadcast standards requir | encoded | sgba-p4-services |  |
| s6(2) | 1006-1008 | (2) Any provision in any Code of Practice that is inconsiste | encoded | sgba-p4-services |  |
| s6(2)(a) | 1009-1010 | (a) to have effect subject to the regulations; or | encoded | sgba-p4-services |  |
| s6(2)(b) | 1011-1013 | (b) where appropriate, having regard to the regulations, to | encoded | sgba-p4-services |  |
| s6(3) | 1014-1017 | (3) The Authority may in any licence exempt any licensee fro | encoded | sgba-p4-services |  |
| s7:heading | 1018-1019 | Restriction on transfer of licences | inert (1) not operative |  | heading, not operative |
| s7(1) | 1020-1023 | 7.—(1) A licence must not be transferred to any other person | encoded | sgba-p4-services |  |
| s7(2) | 1024-1026 | (2) Any purported transfer of any licence is for all purpose | fork | sgba-p4-services | F-BA-02: any purported transfer void (literal, encoded) or only a transfer without the consent s 7(1) requires (encoded as the second function) |
| part:4 | 1027-1030 | Part heading | inert (1) not operative |  | heading, not operative |
| s8:heading | 1031-1032 | Licensing of broadcasting services | inert (1) not operative |  | heading, not operative |
| s8(1) | 1033-1036 | 8.—(1) A person must not provide any licensable broadcasting | encoded | sgba-p4-services |  |
| s8(2) | 1037-1043 | (2) Every broadcasting licence (other than a class licence)  | encoded | sgba-p4-services |  |
| s8(3) | 1044-1048 | (3) The Authority may require any licensee to pay a fee on t | encoded | sgba-p4-services |  |
| s8(4) | 1049-1051 | (4) Without limiting subsection (2), conditions attached to  | encoded | sgba-p4-services |  |
| s8(4)(a) | 1052-1056 | (a) a condition requiring the licensee to broadcast any | encoded | sgba-p4-services |  |
| s8(4)(b) | 1057-1061 | (b) a condition prohibiting or restricting, in a manner spec | encoded | sgba-p4-services |  |
| s8(4)(c) | 1062-1065 | (c) the right of the Authority in the public interest to mak | encoded | sgba-p4-services |  |
| s8(4)(d) | 1066-1069 | (d) a condition requiring the licensee to provide a performa | encoded | sgba-p4-services |  |
| s8(4)(e) | 1070-1073 | (e) broadcast requirements, including conditions relating to | encoded | sgba-p4-services |  |
| s8(4)(f) | 1074-1077 | (f) a condition requiring the payment by the licensee of | encoded | sgba-p4-services |  |
| s8(4)(g) | 1078-1081 | (g) a condition requiring the broadcasting of programmes in | encoded | sgba-p4-services |  |
| s8(4)(h) | 1082-1089 | (h) conditions imposing controls and restrictions, directly  | encoded | sgba-p4-services |  |
| s8(5) | 1090-1095 | (5) The Authority may require any licensee to pay a charge o | fork | sgba-p4-services | F-BA-09, answered 2026-11-04 by the texts: S 244/2024 appoints 1 April 2024 for Act 4 of 2008 (the annotations on s 8(5) and (6) and history item 29 say the same); S 128/2008 was cancelled by S 129/2008; the two-day version and the s 8(5) rule on both texts are in sgba-versions-later |
| s8(6) | 1096-1105 | (6) Every amount collected before the date of commencement o | fork | sgba-p4-services | F-BA-09, answered 2026-11-04 by the texts: the commencement is 1 April 2024 (S 244/2024); on the 2024 text this module still asks whether the amount was collected before it as a plain fact, and sgba-versions-later computes it from the day collected |
| s9:heading | 1106-1107 | Class licences | inert (1) not operative |  | heading, not operative |
| s9(1) | 1108-1112 | 9.—(1) The Authority may, by notification in the Gazette, | encoded | sgba-p4-services |  |
| s9(2) | 1113-1115 | (2) The Authority may include in a class licence any conditi | encoded | sgba-p4-services |  |
| s9(3) | 1116-1117 | (3) Different conditions may be specified for — | encoded | sgba-p4-services |  |
| s9(3)(a) | 1118-1120 | (a) different categories of licensable broadcasting services | encoded | sgba-p4-services |  |
| s9(3)(b) | 1121-1122 | (b) different types of such services. | encoded | sgba-p4-services |  |
| s9(4) | 1123-1128 | (4) Without limiting the conditions that may be imposed, the | encoded | sgba-p4-services |  |
| s10:heading | 1129-1130 | Modification of broadcasting licence conditions | inert (1) not operative |  | heading, not operative |
| s10(1) | 1131-1137 | 10.—(1) The Authority may modify the conditions of a | encoded | sgba-p4-services |  |
| s10(2) | 1138-1141 | (2) Before making any modification to the conditions of a | encoded | sgba-p4-services |  |
| s10(2)(a) | 1142-1148 | (a) stating that it proposes to make the modification in the | encoded | sgba-p4-services |  |
| s10(2)(b) | 1149-1153 | (b) specifying the time (being at least 28 days from the dat | encoded | sgba-p4-services |  |
| s10(3) | 1154-1157 | (3) Upon receiving any written representation mentioned in | encoded | sgba-p4-services |  |
| s10(3)(a) | 1158-1159 | (a) reject the representation; or | encoded | sgba-p4-services |  |
| s10(3)(b) | 1160-1167 | (b) amend the proposed modification or compensation payable | encoded | sgba-p4-services |  |
| s10(4) | 1168-1171 | (4) Any broadcasting licensee aggrieved by a decision of the | encoded | sgba-p4-services |  |
| s10(5) | 1172-1174 | (5) The Authority must not enforce a direction given under | encoded | sgba-p4-services |  |
| s10(5)(a) | 1175-1176 | (a) during the period mentioned in subsection (4); and | encoded | sgba-p4-services |  |
| s10(5)(b) | 1177-1179 | (b) while the broadcasting licensee’s appeal is under | encoded | sgba-p4-services |  |
| s10(6) | 1180-1189 | (6) If no written representation is received by the Authorit | encoded | sgba-p4-services |  |
| s11:heading | 1190-1190 | Modification of class licence conditions | inert (1) not operative |  | heading, not operative |
| s11 | 1191-1191 | 11. The Authority may, by notification in the Gazette — | encoded | sgba-p4-services |  |
| s11(a) | 1192-1192 | (a) modify the conditions specified in any class licence; or | encoded | sgba-p4-services |  |
| s11(b) | 1193-1194 | (b) specify additional conditions of any class licence. | encoded | sgba-p4-services |  |
| s12:heading | 1195-1196 | Suspension or cancellation of broadcasting licence, etc. | inert (1) not operative |  | heading, not operative |
| s12(1) | 1197-1198 | 12.—(1) If the Authority is satisfied that — | encoded | sgba-p4-services |  |
| s12(1)(a) | 1199-1204 | (a) a broadcasting licensee is contravening, or has | encoded | sgba-p4-services |  |
| s12(1)(b) | 1205-1208 | (b) a broadcasting licensee has gone into compulsory or | encoded | sgba-p4-services |  |
| s12(1)(c) | 1209-1211 | (c) a broadcasting licensee has made any assignment to, or | encoded | sgba-p4-services |  |
| s12(1)(d) | 1212-1216 | (d) the public interest or the security of Singapore so requ | encoded | sgba-p4-services |  |
| s12(1)(e) | 1217-1222 | (e) cancel the licence or suspend the licence for any period | encoded | sgba-p4-services |  |
| s12(1)(f) | 1223-1225 | (f) require the payment of a fine of such amount as the | encoded | sgba-p4-services |  |
| s12(2) | 1226-1233 | (2) Any person who is aggrieved by any decision of the Autho | encoded | sgba-p4-services |  |
| s12(3) | 1234-1235 | (3) In this section, “Code of Practice” includes — | encoded | sgba-p4-services |  |
| s12(3)(a) | 1236-1239 | (a) a code of practice issued by the Authority under section | encoded | sgba-p4-services |  |
| s12(3)(b) | 1240-1247 | (b) a code of practice issued under section 17 of the Media | encoded | sgba-p4-services |  |
| s13:heading | 1248-1249 | Compliance with Codes of Practice, etc. | inert (1) not operative |  | heading, not operative |
| s13(1) | 1250-1253 | 13.—(1) Every broadcasting licensee must comply with the Cod | encoded | sgba-p4-services |  |
| s13(2) | 1254-1256 | (2) A broadcasting licensee must not allow to be transmitted | encoded | sgba-p4-services |  |
| s13(2)(a) | 1257-1259 | (a) any broadcast standards specified in any regulations or | encoded | sgba-p4-services |  |
| s13(2)(b) | 1260-1262 | (b) any condition which may be incorporated in its | encoded | sgba-p4-services |  |
| s14:heading | 1263-1264 | Free-to-air broadcasting services | inert (1) not operative |  | heading, not operative |
| s14(1) | 1265-1267 | 14.—(1) A free-to-air licensee must provide broadcasting ser | encoded | sgba-p4-services |  |
| s14(2) | 1268-1271 | (2) Each free-to-air broadcasting service must be broadcast  | encoded | sgba-p4-services |  |
| s15:heading | 1272-1273 | Submission of broadcasting material to Authority | inert (1) not operative |  | heading, not operative |
| s15(1) | 1274-1277 | 15.—(1) A broadcasting licensee must supply to the Authority | encoded | sgba-p4-services |  |
| s15(2) | 1278-1283 | (2) A broadcasting licensee who is required to supply materi | encoded | sgba-p4-services |  |
| s15(2)(a) | 1284-1286 | (a) supply the material in such form as the Authority may | encoded | sgba-p4-services |  |
| s15(2)(b) | 1287-1289 | (b) make available on demand without charge such equipment | encoded | sgba-p4-services |  |
| s15(3) | 1290-1296 | (3) The Authority may, if it is satisfied that any programme | encoded | sgba-p4-services |  |
| s16:heading | 1297-1298 | Directions of Authority | inert (1) not operative |  | heading, not operative |
| s16(1) | 1299-1305 | 16.—(1) The Authority may issue directions in writing to a | encoded | sgba-p4-services |  |
| s16(2) | 1306-1309 | (2) Directions issued under subsection (1) may include a dir | encoded | sgba-p4-services |  |
| s16(3) | 1310-1315 | (3) Any broadcasting licensee and any other person responsib | encoded | sgba-p4-services |  |
| s17:heading | 1316-1317 | Public service broadcasting services | inert (1) not operative |  | heading, not operative |
| s17 | 1318-1323 | 17. A broadcasting licensee must include, within the broadca | encoded | sgba-p4-services |  |
| s17(a) | 1324-1328 | (a) programmes for schools or other educational programmes; | encoded | sgba-p4-services |  |
| s17(b) | 1329-1331 | (b) news and information programmes produced in Singapore | encoded | sgba-p4-services |  |
| s17(c) | 1332-1333 | (c) arts and cultural programmes; and | encoded | sgba-p4-services |  |
| s17(d) | 1334-1335 | (d) drama and sports programmes produced in Singapore. | encoded | sgba-p4-services |  |
| s18:heading | 1336-1337 | General requirements in respect of public service programmes | inert (1) not operative |  | heading, not operative |
| s18(1) | 1338-1343 | 18.—(1) Programmes required under section 17 or pursuant to  | encoded | sgba-p4-services |  |
| s18(2) | 1344-1350 | (2) A broadcasting licensee must, on the request of the Auth | encoded | sgba-p4-services |  |
| s19:heading | 1351-1352 | “Must carry” provision | inert (1) not operative |  | heading, not operative |
| s19(1) | 1353-1357 | 19.—(1) Despite anything in this Act but subject to this sec | encoded | sgba-p4-services |  |
| s19(1)(a) | 1358-1360 | (a) provided by any other person for such transmission and | encoded | sgba-p4-services |  |
| s19(1)(b) | 1361-1362 | (b) specified in its licence or is of a description so speci | encoded | sgba-p4-services |  |
| s19(2) | 1363-1366 | (2) Where the Authority gives a direction under this section | encoded | sgba-p4-services |  |
| s19(3) | 1367-1369 | (3) Where it is proposed to give a direction under this sect | encoded | sgba-p4-services |  |
| s19(3)(a) | 1370-1378 | (a) stating that the Authority proposes to give directions i | encoded | sgba-p4-services |  |
| s19(3)(b) | 1379-1383 | (b) specifying the time (being at least 28 days from the dat | encoded | sgba-p4-services |  |
| s19(4) | 1384-1387 | (4) Upon receiving any written representation mentioned in | encoded | sgba-p4-services |  |
| s19(4)(a) | 1388-1389 | (a) reject the representation; or | encoded | sgba-p4-services |  |
| s19(4)(b) | 1390-1397 | (b) amend the proposed direction or compensation payable in | encoded | sgba-p4-services |  |
| s19(5) | 1398-1401 | (5) Any broadcasting licensee aggrieved by a decision of the | encoded | sgba-p4-services |  |
| s19(6) | 1402-1404 | (6) The Authority must not enforce a direction given under | encoded | sgba-p4-services |  |
| s19(6)(a) | 1405-1406 | (a) during the period mentioned in subsection (5); and | encoded | sgba-p4-services |  |
| s19(6)(b) | 1407-1409 | (b) while the broadcasting licensee’s appeal is under | encoded | sgba-p4-services |  |
| s19(7) | 1410-1418 | (7) If no written representation is received by the Authorit | encoded | sgba-p4-services |  |
| part:5 | 1419-1422 | Part heading | inert (1) not operative |  | heading, not operative |
| s20:heading | 1423-1424 | Licensing of broadcasting apparatus | inert (1) not operative |  | heading, not operative |
| s20(1) | 1425-1426 | 20.—(1) Subject to this section, a person must not — | encoded | sgba-p5-apparatus |  |
| s20(1)(a) | 1427-1429 | (a) install any broadcasting apparatus in any place, or on b | encoded | sgba-p5-apparatus |  |
| s20(1)(b) | 1430-1433 | (b) import, offer for sale, sell or have in the person’s | encoded | sgba-p5-apparatus |  |
| s20(1)(c) | 1434-1440 | (c) operate or have on any premises in Singapore owned or | fork | sgba-p5-apparatus | F-BA-03: whether the premises phrase qualifies both 'operate' and 'have' (encoded) or only 'have' |
| s20(2) | 1441-1444 | (2) Every licence granted under subsection (1) must be in su | encoded | sgba-p5-apparatus |  |
| s20(3) | 1445-1450 | (3) Subsection (1) is not to be construed as requiring any p | encoded | sgba-p5-apparatus |  |
| s20(4) | 1451-1453 | (4) The Authority may exempt any person or broadcasting | encoded | sgba-p5-apparatus |  |
| s21:heading | 1454-1456 | Application of certain provisions of Act to broadcasting app | inert (1) not operative |  | heading, not operative |
| s21 | 1457-1463 | 21. Sections 10, 12 and 16 apply, with the necessary modific | encoded | sgba-p5-apparatus |  |
| part:6 | 1464-1467 | Part heading | inert (1) not operative |  | heading, not operative |
| s22:heading | 1468-1469 | Frequency planning criteria | inert (1) not operative |  | heading, not operative |
| s22 | 1470-1472 | 22. In performing its functions under this Act, the Authorit | encoded | sgba-p6-p7 |  |
| s22(a) | 1473-1474 | (a) the social and economic characteristics within Singapore | encoded | sgba-p6-p7 |  |
| s22(b) | 1475-1477 | (b) the number of existing broadcasting services and the | encoded | sgba-p6-p7 |  |
| s22(c) | 1478-1479 | (c) the developments in technology; | encoded | sgba-p6-p7 |  |
| s22(d) | 1480-1482 | (d) the technical restraints relating to the transmission, | encoded | sgba-p6-p7 |  |
| s22(e) | 1483-1486 | (e) the demand for electromagnetic, and particularly radio | encoded | sgba-p6-p7 |  |
| s22(f) | 1487-1490 | (f) any other matters that the Authority considers appropria | encoded | sgba-p6-p7 |  |
| s23 | 1491-1492 | 23. [Repealed by Act 22 of 2016] | repealed or blank in this text |  | text reads: 23. [Repealed by Act 22 of 2016] |
| s24:heading | 1493-1494 | Separate licence for use of frequency not required | inert (1) not operative |  | heading, not operative |
| s24 | 1495-1507 | 24. Despite anything in the Telecommunications Act 1999, if  | encoded | sgba-p6-p7 |  |
| part:7 | 1508-1511 | Part heading | inert (1) not operative |  | heading, not operative |
| s25:heading | 1512-1513 | Transmission area requirements | inert (1) not operative |  | heading, not operative |
| s25(1) | 1514-1519 | 25.—(1) A broadcasting licensee must, within the time that m | encoded | sgba-p6-p7 |  |
| s25(2) | 1520-1525 | (2) If the Authority so directs, a free-to-air licensee must | encoded | sgba-p6-p7 |  |
| s26:heading | 1526-1527 | Sharing of facilities | inert (1) not operative |  | heading, not operative |
| s26(1) | 1528-1539 | 26.—(1) The Authority may direct any broadcasting licensee o | encoded | sgba-p6-p7 |  |
| s26(2) | 1540-1550 | (2) The Authority may direct any broadcasting licensee to | encoded | sgba-p6-p7 |  |
| s26(3) | 1551-1554 | (3) In this section, “telecommunication licensee” and | encoded | sgba-p6-p7 |  |
| s27:heading | 1555-1556 | Inspection and testing of broadcasting apparatus | inert (1) not operative |  | heading, not operative |
| s27(1) | 1557-1566 | 27.—(1) The Authority or any person authorised by it in that | encoded | sgba-p6-p7 |  |
| s27(2) | 1567-1570 | (2) For the purpose of any inspection or test under subsecti | encoded | sgba-p6-p7 |  |
| s27(2)(a) | 1571-1576 | (a) make available on request to the Authority or any person | encoded | sgba-p6-p7 |  |
| s27(2)(b) | 1577-1579 | (b) assist the Authority or such authorised person in carryi | encoded | sgba-p6-p7 |  |
| s27(2)(c) | 1580-1582 | (c) answer directly and truthfully any question put to them  | encoded | sgba-p6-p7 |  |
| s28:heading | 1583-1585 | Provision of building space, etc., by developer or owner of  | inert (1) not operative |  | heading, not operative |
| s28(1) | 1586-1587 | 28.—(1) Where the Authority — | encoded | sgba-p6-p7 |  |
| s28(1)(a) | 1588-1590 | (a) considers it necessary that any licensable broadcasting | encoded | sgba-p6-p7 |  |
| s28(1)(b) | 1591-1603 | (b) is of the opinion that any broadcasting apparatus or | encoded | sgba-p6-p7 |  |
| s28(2) | 1604-1605 | (2) Where the Authority — | encoded | sgba-p6-p7 |  |
| s28(2)(a) | 1606-1609 | (a) considers it necessary that the reception of any licensa | encoded | sgba-p6-p7 |  |
| s28(2)(b) | 1610-1620 | (b) is of the opinion that any broadcasting apparatus or | encoded | sgba-p6-p7 |  |
| s28(3) | 1621-1622 | (3) Any direction under subsection (1) or (2) may include — | encoded | sgba-p6-p7 |  |
| s28(3)(a) | 1623-1628 | (a) a requirement that the developer or owner of the buildin | encoded | sgba-p6-p7 |  |
| s28(3)(b) | 1629-1630 | (b) any other requirements that the Authority may specify. | encoded | sgba-p6-p7 |  |
| s28(4) | 1631-1634 | (4) Any person who fails to comply with any requirement in a | encoded | sgba-p6-p7 |  |
| s28(5) | 1635-1643 | (5) Nothing in any direction given under subsection (1) is t | encoded | sgba-p6-p7 |  |
| s28(6) | 1644-1647 | (6) In this section, “installation or plant” includes all bu | encoded | sgba-p6-p7 |  |
| part:8 | 1648-1651 | Part heading | inert (1) not operative |  | heading, not operative |
| s29:heading | 1652-1653 | Orders proscribing unacceptable foreign broadcasting service | inert (1) not operative |  | heading, not operative |
| s29(1) | 1654-1657 | 29.—(1) Subject to this section, the Minister may make an or | encoded | sgba-p8-p9-foreign |  |
| s29(2) | 1658-1664 | (2) If the Authority considers that the quality or content o | encoded | sgba-p8-p9-foreign |  |
| s29(3) | 1665-1670 | (3) The Authority must not consider a foreign broadcasting s | encoded | sgba-p8-p9-foreign |  |
| s29(4) | 1671-1675 | (4) In this section and section 30, “foreign broadcasting se | encoded | sgba-p8-p9-foreign |  |
| s30:heading | 1676-1677 | Offence of supporting proscribed foreign broadcasting servic | inert (1) not operative |  | heading, not operative |
| s30(1) | 1678-1682 | 30.—(1) This section applies to any foreign broadcasting ser | encoded | sgba-p8-p9-foreign |  |
| s30(2) | 1683-1688 | (2) Any person who in Singapore does any of the following ac | encoded | sgba-p8-p9-foreign |  |
| s30(2)(a) | 1689-1692 | (a) supplying any equipment or other goods for use in | encoded | sgba-p8-p9-foreign |  |
| s30(2)(b) | 1693-1696 | (b) supplying, or offering to supply, programmes to be | encoded | sgba-p8-p9-foreign |  |
| s30(2)(c) | 1697-1699 | (c) arranging for, or inviting, any other person to supply | encoded | sgba-p8-p9-foreign |  |
| s30(2)(d) | 1700-1703 | (d) advertising, by means of programmes transmitted as part  | encoded | sgba-p8-p9-foreign |  |
| s30(2)(e) | 1704-1709 | (e) publishing the times or other details of any programmes | encoded | sgba-p8-p9-foreign |  |
| s30(2)(f) | 1710-1714 | (f) supplying, or offering to supply, any decoding equipment | encoded | sgba-p8-p9-foreign |  |
| s30(2)(g) | 1715-1716 | (g) promoting, financially or otherwise, a proscribed servic | encoded | sgba-p8-p9-foreign |  |
| s30(3) | 1717-1720 | (3) Any person who is guilty of an offence under subsection  | encoded | sgba-p8-p9-foreign |  |
| s30(4) | 1721-1723 | (4) Any equipment and goods used in the commission of an off | encoded | sgba-p8-p9-foreign |  |
| s30(5) | 1724-1730 | (5) For the purposes of this section, a person exposing deco | encoded | sgba-p8-p9-foreign |  |
| part:9 | 1731-1734 | Part heading | inert (1) not operative |  | heading, not operative |
| s31:heading | 1735-1736 | Declared foreign broadcasting services | inert (1) not operative |  | heading, not operative |
| s31(1) | 1737-1741 | 31.—(1) The Minister may, by order in the Gazette, declare a | encoded | sgba-p8-p9-foreign |  |
| s31(2) | 1742-1745 | (2) A person must not, without the prior approval of the Min | encoded | sgba-p8-p9-foreign |  |
| s31(3) | 1746-1747 | (3) The Minister may — | encoded | sgba-p8-p9-foreign |  |
| s31(3)(a) | 1748-1750 | (a) grant his or her approval under subsection (2) subject t | encoded | sgba-p8-p9-foreign |  |
| s31(3)(b) | 1751-1752 | (b) refuse to grant his or her approval; or | encoded | sgba-p8-p9-foreign |  |
| s31(3)(c) | 1753-1755 | (c) revoke his or her approval at any time without giving an | encoded | sgba-p8-p9-foreign |  |
| s31(4) | 1756-1758 | (4) Without limiting subsection (3), the Minister may, in im | encoded | sgba-p8-p9-foreign |  |
| s31(4)(a) | 1759-1763 | (a) the number of persons capable of receiving any declared | encoded | sgba-p8-p9-foreign |  |
| s31(4)(b) | 1764-1768 | (b) the rebroadcast of any declared foreign broadcasting | encoded | sgba-p8-p9-foreign |  |
| s31(5) | 1769-1776 | (5) Any person who contravenes subsection (2) or fails to co | encoded | sgba-p8-p9-foreign |  |
| s31(6) | 1777-1780 | (6) In this section — | encoded | sgba-p8-p9-foreign |  |
| s31(6)(a) | 1781-1783 | (a) any broadcasting service transmitting from a place | encoded | sgba-p8-p9-foreign |  |
| s31(6)(b) | 1784-1807 | (b) any broadcasting service transmitting from a place in | encoded | sgba-p8-p9-foreign |  |
| part:10 | 1808-1812 | Part heading | inert (1) not operative |  | heading, not operative |
| s32:heading | 1813-1814 | Application of this Part to broadcasting company | inert (1) not operative |  | heading, not operative |
| s32(1) | 1815-1820 | 32.—(1) This Part applies to every broadcasting company unle | encoded | sgba-p10-ownership |  |
| s32(2) | 1821-1835 | (2) In this Part — | encoded | sgba-p10-ownership |  |
| s32(2)(a) | 1836-1837 | (a) any free-to-air licence; or | encoded | sgba-p10-ownership |  |
| s32(2)(b) | 1838-1844 | (b) any broadcasting licence under which a subscription | encoded | sgba-p10-ownership |  |
| s32(2)(c) | 1845-1859 | (c) any other broadcasting licence that the Minister may | encoded | sgba-p10-ownership |  |
| s33:heading | 1860-1861 | Special features of broadcasting company | inert (1) not operative |  | heading, not operative |
| s33(1) | 1862-1866 | 33.—(1) A broadcasting company must not, on or after | encoded | sgba-p10-ownership |  |
| s33(2) | 1867-1873 | (2) Unless the Authority otherwise approves, the chief execu | encoded | sgba-p10-ownership |  |
| s33(3) | 1874-1878 | (3) No chief executive officer, director, or chairperson of  | encoded | sgba-p10-ownership |  |
| s33(3)(a) | 1879-1883 | (a) his or her appointment as chief executive officer, direc | encoded | sgba-p10-ownership |  |
| s33(3)(b) | 1884-1890 | (b) his or her appointment as chief executive officer, direc | encoded | sgba-p10-ownership |  |
| s33(4) | 1891-1895 | (4) Where the Authority does not approve the appointment of  | encoded | sgba-p10-ownership |  |
| s33(5) | 1896-1901 | (5) Any broadcasting company which contravenes this section  | encoded | sgba-p10-ownership |  |
| s33(6) | 1902-1905 | (6) This section has effect despite the provisions of any ot | encoded | sgba-p10-ownership |  |
| s33(7) | 1906-1910 | (7) In this section — | encoded | sgba-p10-ownership |  |
| s33(7)(a) | 1911-1913 | (a) in the direct employment of, or acting for or by | encoded | sgba-p10-ownership |  |
| s33(7)(b) | 1914-1926 | (b) principally responsible for the management and | encoded | sgba-p10-ownership |  |
| s34:heading | 1927-1929 | Application and interpretation of this section and sections  | inert (1) not operative |  | heading, not operative |
| s34(1) | 1930-1935 | 34.—(1) This section and sections 35 to 42 apply to, and in  | encoded | sgba-p10-ownership |  |
| s34(2) | 1936-1954 | (2) In sections 35 to 42, unless the context otherwise requi | encoded | sgba-p10-ownership |  |
| s34(3) | 1955-1965 | (3) In determining whether a person is a substantial shareho | encoded | sgba-p10-ownership |  |
| s35:heading | 1966-1968 | Control of substantial shareholdings in broadcasting compani | inert (1) not operative |  | heading, not operative |
| s35(1) | 1969-1972 | 35.—(1) A person must not, on or after 2 September 2002, bec | encoded | sgba-p10-ownership |  |
| s35(2) | 1973-1979 | (2) Subject to section 37(4), a person who, immediately befo | encoded | sgba-p10-ownership |  |
| s35(3) | 1980-1988 | (3) A person must not, on or after 2 September 2002, enter i | encoded | sgba-p10-ownership |  |
| s35(3A) | 1989-1999 | (3A) In subsection (3), where the broadcasting company conce | encoded | sgba-p10-ownership |  |
| s35(4) | 2000-2010 | (4) Subject to section 37(4), a person who, at any time befo | encoded | sgba-p10-ownership |  |
| s35(5) | 2011-2013 | (5) For the purposes of this section, a person has an intere | encoded | sgba-p10-ownership |  |
| s35(5)(a) | 2014-2016 | (a) the person is deemed to have an interest in that share u | encoded | sgba-p10-ownership |  |
| s35(5)(b) | 2017-2020 | (b) the person otherwise has a legal or an equitable interes | encoded | sgba-p10-ownership |  |
| s35(6) | 2021-2023 | (6) The application of subsection (5) in relation to any sha | encoded | sgba-p10-ownership |  |
| s35(6)(a) | 2024-2026 | (a) subsection (3) of section 7 of the Companies Act 1967 do | encoded | sgba-p10-ownership |  |
| s35(6)(b) | 2027-2029 | (b) paragraph (ca) of section 7(9) of the Companies Act 1967 | encoded | sgba-p10-ownership |  |
| s35(6)(c) | 2030-2031 | (c) a book-entry security is treated as an interest in a sha | encoded | sgba-p10-ownership |  |
| s35(6)(d) | 2032-2038 | (d) a person that is a subsidiary of a VCC does not have an | encoded | sgba-p10-ownership |  |
| s36:heading | 2039-2041 | Control of shareholdings and voting power in broadcasting co | inert (1) not operative |  | heading, not operative |
| s36(1) | 2042-2044 | 36.—(1) A person must not, on or after 2 September 2002, | encoded | sgba-p10-ownership |  |
| s36(1)(a) | 2045-2046 | (a) a 12% controller; or | encoded | sgba-p10-ownership |  |
| s36(1)(b) | 2047-2051 | (b) an indirect controller, | encoded | sgba-p10-ownership |  |
| s36(2) | 2052-2054 | (2) Subject to section 37(4), a person who, immediately befo | encoded | sgba-p10-ownership |  |
| s36(2)(a) | 2055-2056 | (a) a 12% controller; or | encoded | sgba-p10-ownership |  |
| s36(2)(b) | 2057-2066 | (b) an indirect controller, | encoded | sgba-p10-ownership |  |
| s36(3) | 2067-2069 | (3) In subsections (1)(a) and (2)(a), “12% controller” means | encoded | sgba-p10-ownership |  |
| s36(3)(a) | 2070-2072 | (a) holds at least 12% of the shares in the broadcasting | encoded | sgba-p10-ownership |  |
| s36(3)(b) | 2073-2075 | (b) is in a position to control voting power of at least 12% | encoded | sgba-p10-ownership |  |
| s36(3A) | 2076-2081 | (3A) In subsection (3), where the broadcasting company conce | encoded | sgba-p10-ownership |  |
| s36(3A)(a) | 2082-2085 | (a) the reference to the shares in a broadcasting company is | encoded | sgba-p10-ownership |  |
| s36(3A)(b) | 2086-2091 | (b) the reference to voting power in a broadcasting company  | encoded | sgba-p10-ownership |  |
| s36(4) | 2092-2093 | (4) For the purposes of subsections (3) and (3A) — | encoded | sgba-p10-ownership |  |
| s36(4)(a) | 2094-2104 | (a) a person holds a share if — | encoded | sgba-p10-ownership |  |
| s36(4)(b) | 2105-2114 | (b) a reference to the control of a percentage of the voting | encoded | sgba-p10-ownership |  |
| s36(4)(c) | 2115-2168 | (c) a person (A) is an associate of another person (B) if — | encoded | sgba-p10-ownership |  |
| s36(4A) | 2169-2171 | (4A) The application of subsection (4)(a) in relation to any | encoded | sgba-p10-ownership |  |
| s36(4A)(a) | 2172-2174 | (a) paragraph (ca) of section 7(9) of the Companies Act 1967 | encoded | sgba-p10-ownership |  |
| s36(4A)(b) | 2175-2176 | (b) a book-entry security is treated as an interest in a sha | encoded | sgba-p10-ownership |  |
| s36(4A)(c) | 2177-2183 | (c) a person that is a subsidiary of a VCC does not have an | encoded | sgba-p10-ownership |  |
| s36(5) | 2184-2188 | (5) In subsections (1)(b) and (2)(b), “indirect controller”  | encoded | sgba-p10-ownership |  |
| s36(5)(a) | 2189-2193 | (a) in accordance with whose directions, instructions or | encoded | sgba-p10-ownership |  |
| s36(5)(b) | 2194-2198 | (b) who is in a position to determine the policy of the | encoded | sgba-p10-ownership |  |
| s36(5)(c) | 2199-2202 | (c) who is a director or other officer of the broadcasting | encoded | sgba-p10-ownership |  |
| s36(5)(d) | 2203-2211 | (d) in accordance with whose directions, instructions or | encoded | sgba-p10-ownership |  |
| s37:heading | 2212-2213 | Approval of applications | inert (1) not operative |  | heading, not operative |
| s37(1) | 2214-2216 | 37.—(1) The Minister may approve an application made by any | encoded | sgba-p10-ownership |  |
| s37(1)(a) | 2217-2218 | (a) the person is a fit and proper person; | encoded | sgba-p10-ownership |  |
| s37(1)(b) | 2219-2223 | (b) having regard to the person’s likely influence, the | encoded | sgba-p10-ownership |  |
| s37(1)(c) | 2224-2225 | (c) it is in the national interest to do so. | encoded | sgba-p10-ownership |  |
| s37(2) | 2226-2229 | (2) Any approval under this section may be granted to any pe | encoded | sgba-p10-ownership |  |
| s37(2)(a) | 2230-2232 | (a) restricting the person’s disposal or further acquisition | encoded | sgba-p10-ownership |  |
| s37(2)(b) | 2233-2235 | (b) restricting the person’s exercise of voting power in the | encoded | sgba-p10-ownership |  |
| s37(3) | 2236-2243 | (3) Any condition imposed under subsection (2) has effect de | encoded | sgba-p10-ownership |  |
| s37(4) | 2244-2248 | (4) Where the Minister does not approve an application made  | encoded | sgba-p10-ownership |  |
| s37(4)(a) | 2249-2251 | (a) in the case of section 35(2), to cease to be a substanti | encoded | sgba-p10-ownership |  |
| s37(4)(b) | 2252-2257 | (b) in the case of section 35(4), to cease to be a party to  | encoded | sgba-p10-ownership |  |
| s37(4)(c) | 2258-2265 | (c) in the case of section 36(2), to cease to be — | encoded | sgba-p10-ownership |  |
| s38 | 2266-2267 | 38. [Repealed by Act 31 of 2022 wef 01/11/2022] | repealed or blank in this text |  | text reads: 38. [Repealed by Act 31 of 2022 wef 01/11/2022] |
| s39:heading | 2268-2269 | Objection to existing control of broadcasting company | inert (1) not operative |  | heading, not operative |
| s39(1) | 2270-2273 | 39.—(1) The Minister may serve a written notice of objection | encoded | sgba-p10-ownership |  |
| s39(1)(a) | 2274-2276 | (a) any condition of approval imposed on the person under | encoded | sgba-p10-ownership |  |
| s39(1)(b) | 2277-2278 | (b) the person ceases to be a fit and proper person; | encoded | sgba-p10-ownership |  |
| s39(1)(c) | 2279-2283 | (c) having regard to the person’s likely influence, the | encoded | sgba-p10-ownership |  |
| s39(1)(d) | 2284-2289 | (d) it is no longer in the national interest to allow the pe | encoded | sgba-p10-ownership |  |
| s39(1)(e) | 2290-2293 | (e) the person has provided false or misleading information  | encoded | sgba-p10-ownership |  |
| s39(1)(f) | 2294-2298 | (f) the Minister would not have granted his or her approval | encoded | sgba-p10-ownership |  |
| s39(2) | 2299-2310 | (2) Before serving a written notice of objection, the Minist | encoded | sgba-p10-ownership |  |
| s39(3) | 2311-2315 | (3) Upon receiving the written representations of any person | encoded | sgba-p10-ownership |  |
| s39(4) | 2316-2319 | (4) The Minister must, in any written notice of objection, s | encoded | sgba-p10-ownership |  |
| s39(4)(a) | 2320-2325 | (a) take such steps as are necessary to ensure that the pers | encoded | sgba-p10-ownership |  |
| s39(4)(b) | 2326-2328 | (b) comply with any direction or restriction that the Minist | encoded | sgba-p10-ownership |  |
| s39(5) | 2329-2331 | (5) Any person served with a written notice of objection und | encoded | sgba-p10-ownership |  |
| s40:heading | 2332-2333 | Power to make directions | inert (1) not operative |  | heading, not operative |
| s40(1) | 2334-2339 | 40.—(1) Without affecting section 41, if the Minister is sat | encoded | sgba-p10-ownership |  |
| s40(1)(a) | 2340-2345 | (a) direct the transfer or disposal of all or any of the sha | encoded | sgba-p10-ownership |  |
| s40(1)(b) | 2346-2347 | (b) restrict the transfer or disposal of the specified share | encoded | sgba-p10-ownership |  |
| s40(1)(c) | 2348-2353 | (c) make any other direction or restriction that the Ministe | encoded | sgba-p10-ownership |  |
| s40(2) | 2354-2357 | (2) Any person to whom a notice is served under subsection ( | encoded | sgba-p10-ownership |  |
| s40(3) | 2358-2363 | (3) In the case of any direction or restriction made under | encoded | sgba-p10-ownership |  |
| s40(3)(a) | 2364-2367 | (a) no voting rights are exercisable in respect of the speci | encoded | sgba-p10-ownership |  |
| s40(3)(b) | 2368-2372 | (b) no shares of the broadcasting company are to be issued o | encoded | sgba-p10-ownership |  |
| s40(3)(c) | 2373-2384 | (c) except in a liquidation of the broadcasting company, no | encoded | sgba-p10-ownership |  |
| s40(4) | 2385-2387 | (4) In this section, “associate” has the meaning given by | encoded | sgba-p10-ownership |  |
| s41:heading | 2388-2389 | Offences, penalties and defences | inert (1) not operative |  | heading, not operative |
| s41(1) | 2390-2399 | 41.—(1) Any person who contravenes section 35, 36(1)(a) or ( | encoded | sgba-p10-ownership |  |
| s41(2) | 2400-2407 | (2) Any person who contravenes section 36(1)(b) or (2)(b), | encoded | sgba-p10-ownership |  |
| s41(3) | 2408-2411 | (3) Where a person is charged with an offence in respect of  | encoded | sgba-p10-ownership |  |
| s41(3)(a) | 2412-2414 | (a) the person was not aware that the person had contravened | encoded | sgba-p10-ownership |  |
| s41(3)(b) | 2415-2422 | (b) the person has, within 14 days of becoming aware that th | encoded | sgba-p10-ownership |  |
| s41(4) | 2423-2426 | (4) Where a person is charged with an offence in respect of  | encoded | sgba-p10-ownership |  |
| s41(4)(a) | 2427-2431 | (a) the contravention occurred as a result of an increase in | encoded | sgba-p10-ownership |  |
| s41(4)(b) | 2432-2438 | (b) the person has no agreement or arrangement, whether oral | encoded | sgba-p10-ownership |  |
| s41(4)(c) | 2439-2449 | (c) the person has, within 14 days of the date of the | encoded | sgba-p10-ownership |  |
| s41(5) | 2450-2454 | (5) Except as provided in subsections (3) and (4), it is not | encoded | sgba-p10-ownership |  |
| s42:heading | 2455-2456 | Power to obtain information | inert (1) not operative |  | heading, not operative |
| s42(1) | 2457-2460 | 42.—(1) The Authority may, by written notice, direct any | encoded | sgba-p10-ownership |  |
| s42(1)(a) | 2461-2464 | (a) as to whether that shareholder holds any share in the | encoded | sgba-p10-ownership |  |
| s42(1)(b) | 2465-2473 | (b) if the shareholder holds the share as trustee, to indica | encoded | sgba-p10-ownership |  |
| s42(2) | 2474-2479 | (2) The Authority may, by written notice, require any shareh | encoded | sgba-p10-ownership |  |
| s42(2)(a) | 2480-2486 | (a) whether the person holds that interest as beneficial own | encoded | sgba-p10-ownership |  |
| s42(2)(b) | 2487-2499 | (b) whether any share or any voting right attached to the sh | encoded | sgba-p10-ownership |  |
| s42(3) | 2500-2501 | (3) Any person who — | encoded | sgba-p10-ownership |  |
| s42(3)(a) | 2502-2503 | (a) fails to comply with a notice under this section; or | encoded | sgba-p10-ownership |  |
| s42(3)(b) | 2504-2513 | (b) in purported compliance of the notice, knowingly or | encoded | sgba-p10-ownership |  |
| s43:heading | 2514-2516 | Funds from foreign source for purposes of certain broadcasti | inert (1) not operative |  | heading, not operative |
| s43(1) | 2517-2522 | 43.—(1) Subject to this section, a person must not, without  | encoded | sgba-p10-ownership |  |
| s43(2) | 2523-2527 | (2) The Authority may grant its consent under subsection (1) | encoded | sgba-p10-ownership |  |
| s43(3) | 2528-2538 | (3) Despite subsection (1), where any fund from a foreign so | encoded | sgba-p10-ownership |  |
| s43(4) | 2539-2545 | (4) Where any fund from a foreign source has been received b | encoded | sgba-p10-ownership |  |
| s43(5) | 2546-2553 | (5) Any employee of a broadcasting company who, having recei | encoded | sgba-p10-ownership |  |
| s43(6) | 2554-2557 | (6) For the purposes of subsection (5), any fund received fr | encoded | sgba-p10-ownership |  |
| s43(7) | 2558-2561 | (7) Nothing in this section applies to any dealing by any pe | encoded | sgba-p10-ownership |  |
| s43(8) | 2562-2568 | (8) Any person who contravenes subsection (1), (3) or (4) sh | encoded | sgba-p10-ownership |  |
| s43(9) | 2569-2572 | (9) In this section and section 44 — | fork | sgba-p10-ownership | F-BA-06: whether a Singapore body with a non-citizen member or director is a foreign source outright or only if declared; the undeclared case answers NOTHING |
| s43(9)(a) | 2573-2576 | (a) the government of a country outside Singapore or the | encoded | sgba-p10-ownership |  |
| s43(9)(b) | 2577-2584 | (b) any company, association or society incorporated or | encoded | sgba-p10-ownership |  |
| s43(9)(c) | 2585-2587 | (c) any person who is not a citizen of Singapore, whether | encoded | sgba-p10-ownership |  |
| s43(9)(d) | 2588-2608 | (d) any — | encoded | sgba-p10-ownership |  |
| s43(9)(e) | 2609-2619 | (e) any other source outside Singapore that the Minister | encoded | sgba-p10-ownership |  |
| s44:heading | 2620-2621 | Broadcasting company owned by foreign source | inert (1) not operative |  | heading, not operative |
| s44(1) | 2622-2625 | 44.—(1) A company must not, unless the Minister otherwise | encoded | sgba-p10-ownership |  |
| s44(1)(a) | 2626-2637 | (a) any foreign source, alone or together with one or more | encoded | sgba-p10-ownership |  |
| s44(1)(b) | 2638-2650 | (b) all or a majority of the persons having the direction, c | encoded | sgba-p10-ownership |  |
| s44(1A) | 2651-2655 | (1A) In subsection (1), where the holding company concerned  | encoded | sgba-p10-ownership |  |
| s44(1A)(a) | 2656-2659 | (a) the reference to the shares in the holding company is to | encoded | sgba-p10-ownership |  |
| s44(1A)(b) | 2660-2665 | (b) the reference to voting power in the holding company is  | encoded | sgba-p10-ownership |  |
| s44(2) | 2666-2675 | (2) Where the Minister does not grant his or her approval un | encoded | sgba-p10-ownership |  |
| s44(3) | 2676-2677 | (3) For the purposes of this section — | encoded | sgba-p10-ownership |  |
| s44(3)(a) | 2678-2688 | (a) a person holds a share if — | encoded | sgba-p10-ownership |  |
| s44(3)(b) | 2689-2694 | (b) a reference to the control of a percentage of the voting | encoded | sgba-p10-ownership |  |
| s44(4) | 2695-2697 | (4) The application of subsection (3)(a) in relation to any  | encoded | sgba-p10-ownership |  |
| s44(4)(a) | 2698-2700 | (a) paragraph (ca) of section 7(9) of the Companies Act 1967 | encoded | sgba-p10-ownership |  |
| s44(4)(b) | 2701-2702 | (b) a book-entry security is treated as an interest in a sha | encoded | sgba-p10-ownership |  |
| s44(4)(c) | 2703-2709 | (c) a person that is a subsidiary of a VCC does not have an | encoded | sgba-p10-ownership |  |
| s45:heading | 2710-2711 | Appeal under this Part | inert (1) not operative |  | heading, not operative |
| s45 | 2712-2715 | 45. Any person aggrieved by any refusal of the Authority to  | encoded | sgba-p10-ownership |  |
| part:10A | 2716-2723 | Part heading | inert (1) not operative |  | heading, not operative |
| division:Division1 | 2724-2725 | Division heading | inert (1) not operative |  | heading, not operative |
| s45A:heading | 2726-2727 | Purpose | inert (1) not operative |  | heading, not operative |
| s45A | 2728-2730 | 45A. The purpose of this Part is to ensure that providers of | inert (1) not operative |  | purpose clause; creates no rule (ss 45K(1) and 45L(4)(e) refer to its purposes and are encoded) |
| s45A(a) | 2731-2735 | (a) provide a safe online environment for Singapore end-user | inert (1) not operative |  | purpose clause; creates no rule (ss 45K(1) and 45L(4)(e) refer to its purposes and are encoded) |
| s45A(b) | 2736-2739 | (b) place adequate priority on the protection of Singapore e | inert (1) not operative |  | purpose clause; creates no rule (ss 45K(1) and 45L(4)(e) refer to its purposes and are encoded) |
| s45A(c) | 2740-2744 | (c) are regulated in a manner that enables public interest | inert (1) not operative |  | purpose clause; creates no rule (ss 45K(1) and 45L(4)(e) refer to its purposes and are encoded) |
| s45B:heading | 2745-2746 | Application | inert (1) not operative |  | heading, not operative |
| s45B | 2747-2757 | 45B. This Part applies to and in relation to any content tha | encoded | sgba-p10a-d1-d2 |  |
| s45C:heading | 2758-2760 | When content is provided or communicated on online communica | inert (1) not operative |  | heading, not operative |
| s45C(1) | 2761-2764 | 45C.—(1) For the purposes of this Part, content is provided  | encoded | sgba-p10a-d1-d2 |  |
| s45C(2) | 2765-2774 | (2) For the purposes of this Part, content is communicated o | encoded | sgba-p10a-d1-d2 |  |
| s45D:heading | 2775-2776 | Meaning of “egregious content” | inert (1) not operative |  | heading, not operative |
| s45D(1) | 2777-2778 | 45D.—(1) In this Part, “egregious content” means — | encoded | sgba-p10a-d1-d2 |  |
| s45D(1)(a) | 2779-2780 | (a) content that advocates or instructs on suicide or self-h | encoded | sgba-p10a-d1-d2 |  |
| s45D(1)(b) | 2781-2784 | (b) content that advocates or instructs on violence or cruel | encoded | sgba-p10a-d1-d2 |  |
| s45D(1)(c) | 2785-2788 | (c) content that advocates or instructs on sexual violence o | encoded | sgba-p10a-d1-d2 |  |
| s45D(1)(d) | 2789-2793 | (d) content depicting for a sexual purpose, or that exploits | encoded | sgba-p10a-d1-d2 |  |
| s45D(1)(e) | 2794-2801 | (e) content that advocates engaging in conduct in a way that | encoded | sgba-p10a-d1-d2 |  |
| s45D(1)(f) | 2802-2806 | (f) content dealing with matters of race or religion in a wa | encoded | sgba-p10a-d1-d2 |  |
| s45D(1)(g) | 2807-2808 | (g) content that advocates or instructs on terrorism; or | encoded | sgba-p10a-d1-d2 |  |
| s45D(1)(h) | 2809-2811 | (h) any other content that is prescribed by Part 10A regulat | encoded | sgba-p10a-d1-d2 |  |
| s45D(2) | 2812-2814 | (2) It does not matter if the content in subsection (1) rela | encoded | sgba-p10a-d1-d2 |  |
| s45D(3) | 2815-2818 | (3) In this section — | encoded | sgba-p10a-d1-d2 |  |
| s45D(3)(a) | 2819-2827 | (a) an offence under the Penal Code 1871 involving | encoded | sgba-p10a-d1-d2 |  |
| s45D(3)(b) | 2828-2830 | (b) an offence under section 8 of the Children and Young | encoded | sgba-p10a-d1-d2 |  |
| s45D(3)(c) | 2831-2833 | (c) an abetment of or a conspiracy to commit an offence | encoded | sgba-p10a-d1-d2 |  |
| s45D(3)(d) | 2834-2836 | (d) an attempt to commit an offence specified in | encoded | sgba-p10a-d1-d2 |  |
| s45D(3)(e) | 2837-2880 | (e) conduct outside Singapore which, had it been | encoded | sgba-p10a-d1-d2 |  |
| s45D(3)(f) | 2881-2886 | (f) an offence specified in paragraph (a), (b), (c), (d) or | encoded | sgba-p10a-d1-d2 |  |
| division:Division2 | 2887-2888 | Division heading | inert (1) not operative |  | heading, not operative |
| s45E:heading | 2889-2891 | Offence of not stopping egregious content on online communic | inert (1) not operative |  | heading, not operative |
| s45E(1) | 2892-2893 | 45E.—(1) A person commits an offence if — | encoded | sgba-p10a-d1-d2 |  |
| s45E(1)(a) | 2894-2896 | (a) the person provides an online communication service with | encoded | sgba-p10a-d1-d2 |  |
| s45E(1)(b) | 2897-2899 | (b) the online communication service provides or can be used | encoded | sgba-p10a-d1-d2 |  |
| s45E(1)(c) | 2900-2901 | (c) the content is egregious content; | encoded | sgba-p10a-d1-d2 |  |
| s45E(1)(d) | 2902-2908 | (d) the person knows, or ought reasonably to know that — | encoded | sgba-p10a-d1-d2 |  |
| s45E(1)(e) | 2909-2913 | (e) the person fails in the person’s duty under section 45J  | encoded | sgba-p10a-d1-d2 |  |
| s45E(2) | 2914-2923 | (2) A person that is guilty of an offence under subsection ( | encoded | sgba-p10a-d1-d2 |  |
| s45E(3) | 2924-2927 | (3) For the purposes of subsection (1), it is immaterial whe | encoded | sgba-p10a-d1-d2 |  |
| s45E(4) | 2928-2929 | (4) If — | encoded | sgba-p10a-d1-d2 |  |
| s45E(4)(a) | 2930-2932 | (a) a section 45H direction is given in relation to an onlin | encoded | sgba-p10a-d1-d2 |  |
| s45E(4)(b) | 2933-2940 | (b) in a prosecution of the person for an offence against | encoded | sgba-p10a-d1-d2 |  |
| s45E(4)(c) | 2941-2944 | (c) that the online communication service provides or can be | encoded | sgba-p10a-d1-d2 |  |
| s45E(4)(d) | 2945-2949 | (d) that the content is egregious content at the time the | encoded | sgba-p10a-d1-d2 |  |
| s45F:heading | 2950-2951 | Offence of not stopping access to online communication servi | inert (1) not operative |  | heading, not operative |
| s45F(1) | 2952-2953 | 45F.—(1) A person commits an offence if — | encoded | sgba-p10a-d1-d2 |  |
| s45F(1)(a) | 2954-2956 | (a) the person provides an internet access service with a | encoded | sgba-p10a-d1-d2 |  |
| s45F(1)(b) | 2957-2960 | (b) the internet access service can be used by a Singapore e | encoded | sgba-p10a-d1-d2 |  |
| s45F(1)(c) | 2961-2962 | (c) the content is egregious content; | encoded | sgba-p10a-d1-d2 |  |
| s45F(1)(d) | 2963-2975 | (d) the person knows, or ought reasonably to know that — | encoded | sgba-p10a-d1-d2 |  |
| s45F(1)(e) | 2976-2980 | (e) the person fails in the person’s duty under section 45J  | encoded | sgba-p10a-d1-d2 |  |
| s45F(2) | 2981-2986 | (2) A person that is guilty of an offence under subsection ( | encoded | sgba-p10a-d1-d2 |  |
| s45F(3) | 2987-2990 | (3) For the purposes of subsection (1), it is immaterial whe | encoded | sgba-p10a-d1-d2 |  |
| s45F(4) | 2991-2992 | (4) If — | encoded | sgba-p10a-d1-d2 |  |
| s45F(4)(a) | 2993-2995 | (a) a section 45I blocking direction is given in relation to | encoded | sgba-p10a-d1-d2 |  |
| s45F(4)(b) | 2996-3006 | (b) in a prosecution of the person for an offence against | encoded | sgba-p10a-d1-d2 |  |
| s45F(4)(c) | 3007-3011 | (c) that the internet access service can, at the time the di | encoded | sgba-p10a-d1-d2 |  |
| s45F(4)(d) | 3012-3019 | (d) that the content is egregious content at the time the | encoded | sgba-p10a-d1-d2 |  |
| s45G:heading | 3020-3021 | Defence | inert (1) not operative |  | heading, not operative |
| s45G | 3022-3025 | 45G. In a prosecution of the person for an offence against | encoded | sgba-p10a-d1-d2 |  |
| s45G(a) | 3026-3028 | (a) it was not reasonably practicable to do more than what w | encoded | sgba-p10a-d1-d2 |  |
| s45G(b) | 3029-3033 | (b) there was no better practicable means than was in fact u | encoded | sgba-p10a-d1-d2 |  |
| s45H:heading | 3034-3035 | Section 45H direction | inert (1) not operative |  | heading, not operative |
| s45H(1) | 3036-3037 | 45H.—(1) If the Authority is satisfied that — | encoded | sgba-p10a-d1-d2 |  |
| s45H(1)(a) | 3038-3041 | (a) any egregious content is being provided on an online | encoded | sgba-p10a-d1-d2 |  |
| s45H(1)(b) | 3042-3047 | (b) Singapore end-users of the service can access the | encoded | sgba-p10a-d1-d2 |  |
| s45H(1)(c) | 3048-3072 | (c) to do one or more of the following as the Authority | fork | sgba-p10a-d1-d2 | F-BA-07: whether the closing words printed as '(ii)' end paragraph (c)(ii) only (encoded) or the whole of (c) |
| s45H(1)(d) | 3073-3076 | (d) to do so within the period specified in the written dire | encoded | sgba-p10a-d1-d2 |  |
| s45H(2) | 3077-3078 | (2) To avoid doubt, a requirement in subsection (1)(c)(ii) — | encoded | sgba-p10a-d1-d2 |  |
| s45H(2)(a) | 3079-3082 | (a) may include requiring altering, terminating or suspendin | encoded | sgba-p10a-d1-d2 |  |
| s45H(2)(b) | 3083-3086 | (b) must not require the doing of any thing with respect to  | encoded | sgba-p10a-d1-d2 |  |
| s45H(3) | 3087-3090 | (3) In addition, a requirement in subsection (1)(c) must not | encoded | sgba-p10a-d1-d2 |  |
| s45H(4) | 3091-3095 | (4) The egregious content must be, so far as is reasonably | encoded | sgba-p10a-d1-d2 |  |
| s45H(5) | 3096-3097 | (5) In this section, “account” includes — | encoded | sgba-p10a-d1-d2 |  |
| s45H(5)(a) | 3098-3099 | (a) a free account; | encoded | sgba-p10a-d1-d2 |  |
| s45H(5)(b) | 3100-3101 | (b) a prepaid account; and | encoded | sgba-p10a-d1-d2 |  |
| s45H(5)(c) | 3102-3106 | (c) anything that may reasonably be regarded as the equivale | encoded | sgba-p10a-d1-d2 |  |
| s45I:heading | 3107-3108 | Section 45I blocking direction | inert (1) not operative |  | heading, not operative |
| s45I(1) | 3109-3111 | 45I.—(1) This section applies to a provider of an internet a | encoded | sgba-p10a-d1-d2 |  |
| s45I(2) | 3112-3113 | (2) If the Authority is satisfied that — | encoded | sgba-p10a-d1-d2 |  |
| s45I(2)(a) | 3114-3120 | (a) a provider of an online communication service with a | encoded | sgba-p10a-d1-d2 |  |
| s45I(2)(b) | 3121-3130 | (b) the internet access service has control over access by | encoded | sgba-p10a-d1-d2 |  |
| s45J:heading | 3131-3132 | Duty to comply | inert (1) not operative |  | heading, not operative |
| s45J(1) | 3133-3137 | 45J.—(1) Every provider of an online communication service o | encoded | sgba-p10a-d1-d2 |  |
| s45J(2) | 3138-3146 | (2) No civil or criminal liability is incurred by a provider | encoded | sgba-p10a-d1-d2 |  |
| division:Division3 | 3147-3148 | Division heading | inert (1) not operative |  | heading, not operative |
| s45K:heading | 3149-3150 | Regulated online communication service | inert (1) not operative |  | heading, not operative |
| s45K(1) | 3151-3155 | 45K.—(1) The Authority may designate an online communication | encoded | sgba-p10a-d3 |  |
| s45K(1)(a) | 3156-3158 | (a) the range of all online communication services provided  | encoded | sgba-p10a-d3 |  |
| s45K(1)(b) | 3159-3169 | (b) the extent and nature of the effect that the different t | encoded | sgba-p10a-d3 |  |
| s45K(2) | 3170-3174 | (2) The Authority must cause notice of every designation und | encoded | sgba-p10a-d3 |  |
| s45K(3) | 3175-3179 | (3) A designation under subsection (1) may be revoked at any | encoded | sgba-p10a-d3 |  |
| s45K(4) | 3180-3186 | (4) To avoid doubt, the non-publication of any notice of a | encoded | sgba-p10a-d3 |  |
| s45L:heading | 3187-3189 | Online Code of Practice for regulated online communication s | inert (1) not operative |  | heading, not operative |
| s45L(1) | 3190-3192 | 45L.—(1) Without limiting section 6, the Authority may, from | encoded | sgba-p10a-d3 |  |
| s45L(1)(a) | 3193-3196 | (a) issue one or more online Codes of Practice applicable to | encoded | sgba-p10a-d3 |  |
| s45L(1)(b) | 3197-3202 | (b) amend or revoke any online Code of Practice issued under | encoded | sgba-p10a-d3 |  |
| s45L(2) | 3203-3209 | (2) The Minister may make rules prescribing the manner or fo | encoded | sgba-p10a-d3 |  |
| s45L(2)(a) | 3210-3221 | (a) to give prior notice of any draft online Code of Practic | encoded | sgba-p10a-d3 |  |
| s45L(2)(b) | 3222-3225 | (b) to specify the place or places where copies of any draft | encoded | sgba-p10a-d3 |  |
| s45L(2)(c) | 3226-3229 | (c) to invite objections and representations in connection w | encoded | sgba-p10a-d3 |  |
| s45L(2)(d) | 3230-3232 | (d) to consider or inquire into all or any of those objectio | encoded | sgba-p10a-d3 |  |
| s45L(3) | 3233-3236 | (3) If any provision in any online Code of Practice issued o | encoded | sgba-p10a-d3 |  |
| s45L(3)(a) | 3237-3239 | (a) is to have effect subject to this Act and the Part 10A | encoded | sgba-p10a-d3 |  |
| s45L(3)(b) | 3240-3242 | (b) having regard to the provisions of this Act and the Part | encoded | sgba-p10a-d3 |  |
| s45L(4) | 3243-3247 | (4) An online Code of Practice issued or amended under this  | encoded | sgba-p10a-d3 |  |
| s45L(4)(a) | 3248-3265 | (a) requirements that a provider of the regulated online | encoded | sgba-p10a-d3 |  |
| s45L(4)(b) | 3266-3271 | (b) any matter so as to provide practical guidance or certai | encoded | sgba-p10a-d3 |  |
| s45L(4)(c) | 3272-3293 | (c) the procedures to be followed by a provider of the | encoded | sgba-p10a-d3 |  |
| s45L(4)(d) | 3294-3310 | (d) a requirement for collaboration or cooperation by the | encoded | sgba-p10a-d3 |  |
| s45L(4)(e) | 3311-3315 | (e) any matter that promotes or furthers any purpose in | encoded | sgba-p10a-d3 |  |
| s45M:heading | 3316-3317 | Duty of regulated online communication service provider | inert (1) not operative |  | heading, not operative |
| s45M(1) | 3318-3322 | 45M.—(1) Every provider of a regulated online communication | encoded | sgba-p10a-d3 |  |
| s45M(2) | 3323-3326 | (2) Where it is alleged for the purposes of this Act that an | encoded | sgba-p10a-d3 |  |
| s45M(2)(a) | 3327-3329 | (a) it was not reasonably practicable to do more than what w | encoded | sgba-p10a-d3 |  |
| s45M(2)(b) | 3330-3332 | (b) there was no better practicable means than was in fact u | encoded | sgba-p10a-d3 |  |
| s45M(3) | 3333-3336 | (3) A requirement of an online Code of Practice applicable t | encoded | sgba-p10a-d3 |  |
| s45M(3)(a) | 3337-3339 | (a) any duty of confidentiality or privacy imposed by any ru | encoded | sgba-p10a-d3 |  |
| s45M(3)(b) | 3340-3345 | (b) any duty imposed by any contract or any rule of | encoded | sgba-p10a-d3 |  |
| s45M(4) | 3346-3352 | (4) No civil or criminal liability is incurred by a provider | encoded | sgba-p10a-d3 |  |
| s45M(5) | 3353-3360 | (5) An online Code of Practice otherwise does not have legis | encoded | sgba-p10a-d3 |  |
| s45N:heading | 3361-3362 | Regulatory action | inert (1) not operative |  | heading, not operative |
| s45N(1) | 3363-3367 | 45N.—(1) Subject to section 45O, if the Authority is satisfi | encoded | sgba-p10a-d3 |  |
| s45N(1)(a) | 3368-3372 | (a) order the defaulting provider to pay, within a period | encoded | sgba-p10a-d3 |  |
| s45N(1)(b) | 3373-3376 | (b) direct the defaulting provider to take any steps, whethe | encoded | sgba-p10a-d3 |  |
| s45N(2) | 3377-3383 | (2) A defaulting provider that does not comply with a direct | encoded | sgba-p10a-d3 |  |
| s45N(3) | 3384-3389 | (3) For the purposes of subsection (2), it is immaterial whe | encoded | sgba-p10a-d3 |  |
| s45O:heading | 3390-3391 | Procedure for regulatory action under section 45N | inert (1) not operative |  | heading, not operative |
| s45O(1) | 3392-3396 | 45O.—(1) Before exercising any powers under section 45N(1) i | encoded | sgba-p10a-d3 |  |
| s45O(1)(a) | 3397-3399 | (a) stating that the Authority intends to take regulatory ac | encoded | sgba-p10a-d3 |  |
| s45O(1)(b) | 3400-3403 | (b) specifying the type of action in section 45N(1) the | encoded | sgba-p10a-d3 |  |
| s45O(1)(c) | 3404-3412 | (c) specifying the time (being at least 14 days from the dat | encoded | sgba-p10a-d3 |  |
| s45O(2) | 3413-3416 | (2) The Authority may, after considering any written represe | encoded | sgba-p10a-d3 |  |
| s45O(3) | 3417-3420 | (3) Where the Authority has made any decision under | encoded | sgba-p10a-d3 |  |
| s45O(4) | 3421-3427 | (4) Subject to section 59(2), a decision which is specified  | encoded | sgba-p10a-d3 |  |
| division:Division4 | 3428-3429 | Division heading | inert (1) not operative |  | heading, not operative |
| s45P:heading | 3430-3431 | Regulations | inert (1) not operative |  | heading, not operative |
| s45P(1) | 3432-3436 | 45P.—(1) The Authority may, with the approval of the Ministe | encoded | sgba-p10a-d4 |  |
| s45P(2) | 3437-3442 | (2) All subsidiary legislation made under this Part must be | encoded | sgba-p10a-d4 |  |
| s45Q:heading | 3443-3444 | Incorporation by reference | inert (1) not operative |  | heading, not operative |
| s45Q(1) | 3445-3458 | 45Q.—(1) Any subsidiary legislation made under this Part or  | encoded | sgba-p10a-d4 |  |
| s45Q(2) | 3459-3462 | (2) Any material referred to in subsection (1) may be applie | encoded | sgba-p10a-d4 |  |
| s45Q(2)(a) | 3463-3464 | (a) in whole or in part; or | encoded | sgba-p10a-d4 |  |
| s45Q(2)(b) | 3465-3468 | (b) with modifications, additions, or variations specified i | encoded | sgba-p10a-d4 |  |
| s45Q(3) | 3469-3473 | (3) A copy of any material applied, adopted or incorporated  | encoded | sgba-p10a-d4 |  |
| s45Q(3)(a) | 3474-3476 | (a) certified as a correct copy of the material by the Minis | encoded | sgba-p10a-d4 |  |
| s45Q(3)(b) | 3477-3478 | (b) retained by the Authority. | encoded | sgba-p10a-d4 |  |
| s45Q(4) | 3479-3489 | (4) Any material applied, adopted or incorporated in any sub | encoded | sgba-p10a-d4 |  |
| s45Q(5) | 3490-3494 | (5) Where any material referred to in subsection (1) is appl | encoded | sgba-p10a-d4 |  |
| s45Q(5)(a) | 3495-3503 | (a) that the material is incorporated in the subsidiary | encoded | sgba-p10a-d4 |  |
| s45Q(5)(b) | 3504-3506 | (b) that the material is available for inspection during wor | encoded | sgba-p10a-d4 |  |
| s45Q(5)(c) | 3507-3509 | (c) the place where the material can be inspected without | encoded | sgba-p10a-d4 |  |
| s45Q(5)(d) | 3510-3511 | (d) that copies of the material can be purchased; | encoded | sgba-p10a-d4 |  |
| s45Q(5)(e) | 3512-3514 | (e) the place where copies of the material can be purchased; | encoded | sgba-p10a-d4 |  |
| s45Q(5)(f) | 3515-3518 | (f) if copies of the material are available in other ways, t | encoded | sgba-p10a-d4 |  |
| s45Q(6) | 3519-3523 | (6) In this section, “modification” includes omissions, addi | encoded | sgba-p10a-d4 |  |
| s45R:heading | 3524-3525 | Interface with other laws and civil liability | inert (1) not operative |  | heading, not operative |
| s45R(1) | 3526-3530 | 45R.—(1) To avoid doubt, section 26(1) of the Electronic | encoded | sgba-p10a-d4 |  |
| s45R(2) | 3531-3532 | (2) Nothing in section 45J or 45M is to be construed — | encoded | sgba-p10a-d4 |  |
| s45R(2)(a) | 3533-3536 | (a) as conferring a right of action in any civil proceedings | encoded | sgba-p10a-d4 |  |
| s45R(2)(b) | 3537-3540 | (b) as conferring a defence to an action in any civil | encoded | sgba-p10a-d4 |  |
| s45R(3) | 3541-3545 | (3) For the purposes of sections 45E(1), 45F(1), 45H and 45I | encoded | sgba-p10a-d4 |  |
| s45R(3)(a) | 3546-3551 | (a) the accessing of the content is necessary for enforcing  | encoded | sgba-p10a-d4 |  |
| s45R(3)(b) | 3552-3555 | (b) the accessing of the content is necessary for monitoring | encoded | sgba-p10a-d4 |  |
| s45R(3)(c) | 3556-3558 | (c) the accessing of the content is solely for the purposes  | encoded | sgba-p10a-d4 |  |
| s45R(3)(d) | 3559-3570 | (d) the accessing of the content is both — | encoded | sgba-p10a-d4 |  |
| s45S:heading | 3571-3572 | Modification of section 50 | inert (1) not operative |  | heading, not operative |
| s45S(1) | 3573-3578 | 45S.—(1) Where the person that commits an offence under | encoded | sgba-p10a-d4 |  |
| s45S(2) | 3579-3584 | (2) The power under section 50(1) to require the provision o | encoded | sgba-p10a-d4 |  |
| s45T:heading | 3585-3585 | Interpretation of this Part | inert (1) not operative |  | heading, not operative |
| s45T(1) | 3586-3609 | 45T.—(1) In this Part, unless the context otherwise requires | encoded | sgba-p10a-d4 |  |
| s45T(1)(a) | 3610-3614 | (a) the sole or primary purpose of the service is to enable | encoded | sgba-p10a-d4 |  |
| s45T(1)(b) | 3615-3617 | (b) the service allows end-users to communicate content | encoded | sgba-p10a-d4 |  |
| s45T(1)(c) | 3618-3628 | (c) any other characteristics that are prescribed by Part | encoded | sgba-p10a-d4 |  |
| s45T(2) | 3629-3631 | (2) To avoid doubt, “content” in this Part includes user-gen | encoded | sgba-p10a-d4 |  |
| s45T(3) | 3632-3633 | (3) Where — | encoded | sgba-p10a-d4 |  |
| s45T(3)(a) | 3634-3639 | (a) by or under any provision of this Part or any Part 10A | encoded | sgba-p10a-d4 |  |
| s45T(3)(b) | 3640-3646 | (b) failure to do that act or thing within the period or bef | encoded | sgba-p10a-d4 |  |
| s45T(3)(c) | 3647-3653 | (c) that act or thing is not done within the period or befor | encoded | sgba-p10a-d4 |  |
| s45T(4) | 3654-3659 | (4) For the purposes of this Part, an online communication s | encoded | sgba-p10a-d4 |  |
| part:11 | 3660-3663 | Part heading | inert (1) not operative |  | heading, not operative |
| s46:heading | 3664-3665 | Offences relating to licensable broadcasting services | inert (1) not operative |  | heading, not operative |
| s46 | 3666-3672 | 46. Any person who contravenes section 8(1) shall be guilty  | encoded | sgba-p11-offences |  |
| s47:heading | 3673-3675 | Offences relating to installation, sale, import or possessio | inert (1) not operative |  | heading, not operative |
| s47 | 3676-3682 | 47. Any person who contravenes section 20(1)(a), (b) or (c)  | encoded | sgba-p11-offences |  |
| s48:heading | 3683-3685 | Offences relating to unauthorised decoders and unauthorised  | inert (1) not operative |  | heading, not operative |
| s48(1) | 3686-3693 | 48.—(1) A person must not manufacture, assemble, modify, | encoded | sgba-p11-offences |  |
| s48(2) | 3694-3698 | (2) A person must not wilfully receive or rebroadcast any en | encoded | sgba-p11-offences |  |
| s48(3) | 3699-3704 | (3) Any person who contravenes subsection (1) or (2) shall b | encoded | sgba-p11-offences |  |
| s48(4) | 3705-3710 | (4) Where it is proved that a person has manufactured, assem | encoded | sgba-p11-offences |  |
| s48(5) | 3711-3720 | (5) In this section and section 48A — | encoded | sgba-p11-offences |  |
| s48(5)(a) | 3721-3722 | (a) a person who holds a broadcasting licence; or | encoded | sgba-p11-offences |  |
| s48(5)(b) | 3723-3736 | (b) in the case of a broadcasting service transmitted from | encoded | sgba-p11-offences |  |
| s48A:heading | 3737-3739 | Civil action in relation to unauthorised decoders and decode | inert (1) not operative |  | heading, not operative |
| s48A(1) | 3740-3741 | 48A.—(1) Where — | encoded | sgba-p11-offences |  |
| s48A(1)(a) | 3742-3744 | (a) a person does an act mentioned in section 48(1) in relat | encoded | sgba-p11-offences |  |
| s48A(1)(b) | 3745-3747 | (b) the unauthorised decoder is used to decode an encrypted | encoded | sgba-p11-offences |  |
| s48A(1)(c) | 3748-3756 | (c) the lawful provider of a broadcasting service who had | encoded | sgba-p11-offences |  |
| s48A(2) | 3757-3758 | (2) Where — | encoded | sgba-p11-offences |  |
| s48A(2)(a) | 3759-3763 | (a) a person does an act mentioned in section 48(2) in relat | encoded | sgba-p11-offences |  |
| s48A(2)(b) | 3764-3771 | (b) the lawful provider of the broadcasting service or the | encoded | sgba-p11-offences |  |
| s48A(3) | 3772-3775 | (3) An action must not be brought under subsection (1) or (2 | fork | sgba-p11-offences | F-BA-04: six years read on dates, anniversary inclusive (encoded); other counting not encoded |
| s49:heading | 3776-3777 | Offence of hindering employee or agent of Authority | inert (1) not operative |  | heading, not operative |
| s49 | 3778-3785 | 49. Any person who obstructs or hinders any employee or agen | encoded | sgba-p11-offences |  |
| s50:heading | 3786-3787 | Power of Authority to requisition information | inert (1) not operative |  | heading, not operative |
| s50(1) | 3788-3795 | 50.—(1) The Authority or any person the Authority authorises | encoded | sgba-p11-offences |  |
| s50(2) | 3796-3800 | (2) Any person who, on being required by any notice under | encoded | sgba-p11-offences |  |
| s50(3) | 3801-3802 | (3) Any person who — | encoded | sgba-p11-offences |  |
| s50(3)(a) | 3803-3806 | (a) intentionally alters, suppresses or destroys any documen | encoded | sgba-p11-offences |  |
| s50(3)(b) | 3807-3814 | (b) in providing any estimate, return or other information | encoded | sgba-p11-offences |  |
| s50(4) | 3815-3818 | (4) Any person guilty of an offence under subsection (2) or  | encoded | sgba-p11-offences |  |
| s51:heading | 3819-3821 | Power of police officer and other authorised persons against | inert (1) not operative |  | heading, not operative |
| s51(1) | 3822-3825 | 51.—(1) Any police officer or any employee authorised by the | encoded | sgba-p11-offences |  |
| s51(1)(a) | 3826-3831 | (a) a broadcasting service has been or is being provided in | encoded | sgba-p11-offences |  |
| s51(1)(b) | 3832-3834 | (b) a broadcasting service has been or is being provided in | encoded | sgba-p11-offences |  |
| s51(1)(c) | 3835-3841 | (c) any broadcasting apparatus used is not licensed by the | encoded | sgba-p11-offences |  |
| s51(2) | 3842-3846 | (2) If there is no prosecution with regard to any broadcasti | encoded | sgba-p11-offences |  |
| s51(3) | 3847-3851 | (3) Any person asserting that the person is the owner of any | encoded | sgba-p11-offences |  |
| s51(4) | 3852-3855 | (4) On receiving the notice, the Authority may direct that t | encoded | sgba-p11-offences |  |
| s51(5) | 3856-3859 | (5) The District Court or the Magistrate’s Court may proceed | encoded | sgba-p11-offences |  |
| s52:heading | 3860-3861 | Power of arrest and search | inert (1) not operative |  | heading, not operative |
| s52(1) | 3862-3865 | 52.—(1) The Chief Executive or any employee of the Authority | encoded | sgba-p11-offences |  |
| s52(1)(a) | 3866-3869 | (a) any person found committing or attempting to commit or | encoded | sgba-p11-offences |  |
| s52(1)(b) | 3870-3881 | (b) any person against whom a reasonable suspicion exists th | encoded | sgba-p11-offences |  |
| s52(2) | 3882-3885 | (2) Every person so arrested must, together with any article | encoded | sgba-p11-offences |  |
| s52(3) | 3886-3889 | (3) For the purposes of this section, offences punishable un | encoded | sgba-p11-offences |  |
| s53:heading | 3890-3891 | No entitlement to costs or damages | inert (1) not operative |  | heading, not operative |
| s53 | 3892-3899 | 53. No person is entitled, in any proceedings before any cou | encoded | sgba-p11-offences |  |
| s54:heading | 3900-3901 | Offence against other laws | inert (1) not operative |  | heading, not operative |
| s54 | 3902-3903 | 54. Nothing in this Act prevents any person — | encoded | sgba-p11-offences |  |
| s54(a) | 3904-3907 | (a) from being prosecuted under any other written law for an | encoded | sgba-p11-offences |  |
| s54(b) | 3908-3913 | (b) from being liable under that other written law to any | encoded | sgba-p11-offences |  |
| s55:heading | 3914-3915 | Conduct of proceedings by officers | inert (1) not operative |  | heading, not operative |
| s55 | 3916-3925 | 55. Proceedings in respect of any offence under this Act may | encoded | sgba-p11-offences |  |
| s56:heading | 3926-3927 | Corporate offenders and unincorporated associations | inert (1) not operative |  | heading, not operative |
| s56(1) | 3928-3934 | 56.—(1) Where an offence under this Act committed by a body | encoded | sgba-p11-offences |  |
| s56(2) | 3935-3939 | (2) Where the affairs of the body corporate are managed by i | encoded | sgba-p11-offences |  |
| s56(3) | 3940-3946 | (3) Proceedings for an offence alleged to have been committe | encoded | sgba-p11-offences |  |
| s56(4) | 3947-3952 | (4) Where an offence under this Act committed by a partnersh | encoded | sgba-p11-offences |  |
| s56(5) | 3953-3960 | (5) Where an offence under this Act committed by an | encoded | sgba-p11-offences |  |
| s56(6) | 3961-3970 | (6) Without limiting section 66, the Authority may make | encoded | sgba-p11-offences |  |
| s56(7) | 3971-3974 | (7) In this section — | encoded | sgba-p11-offences |  |
| s56(7)(a) | 3975-3980 | (a) in relation to a body corporate, means a director, | encoded | sgba-p11-offences |  |
| s56(7)(b) | 3981-3989 | (b) in relation to an unincorporated association (other | encoded | sgba-p11-offences |  |
| s57:heading | 3990-3991 | Composition of offences | inert (1) not operative |  | heading, not operative |
| s57(1) | 3992-3996 | 57.—(1) The Authority may compound any offence under this Ac | encoded | sgba-p11-offences |  |
| s57(2) | 3997-3999 | (2) The Authority may, with the approval of the Minister, ma | encoded | sgba-p11-offences |  |
| s58:heading | 4000-4001 | Jurisdiction of court | inert (1) not operative |  | heading, not operative |
| s58 | 4002-4009 | 58. Despite any provision to the contrary in the Criminal Pr | encoded | sgba-p11-offences |  |
| part:12 | 4010-4013 | Part heading | inert (1) not operative |  | heading, not operative |
| s59:heading | 4014-4015 | Appeal to Minister | inert (1) not operative |  | heading, not operative |
| s59(1) | 4016-4019 | 59.—(1) Any licensee, any provider of an online communicatio | encoded | sgba-p12-misc |  |
| s59(1)(a) | 4020-4022 | (a) any decision of the Authority in the exercise of any | encoded | sgba-p12-misc |  |
| s59(1)(b) | 4023-4029 | (b) anything contained in any Code of Practice or direction | encoded | sgba-p12-misc |  |
| s59(2) | 4030-4033 | (2) Unless otherwise provided, where an appeal is made under | encoded | sgba-p12-misc |  |
| s59(3) | 4034-4037 | (3) The Minister may determine an appeal under this section  | encoded | sgba-p12-misc |  |
| s59(4) | 4038-4039 | (4) The decision of the Minister in any appeal is final. | encoded | sgba-p12-misc |  |
| s59(5) | 4040-4050 | (5) In relation to the Minister determining an appeal agains | encoded | sgba-p12-misc |  |
| s60:heading | 4051-4052 | Exemption | inert (1) not operative |  | heading, not operative |
| s60 | 4053-4055 | 60. The Minister may, subject to any terms and conditions th | encoded | sgba-p12-misc |  |
| s60(a) | 4056-4061 | (a) any class or description of shares or interests in share | encoded | sgba-p12-misc |  |
| s60(b) | 4062-4065 | (b) any person or class of persons from all or any of the | encoded | sgba-p12-misc |  |
| s61:heading | 4066-4067 | Equipment of licensee not subject to distress, etc. | inert (1) not operative |  | heading, not operative |
| s61(1) | 4068-4076 | 61.—(1) No equipment or related facility of a licensee used  | encoded | sgba-p12-misc |  |
| s61(2) | 4077-4078 | (2) This section does not apply to any class licensee. | encoded | sgba-p12-misc |  |
| s62:heading | 4079-4080 | International dealings of Authority | inert (1) not operative |  | heading, not operative |
| s62 | 4081-4087 | 62. For the purposes of the conduct of any international bro | encoded | sgba-p12-misc |  |
| s62(a) | 4088-4090 | (a) the purpose of providing facilities, fixing rates, arran | encoded | sgba-p12-misc |  |
| s62(b) | 4091-4092 | (b) operational, engineering or administrative purposes; or | encoded | sgba-p12-misc |  |
| s62(c) | 4093-4095 | (c) any other purpose necessary to properly fulfil its funct | encoded | sgba-p12-misc |  |
| s63:heading | 4096-4097 | Government’s right to determine international relations | inert (1) not operative |  | heading, not operative |
| s63(1) | 4098-4101 | 63.—(1) Nothing in section 62 is deemed to abrogate the righ | encoded | sgba-p12-misc |  |
| s63(2) | 4102-4109 | (2) The Authority and each broadcasting licensee must so dis | encoded | sgba-p12-misc |  |
| s64:heading | 4110-4111 | Service of documents | inert (1) not operative |  | heading, not operative |
| s64(1) | 4112-4114 | 64.—(1) A document that is permitted or required by this Act | encoded | sgba-p12-misc |  |
| s64(2) | 4115-4117 | (2) A document permitted or required by this Act to be serve | encoded | sgba-p12-misc |  |
| s64(2)(a) | 4118-4119 | (a) by giving it to the individual personally; | encoded | sgba-p12-misc |  |
| s64(2)(b) | 4120-4124 | (b) by sending it by prepaid registered post to the address | encoded | sgba-p12-misc |  |
| s64(2)(c) | 4125-4128 | (c) by leaving it at the individual’s residential address wi | encoded | sgba-p12-misc |  |
| s64(2)(d) | 4129-4131 | (d) by affixing a copy of the document in a conspicuous plac | encoded | sgba-p12-misc |  |
| s64(2)(e) | 4132-4135 | (e) by sending it by fax to the fax number last known to the | encoded | sgba-p12-misc |  |
| s64(2)(f) | 4136-4138 | (f) by sending it by email to the individual’s last email | encoded | sgba-p12-misc |  |
| s64(3) | 4139-4142 | (3) A document permitted or required by this Act to be serve | encoded | sgba-p12-misc |  |
| s64(3)(a) | 4143-4145 | (a) by giving it to any partner or other similar officer of  | encoded | sgba-p12-misc |  |
| s64(3)(b) | 4146-4148 | (b) by leaving it at, or by sending it by prepaid registered | encoded | sgba-p12-misc |  |
| s64(3)(c) | 4149-4151 | (c) by sending it by fax to the fax number used at the | encoded | sgba-p12-misc |  |
| s64(3)(d) | 4152-4157 | (d) by sending it by email to the partnership’s last email | encoded | sgba-p12-misc |  |
| s64(4) | 4158-4161 | (4) A document permitted or required by this Act to be serve | encoded | sgba-p12-misc |  |
| s64(4)(a) | 4162-4165 | (a) by giving it to the secretary or other similar officer o | encoded | sgba-p12-misc |  |
| s64(4)(b) | 4166-4169 | (b) by leaving it at, or by sending it by prepaid registered | encoded | sgba-p12-misc |  |
| s64(4)(c) | 4170-4173 | (c) by sending it by fax to the fax number used at the body | encoded | sgba-p12-misc |  |
| s64(4)(d) | 4174-4176 | (d) by sending it by email to the body corporate’s or | encoded | sgba-p12-misc |  |
| s64(5) | 4177-4180 | (5) In addition, a document permitted or required by this Ac | encoded | sgba-p12-misc |  |
| s64(5)(a) | 4181-4188 | (a) by giving an electronic notice to the individual, | encoded | sgba-p12-misc |  |
| s64(5)(b) | 4189-4196 | (b) where by the exercise of reasonable diligence, the name  | encoded | sgba-p12-misc |  |
| s64(5)(c) | 4197-4204 | (c) by any other method authorised by the regulations for th | encoded | sgba-p12-misc |  |
| s64(6) | 4205-4206 | (6) Service of a document under this section takes effect — | encoded | sgba-p12-misc |  |
| s64(6)(a) | 4207-4210 | (a) if the document is sent by fax and a notification of | encoded | sgba-p12-misc |  |
| s64(6)(b) | 4211-4214 | (b) if the document is sent by email — at the time that the | encoded | sgba-p12-misc |  |
| s64(6)(c) | 4215-4218 | (c) if the document is sent by prepaid registered post — 2 d | encoded | sgba-p12-misc |  |
| s64(6)(d) | 4219-4222 | (d) if the document is posted on a website mentioned in | encoded | sgba-p12-misc |  |
| s64(7) | 4223-4227 | (7) However, service of any document under this Act on a per | encoded | sgba-p12-misc |  |
| s64(8) | 4228-4230 | (8) This section does not apply to documents to be served in | encoded | sgba-p12-misc |  |
| s64(9) | 4231-4236 | (9) In this section — | encoded | sgba-p12-misc |  |
| s64(9)(a) | 4237-4240 | (a) in the case of an individual, the individual’s usual or | encoded | sgba-p12-misc |  |
| s64(9)(b) | 4241-4273 | (b) in the case of a partnership (other than a limited | encoded | sgba-p12-misc |  |
| s64A:heading | 4274-4275 | Financial penalties, etc., payable to Consolidated Fund | inert (1) not operative |  | heading, not operative |
| s64A | 4276-4278 | 64A. All fines imposed under section 12(1) and all financial | encoded | sgba-p12-misc |  |
| s64A(a) | 4279-4282 | (a) may be recovered by the Authority in any court of | encoded | sgba-p12-misc |  |
| s64A(b) | 4283-4286 | (b) must be paid into the Consolidated Fund. | encoded | sgba-p12-misc |  |
| s65:heading | 4287-4288 | Amendment of First, Second and Third Schedules | inert (1) not operative |  | heading, not operative |
| s65(1) | 4289-4291 | 65.—(1) The Minister may, by notification in the Gazette, at | encoded | sgba-p12-misc |  |
| s65(2) | 4292-4295 | (2) The Minister may, in any notification made under | encoded | sgba-p12-misc |  |
| s66:heading | 4296-4297 | Regulations | inert (1) not operative |  | heading, not operative |
| s66 | 4298-4303 | 66. The Authority may, with the approval of the Minister, ma | encoded | sgba-p12-misc |  |
| s66(a) | 4304-4305 | (a) required or permitted to be prescribed by this Act; and | encoded | sgba-p12-misc |  |
| s66(b) | 4306-4308 | (b) necessary or convenient to be prescribed for carrying ou | encoded | sgba-p12-misc |  |
| s67 | 4309-4310 | 67. [Repealed by Act 22 of 2016] | repealed or blank in this text |  | text reads: 67. [Repealed by Act 22 of 2016] |
| s68:heading | 4311-4312 | Transitional and saving provisions | inert (1) not operative |  | heading, not operative |
| s68(1) | 4313-4317 | 68.—(1) All acts done by the Singapore Broadcasting Authorit | encoded | sgba-p12-misc |  |
| s68(2) | 4318-4325 | (2) Any decision, document, licence, consent, approval or | encoded | sgba-p12-misc |  |
| s68(3) | 4326-4330 | (3) Where anything has been commenced by or on behalf of the | encoded | sgba-p12-misc |  |
| s68(4) | 4331-4336 | (4) Despite the repeal of Part XI of the Singapore Broadcast | encoded | sgba-p12-misc |  |
| s68(5) | 4337-4341 | (5) In this section, “broadcasting successor companies” mean | encoded | sgba-p12-misc |  |
| sch-first:heading | 4342-4346 | first schedule heading and title | inert (1) not operative |  | heading, not operative |
| sch-first:item-1 | 4347-4353 | item 1 | encoded | sgba-sched |  |
| sch-first:interpretation | 4354-4358 | interpretation paragraph | encoded | sgba-sched |  |
| sch-second:heading | 4359-4363 | second schedule heading and title | inert (1) not operative |  | heading, not operative |
| sch-second:item-1 | 4364-4364 | item 1 | encoded | sgba-sched |  |
| sch-second:item-2 | 4365-4365 | item 2 | encoded | sgba-sched |  |
| sch-second:item-3 | 4366-4366 | item 3 | encoded | sgba-sched |  |
| sch-second:item-4 | 4367-4367 | item 4 | encoded | sgba-sched |  |
| sch-second:item-5 | 4368-4368 | item 5 | encoded | sgba-sched |  |
| sch-second:item-6 | 4369-4369 | item 6 | encoded | sgba-sched |  |
| sch-second:item-7 | 4370-4370 | item 7 | encoded | sgba-sched |  |
| sch-second:item-8 | 4371-4371 | item 8 | encoded | sgba-sched |  |
| sch-second:item-9 | 4372-4372 | item 9 | encoded | sgba-sched |  |
| sch-second:item-10 | 4373-4373 | item 10 | encoded | sgba-sched |  |
| sch-second:item-11 | 4374-4374 | item 11 | encoded | sgba-sched |  |
| sch-second:item-12 | 4375-4375 | item 12 | encoded | sgba-sched |  |
| sch-second:item-13 | 4376-4376 | item 13 | encoded | sgba-sched |  |
| sch-second:item-14 | 4377-4377 | item 14 | encoded | sgba-sched |  |
| sch-second:item-15 | 4378-4378 | item 15 | encoded | sgba-sched |  |
| sch-second:item-16 | 4379-4379 | item 16 | encoded | sgba-sched |  |
| sch-second:item-17 | 4380-4380 | item 17 | encoded | sgba-sched |  |
| sch-second:item-18 | 4381-4381 | item 18 | encoded | sgba-sched |  |
| sch-second:item-19 | 4382-4382 | item 19 | encoded | sgba-sched |  |
| sch-second:item-20 | 4383-4383 | item 20 | encoded | sgba-sched |  |
| sch-second:interpretation | 4384-4390 | interpretation paragraph | encoded | sgba-sched |  |
| sch-third:heading | 4391-4400 | third schedule heading and title | encoded | sgba-sched | the heading and column headings (4391-4399) are not operative; the first provider named in the table (4400) is encoded |
| sch-third:row-1 | 4401-4403 | table row 1 (service; providers (a) and (b)) | encoded | sgba-sched |  |
| sch-fourth:heading | 4404-4408 | fourth schedule heading and title | inert (1) not operative |  | heading, not operative |
| sch-fourth:part-1 | 4409-4410 | Part heading | inert (1) not operative |  | heading, not operative |
| sch-fourth:part-1-item-1 | 4411-4411 | item 1 | encoded | sgba-p1-online |  |
| sch-fourth:part-1-item-2 | 4412-4413 | item 2 | encoded | sgba-p1-online |  |
| sch-fourth:part-2 | 4414-4417 | Part heading | inert (1) not operative |  | heading, not operative |
| sch-fourth:p2-item-1 | 4418-4419 | item 1 (definitions chapeau) | encoded | sgba-p1-online |  |
| sch-fourth:def:app | 4420-4423 | app | encoded | sgba-p1-online |  |
| sch-fourth:def:app distribution service | 4424-4431 | app distribution service | encoded | sgba-p1-online |  |
| history:legislative-history | 4432-4775 | Legislative History (the text says it is not part of the Act | inert (1) not operative |  | the text says it is not part of the Act; used only as a lead (BA1994.txt:4645-4648, F-BA-08) |


Totals: 842 rows; encoded 709; fork 8; inert (1) not operative 121; inert (2) machinery 1; repealed or blank in this text 3
Every one of the 3380 non-blank lines of the text is in exactly one row (201 of them page furniture, kept in the row they sit in).

### Instruments made under the Act

One row per instrument found, whether or not a text could be deposited.
Thirty-one instrument deposits are in hand: twelve are lawplain's rendering, line-broken by hand, a secondary source (each its own subject under `subjects/sg/`, with `SOURCE-LICENSE.md`, `meta.json` and `subject.json`), and nineteen are e-Gazette PDFs, `pdftotext -layout`, unedited, each with a `.meta.json` beside the text; seventeen of those are their own subjects and two (the as-made S 523/2010 with its Schedule, and the Exemption Order of the 2004 Revised Edition) are further deposits in the subjects of lawplain rows.
A quotation in an instrument module is checked against that instrument's own deposit (`srcrefs.py check --strict`), 0 problems on each.

| row | instrument | made under | deposit | module | tests | disposition | note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RG3 | Broadcasting (TVRO System) Regulations (G.N. S 126/1991; Rg 3, 2004 Revised Edition, amendments shown to S 354/2001) | s 66 | `../../../broadcasting-tvro-system-regulations-1991/registers/source-bundle/BA1994-RG3.txt` | `sgba-i-tvro-regs.l4` | `sgba-tests-instruments-tv.l4` | encoded | regs 2 to 14 quoted and encoded; reg 1 (citation), headings and the amendment note are not quoted (inert 1 and 2); F-BA-05 |
| RG2 | Broadcasting (Composition of Offences) Regulations (G.N. S 332/2004; Rg 2, 2007 Revised Edition) | s 57(2) | `../../../broadcasting-composition-of-offences-regulations-2004/registers/source-bundle/BA1994-RG2.txt` | `sgba-i-composition.l4` | `sgba-tests-instruments-tv.l4` | encoded | reg 2 quoted and encoded; reg 1 (citation) and the heading are not quoted (inert 1 and 2) |
| N1 | Broadcasting (Class Licence) Notification (G.N. S 306/1996; N 1, 2004 Revised Edition, amended to S 478/2020) | s 9 | `../../../broadcasting-class-licence-notification-1996/registers/source-bundle/BA1994-N1.txt` | `sgba-i-class-licence.l4` | `sgba-tests-instruments-licensing.l4` | encoded | paras 2 to 5 quoted and encoded; para 1 (citation), headings and amendment notes are not quoted; the Schedule is a separate row below |
| S477 | Broadcasting (Class Licence - Broadcasting to Digital Display Panels) Notification 2020 (S 477/2020) | s 9 | `../../../broadcasting-class-licence-digital-display-panels-notification-2020/registers/source-bundle/BA1994-S477-2020.txt` | `sgba-i-digital-panels.l4` | `sgba-tests-instruments-licensing.l4` | encoded | paras 2 to 5 quoted and encoded; para 1 (citation and commencement), headings and the signature block are not quoted |
| OR1 | Broadcasting (Exemption) Order (G.N. S 307/1996; O 1, 2004 Revised Edition, amended by S 600/2014) | s 60 | `../../../broadcasting-exemption-order-1996/registers/source-bundle/BA1994-OR1.txt` | `sgba-i-exempt-1996.l4` | `sgba-tests-instruments-licensing.l4` | encoded | para 1(a) to (g) quoted and encoded; para 2 reads "[ Deleted by S 600/2014 wef 15/09/2014 ]" (repealed or blank in this text) |
| OR2 | Broadcasting (Exemption) (No. 2) Order (G.N. S 591/2002; O 2, 2004 Revised Edition, amended by S 212/2022) | s 60(b) | `../../../broadcasting-exemption-no-2-order-2002/registers/source-bundle/BA1994-OR2.txt` | `sgba-i-exempt-no2.l4` | `sgba-tests-instruments-licensing.l4` | encoded | para 2 quoted and encoded; item (a) reads "[ Deleted by S 212/2022 wef 25/03/2022 ]" (repealed or blank in this text); para 1 (citation) not quoted; the Order that deleted (a) is deposited and encoded (row S212_22), and the text of O 2 before it is not held |
| OR3 | Broadcasting (Exemption) (No. 3) Order (G.N. S 378/2004; O 3, 2007 Revised Edition) | s 60(b) | `../../../broadcasting-exemption-no-3-order-2004/registers/source-bundle/BA1994-OR3.txt` | `sgba-i-exempt-no3.l4` | `sgba-tests-instruments-licensing.l4` | encoded | para 2 quoted and encoded; para 1 (citation) not quoted |
| S121 | Broadcasting (Exemption) Order 2008 (S 121/2008) | s 60 | `../../../broadcasting-exemption-order-2008/registers/source-bundle/BA1994-S121-2008.txt` | `sgba-i-exempt-2008.l4` | `sgba-tests-instruments-licensing.l4` | encoded | para 2(1) and (2) quoted and encoded; para 1 (citation and commencement) and the signature block are not quoted |
| S211 | Broadcasting (Exemption) Order 2022 (S 211/2022) | s 60 | `../../../broadcasting-exemption-order-2022/registers/source-bundle/BA1994-S211-2022.txt` | `sgba-i-exempt-2022.l4` | `sgba-tests-instruments-licensing.l4` | encoded | para 2(a) and (b) quoted and encoded; para 1 (citation and commencement, deemed from 4 February 2022) and the signature block are not quoted |
| S523 | Broadcasting (Exemption of Broadcasting Services by Educational Institutions) Order 2010 (S 523/2010) | s 60 | `../../../broadcasting-exemption-educational-institutions-order-2010/registers/source-bundle/BA1994-S523-2010.txt` | `sgba-i-exempt-educ.l4` | `sgba-tests-instruments-licensing.l4` | encoded | paras 2 to 5 quoted and encoded; para 1 (citation and commencement), headings and the signature block are not quoted; the Schedule is a separate row below |
| S30 | Broadcasting (Service of Documents Website) Notification 2023 (S 30/2023) | s 64(5)(b) | `../../../broadcasting-service-of-documents-website-notification-2023/registers/source-bundle/BA1994-S30-2023.txt` | `sgba-i-service-website.l4` | `sgba-tests-instruments-licensing.l4` | encoded | para 2 quoted and encoded; para 1 (citation and commencement) and the signature block are not quoted |
| S47 | Broadcasting (Online Codes of Practice Procedure) Rules 2023 (S 47/2023) | s 45L(2) | `../../../broadcasting-online-codes-of-practice-procedure-rules-2023/registers/source-bundle/BA1994-S47-2023.txt` | `sgba-i-online-cop-rules.l4` | `sgba-tests-instruments-licensing.l4` | encoded | rules 2 to 6 quoted and encoded; rule 1 (citation and commencement), headings and the signature block are not quoted |
| S549 | Broadcasting Act (Amendment of First Schedule) Notification 2012 (S 549/2012; made 30 October 2012, first published 31 October 2012, deemed in operation from 1 January 2011) | s 65 | `../../../broadcasting-amendment-of-first-schedule-notification-2012/registers/source-bundle/BA1994-S549-2012.txt` | `sgba-i-s549-2012.l4` | `sgba-tests-versions.l4` | encoded | paragraphs 1 and 2 quoted and encoded as a version row with two dates; e-Gazette text, not lawplain; F-BA-08 resolved |
| S559 | Broadcasting Act (Amendment of Third Schedule) Notification 2010 (S 559/2010; made 28 September 2010, first published 30 September 2010, in operation from 1 October 2010) | s 65 | `../../../broadcasting-amendment-of-third-schedule-notification-2010/registers/source-bundle/BA1994-S559-2010.txt` | `sgba-i-s559-2010.l4` | `sgba-tests-versions.l4` | encoded | paragraphs 1 and 2 quoted and encoded as a version row with two dates; e-Gazette text, not lawplain |
| RG1 | Broadcasting (Television and Radio Licensing) Regulations (Rg 1, 2004 Revised Edition, 29.2.2004; G.N. S 21/80, amended to S 212/99) | s 66 | `../../../broadcasting-television-and-radio-licensing-regulations/registers/source-bundle/BA1994-RG1.txt` | `sgba-i-rg1.l4` | `sgba-tests-rg1.l4` | encoded | e-Gazette text; regs 2, 4 to 37 and 39 and both Schedules quoted and encoded as printed (reg 17(3), the meaning of "sale", is quoted with reg 17 but is not a separate rule), with the version row; reg 1 (citation), reg 3 (licensing authority), reg 38 (forms) and reg 2(2) (interpretation) not encoded (inert 1 and 2); F-BA-10, F-BA-12 |
| S333 | Broadcasting (Television and Radio Licensing) (Amendment) Regulations 2004 (S 333/2004; published 15 June 2004, in operation 21 June 2004) | s 66 | `../../../broadcasting-television-and-radio-licensing-amendment-regulations-2004/registers/source-bundle/BA1994-S333-2004.txt` | `sgba-i-s333-2004.l4` | `sgba-tests-rg1.l4` | encoded | e-Gazette text; every substituted or new provision encoded (regs 2, 5, 6, 8, 15, 16, 23, 27, 28, 29A, 31, 33, 36, 37 and the Second Schedule), deletions and the renaming of the licensing authority recorded in comments; version row; F-BA-11, R-4 |
| S548 | Broadcasting (Television and Radio Licensing) (Revocation) Regulations 2012 (S 548/2012; published 31 October 2012 at 5.00 pm, deemed in operation from 1 January 2011) | s 66 | `../../../broadcasting-television-and-radio-licensing-revocation-regulations-2012/registers/source-bundle/BA1994-S548-2012.txt` | `sgba-i-s548-2012.l4` | `sgba-tests-rg1.l4` | encoded | e-Gazette text; regs 1 and 2 quoted and encoded: the version row on two dates, the savings of reg 2(2)(a) to (c) and the refund of reg 2(3); validity of the retrospective revocation not addressed |
| S212_99 | Singapore Broadcasting Authority (Broadcasting and Television) (Amendment) Regulations 1999 (S 212/1999; published 14 May 1999, in operation the same day) | s 79 of the Singapore Broadcasting Authority Act (Cap. 297) | `../../../singapore-broadcasting-authority-broadcasting-and-television-amendment-regulations-1999/registers/source-bundle/BA1994-S212-1999.txt` | `sgba-i-s212-1999.l4` | `sgba-tests-rg1.l4` | encoded | e-Gazette text; para 2 (reg 8 amended) quoted; only the amended words are printed, so the rule is the power to waive or reduce from 14 May 1999 |
| S354 | Singapore Broadcasting Authority (TVRO System) (Amendment) Regulations 2001 (S 354/2001; published 23 July 2001, in operation 1 August 2001) | s 79 of the Singapore Broadcasting Authority Act (Cap. 297) | `../../../singapore-broadcasting-authority-tvro-system-amendment-regulations-2001/registers/source-bundle/BA1994-S354-2001.txt` | `sgba-i-s354-2001.l4` | `sgba-tests-rg1.l4` | encoded | e-Gazette text; every substituted regulation encoded (2, 3, 4, 5, 8, 9); para 5 (wording changes) in a comment; reg 3(2), the institution-only rule, dates from 1 August 2001 |
| S600 | Broadcasting (Exemption) (Amendment) Order 2014 (S 600/2014; published 15 September 2014, in operation the same day) | s 60 | `../../../broadcasting-exemption-amendment-order-2014/registers/source-bundle/BA1994-S600-2014.txt` | `sgba-i-s600-2014.l4` | `sgba-tests-amendments.l4` | encoded | e-Gazette text; paras 2 and 3 encoded |
| OR1_04 | Broadcasting (Exemption) Order (O 1, 2004 Revised Edition, 29.2.2004), before S 600/2014 | s 60 | `../../../broadcasting-exemption-order-1996/registers/source-bundle/BA1994-OR1.20040229.txt` | `sgba-i-or1-2004.l4` | `sgba-tests-amendments.l4` | encoded | e-Gazette text; only paras 1(f) and 2, which S 600/2014 changed, are encoded; the rest reads the same as the lawplain row OR1 |
| S523_G | Broadcasting (Exemption of Broadcasting Services by Educational Institutions) Order 2010 (S 523/2010) as made, with its Schedule | s 60 | `../../../broadcasting-exemption-educational-institutions-order-2010/registers/source-bundle/BA1994-S523-2010.20100916.txt` | `sgba-i-s523-2010-schedule.l4` | `sgba-tests-amendments.l4` | encoded | e-Gazette text; the Schedule (items 1 to 3) encoded; the lawplain text, which has no Schedule, is row S523 |
| S478 | Broadcasting (Class Licence) (Amendment) Notification 2020 (S 478/2020; published 22 June 2020, in operation the same day) | s 9 | `../../../broadcasting-class-licence-amendment-notification-2020/registers/source-bundle/BA1994-S478-2020.txt` | `sgba-i-s478-2020.l4` | `sgba-tests-amendments.l4` | encoded | e-Gazette text; para 2 (N 1 para 3A(4)) encoded |
| S196 | Broadcasting (Class Licence) (Amendment) Notification 2004 (S 196/2004; published 15 April 2004, in operation the same day) | ss 9 and 11 | `../../../broadcasting-class-licence-amendment-notification-2004/registers/source-bundle/BA1994-S196-2004.txt` | `sgba-i-s196-2004.l4` | `sgba-tests-amendments.l4` | encoded | e-Gazette text; para 2 (Schedule para 11A) encoded; not named in the amendment notes of the lawplain text of N 1 |
| S555 | Broadcasting (Class Licence) (Amendment) Notification 2003 (S 555/2003; published 28 November 2003, in operation 1 December 2003) | ss 9 and 11 | `../../../broadcasting-class-licence-amendment-notification-2003/registers/source-bundle/BA1994-S555-2003.txt` | `sgba-i-s555-2003.l4` | `sgba-tests-amendments.l4` | encoded | e-Gazette text; Schedule paras 9 and 9A encoded; the cross-reference corrections are recorded in a comment |
| S496 | Singapore Broadcasting Authority (Class Licence) (Amendment) Notification 2001 (S 496/2001; published 8 October 2001, in operation 10 October 2001) | ss 21 and 23 of the Singapore Broadcasting Authority Act (Cap. 297) | `../../../singapore-broadcasting-authority-class-licence-amendment-notification-2001/registers/source-bundle/BA1994-S496-2001.txt` | `sgba-i-s496-2001.l4` | `sgba-tests-amendments.l4` | encoded | e-Gazette text; Schedule paras 2A and 5 encoded; the deletion in para 3 and the wording change in para 6 are recorded in comments |
| S70 | Broadcasting (Class Licence) (Amendment) Notification 2012 (S 70/2012; published 23 February 2012, in operation the same day) | ss 9 and 11 | `../../../broadcasting-class-licence-amendment-notification-2012/registers/source-bundle/BA1994-S70-2012.txt` | `sgba-i-s70-2012.l4` | `sgba-tests-amendments.l4` | encoded | e-Gazette text; Schedule para 2A encoded (replaced by S 674/2016 from 28 December 2016); the wording changes to paras 15(f) and (g) are recorded in comments; not named in the amendment notes of the lawplain text of N 1 |
| S330 | Broadcasting (Class Licence) (Amendment) Notification 2013 (S 330/2013; published 29 May 2013, in operation 1 June 2013) | ss 9 and 11 | `../../../broadcasting-class-licence-amendment-notification-2013/registers/source-bundle/BA1994-S330-2013.txt` | `sgba-i-s330-2013.l4` | `sgba-tests-amendments.l4` | encoded | e-Gazette text; paras 2 and 3 (N 1 paras 3 and 3A) encoded |
| S674 | Broadcasting (Class Licence) (Amendment) Notification 2016 (S 674/2016; published 27 December 2016, in operation 28 December 2016) | ss 9 and 11 | `../../../broadcasting-class-licence-amendment-notification-2016/registers/source-bundle/BA1994-S674-2016.txt` | `sgba-i-s674-2016.l4` | `sgba-tests-amendments.l4` | encoded | e-Gazette text; Schedule para 2A as substituted encoded; not named in the amendment notes of the lawplain text of N 1 |
| S212_22 | Broadcasting (Exemption) (No. 2) (Amendment) Order 2022 (S 212/2022; made 22 March 2022, first published 25 March 2022 at 5 pm, in operation 25 March 2022) | s 60 | `../../../broadcasting-exemption-no-2-amendment-order-2022/registers/source-bundle/BA1994-S212-2022.txt` | `sgba-i-s212-2022.l4` | `sgba-tests-versions-acts.l4` | encoded | e-Gazette text; para 2 (sub-paragraph (a) of paragraph 2 of O 2 deleted) encoded, and O 2 read on two days (`sgba-versions-acts.l4`); the Order has no commencement clause, so it takes effect on its publication day under the Interpretation Act (assumed, not ruled); para 1 (citation) and the signature block are not quoted; no receiver is within O 2 |
| S738 | Broadcasting Act 1994 (Amendment of Fourth Schedule) Order 2024 (S 738/2024; made 18 September 2024, first published 24 September 2024 at 5 pm, in operation 25 September 2024, the day the Order states) | s 2B(1) | `../../../broadcasting-act-1994-amendment-of-fourth-schedule-order-2024/registers/source-bundle/BA1994-S738-2024.txt` | `sgba-versions-later.l4` | `sgba-tests-versions-later.l4` | encoded | e-Gazette text; paras 1 and 2 quoted; the Fourth Schedule read on two days (the Act 38 of 2022 item and the Order's Parts 1 and 2); the schedule itself is encoded on the 2024 text in `sgba-sched.l4`; no receiver is within it |
| N1 Schedule | Schedule to the Class Licence Notification (the conditions of the class licence, referred to in paras 4 and 5); the original text of the Schedule is not in hand, but six notifications that amended it (S 496/2001, S 555/2003, S 196/2004, S 70/2012, S 674/2016, and S 330/2013 for paragraph 3) are deposited and encoded | s 9 | not in the text lawplain served | | | source not obtained | Looked: lawplain (2026-11-03): the corpus holds 12 documents under parent BA1994 (a search with parent_act_id BA1994), all deposited, none of them this one; a get_document on S 549/2012 was answered HTTP 404 (not found). egazette.gov.sg: robots.txt disallows /search, the browse page is a client-rendered application, the sitemap lists 7 pages and no instruments; nothing fetched. SSO: see "The single SSO attempt". IMDA (imda.gov.sg): pages client-rendered, no text returned. |
| S 308/1996 | Singapore Broadcasting Authority Act (Amendment of Second Schedule) Notification 1996 (history item 8, commencement 15 July 1996; the Act's former name) | the power to amend the Schedules (now s 65(1)) | none | | | source not obtained | Looked: lawplain (2026-11-03): the corpus holds 12 documents under parent BA1994 (a search with parent_act_id BA1994), all deposited, none of them this one; a get_document on S 549/2012 was answered HTTP 404 (not found). egazette.gov.sg: robots.txt disallows /search, the browse page is a client-rendered application, the sitemap lists 7 pages and no instruments; nothing fetched. SSO: see "The single SSO attempt". IMDA (imda.gov.sg): pages client-rendered, no text returned. |
| Rg 1 earlier history | G.N. S 21/80 (the original Television and Radio Licensing Regulations) and the amendments S 46/83, S 52/83, S 314/83, S 151/87, S 105/88, S 404/90, S 125/91, S 525/93, S 87/95, S 214/95 and S 291/96, named in the history line of the Revised Edition 2004 of Rg 1 (only S 212/99 was obtained, and S 333/2004 after the edition) | s 66 (and, before 1 January 2003, s 79 of the Singapore Broadcasting Authority Act) | none | | | source not obtained | Looked: lawplain (2026-11-03): the corpus holds 12 documents under parent BA1994 (a search with parent_act_id BA1994), all deposited, none of them this one; a get_document on S 549/2012 was answered HTTP 404 (not found). egazette.gov.sg: robots.txt disallows /search, the browse page is a client-rendered application, the sitemap lists 7 pages and no instruments; nothing fetched. SSO: see "The single SSO attempt". IMDA (imda.gov.sg): pages client-rendered, no text returned. |
| Codes of Practice | the Codes of Practice issued by the Authority under s 6 and the online Codes of Practice under s 45L(1), if any (none was in any source) | ss 6 and 45L(1) | none | | | source not obtained | Looked: lawplain (2026-11-03): the corpus holds 12 documents under parent BA1994 (a search with parent_act_id BA1994), all deposited, none of them this one; a get_document on S 549/2012 was answered HTTP 404 (not found). egazette.gov.sg: robots.txt disallows /search, the browse page is a client-rendered application, the sitemap lists 7 pages and no instruments; nothing fetched. SSO: see "The single SSO attempt". IMDA (imda.gov.sg): pages client-rendered, no text returned. |
| Part 10A regulations | regulations under s 45P(1) (none was found) | s 45P(1) | none | | | source not obtained | Looked: lawplain (2026-11-03): the corpus holds 12 documents under parent BA1994 (a search with parent_act_id BA1994), all deposited, none of them this one; a get_document on S 549/2012 was answered HTTP 404 (not found). egazette.gov.sg: robots.txt disallows /search, the browse page is a client-rendered application, the sitemap lists 7 pages and no instruments; nothing fetched. SSO: see "The single SSO attempt". IMDA (imda.gov.sg): pages client-rendered, no text returned. |
| s 20(4) exemptions | exemptions of a person, apparatus or class of apparatus from s 20(1), if the Authority gave any (none was found in any source) | s 20(4) | none | | | source not obtained | Looked: lawplain (2026-11-03): the corpus holds 12 documents under parent BA1994 (a search with parent_act_id BA1994), all deposited, none of them this one; a get_document on S 549/2012 was answered HTTP 404 (not found). egazette.gov.sg: robots.txt disallows /search, the browse page is a client-rendered application, the sitemap lists 7 pages and no instruments; nothing fetched. SSO: see "The single SSO attempt". IMDA (imda.gov.sg): pages client-rendered, no text returned. |
| ss 29 and 31 instruments | orders under s 29 proscribing a foreign broadcasting service, and approvals and declarations under s 31, if any (none was found in any source) | ss 29 and 31 | none | | | source not obtained | Looked: lawplain (2026-11-03): the corpus holds 12 documents under parent BA1994 (a search with parent_act_id BA1994), all deposited, none of them this one; a get_document on S 549/2012 was answered HTTP 404 (not found). egazette.gov.sg: robots.txt disallows /search, the browse page is a client-rendered application, the sitemap lists 7 pages and no instruments; nothing fetched. SSO: see "The single SSO attempt". IMDA (imda.gov.sg): pages client-rendered, no text returned. |

Totals, instruments: 38 rows; encoded 31; source not obtained 7.

### Amending Acts and Orders after the Revised Edition 2003, and the notifications that brought them into operation

The legislative history of the 2024 consolidation lists, after the Revised Edition 2003, Act 55 of 2004, Act 10 of 2005, Act 21 of 2005, S 559/2010, S 549/2012, Act 15 of 2010, the Revised Edition 2012, Act 22 of 2016, the 2020 Revised Edition, S 26/2022, Act 25 of 2021, Act 31 of 2022, Act 38 of 2022, Act 4 of 2008 and S 738/2024; `The legislative history, item by item` above gives the status of each.
The rows for Acts 55 of 2004, 21 of 2005, 15 of 2010, 38 of 2022 and 4 of 2008, their commencement notifications (S 750/2004, S 878/2005, S 776/2010, S 29/2023, S 128/2008, S 129/2008, S 244/2024) and S 250/2022, and the 2020 Revised Edition, are e-Gazette deposits of this encoding (each its own subject, or an edition in the Act's own source bundle, `pdftotext -layout`, unedited); the eight rows for Act 10 of 2005, Act 22 of 2016, Act 25 of 2021, Act 31 of 2022, S 26/2022 and the notifications S 76/2005, S 461/2016 and S 850/2022 are deposits of the Telecommunications Act encoder, used from where they are and cited from there, not copied; S 559/2010, S 549/2012 and S 738/2024 are in the instruments table.

| row | text | deposit | module | tests | disposition | note |
| --- | --- | --- | --- | --- | --- | --- |
| ACT55 | Broadcasting (Amendment) Act 2004 (Act 55 of 2004; passed 16 November 2004, assented 29 November 2004, first published 14 December 2004; Acts Supplement No. 58 of 2004) | `../../../broadcasting-amendment-act-2004/registers/source-bundle/BA1994-ACT55-2004.txt` | `sgba-versions-acts.l4` | `sgba-tests-versions-acts.l4` | encoded | e-Gazette text; s 1 and s 2 quoted; s 2 (section 48 repealed and re-enacted, new section 48A) encoded as a two-date version: the Revised Edition 2003 s 48 before 1 January 2005, the new s 48 and s 48A from then; off the receiver chain (decoders) |
| S750_04 | Broadcasting (Amendment) Act (Commencement) Notification 2004 (S 750/2004; made 9 December 2004, first published 17 December 2004) | `../../../broadcasting-amendment-act-commencement-notification-2004/registers/source-bundle/BA1994-S750-2004.txt` | `sgba-versions-acts.l4` | `sgba-tests-versions-acts.l4` | encoded | e-Gazette text; para 2 quoted and encoded: Act 55 of 2004 in operation on 1 January 2005; para 1 (citation) not quoted |
| ACT21 | Companies (Amendment) Act 2005 (Act 21 of 2005; passed 16 May 2005, assented 31 May 2005, first published 6 June 2005; Acts Supplement No. 18 of 2005) | `../../../companies-amendment-act-2005/registers/source-bundle/BA1994-ACT21-2005.txt` | `sgba-versions-acts.l4` | `sgba-tests-versions-acts.l4` | encoded | e-Gazette text; the whole Act is deposited, and s 1, s 58 and item (3) of the Schedule (Broadcasting Act s 35(3): "nominal amount of" replaced by "total votes attached to") are quoted and encoded as a two-date version; the only place in the Act that names the Broadcasting Act; off the receiver chain |
| S878_05 | Companies (Amendment) Act (Commencement) Notification 2005 (S 878/2005; made 21 December 2005, first published 30 December 2005) | `../../../companies-amendment-act-commencement-notification-2005/registers/source-bundle/BA1994-S878-2005.txt` | `sgba-versions-acts.l4` | `sgba-tests-versions-acts.l4` | encoded | e-Gazette text; para 2 quoted and encoded: Act 21 of 2005 in operation on 30 January 2006; para 1 (citation) not quoted |
| ACT15 | Criminal Procedure Code 2010 (Act 15 of 2010, as enacted; passed 19 May 2010, assented 10 June 2010, first published 21 June 2010; Acts Supplement No. 13 of 2010) | `../../../criminal-procedure-code-2010-act-as-enacted/registers/source-bundle/BA1994-ACT15-2010.txt` | `sgba-versions-acts.l4` | `sgba-tests-versions-acts.l4` | encoded | e-Gazette text; the whole Code as enacted is deposited, and s 1(2), s 429(2)(a), s 430 and item 8 of the Sixth Schedule (Broadcasting Act s 55: ", with the authorisation of the Public Prosecutor," inserted) are quoted and encoded as a two-date version; the only place in the Code that names the Broadcasting Act; touches the procedure for a s 47 offence, not its elements or penalty (fork F-BA-13) |
| S776_10 | Criminal Procedure Code (Commencement) Notification 2010 (S 776/2010; made 20 December 2010, first published 20 December 2010) | `../../../criminal-procedure-code-commencement-notification-2010/registers/source-bundle/BA1994-S776-2010.txt` | `sgba-versions-acts.l4` | `sgba-tests-versions-acts.l4` | encoded | e-Gazette text; para 2 quoted and encoded: the Code in operation on 2 January 2011; para 1 (citation) not quoted |
| ACT10 | Telecommunications (Amendment) Act 2005 (Act 10 of 2005; first published 16 February 2005), section 32 only (it repeals and re-enacts section 26 of the Broadcasting Act) | `../../../telecommunications-act-1999/registers/source-bundle/TA1999.ACT10-2005.txt` | `sgba-versions-later.l4` | `sgba-tests-versions-later.l4` | encoded | deposited by the Telecommunications Act encoder and cited from there, not copied; s 32 quoted and encoded as a two-date version (s 26(1) the same in both texts; s 26(2) a new power from 16 February 2005); the rest of the Act is the Telecommunications Act's; off the receiver chain |
| S76_05 | Telecommunications (Amendment) Act (Commencement) Notification 2005 (S 76/2005; first published 16 February 2005) | `../../../telecommunications-act-1999/registers/source-bundle/TA1999.S76-2005.txt` | `sgba-versions-later.l4` | `sgba-tests-versions-later.l4` | encoded | deposited by the Telecommunications Act encoder; para 2 quoted: the Act in operation on 16 February 2005 except ss 10 and 11 |
| ACT22 | Info-communications Media Development Authority Act 2016 (Act 22 of 2016; first published 29 September 2016), section 93 only (nine amendments to the Broadcasting Act) | `../../../telecommunications-act-1999/registers/source-bundle/TA1999.ACT22-2016.txt` | `sgba-versions-later.l4` | `sgba-tests-versions-later.l4` | encoded | deposited by the Telecommunications Act encoder; s 93(a) to (i) quoted and each encoded as a two-date wording (the definitions of Authority, Chairman, chief executive and the Info-communications Development Authority of Singapore, s 12(3), s 22(f), s 23 repealed, ss 52(1) and 55, s 57(3) deleted, s 67 repealed); none is on the receiver chain |
| S461_16 | Info-communications Media Development Authority Act 2016 (Commencement) Notification 2016 (S 461/2016; first published 29 September 2016) | `../../../telecommunications-act-1999/registers/source-bundle/TA1999.S461-2016.txt` | `sgba-versions-later.l4` | `sgba-tests-versions-later.l4` | encoded | deposited by the Telecommunications Act encoder; para 2 quoted: the Act in operation on 1 October 2016 except ss 89, 90(1) and 96(v) |
| ACT25 | Courts (Civil and Criminal Justice) Reform Act 2021 (Act 25 of 2021), section 84 only ("in execution" in s 61(1) replaced) | `../../../telecommunications-act-1999/registers/source-bundle/TA1999.ACT25-2021.txt` | `sgba-versions-later.l4` | `sgba-tests-versions-later.l4` | encoded | deposited by the Telecommunications Act encoder; s 84 quoted and encoded as a two-date wording; it was brought into operation on 1 April 2022 by S 250/2022 (deposited here, row S250_22), which excepts a list of sections not including s 84; off the receiver chain |
| ACT31 | Statutes (Miscellaneous Amendments) Act 2022 (Act 31 of 2022; first published 28 October 2022), section 23(1) only (section 38 of the Broadcasting Act deleted) | `../../../telecommunications-act-1999/registers/source-bundle/TA1999.ACT31-2022.txt` | `sgba-versions-later.l4` | `sgba-tests-versions-later.l4` | encoded | deposited by the Telecommunications Act encoder; s 23(1) quoted and encoded as a two-date presence; off the receiver chain |
| S850_22 | Statutes (Miscellaneous Amendments) Act 2022 (Commencement) Notification 2022 (S 850/2022; first published 31 October 2022) | `../../../telecommunications-act-1999/registers/source-bundle/TA1999.S850-2022.txt` | `sgba-versions-later.l4` | `sgba-tests-versions-later.l4` | encoded | deposited by the Telecommunications Act encoder; para 2 quoted: the Act in operation on 1 November 2022 except sections 4(1)(a) to (d) and (f), 10, 12(2) to (6), 16(b), 20(2) and 22(3) |
| S26_22 | Variable Capital Companies (Consequential Amendments to Other Acts) Order 2022 (S 26/2022; first published 12 January 2022 at 7 pm, in operation 13 January 2022), paragraph 3 only (the variable capital company provisions inserted into Part 10 of the Broadcasting Act) | `../../../telecommunications-act-1999/registers/source-bundle/TA1999.S26-2022.txt` | `sgba-versions-later.l4` | `sgba-tests-versions-later.l4` | encoded | deposited by the Telecommunications Act encoder; para 1(1) and para 3 (limbs (a) to (l)) quoted and encoded as a two-date presence; the inserted provisions are encoded on the 2024 text in `sgba-p10-ownership.l4`; off the receiver chain |
| ACT38 | Online Safety (Miscellaneous Amendments) Act 2022 (Act 38 of 2022; passed 9 November 2022, assented 24 November 2022, first published 21 December 2022; Acts Supplement No. 37 of 2022) | `../../../online-safety-miscellaneous-amendments-act-2022/registers/source-bundle/BA1994-ACT38-2022.txt` | `sgba-versions-later.l4` | `sgba-tests-versions-later.l4` | encoded | e-Gazette text; Part 1 (ss 2 to 8) quoted by its lead-in lines and encoded as a two-day wording (the long title, s 59(1), s 64) or presence (the s 2(1) definitions, ss 2A to 2D, Part 10A, s 59(5), s 64A) or schedule (the Fourth Schedule); Parts 2 and 3 amend the Electronic Transactions Act 2010 and are not the Broadcasting Act's; the supplement prints the Bill's cover above the Act; the number is read off the heading, "No. 38 of 2022." |
| S29_23 | Online Safety (Miscellaneous Amendments) Act 2022 (Commencement) Notification 2023 (S 29/2023; made 30 January 2023, first published 31 January 2023) | `../../../online-safety-miscellaneous-amendments-act-commencement-notification-2023/registers/source-bundle/BA1994-S29-2023.txt` | `sgba-versions-later.l4` | `sgba-tests-versions-later.l4` | encoded | e-Gazette text; para 2 quoted and encoded: the Act in operation on 1 February 2023; the file is named 029.pdf and the notification is S 29/2023 |
| ACT4 | Statutes (Miscellaneous Amendments) Act 2008 (Act 4 of 2008; assented 6 February 2008, first published 25 February 2008; Acts Supplement No. 4 of 2008) | `../../../statutes-miscellaneous-amendments-act-2008/registers/source-bundle/BA1994-ACT4-2008.txt` | `sgba-versions-later.l4` | `sgba-tests-versions-later.l4` | encoded | e-Gazette text; s 1 and s 3 (s 8(5) and (6) of the Broadcasting Act inserted) quoted and encoded as presence and a rule on two days; the only place in the Act that names the Broadcasting Act |
| S128_08 | Statutes (Miscellaneous Amendments) Act (Commencement) Notification 2008 (S 128/2008; made 17 March 2008, first published 18 March 2008 at 5.00 pm), cancelled by S 129/2008 | `../../../statutes-miscellaneous-amendments-act-commencement-notification-2008/registers/source-bundle/BA1994-S128-2008.txt` | `sgba-versions-later.l4` | `sgba-tests-versions-later.l4` | encoded | e-Gazette text; para 2 quoted: the Act in operation on 18 March 2008; cancelled, so it brought nothing into operation |
| S129_08 | Statutes (Miscellaneous Amendments) Act (Commencement) Notification 2008 (Corrigendum) (S 129/2008; first published 18 March 2008 at 8.00 pm) | `../../../statutes-miscellaneous-amendments-act-commencement-notification-2008-corrigendum/registers/source-bundle/BA1994-S129-2008.txt` | `sgba-versions-later.l4` | `sgba-tests-versions-later.l4` | encoded | e-Gazette text; says S 128/2008 "has been published in error is to be treated as cancelled"; encoded as a function of the reading day (the hour is not kept) |
| S244_24 | Statutes (Miscellaneous Amendments) Act 2008 (Commencement) Notification 2024 (S 244/2024; made 27 March 2024, first published 28 March 2024) | `../../../statutes-miscellaneous-amendments-act-2008-commencement-notification-2024/registers/source-bundle/BA1994-S244-2024.txt` | `sgba-versions-later.l4` | `sgba-tests-versions-later.l4` | encoded | e-Gazette text; para 2 quoted and encoded: the Act, except sections 9 and 12, in operation on 1 April 2024; s 3 (the amendment of s 8) is not excepted; answers fork F-BA-09 |
| S250_22 | Courts (Civil and Criminal Justice) Reform Act 2021 (Commencement) Notification 2022 (S 250/2022; made 30 March 2022, first published 31 March 2022 at 5 pm) | `../../../courts-civil-and-criminal-justice-reform-act-commencement-notification-2022/registers/source-bundle/BA1994-S250-2022.txt` | `sgba-versions-later.l4` | `sgba-tests-versions-later.l4` | encoded | e-Gazette text; para 2 quoted and encoded: the Act in operation on 1 April 2022 at 12.00 a.m. except the sections it lists, which do not include s 84; the orchestrating session named four candidate notifications for Act 25 of 2021, S 250/2022 first; S 250/2022 was read first and brings s 84 into operation, so the others were not fetched |
| RE2020 | Broadcasting Act 1994, 2020 Revised Edition as printed (operation 31 December 2021; incorporates all amendments up to and including 1 December 2021) | `../../../broadcasting-act-1994/registers/source-bundle/BA1994.20211231.txt` | `sgba-versions-later.l4` | `sgba-tests-versions-later.l4` | encoded | e-Gazette text; the base of the Act 38 of 2022 wording tables; compared by script with the 2024 consolidation: s 2(1) "broadcasting apparatus", s 20(1) to (4), s 47 and the First Schedule are word for word identical (the consolidation adds the running head "FIRST SCHEDULE - continued" at a page break) |

Totals, amending Acts, Orders and notifications: 22 rows; encoded 22.

No row, in the Act or among the instruments, is `deferred`.
