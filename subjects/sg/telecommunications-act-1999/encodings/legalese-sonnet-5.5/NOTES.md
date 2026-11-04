# Telecommunications Act 1999 (Singapore): L4 encoding of the whole Act and every instrument found, `legalese-sonnet-5.5`

Status: draft, written 2026-11-03 and 2026-11-04 by one encoder session (Claude Sonnet 5.5), target compiler `main` (build 1.6.98).
No domain expert has read it against the sources (`encoding.json`, `not_reviewed`).
A second Claude session (Opus 5.5) read it once, after the encoders finished; that is not a domain expert's review, and "Independent review" below and `review/README.md` say what it did and did not cover.
The brief is `BRIEF.md` in this folder; this file does not repeat it.

Scope, ruled by Meng on 2026-11-03: the whole Act and every instrument found under it, with no deferred rows.
Result, by `gen-coverage.py` from the deposited texts and the `@ref` locators: the Act has 1,203 rows, of which 1,183 are encoded, 4 are fork rows, 16 are inert and 0 are pending; the 73 instrument texts have 1,109 rows, of which 980 are encoded, 2 are fork rows, 127 are inert and 0 are pending.
A row is `encoded` only when every content line of it lies inside an `@ref` locator, so the table cannot say "encoded" for a provision whose text no rule quotes.

In this folder "the team lead" and "team-lead" mean the orchestrating session, a Claude session that fetched Gazette pages and passed the encoder their URLs; PROGRESS.md keeps the encoder's own log of those messages as they arrived.

Not done: the one attempt on Singapore Statutes Online for the SSO consolidations of the Act by date.
It was gated on the Broadcasting Act encoder's own attempt (a file is created by hand only after that encoder reports that its attempt did not end on a 403, 429, 503 or challenge).
That encoder reported at 03:08 SGT on 2026-11-04 that its single attempt, made at 03:07:48, ended at https://sso.agc.gov.sg/robots.txt with a 403 (919 bytes, a CloudFront "Request blocked" page), so I made no request to SSO and created no gate file; the team lead ruled that a block is a no for every agent from this client, and I cancelled the armed job and deleted its arming script.
SSO: not attempted by the TA encoder because the BA encoder's one attempt was refused at robots.txt (403, CloudFront block page, 2026-11-04 03:07:48 SGT); no SSO text used, no mirror.
`PROGRESS.md` holds the request list that was not used (`scratchpad/sso-1104/urls.txt`).
What replaces it for the days before 2 October 2026 is the e-Gazette: the Revised Edition 2000, Act 10 of 2005, Act 19 of 2011 and its commencement notification S 33/2012 are deposited (2026-11-04), so the Act's text is printed for conduct from 30 Dec 2000 to 30 Sep 2016.
Acts 22 and 30 of 2016 and Act 15 of 2017 are deposited as enacted (findings 27 and 28), so the printed texts cover the Act up to 15 May 2018; eight Acts and one Order after Act 15 of 2017 are deposited as enacted and encoded (`sgta-i-acts-after-2017.l4`; findings 36 and 38) but not wired into the seat's version table, so for 16 May 2018 to 1 Oct 2026 the seat answers from the deposited consolidation's own margin markers, the Gazette's 2020 Revised Edition (31 Dec 2021) agreeing with the 2026 consolidation word for word on ss 54, 55, 85 and 95 (finding 18).
The SSO consolidations by date are therefore not deposited, and the Act's printed text stops where the e-Gazette's copies stop (finding 28).

The answer to the question the encoding was built for is in `TV-QUESTION.md`, `sgta-tv-seat.l4` and `sgta-tv-cases.l4` only.
This file, the layer-1 modules and their tests record what each provision says and how I read it.
Forks on the provisions the question runs through (FORK 1 to FORK 5) are in `TV-QUESTION.md` section 4: one-line pointers are in the register below and in the `fork` rows of `COVERAGE.md`.

## Method

- One session, one context, no sub-agents.
  Sources were gathered first, then the coverage table by script, then the nouns, then the rules with quotations copied by script, then the tests, then the seat layer last.
- Every rule carries `@ref` with a `src:` locator and sits under `-- src:N | text` quote lines produced by `srcrefs.py` (with a helper, `expand-quotes.py`, in my scratchpad and not committed), never retyped.
  `python3 -I srcrefs.py check --strict` is clean on every rule module (numbers below).
  The raw texts the locators name are deposited in this repository: `subjects/sg/telecommunications-act-1999/registers/source-bundle/TA1999.txt` for the Act, and for each instrument the `TA1999-<instrument>[-S<n>-<year>].txt` files of its own subject (see "Editions"; the extraction is `pdftotext -layout`, or tesseract OCR for the two scans).
  `srcrefs-all.sh` runs the checker on each module against its own deposited texts.
- Expected values in tests are written by hand from the text, and every test file says which provision it tests.
  No test was edited to match the code; two expectations of mine that were wrong were corrected from the text (finding 17).
- Modelling conventions, used the same way in every module:
  - A definition that says "means" is a `BOOLEAN` function; one that says "includes" is a `MAYBE BOOLEAN` (`JUST TRUE` for a listed case, `NOTHING` for a case the list does not settle).
  - A term defined in another Act is a plain `BOOLEAN` input, not a re-encoding of that Act.
  - A list of matters ("including ...") is `elem x (LIST ...)`.
  - A rule that says the Authority may act "notwithstanding that it may prejudice contractual obligations" is a function that returns constant `FALSE` for "the prejudice bars the Authority", so the sentence has a place in the code and a test.
  - Every `NOT` is parenthesised.
    L4 reads `NOT a OR b` as `NOT (a OR b)`; a test found this bug in s 45(2) and (3) (finding 17).
- The s 95 carve-out is applied inside the layer-1 outcome functions of s 54(2) (two readings) but, for s 55(1), only in the seat's helper `s 55(1) outcome`, because the layer-1 `s 55(1)` function states the section alone; a reviewer comparing the two should expect that asymmetry.
- The field `a licence under the Broadcasting Act 1994 for this apparatus` of `What the person holds` is a placeholder: no layer-1 rule reads it (s 95 is applied through its own inputs) and the seat sets it to FALSE.
- Where the sources do not answer, a function returns `NOTHING` in a `MAYBE` and the tests assert `NOTHING`; there is no `REFUSE` (not on `main`).
- Vintages are inputs.
  A rule that changed on a date has one function per form and a dispatcher that takes the date; a date before a deposited vintage begins answers `NOTHING`, never a figure from another vintage.
- Toolchain: `$HOME/.cache/l4-main/98/l4`, `1.6.98 (main, 7689b0d, 2026-10-19)`, `JL4_LIBRARY_PATH` unset.
  `check.sh` was run with `L4=$HOME/.cache/l4-main/98/l4 L4_MAIN_BUILD=98`.

## Editions encoded, and where each text could not be had

| Text | What I used | Status |
| --- | --- | --- |
| Telecommunications Act 1999 | `registers/source-bundle/TA1999.txt`: SSO's informal consolidation headed "version in force from 2/10/2026", 2020 Revised Edition. `TA1999.meta.json` says retrieved 2026-10-09, "Current version as at 09 Oct 2026", and its `historical_versions` stops at 20251001, one version behind the text (the text carries "[Act 13 of 2026 wef 02/10/2026]" at s 97(2)(ga)). I took 2 October 2026 as the first day the deposited text speaks for. | deposited, SSO terms (cl. 13) |
| Telecommunications Act, earlier versions, as printed in the e-Gazette | `registers/source-bundle/TA1999.20001230.txt` (Revised Edition 2000, 30 Dec 2000), `TA1999.ACT10-2005.txt` (Act 10 of 2005, first published 16 Feb 2005 at 5:00 pm; a scan, OCR, four of 27 pages compared with the images), `TA1999.ACT19-2011.txt` (Act 19 of 2011, first published 20 Jan 2012), `TA1999.S33-2012.txt` (commencement notification, first published 31 Jan 2012, brings Act 19 of 2011 into operation on 1 Feb 2012), `TA1999.BILL20-2011.txt` and `TA1999.BILL30-2016.txt` (Bills with explanatory statements), `TA1999.RevEd2020-printed.txt` (the 2020 Revised Edition as printed, in operation 31 Dec 2021). The Revised Edition 2000 and the two Acts are my ASSEMBLY of the text for ss 2, 34 to 36, 65, 72 and 73 on each day, from primary texts: it is not an official consolidation. | fetched 2026-11-04, one GET each, 5 s apart, commons User-Agent, no search path; reliance on the e-Gazette Terms of Use cl. 11 (`SOURCE-LICENSE-GAZETTE.md` in that folder), not a clearance |
| Telecommunications Act, the SSO consolidations by date | not deposited. SSO answered 403 on 2026-10-20 and 2026-11-03 (per the brief); I made no attempt: the Broadcasting Act encoder's single attempt at 03:07:48 SGT on 2026-11-04 ended in a 403 at robots.txt, which was the gate (see above). lawplain serves one version of each Act and ignores `as_at`, `version` and `kind=` for history. Three amending Bills were also read through lawplain on 2026-11-04 before the Gazette copies arrived (Bills 67/2004, 20/2011 and 30/2016, as introduced; `https://sso.agc.gov.sg/Bills-Supp/67-2004/Published/20041125?DocDate=20041125`, `.../20-2011/Published/20111020?DocDate=20111020`, `.../30-2016/Published/20161010?DocDate=20161010`); Bills 20/2011 and 30/2016 are now deposited from the Gazette; the clause 2 of Bill 20/2011 reads word for word as clause 2 of Act 19 of 2011 as printed (`TA1999.ACT19-2011.txt:42-60`), and the Act of 2016 is not deposited, so Bill 30/2016 is as introduced only. | not available |
| The e-Gazette's copies of the instruments | Two Rg 6 texts first (`telecommunications-dealers-regulations-2003/registers/source-bundle/TA1999-RG6-GAZ-RevEd2004.txt` and `TA1999-RG6-S178-2011-GAZ.txt`, deposited to check the IMDA copies), then, on the team lead's exact URLs, 29 more fetched on 2026-11-04 (one GET each, 5 seconds apart, the commons User-Agent, each answered 200 with a PDF with a text layer): 23 are the Gazette copies of amending instruments that IMDA also lists (N 1: 8; Rg 5: 5; Rg 6: 6; Composition: 2; Rg 3: S 685/2011 and S 76/2007, the second not on the team lead's list of 23 but compared in the same way), deposited as `TA1999-<id>-GAZ.txt` beside the IMDA copy (finding 23); the Gazette copies of S 685/2011 and S 686/2011 REPLACE the OCR text as `TA1999-RG3-S685-2011.txt` and `TA1999-COMP-S686-2011.txt`, the OCR text being kept as `-OCR.txt` and not quoted; and six are texts IMDA's list does not include (S 525/2001, S 78/2017, S 485/2016, S 23/2011, S 24/2011 and S 76/2005, the commencement notification of Act 10 of 2005, which is under the Act's folder). The index date the team lead gave for each of the 29 (23 in the list of URLs, six in the note on the extra instruments) agreed with the "First published in the Government Gazette, Electronic Edition, on" line inside the PDF in every case. Earlier:  S 178/2011 agrees with the IMDA copy except for the page headers, the Gazette's publication line, "1" against "1st" in the commencement words, and the order of two words that the table layout moves (word diff by script, 2026-11-04). The Revised Edition 2004 does NOT agree: the IMDA file reads reg 10(2) and (4) as S 478/2005 reg 6 substitutes them, the Gazette's edition has the 5-year class-licence fee, and the IMDA arrangement of regulations carries the later titles of regs 20 to 22 (finding 19). | fetched 2026-11-04; same reliance
| The ten instrument groups under the Act, 40 texts in all | IMDA's Telecommunications Act 1999 page links the 2002 and 2004 Revised Editions and every gazetted amendment to 2016; all 40 PDFs on that page were fetched once each on 2026-11-03 (robots.txt read first, 6 seconds apart, the commons User-Agent). Two are scans (S 685/2011 and S 686/2011) and were read by OCR on 2026-11-03; on 2026-11-04 the e-Gazette copies, which have text layers, replaced the OCR text (row above). They are an aid: IMDA is not the Attorney-General's Chambers. The groups are Rg 1 (ship station operators, 1 text), Rg 3 (class licences, 8), Rg 4 (cable detection workers, 3), Rg 5 (radio-communication, 6), Rg 6 (dealers, 8), N 1 (exemption from ss 33, 34(1)(b) and 35, 9), the Composition of Offences Regulations 2005 (2), the Internal Wiring Regulations 2005 (1), the Resellers of Local Calls Operating Coinafons Notification 2007 (1) and the Prescribed Trusts Regulations 2017 (1). | read; the text of each, a `.meta.json` (URL, retrieval date, sha256 of the PDF and of the text, the header line as printed) and a `SOURCE-LICENSE.md` are deposited under `subjects/sg/telecommunications-*` (Meng's ruling of 2026-11-03: deposit, as a reliance on SSO's cl. 13 and not a clearance from IMDA or the Attorney-General's Chambers); the two scans' OCR text is kept as `-OCR.txt` and is no longer quoted |
| Instruments made after those IMDA lists, or missing from them | IMDA's list ends at S 725/2014 (Rg 6), S 726/2014 (N 1), S 100/2016 (Rg 5). The e-Gazette supplied two instruments the list lacks: S 78/2017 (N 1, in operation 1 Apr 2017) and S 485/2016 (Rg 3, deemed in operation 1 Oct 2016); and three of 2001 and 2011 that the list lacks: S 525/2001 (N 1, in operation 17 Oct 2001), S 23/2011 and S 24/2011 (the Designated Telecommunication Licensees notifications, in operation 21 Jan 2011). From the team lead's second list of exact URLs: S 115/2001 (N 1 as made, 2 Mar 2001), the notifications S 86/2005, S 233/2005, S 390/2007, S 35/2012, S 192/2012 and S 521/2017 (finding 27), and Acts 22 and 30 of 2016 with S 461/2016 and S 14/2017. Whether the Gazette's browse page is complete is not established; finding 25. | fetched 2026-11-04 |
| The third list of exact URLs (team lead, 2026-11-04) | Seven PDFs, one GET each 5 seconds apart with the commons User-Agent, each 200 with a text layer: Rg 5 as made, S 114/2001 (2 Mar 2001); the 2001 amendments S 339/2001 (9 Jul 2001), S 373/2001 (a Corrigendum, 1 Aug 2001), S 374/2001 (1 Aug 2001) and S 450/2001 (18 Sep 2001); the Composition Regulations as made, S 516/2001 (15 Oct 2001); the Companies (Amendment) Act 2017, Act 15 of 2017 (Acts Supplement No. 17 of 2017, 30 Mar 2017). The date the team lead gave agreed with the "First published" line inside every PDF. Finding 28. | deposited 2026-11-04 |
| The follow-up list (team lead, 2026-11-04, after the independent review) | 34 PDFs, one GET each at least 5 seconds apart with the commons User-Agent, each 200 and a PDF: the TAS-era Order O 3 (S 549/1998 and the 1999 Revised Edition), the 1999 Revised Editions of Rg 7 (Dealers) and Rg 3 (Radio-communication), S 588/2023, S 589/2023, S 560/2024, S 381/2024, S 559/2024, S 852/2024, twenty Acts (seven amend this Act and are deposited as `TA1999.<ACT>.txt`; thirteen amend nothing in it and are not deposited) and four Bills (not deposited); `sgta-i-o3-1998.l4`, `sgta-i-rg7-1999.l4`, `sgta-i-rg3-1999.l4`, `sgta-i-erp-s381-2024.l4`, `sgta-i-ww-2024.l4`, `sgta-i-acts-after-2017.l4` and new vintages in four existing modules | Gazette copies, each with a `.meta.json` and a licence note; findings 33 to 37 |
| The Part 3 list (team lead, 2026-11-04, after Part 2 was accepted) | Ten GETs on the exact URLs, the commons User-Agent, the first nine at least 5 seconds apart in one run and the tenth later, each 200 and a PDF with a text layer: the 2010 Subject Index (deposited as an AID, finding 40), Act 31 of 2022 and its commencement notification S 850/2022, Bill 24/2022 (extrinsic), S 26/2022, S 362/2001 (Rg 7), S 185/2003 (Rg 6 as made), S 48/2004, S 593/2004, and Bill 20/2026 (read, not deposited: the Bills table below). `sgta-i-rg6-as-made.l4` is new; `sgta-i-rg7-1999.l4`, `sgta-i-acts-after-2017.l4`, `sgta-i-versions.l4` and `sgta-i-o3-1998.l4` changed | Gazette copies, each with a `.meta.json` and a licence note; findings 38 to 41 |
| S 22/2011 (the Telecommunications (Cancellation) Notification 2011), found by the independent reviewer | One GET on 2026-11-04 at 11:13 SGT, the commons User-Agent, at the exact URL that the orchestrating session read off a result in the e-Gazette index and passed to the encoder; 200 and a PDF with a text layer of 3 pages; the sha256 of the PDF (`d682419753b958efb5e28175517e66d12ad734ecb3214cd995019c37f8b058a5`) and of the text (`aa8180945959322a8308b39d8ea307216826964831588f7f98ff0ce077e272b0`) are equal to the reviewer's. Deposited as its own subject, `telecommunications-cancellation-notification-2011` (`TA1999-CANC-S22-2011`); `sgta-i-canc-s22-2011.l4` | Gazette copy with a `.meta.json` and licence notes; finding 42 |
| Broadcasting Act 1994 and its instruments | the Broadcasting Act folder's own encoding and deposits (another session owns them). The Telecommunications Act encoding reads the deposited `BA1994.txt` (25 September 2024) for a few facts and takes the Broadcasting Act's answer as an input. | see the register below |

The rule of the brief, "do not reconstruct a past text from the present one", is applied this way: every function that answers for a date takes the date and says `NOTHING` where no text is deposited for it.
The deposited Act's own margin markers are a separate, labelled inference (`sgta-ta-vintage.l4`), never silently used.

## Coverage

`COVERAGE.md` has one row per section, subsection, paragraph, sub-paragraph, sub-sub-paragraph, defined term and Part of the Act, and one row per provision, schedule item, front-matter block and back-matter block of each instrument text.
`python3 -I gen-coverage.py` checks that the sections found are exactly 1 to 98 and all appear in the arrangement of sections, that every non-blank line of the Act falls in a row or is a heading or page furniture, that every inert row has one of the three allowed reasons, and that no row is pending; it exits 1 otherwise.
All six checks print PASS on the final run (`grep -c '^- PASS' COVERAGE.md` gives 6).

| text | disposition | rows | what they are |
| --- | --- | --- | --- |
| Act | encoded | 1,183 | every content line quoted and cited by a rule |
| Act | fork | 4 | s 2 "equipment", s 2 "radio-communication", s 53(1), s 95: encoded, and pointed at a fork in `TV-QUESTION.md` section 4 |
| Act | inert | 16 | cover and edition notice, arrangement of sections, long title, legislative history and comparative table (reason 1, not part of the Act); s 1 short title (reason 2, machinery); eleven Part headings (reason 1) |
| Act | pending | 0 | |
| instruments | encoded | 980 | |
| instruments | fork | 2 | Rg 6 as amended by S 478/2005 reg 8 (which substitutes reg 22), and N 1 Schedule item 11 |
| instruments | inert | 127 | title, arrangement and enacting words (reason 1, or 2 where the enacting words name the power); date of making and signature rows (reason 1); six citation regulations (reason 2) |
| instruments | pending | 0 | |

### Acts and instruments whose source was not obtained

Each row below is a text that the Act's own Legislative History (`TA1999.txt:7181-7302`), an instrument or a Revised Edition names, or that an instrument refers to, and that is not deposited.
`gen-coverage.py` cannot count them: it parses only deposited texts.
The disposition of every row is **source not obtained**; none is `deferred`, and none is encoded.
Where the team lead or an independent reviewer looked, and what that returned, is their report of 2026-11-04 (the e-Gazette's browse page and title searches); this encoder did not repeat those searches.
The last column is what stands in the encoding for the missing text.
Seven Acts that were rows of this table until Part 2 of the follow-up, and Act 31 of 2022, G.N. No. S 26/2022, G.N. Nos. S 185/2003, S 48/2004 and S 593/2004 and G.N. No. S 362/2001 that were rows until Part 3 (all 2026-11-04), were obtained from the follow-up lists and are in the next subsections (findings 36 to 39).

| Text | What it amended or what names it | Commencement or date | Where looked, what returned | What stands in for it |
| --- | --- | --- | --- | --- |
| Code of Practice for Competition in the Provision of Telecommunication Services 2005, G.N. No. S 87/2005 (the Code the designation notifications refer to; Rg 5 reg 76 names a different Code, S 412/2000) | not an amending text: cited by S 86/2005, S 233/2005, S 390/2007, S 23/2011 and S 24/2011 | | the only 2005 Code in the Gazette's index is S 718/2005 (16 Nov 2005, "Code of Practice for Competition in the Provision of Telecommunication Services"), which is not S 87/2005; S 262/2005 and S 524/2005 are dominant-licensee exemptions, off this path | nothing: the notifications are encoded as the Gazette prints them, and the Code is a name in them |
| Government Gazette (main series), "Notices under other Acts", 2010 to 2013 (telecommunications exemption notices) | not an Act or an instrument of this Act: a series in which some Telecommunications Act exemptions have been published | | searched by the team lead on 2026-11-04 in the e-Gazette index with the query "Telecommunications Act Exemption", one query per year, FIRST PAGE of results only (2010: 5 results, none in that series; 2011: 18; 2012: 16; 2013: 5); the only Government Gazette rows were seven "Gazette Contents" index files (21 Jan 2011, 1 Apr 2011, 30 Dec 2011, 20 Jan 2012, 3 Feb 2012, 11 May 2012, 26 Apr 2013), whose dates coincide with Telecommunications Act supplements already held (S 21 to 24/2011, S 178 and 179/2011, S 685 and 686/2011, S 34 and 35/2012, S 191 and 192/2012, S 251 and 252/2013); no notice in that series named a receiver; earlier hits for 2006 and 2009 (0178, 2149, 1002) are licensee-specific | nothing: the search was not exhaustive and the absence of a hit is not proof that no notice exists, so no answer rests on there being none |
| Telecommunication Authority of Singapore Act (Cap. 323, 1993 Revised Edition), the "repealed Act" of s 2 (`TA1999.txt:459-462`), including its section 30 | named by the Order O 3 ("section 30 (1) to (5) of the Act") and by TA s 98 | repealed 1 Dec 1999 (TA s 98 and s 3(1)) | the e-Gazette's index (no text of the Act); lawplain lists it as `TASA1992` with no sections and its copy of the 1992 Bill stops after clause 2 (independent reviewer, REQUESTS R4); Singapore Statutes Online: the Broadcasting Act encoder's single attempt was refused at robots.txt (403) and this encoder made none | a fork, `sgta-i-o3-1998.l4`: `What section 30 of the TAS Act provided` has three values (approval-before-use; the prohibition on possessing or operating equipment; text not held), and the function answers NOTHING for the third |
| Amendments of Rg 7 (Dealers, 1999 Ed.) other than S 362/2001, and of Rg 3 (Radio-communication, 1999 Ed.), made after 1 July 1999 | none known: the title pages list S 327/94, S 88/95, S 70/96, S 425/96, S 166/98, S 540/98 (Rg 7) and S 328/94, S 144/96, S 161/97, S 615/98, S 227/99 (Rg 3), all incorporated in the Revised Editions; S 362/2001 is the one amendment of Rg 7 held (finding 39) | between 1 Jul 1999 and 1 Apr 2003 (Rg 7) and 1 Mar 2001 (Rg 3) | not searched; the 2010 Subject Index (now deposited as an aid, finding 40) does not list either Edition | the 1999 Revised Edition, with S 362/2001 for Rg 7, is the latest text held, so a later amendment, if there is one, is unknown to the encoding |
| The thirteen notifications cancelled by S 22/2011, items (a) to (m): G.N. Nos. 407/2005, 409/2005, 410/2005, 411/2005, 412/2005, 413/2005, S 262/2005, S 524/2005, 293/2006, 1001/2006, 119/2007, 178/2009 and 1757/2009 | named in items (a) to (m) of S 22/2011 (`TA1999-CANC-S22-2011.txt:34-80`; finding 42) | not held; the cancellation begins 21 Jan 2011 (S 22/2011 para 1) | not searched for by this encoder (S 262/2005 and S 524/2005 also appear in the Code of Practice row above, as hits of the orchestrating session's index search) | nothing: their titles, as S 22/2011 prints them, are exemptions from the Telecom Competition Code or its Dominant Licensee Provisions (items (a) to (j)) and exemptions for named services (items (k) to (m)), none names a receiver, and they are off the receiver question; `sgta-i-canc-s22-2011.l4` says only that they are named and when the cancellation begins |

### Acts after Act 15 of 2017 that amend this Act: obtained 2026-11-04 (follow-up list, Parts 2 and 3)

Eight Acts and one Order, each the Gazette's copy (one GET each on 2026-11-04, the commons User-Agent, five seconds apart), deposited in `registers/source-bundle/` as `TA1999.<ACT>.txt` with a `.meta.json`; the seven of Part 2 first, then Act 31 of 2022 and G.N. No. S 26/2022 in Part 3.
They are encoded in `sgta-i-acts-after-2017.l4`, with a test file `sgta-tests-acts-after-2017.l4`.
The commencement notification of seven of them is not deposited, so, as for Act 15 of 2017, the effective day is the Legislative History's and the day a reader could see it is ASSUMED to be the same.
For Act 31 of 2022 the notification S 850/2022 IS deposited, and for G.N. No. S 26/2022 the Order carries its own commencement; for those two the day a reader could see the amendment is read from a printed "First published" line.

| Act | What it amends in the Telecommunications Act (the numbers the Act prints) | First published (Gazette) | Commencement (Legislative History, `TA1999.txt`) | On the decisive chain? |
| --- | --- | --- | --- | --- |
| Act 26 of 2018, Public Order and Safety (Special Powers) Act 2018, s 61 | s 58: new subsection (10) (no direction while an activation order is in force) | 20 Apr 2018 | 16 May 2018 (`:7205`) | no |
| Act 15 of 2019, Criminal Law Reform Act 2019, s 187 | repeals s 45 (sending false message); deletes "45," in s 60(3) | 4 Jun 2019 | 1 Jan 2020 (`:7220`) | no |
| Act 40 of 2018, Insolvency, Restructuring and Dissolution Act 2018, s 517 | ss 32I(3)(b), 32J(3), (6), 32L(1), (2): the Companies Act references replaced by references to the 2018 Act; new 32J(3)(ba), 32L(1)(ca), 32L(2)(ba) | 7 Nov 2018 | 30 Jul 2020 (`:7234`) | no |
| Act 4 of 2021, Statute Law Reform Act 2021, s 22(9) | s 2, definition of "owner": the HUDC housing estate words removed from paragraph (b) and sub-paragraph (b)(iv) | 18 Feb 2021 | 1 Mar 2021 (`:7245`) | s 2, but not "equipment", "radio-communication" or "broadcasting apparatus" |
| Act 25 of 2021, Courts (Civil and Criminal Justice) Reform Act 2021, s 212 | s 25(1) "in execution" to "under or pursuant to an enforcement order"; ss 29(8), 33(7), 47(5), 49(5) "leave" to "permission"; s 32L(1)(e) "execute or" deleted | 11 Oct 2021 | 1 Apr 2022 (`:7265`) | s 33(7) of the 2000 Edition, now s 53(7): one word, in the notice of the defence of the licensing offence |
| Act 12 of 2020, Building Control (Amendment) Act 2020, s 50(4)(g) | s 2, definitions of "common property" and "owner" (paragraph (a)(iii)): "Building Maintenance and Strata Management Act" to "Building (Strata Management) Act" | 11 May 2020 | 1 Oct 2025 (`:7289`) | s 2, but not the three definitions |
| Act 13 of 2026, Info-communications Media Development Authority (Amendment) Act 2026, s 18 | ss 37(13), 37(14), 38(9) to (13), 40(11), 42(1), 92(3)(c)(iv), 92(6), 92(12), 92(19), 92(20), 97(2)(ga) (2020 Edition numbers) | 5 Jun 2026 | 2 Oct 2026 (`:7302`) | no |
| Act 31 of 2022, Statutes (Miscellaneous Amendments) Act 2022, s 21(7) (Acts Supplement No. 30 of 2022) | s 46(3)(b) (2020 Edition number): "Part 7" replaced by "Parts 7 and 9" (of the Insolvency, Restructuring and Dissolution Act 2018) | 28 Oct 2022 at 5 pm | 1 Nov 2022 (`:7276`), by S 850/2022 para 2 (first published 31 Oct 2022) | no |
| G.N. No. S 26/2022, Variable Capital Companies (Consequential Amendments to Other Acts) Order 2022, paragraph 22 | s 2: "(including a VCC)" after "to a company" in "securities", and new definitions "VCC" and "VCC Act"; ss 40(7)(a) and 41(7)(a): "and the Trustees Act 1967" replaced by ", the Trustees Act 1967 and the VCC Act" (2020 Edition numbers) | 12 Jan 2022 at 7 pm | 13 Jan 2022 (`:7254`; the Order's paragraph 1(1)) | s 2, but not "equipment", "radio-communication" or "broadcasting apparatus" |

Whether these should be rows of the version table of `sgta-ta-versions.l4`: the instruction was to encode as a version an Act that amends s 2, ss 5, 53 to 56, 85, 95 or the licensing chain.
Acts 4 of 2021 and 12 of 2020 and the Order S 26/2022 amend s 2 (other definitions), and Act 25 of 2021 amends s 53(7); the module `sgta-i-acts-after-2017.l4` has the version rule for all nine (`Instruments after Act 15 of 2017 whose amendments of the Telecommunications Act are in operation for the conduct day, as read on the reading day`) and the wording functions for the three provisions.
They are NOT rows of `Act text version`: the seat's "on the texts deposited" tier answers NOTHING for 16 May 2018 to 1 Oct 2026 and its "also on the markers" tier answers those days, and splitting the one row `as amended by Acts after Act 15 of 2017 that are not deposited` into nine would move the first tier from NOTHING to an answer for those days (not run; I do not claim it would equal the second tier's on every case).
That is a change to the seat's output, so it was not made and is reported (finding 36).

**Assumed, not ruled** (team lead's ruling of 2026-11-04, not Meng's): the nine stay a parallel version rule in `sgta-i-acts-after-2017.l4`, and the bucket row of `sgta-ta-versions.l4` is not split.
What splitting would change: the seat's tier "on the texts deposited" would answer, from the Acts' own texts, the days 16 May 2018 to 1 Oct 2026 that it now answers NOTHING for; the "what the answer rests on" string for those days would change, and with it the two case assertions `sgta-tv-cases.l4:247` and `:381` and the constructor `as amended by Acts after Act 15 of 2017 that are not deposited` that the seat names; I have not run the wiring and do not claim the two tiers would then agree on every case.
To revert: split the one row into a row per instrument in `sgta-ta-versions.l4` and re-bless those two assertions.

### Acts and Bills fetched and read on 2026-11-04 that do not amend the Telecommunications Act

Thirteen Acts and four Bills were fetched from the follow-up list (one GET each) and read; none amends the Telecommunications Act, and none is deposited as a source (their text is outside this Act's folder).
Each row says what the Act does with the Telecommunications Act: a reference only.

| Act or Bill | What it says about the Telecommunications Act |
| --- | --- |
| Act 21 of 2018, Cross-Border Railways Act 2018 | no mention of the Act; "telecommunication ... services" in a list of utilities |
| Act 25 of 2018, an Act amending the Films Act | "telecommunications" has the meaning given by section 2 of the Telecommunications Act (`:419-420`): a definition by reference |
| Act 52 of 2018, an Act amending the Goods and Services Tax Act | no reference to the Telecommunications Act: "any telecommunication service as defined in the Fifth Schedule to the Goods and Services Tax (International Services) Order" (`:1917-1918`) |
| Act 17 of 2019, an Act amending the Protection from Harassment Act | "a telecommunication service" in a list; no reference to the Act by name |
| Act 18 of 2019, Protection from Online Falsehoods and Manipulation Act 2019 | "service provider licensed under section 5 of the Telecommunications Act" (`:518`), "telecommunication service" by reference to s 2 (`:596-597`), "a prescribed holder of a licence under section 5" (`:1230`) |
| Act 39 of 2020, an Act amending the Insolvency, Restructuring and Dissolution Act 2018 | its new s 72U(1) lets the Minister make orders in the Gazette modifying or amending provisions of a "specified Act", for their application to a company in the simplified debt restructuring programme, and the Telecommunications Act (Cap. 323) is item (q) of the definition (`:1176-1221`); the Act itself amends nothing in the Telecommunications Act; whether an order under that power was made is not known |
| Act 13 of 2020, an Act amending the Public Utilities Act | "telecommunications" has the meaning given by section 2 of the Telecommunications Act (`:120-121`) |
| Act 38 of 2022, an Act amending the Broadcasting Act 1994 and the Electronic Transactions Act | a service "covered by a licence under the Telecommunications Act 1999" (`:166`) |
| Act 15 of 2022, Gambling Control Act 2022 | "telecommunication service" by reference to the Act (`:1838`) |
| Act 16 of 2024, an Act amending the Miscellaneous Offences (Public Order and Nuisance) Act | "telecommunication licensee" has the meaning given by section 2 of the Telecommunications Act 1999 (`:100-101`) |
| Act 7 of 2025, Food Safety and Security Act 2025 | "telecommunication service" by reference to s 2 of the Telecommunications Act 1999 (`:2562`) |
| Act 21 of 2026, an Act amending the Protection from Scams Act 2025 (Bill 16/2026, passed) | "telecommunication service" by reference to section 2 of the Telecommunications Act (`:152-153`) |
| Act 16 of 2026, Cross-Border Railways (Border Control Co-location) Act 2026 (Bill 10/2026, passed) | the Telecommunications Act 1999 is item (46) in the Second Schedule's list of "Singapore border control laws" for section 3(1) (`:4190`): a reference, not an amendment |
| Bill 9/2026 | passed as Act 13 of 2026 (above) |
| Bill 20/2026, Digital Infrastructure Bill (Bills Supplement first published 8 Sep 2026; read the first time 8 Sep 2026; `26bills20.pdf`, 136 pages, sha256 `e74a98b41a04a54bb1a97ce9cd25dd7966f42f3ff087c216286528bc05a55408` of the PDF, retrieved 2026-11-04T00:21:30Z, re-fetched once on 2026-11-04 at 08:21 SGT and read, not deposited) | the one place "Telecommunications Act" occurs in the text is clause 3(5)(d), "a data centre operated by a licensee under the Telecommunications Act 1999, Electricity Act 2001 or Gas Act 2001" (`:445`); its Explanatory Statement says Part 8 (clause 70) makes related amendments to the Cybersecurity Act 2018, so it amends nothing in this Act; "radio-communication", "broadcasting apparatus" and a receiver (other than a liquidator's receiver) do not occur. Status: in the team lead's e-Gazette index searches of 2026-11-04 (the queries "Digital Infrastructure" and "Digital Infrastructure Act 2026", year 2026, first page) it appears only as a Bill and no Act of that name appears; this encoder made no search for it and says nothing further |

The row-by-row table (section, heading, 2000 Edition number, rows, module) is in `COVERAGE.md`; it is generated and is not copied here, because a copy would go stale at the next edit.
The 2000 Edition number is the Law Revision Commission's margin marker on each section; the pre-2020 instruments cite those numbers.

## Modules

| Part of the Act, or instrument | Rule modules | Tests |
| --- | --- | --- |
| nouns | `sgta-nouns.l4` | |
| s 2 (definitions) | `sgta-s2-definitions.l4`, `sgta-s2-more-definitions.l4` | `sgta-tests-act-defs.l4`, `sgta-tests-s2-s5.l4` |
| ss 3 to 5 | `sgta-s3-5-privilege-licensing.l4`, `sgta-s5-licence-terms.l4` | `sgta-tests-s2-s5.l4`, `sgta-tests-act-part2.l4` |
| ss 6 to 14 | `sgta-s6-8-spectrum-orbit-designation.l4`, `sgta-s9-10-conditions-and-sanctions.l4`, `sgta-s11-approval.l4`, `sgta-s11-14-approval-and-residual.l4` | `sgta-tests-act-part2.l4` |
| Part 3 (ss 15 to 29) | `sgta-part3-ss15-22.l4`, `sgta-part3-ss23-29.l4` | `sgta-tests-act-part3.l4` |
| Parts 4 and 5 (ss 30 to 36) | `sgta-part4-ss30-32.l4`, `sgta-part5-ss33-36.l4` | `sgta-tests-act-part4-5c.l4` |
| Part 5A (ss 37 to 43) | `sgta-part5a-s37.l4`, `sgta-part5a-s38-39.l4`, `sgta-part5a-s40.l4`, `sgta-part5a-s41-43.l4` | `sgta-tests-act-part4-5c.l4` |
| Parts 5B and 5C (ss 44 to 52) | `sgta-part5b-5c-ss44-52.l4` | `sgta-tests-act-part4-5c.l4` |
| Part 6 (ss 53 to 71) | `sgta-part6-offences.l4` (ss 53 to 64), `sgta-part6-more.l4` (ss 53 to 70, the remainder) | `sgta-tests-part6-part8.l4`, `sgta-tests-act-part6-8.l4` |
| ss 34, 35 and 36 of the Revised Edition 2000 (today's ss 54, 55 and 56), with the version dispatchers that pick the text each version of the Act prints | `sgta-part6-2000ed.l4` | `sgta-tests-part6-2000ed.l4` |
| Part 7 (ss 72 to 77) | `sgta-part7-international-and-directions.l4` | `sgta-tests-act-part6-8.l4` |
| Part 8 (ss 78 to 88) | `sgta-part8-more.l4`, `sgta-part8-penalties.l4` | `sgta-tests-part6-part8.l4`, `sgta-tests-act-part6-8.l4` |
| Part 9 (ss 89 to 98) | `sgta-part9-s89-90.l4`, `sgta-part9-s91-92.l4`, `sgta-part9-s93-94-97.l4`, `sgta-part9-general.l4` (ss 95, 96, 98) | `sgta-tests-act-part9.l4`, `sgta-tests-part6-part8.l4` |
| Rg 1 (ship station operators) | `sgta-i-rg1-ship.l4` | `sgta-tests-small-instruments.l4` |
| Rg 3 (class licences) | `sgta-i-rg3-licences.l4`, `sgta-i-rg3-class.l4`, `sgta-i-rg3-amendments.l4`, `sgta-i-rg3-s485-2016.l4` | `sgta-tests-rg3.l4`, `sgta-tests-more-notifications.l4` |
| Rg 4 (cable detection workers) | `sgta-i-rg4-cable.l4` | `sgta-tests-small-instruments.l4` |
| Rg 5 (radio-communication) | `sgta-i-rg5-definitions.l4`, `sgta-i-rg5-spectrum.l4`, `sgta-i-rg5-licences.l4`, `sgta-i-rg5-radio.l4`, `sgta-i-rg5-duties.l4`, `sgta-i-rg5-schedules.l4`, `sgta-i-rg5-amendments.l4`, `sgta-i-rg5-as-made.l4` (S 114/2001 as made, a regulation-by-regulation comparison with the Revised Edition, and the four amendments of 2001) | `sgta-tests-rg5.l4`, `sgta-tests-rg5-b.l4`, `sgta-tests-rg5-amend.l4`, `sgta-tests-instruments.l4`, `sgta-tests-rg5-as-made.l4` |
| Rg 6 (dealers), as made (S 185/2003, 2 Apr 2003) with S 48/2004 and S 593/2004, then the 2004 Revised Edition to S 589/2023 (1 Sep 2023) | `sgta-i-rg6-definitions.l4`, `sgta-i-rg6-licensing.l4`, `sgta-i-rg6-dealers.l4`, `sgta-i-rg6-amendments.l4`, `sgta-i-rg6-as-made.l4` (S 185/2003 as made, a regulation-by-regulation comparison with the 2004 Revised Edition, and the two amendments of 2004) | `sgta-tests-rg6.l4`, `sgta-tests-instruments.l4`, `sgta-tests-2023-24.l4`, `sgta-tests-dealers-chain.l4` |
| N 1 (exemption), from S 525/2001 (17 Oct 2001) to S 588/2023 (1 Sep 2023) | `sgta-i-n1-exemption.l4`, `sgta-i-n1-bands.l4` | `sgta-tests-n1-bands.l4`, `sgta-tests-instruments.l4`, `sgta-tests-2023-24.l4` |
| Designated Telecommunication Licensees notifications: S 86/2005, S 233/2005, S 390/2007, S 23/2011, S 24/2011, S 35/2012, S 192/2012, S 521/2017 | `sgta-i-dtl-notifications.l4` | `sgta-tests-more-notifications.l4` |
| Composition of Offences Regulations 2001 (as made, S 516/2001), 2005, the 2011 amendment and the 2024 amendment (S 560/2024) | `sgta-i-comp.l4` | `sgta-tests-instr-more.l4`, `sgta-tests-instruments.l4`, `sgta-tests-2023-24.l4` |
| Cancellation Notification 2011 (S 22/2011), which cancels thirteen exemption notifications | `sgta-i-canc-s22-2011.l4` | `sgta-tests-canc-s22-2011.l4` |
| Internal Wiring, Resellers, Prescribed Trusts | `sgta-i-iw-wiring.l4`, `sgta-i-resell.l4`, `sgta-i-trusts.l4` | `sgta-tests-small-instruments.l4`, `sgta-tests-instr-more.l4` |
| Wiring Work Regulations 2024 (S 559/2024, S 852/2024), which revoke the Internal Wiring Regulations 2005 from 1 Jul 2024 | `sgta-i-ww-2024.l4` | `sgta-tests-2023-24.l4`, `sgta-tests-eval-1999-2024.l4` |
| In-vehicle unit exemption (S 381/2024) | `sgta-i-erp-s381-2024.l4` | `sgta-tests-2023-24.l4`, `sgta-tests-eval-1999-2024.l4` |
| TAS-era Order O 3 (S 549/1998 and the 1999 Revised Edition), with the fork on section 30 of the TAS Act | `sgta-i-o3-1998.l4` | `sgta-tests-1999-regs.l4`, `sgta-tests-eval-1999-2024.l4` |
| Rg 7 (Dealers), 1999 Revised Edition, from 1 Dec 1999 to 1 Apr 2003 (revoked by reg 26 of S 185/2003), with S 362/2001 (1 Aug 2001) | `sgta-i-rg7-1999.l4` | `sgta-tests-1999-regs.l4`, `sgta-tests-dealers-chain.l4`, `sgta-tests-eval-1999-2024.l4` |
| Rg 3 (Radio-communication, NOT the Class Licences "Rg 3" above), 1999 Revised Edition, from 1 Dec 1999 to 1 Mar 2001 | `sgta-i-rg3-1999.l4` | `sgta-tests-1999-regs.l4`, `sgta-tests-eval-1999-2024.l4` |
| The eight Acts and one Order after Act 15 of 2017 that amend the Act (Acts 26 and 40 of 2018, 15 of 2019, 12 of 2020, 4 and 25 of 2021, 31 of 2022, 13 of 2026, and G.N. No. S 26/2022) | `sgta-i-acts-after-2017.l4` | `sgta-tests-acts-after-2017.l4` |
| which text the deposit speaks for, and what its markers say | `sgta-ta-vintage.l4` | `sgta-tests-act-defs.l4` |
| which printed version of the Act governs a day, on two time axes (Revised Edition 2000, Acts 10 of 2005, 19 of 2011, 22 of 2016, 30 of 2016 and 15 of 2017, the later Acts as one row (eight Acts and one Order are deposited, not split into rows: finding 36), the 2020 consolidation) | `sgta-ta-versions.l4` | `sgta-tests-act-versions.l4` |
| which version of N 1, Rg 5, Rg 6 (from S 185/2003, 2 Apr 2003), Rg 3 (1999 Ed.), Rg 7 (1999 Ed., and as amended by S 362/2001), the Wiring Work Regulations 2024, S 381/2024 and the 2024 Composition amendment governs a day, on two time axes | `sgta-i-versions.l4` | `sgta-tests-i-versions.l4`, `sgta-tests-2023-24.l4`, `sgta-tests-1999-regs.l4` |
| the seat and the Broadcasting Act's First Schedule as a table of versions (quarantined) | `sgta-tv-seat.l4`, `sgta-tv-ba-schedule.l4` | `sgta-tv-cases.l4` |

Functions: 1,460 rule functions in the rule modules; 27 are not named in any test (`scratchpad/tools/untested.py`, not committed).
Of the 1,460, 143 boolean wrapper functions of the 1999 and 2024 modules (`sgta-i-rg7-1999`, `sgta-i-rg3-1999`, `sgta-i-ww-2024`, `sgta-i-erp-s381-2024`, `sgta-i-o3-1998`; the generator also reads `sgta-i-rg6-as-made`, whose boolean wrappers and those added to `sgta-i-rg7-1999` for S 362/2001 are all named in `sgta-tests-dealers-chain.l4`, so they add none) are exercised ONLY by `sgta-tests-eval-1999-2024.l4`, an evaluation differential (494 assertions): the expected value is computed by an independent evaluation of the body text, so it checks how l4 parses and evaluates the body and NOT that the body is the regulation.
For those functions the check against the regulation is the quoted text beside each, and the review of the quotation by `srcrefs.py --strict`; no test of meaning stands behind them.
They are the per-vintage functions of five groups: eleven band functions in `sgta-i-n1-bands.l4`, five item-list functions in `sgta-i-n1-exemption.l4`, six Fifth Schedule item 1 functions in `sgta-i-rg6-amendments.l4`, three First Schedule category functions (as made; as amended by S 339/2001 or S 374/2001; as amended by S 450/2001) in `sgta-i-rg5-as-made.l4`, and two list functions of the 2001 Composition Regulations in `sgta-i-comp.l4` (the sections, and the regulations of S 114/2001, that reg 2 names).
Each is reached through its date dispatcher (`N 1 Schedule: the authorised radio frequency bands ... on the date`, `N 1: the items the (First) Schedule names on the date`, `Rg 6 Fifth Schedule item 1: ... on the date`, `Rg 5 First Schedule: the category named at the entry, for the conduct day, as read on the reading day`, `Comp Regs 2001 reg 2(a) ... on the date` and `reg 2(b) ... on the date`), and the dispatchers are tested at the edge of every amendment.

## The seat

The individual to whom the television question applies: a person who owns a television in Singapore and asks "Do I need a licence?", "Am I committing an offence?", "What is the most I can be punished with?".
The seat layer is `sgta-tv-seat.l4`, with `sgta-tv-ba-schedule.l4` (the Broadcasting Act's First Schedule as a table) and cases in `sgta-tv-cases.l4`; no second seat was written (a dealer who sells receivers would be the natural second).
The seat takes the KIND of receiver (television, FM radio, AM radio, satellite dish system) and two days, the day of the conduct and the day the law is read as at; see "Two time axes" below.
No official's seat was written.
The seat IMPORTs the layer-1 modules and calls their rules; the only rules defined in it are helpers that assemble inputs.
Every question has `@export` and `@desc`, takes plain facts (a date as day, month, year; yes or no; a choice from a list), and is grouped under `§` headings.
Each of the two offence questions comes in two forms that are kept apart: on the texts deposited for the day, and also on the Act's own amendment markers for the days (16 May 2018 to 1 Oct 2026) for which no Act text is deposited; the forms are named in the question, and `TV-QUESTION.md` section 1 sets them side by side.

## Two time axes (assumed design, not ruled)

Design instruction of 2026-11-04 (team lead; Meng: the retrospective publication of S 549/2012 is a test of the multitemporal semantics).
Each version of a rule is a row {effective day, published day, text, source}.
A question carries the day of the CONDUCT (valid time) and the day the law is READ AS AT (rule-version time).
The answer is the version with the latest published day among those published on or before the reading day whose effective day is on or before the conduct day; with none, NOTHING.
`sgta-ta-versions.l4` does this for the Act, `sgta-i-versions.l4` for N 1, Rg 5 and Rg 6 (it returns the version's effective day, which the existing date dispatchers take), and `sgta-tv-ba-schedule.l4` for the Broadcasting Act's First Schedule.
Stable l4 1.6.98 has no `RULES EFFECTIVE DATE`, `EVAL UNDER VALID TIME` or `EVAL AS OF SYSTEM TIME` (removed in build 98), so the two days are ordinary `GIVEN` DATE inputs and the versions are a table; on `unstable` the table would use the built-ins.
Every published day is read from a printed "First published" line: those of Act 10 of 2005 (16 Feb 2005; its commencement notification S 76/2005 was first published the same day), Act 19 of 2011 (Act 20 Jan 2012; its date of effect, S 33/2012, 31 Jan 2012, is the day the version counts as published), S 549/2012 (31 Oct 2012), and, since 2026-11-04, every amending instrument of N 1, Rg 5 and Rg 6 in `sgta-i-versions.l4`, from the e-Gazette copy of each. The assumed published days are those of the two Revised Edition rows of that file (Fork B), and, in `sgta-ta-versions.l4`, those of the Act 15 of 2017 row (23 May 2017: its commencement notification is not deposited, so the day is the Legislative History's), the row standing for the Acts after it (16 May 2018) and the 2026 consolidation (2 Oct 2026).
S 549/2012 is the test of the design: it is "deemed to have come into operation on 1st January 2011" and was first published on 31 October 2012; the pairs of days around it are in `sgta-tv-cases.l4`.

## Mechanical search of the deposited texts for a receiver, a sound broadcast or an AM or FM band

`scratchpad/tools/fmam-search.py` (not committed) counted each term, case-insensitively unless marked, in 95 deposited files: the Act in eight versions (`TA1999.txt`, the Revised Edition 2000, Acts 10 of 2005, 19 of 2011, 22 of 2016, 30 of 2016 and 15 of 2017, the printed 2020 Revised Edition), the 58 Telecommunications Act instrument texts (IMDA's 40, with the Gazette's copies of S 685/2011 and S 686/2011 in place of the OCR, and eighteen the e-Gazette supplied, the last six of them the third list: S 114/2001, S 339/2001, S 373/2001, S 374/2001, S 450/2001 and S 516/2001), the Broadcasting Act's three deposited versions (`BA1994.txt`, the Revised Editions 2003 and 2012), and the 26 Broadcasting Act instrument texts the Broadcasting Act folder has deposited (S 549/2012, Rg 1, S 333/2004, S 548/2012 and the TVRO Regulations among them), read here for facts only.
Every hit for `receiver`, `sound`, `kHz`, `car`, `TV`, `88`, `108`, `general reception`, `receive-only`, `licence fee`, `television` (instruments), `domestic / household` and `vehicle` was read in context; what they say is in `TV-QUESTION.md` section 10.

| search term | total hits | files with a hit |
| --- | --- | --- |
| `receiver` | 206 | 21 |
| `receiv* (any form)` | 389 | 33 |
| `radio receiver` | 0 | 0 |
| `medium wave` | 0 | 0 |
| `AM (capitals)` | 0 | 0 |
| `FM (capitals)` | 0 | 0 |
| `amplitude modulation` | 0 | 0 |
| `frequency modulation` | 0 | 0 |
| `sound` | 74 | 11 |
| `television` | 169 | 16 |
| `TV` | 6 | 6 |
| `reception` | 80 | 18 |
| `receive-only` | 10 | 6 |
| `broadcast` | 1852 | 38 |
| `broadcasting apparatus` | 157 | 11 |
| `general reception` | 3 | 3 |
| `kHz` | 59 | 9 |
| `MHz` | 711 | 22 |
| `GHz` | 65 | 12 |
| `526` | 0 | 0 |
| `1606` | 0 | 0 |
| `87.5` | 0 | 0 |
| `88` | 10 | 10 |
| `108` | 15 | 13 |
| `car` | 12 | 7 |
| `vehicle` | 89 | 22 |
| `domestic / household` | 30 | 11 |
| `licence fee` | 12 | 10 |

The counts of `broadcast` and `MHz` are dominated by the Broadcasting Act and by the frequency tables and were not read line by line; the two terms that could name an AM or an FM service, "AM" and "FM" in capitals, and the AM and FM band edges "526", "1606" and "87.5", have no hit.
Of the 26 Broadcasting Act instrument texts now deposited, 21 contain none of `apparatus`, `section 20` and `receiver` (counted 2026-11-04 with `grep -c -i` over each file); the five that do are Rg 1, S 333/2004, the TVRO Regulations, S 548/2012 and S 549/2012.

## Register of links to other folders (stable l4 cannot IMPORT across folders, so none is code)

| This encoding | needs | where it lives |
| --- | --- | --- |
| `sgta-part9-general.l4`, s 95 | whether an apparatus is "broadcasting apparatus" as the Broadcasting Act 1994 defines it (s 2 there: capable of or designed for reception of a broadcasting service AND specified in the First Schedule) | taken as a plain input; the Broadcasting Act's own encoding in `subjects/sg/broadcasting-act-1994/encodings/legalese-sonnet-5.5/` |
| `sgta-part6-offences.l4`, `What the person holds` | whether the person holds a Broadcasting Act licence for the apparatus | a plain input; the Broadcasting Act's s 20 and its instruments are encoded in that folder |
| `sgta-tv-seat.l4` | the First Schedule's list on a date | a plain input of the seat (`Is the receiver on the Broadcasting Act list`), supplied in the cases with the source named |
| `sgta-tv-ba-schedule.l4` | whether the Broadcasting Act's television and radio licensing regulations (Rg 1) are in operation on two days, and what each of Rg 1's three versions (Revised Edition 2004, as amended by S 333/2004, as revoked by S 548/2012) says in terms about a licence | read from the Broadcasting Act folder's deposits (`broadcasting-television-and-radio-licensing-regulations/`, `-amendment-regulations-2004/`, `-revocation-regulations-2012/`) for facts only; the module states them as a table of versions, and nothing is imported |
| s 9A of the Interpretation Act 1965 | the encoding of s 9A | cited, not re-encoded: `subjects/sg/interpretation-act/encodings/legalese-sonnet-5.5/`; the seat's `s 9A: the weighing of the literal answer` takes a court's finding as an input and never changes the literal answer |
| terms defined in other Acts that s 2 and the Parts use (the Companies Act, the Securities and Futures Act, the Building Control Act and others) | what those Acts say | plain `BOOLEAN` inputs, named for the term |

## What the Act (and its instruments) turn out to say

Numbered findings about provisions.
Each is asserted in a test, as stated, unless it says it is not.

1. **ss 54 and 55 state no penalty of their own.**
   The penalty is that of s 85: a fine not exceeding $10,000, or imprisonment not exceeding 3 years, or both, a further fine not exceeding $1,000 for every day or part of a day the offence continues after conviction, and forfeiture of any article seized.
   Asserted (`sgta-tests-part6-part8.l4`, s 85).
2. **The Act has no defined term "radio-communication equipment".**
   "equipment" and "radio-communication" are separate definitions in s 2; the encoding composes them (FORK 1, pointer below).
   Asserted on a walkie-talkie, a GPS receiver, a wired telephone, a fibre-optic modem and a paperweight (`sgta-tests-s2-s5.l4`).
3. **s 55(2) turns possession into deemed operation until the contrary is proved; s 55(3) makes the occupier guilty and s 55(4) gives the occupier a two-limb defence (not aware AND could not with reasonable diligence have become aware).**
   Asserted.
4. **s 53(1) lists five verbs (establishes, installs, maintains, provides, operates) and then adds "or otherwise infringes the privilege conferred upon the Authority by section 3", while s 3(2)(a) lists ten rights including using, hiring, selling and promoting.**
   Asserted: "using" is outside the five and inside the closing words.
   From 1 Feb 2017 s 53(1) also reaches a person "during the suspension of the person's licence under section 10" (inserted by Act 30 of 2016 section 18; finding 27); `sgta-ta-versions.l4` carries the flag by version.
5. **The 2000 Revised Edition section numbers are printed as margin markers at the end of each section** ("[33" at the end of s 53, "[34" at s 54, "[35" at s 55, "[73" at s 96, "[74" at s 97).
   The pre-2020 instruments cite those numbers: N 1's title ("sections 33, 34(1)(b) and 35") is ss 53, 54(1)(b) and 55.
   The Comparative Table at the end of the deposit is column-garbled in the text extraction ("54 33" and so on read one row out), so the markers, not the table, are the evidence.
6. **s 95 turns on a Broadcasting Act definition with two conjuncts, and has two exceptions** (regulation of a telecommunication system required for a broadcasting service; approval of broadcasting apparatus under s 11).
   Asserted on each combination.
7. **s 84(1) caps a composition at $5,000 and needs an officer specially authorised by name; the Composition of Offences Regulations 2005 (from 11 November 2005) name the 2000 Edition offences 33(1), (3), (4), 34(2), 35(1), (3) among others.**
   Asserted.
8. **s 85 and s 95 carry "[10/2005]", commencing 16 February 2005; ss 54 to 59, 64, 71, 86 to 88, 96 and 98 carry no marker after the 2000 Revised Edition; s 53 carries 30/2016 and Act 25 of 2021; s 2 carries, besides the closing list of five Acts (10/2005, 19/2011, 22/2016, 30/2016, 4/2021), Act 12 of 2020 (wef 1 October 2025) on two definitions and S 26/2022 (wef 13 January 2022) on three, so its last marked amendment is 1 October 2025.**
   The Telecommunications (Amendment) Bill 2004 (lawplain `bills`, B67-2004, as introduced) shows that the 2005 amendment added the daily fine for a continuing offence to the general penalties section (clause 28) and renamed the Broadcasting Act in what is now s 95 (clause 30); the Act's legislative history lists no Notice of Amendments for it.
   Asserted at the edges of 16 February 2005.
9. **N 1 para 2 has two forms: (a) a station that the Authority has permitted to use a band under reg 75 of Rg 5, and (b) localised on-site installation or operation of the Schedule's equipment; from 1 November 2014 it adds (c) and (d), installation and operation of the Second Schedule's white space devices in accordance with the published technical specification.**
   The Schedule's item titles change on 2 January 2008 (items 17 and 18 added) and 1 November 2014 (the "Communication Receivers ... and MMDS Receivers" item is absent from the substituted First Schedule; a Second Schedule is added).
   The other six amendments change bands and power limits only.
   Asserted at the edge of every amendment.
10. **Rg 5 reg 19(1) says a station "may be possessed, established, installed, maintained, provided or operated" if authorised by a licence of one of three kinds; it is not an offence provision and reg 78 never lists it.**
    Reg 65 gives a class licence to a person who possesses or uses a relevant station, defined by connection to public systems (five from the 2002 Revised Edition, six from 1 June 2006), and from 2 October 2009 excludes a telecommunication licensee and adds reg 65A.
    Reg 78's list changes on 1 April 2016.
    Asserted at each edge.
11. **Rg 6 reg 22 was rewritten on 21 July 2005: from "the Authority may ... test that equipment" at the request of a person intending to use it for personal purposes, to "any person intending to use any telecommunication equipment for personal purposes shall not be required to obtain the approval of the Authority provided that" it conforms to the Authority's published standards.**
    The Fifth Schedule from 15 April 2010 lists equipment for which registration fees do not apply; item 3 ("Integrated receiver decoder devices intended for use with second generation digital terrestrial television broadcasting system") was inserted on 25 April 2013.
    Asserted at each edge.
12. **IMDA's list was the first source of the instruments' text that I could reach, and the e-Gazette's copies (finding 23) now check 25 of its 40 texts**; two of the amending instruments were scans, read by OCR, and the Gazette's copies replace the OCR text (finding 23); the base instruments carry the Law Revision Commission's edition headers.
13. **Rg 5 reg 2 defines "reception", "in relation to any radio emission", to include interception (`TA1999-RG5.txt:270`), and reg 68(1) provides that, except as s 42(2) of the Act provides, "no person shall intercept or acquaint himself with the contents of any radio-communication other than those transmitted for general information or for the information of licensees belonging to the same licensed network" (`TA1999-RG5.txt:1133-1136`).**
    Reg 68(2) is the duty of secrecy of a person with access to radio-communications other than those transmitted for general information (`:1137-1140`).
    Asserted (`sgta-tests-rg5-b.l4`).
    What these provisions bear on the television question, if anything, is in `TV-QUESTION.md` and nowhere else.
14. **Rg 6 First Schedule, headed "Telecommunication equipment not requiring approval", has thirteen items: telephone (1), telephone line interface (2), telephone ancillary (3), autodialler (4), auto answering/recording set (5), caller identification equipment (6), security alarm system (7), facsimile transceiver (8), voice band modem (9), EFTPOS/CCAT (10), telex equipment (11), digital leased circuit equipment (12) and "other equipment as determined by the Authority" (13) (`TA1999-RG6.txt:418-434`).**
    Rg 6 Second Schedule item 9 requires a Class Licensee to inform every purchaser or hirer of the need to obtain a licence from the Authority under the Act and the Regulations for the possession, operation, installation or use of that equipment (`TA1999-RG6.txt:503-506`).
    Asserted (`sgta-tests-rg6.l4`).
    Item 10 was first counted `inert` ("blank") by `gen-coverage.py`, because its all-capitals text matched the heading rule although a rule quotes it (`sgta-i-rg6-licensing.l4:586`); the generator now treats the first line of a numbered row as content, and the row is `encoded`.
15. **N 1's Schedule ends with a footnote that exempts "other low power equipment that operate in radio frequency bands other than those listed, but which meet the output power limits specified for the same type of equipment ... as long as both the output power limits and the radio frequency bands are approved by the Authority" (`TA1999-N1.txt:161-164`).**
    It is modelled as `N 1 Schedule footnote: the other low power equipment is exempted from licensing` (`sgta-i-n1-bands.l4:692`), with the Authority's approval of both limits and bands as two plain inputs.
    Asserted.
16. **The deposit's s 2 carries one closing marker list for the whole section, so it cannot say which definition an Act touched.**
    I read clause 2 of the three Telecommunications (Amendment) Bills (lawplain `bills`: B67-2004, B20-2011, B30-2016, each as introduced; the Act's history lists one date for the Second and Third Readings of each and no Notice of Amendments, `TA1999.txt:7134-7143`, `7145-7151`, `7171-7178`) and recorded the result per term in `sgta-ta-vintage.l4`:
    - "broadcasting apparatus" and "broadcasting service" were inserted by Act 10 of 2005, from 16 February 2005.
    - "equipment" and "telecommunication system" were amended by Act 19 of 2011, from 1 February 2012: before that date "equipment" ended "... for telecommunication purposes" and had no words about broadcasting (Bill 20/2011, clause 2(b) and (e)).
      So for any date before 1 February 2012 the deposited consolidation's wording of "equipment" is not the wording in force.
      CORRECTED 2026-11-04 (independent review, D8): this finding first said the pre-2012 words were not encoded because they come from a Bill that is not deposited.
      They are printed in the 2000 Revised Edition, which is deposited ("‘‘equipment’’ includes any appliance, apparatus or accessory used or intended to be used for telecommunication purposes;", `TA1999.20001230.txt:226-227`), and `sgta-ta-versions.l4` quotes those lines with Act 19 of 2011 section 2(b) and flags the wording by version (`TA versions: s 2 "equipment" ends "used or intended to be used for telecommunication purposes"`).
    - "telecommunication service" gained ", including the leasing of a telecommunication cable," from 1 February 2017 (Act 30 of 2016).
    - "telecommunications", "radio-communication" and "Hertzian or radio waves" are named by none of the three Bills.
    - Not read: the s 2 changes made by section 100 of the Info-communications Media Development Authority Act 2016 (lawplain's copy of Bill 21/2016 stops at its own s 2) and by the Statute Law Reform Act 2021 (Bill 45/2020 as introduced has 11 clauses and none on this Act, while the history says its amendments were made by its section 22(9)).
    Asserted (`sgta-tests-act-defs.l4`, 18 assertions); the result is an inference from Bills as introduced, labelled so in the module, except for the 2012 change to "equipment", which is now read from the printed Act and the 2000 Revised Edition (above).
17. **Tests found three defects of mine, and mechanical coverage found two more.**
    - s 45(2) and (3) were written `NOT a OR b`, which L4 reads as `NOT (a OR b)`; a test failed, the code was fixed to `((NOT a) OR b) AND ((NOT c) OR d)`, and the test was kept.
    - My expected value for s 91(3)(a) was wrong (the case in which the Act says the voting rights are NOT exercisable); corrected from the text, not from the code.
    - Three Rg 5 expectations had the arguments in the wrong order; corrected the same way.
    - Coverage found two quotations that stopped one line short (Rg 3 reg 3, line 81; the S 210/2010 locator), and five Act quotations that omitted an opening or closing line (ss 6(5), 25(2), 38(15)(b), 65 and 87); all widened.
    - Three functions of the form `x OR NOT x` (ss 25(4), 26(3), 47(3)) were tautologies that could never fail; they became "the prejudice bars the Authority" functions returning `FALSE`, and unused `GIVEN` parameters in ss 6(1)(a), 16(1)(a) and 79(1)(a) were removed.

18. **The Gazette's 2020 Revised Edition (31 Dec 2021) and the SSO consolidation (2 Oct 2026) are word for word identical in ss 54, 55, 85 and 95.**
    Compared by script on 2026-11-04 after normalising spacing, quotation marks and hyphens: `TA1999.txt:4894-4910, 4911-4934, 5941-5955, 6987-6999` against `TA1999.RevEd2020-printed.txt:3875-3885, 3886-3907, 4696-4707, 5525-5534`.
    The 2000 Revised Edition's ss 34, 35, 65 and 72 differ from them in style ("No person shall" for "A person must not") and, for ss 65 and 72, in the two amendments of Act 10 of 2005 (finding 20).
    This is evidence for the markers inference on the days 16 May 2018 to 1 Oct 2026 (Acts 22 and 30 of 2016 and Act 15 of 2017, which cover the days before, are now deposited); it does not show that no Act in between changed a section and changed it back.
19. **The IMDA file deposited as the Rg 6 "2004 Revised Edition" is not the Gazette's Revised Edition 2004.**
    Word diff against `TA1999-RG6-GAZ-RevEd2004.txt` (page headers stripped): the IMDA reg 10(2) ("$50") and reg 10(4) (payment within 90 days of the registration) are the paragraphs S 478/2005 reg 6 substitutes (`TA1999-RG6-S478-2005.txt:73-82`), while the Gazette's edition has reg 10(2)(a) and (b), "$50 for the first 5 years ... and $50 for every subsequent period of 5 years", and reg 10(4)(a) and (b) (`TA1999-RG6-GAZ-RevEd2004.txt:311-333`); the IMDA arrangement of regulations carries "20. Approval for sale; 21. False or misleading information; Part VI Telecommunication equipment for personal use; 22. Telecommunication equipment for personal use", where the Gazette's has "20. Application for type-approval; 21. Application for registration of equipment; Part VI Testing; 22. Testing of telecommunication equipment for personal use".
    Regs 22(1), the First Schedule and the Second Schedule agree.
    `sgta-i-rg6-licensing.l4` reg 10(2) and (4) follow the IMDA text, which is the text S 478/2005 substitutes: right from 21 July 2005, wrong for 1 Jan 2005 to 20 Jul 2005.
    The Gazette's text for those days is now encoded beside them (`Rg 6 reg 10(2) (Revised Edition 2004)`, `reg 10(4)(a)` and `(b)`, and the dated `Rg 6 reg 10(2) and (4): the class licence fee falls due for each period of 5 years, on the date`; quotes from `TA1999-RG6-GAZ-RevEd2004.txt:311-315, 325-333`; ten assertions at the end of `sgta-tests-rg6.l4`).
20. **Act 10 of 2005 and Act 19 of 2011, as printed, amend the Act in these ways that bear on a receiver.**
    Act 10 of 2005 (first published 16 Feb 2005 at 5:00 pm): section 2(a) inserts the definitions "broadcasting apparatus" and "broadcasting service" by reference to the Broadcasting Act (`TA1999.ACT10-2005.txt:42-47`); section 28 adds the further daily fine to s 65 (now s 85; `:961-964`); section 30 substitutes "Broadcasting Act (Cap. 28)" for "Singapore Broadcasting Authority Act (Cap. 297)" in s 72 (now s 95; `:1188-1190`).
    Act 19 of 2011 (first published 20 Jan 2012, in operation 1 Feb 2012 by S 33/2012 published 31 Jan 2012): section 2(b) substitutes for "telecommunication purposes" in "equipment" the words "telecommunications, including (for the avoidance of doubt) any such appliance, apparatus or accessory capable of being used for the operation of any broadcasting service" (`TA1999.ACT19-2011.txt:49-54`); the Bill's explanatory statement says it is "to clarify that the term includes" such equipment (`TA1999.BILL20-2011.txt:2571-2574`).
    Neither Act amends ss 33 to 36 or 73 of the 2000 Edition (their lists of "Amendment of section" headings, by `grep`).
    Asserted (`sgta-tests-act-versions.l4`, 40 assertions, and the per-term markers in `sgta-tests-act-defs.l4`).
21. **S 263/2006 (Rg 5) is in operation on 1 June 2006 and deems two of its regulations in operation on 1 May 2006** (the Radio Amateur Examination fee, reg 39(2), and the deletion of the Second Schedule; `sgta-i-rg5-amendments.l4:106, 218-232`).
    Among the instruments of `sgta-i-versions.l4` it is the only one with a retrospective element; S 485/2016 (Rg 3) is retrospective as a whole (finding 25).
22. **The Gazette's e-Gazette static host answers a missing file with 403 AccessDenied** (probed once, 2026-11-04, with a deliberately nonexistent name), the same status as a refusal; URLs were therefore not guessed.

23. **Every Gazette copy was compared with the IMDA copy of the same instrument (25 pairs: the two Rg 6 pairs of the morning and 23 more); the IMDA copies carry defects that touch a printed value or word, and the Gazette's text governs.**
    Method: a word diff, and a multiset of the numbers in each text, after setting aside page furniture, the Gazette's banner and the lists of earlier notifications at the foot (`scratchpad/tools/gazette-compare.py`, `gazette-bag.py` and `gazette-numbers.py`, not committed); each difference below was then read in both texts.
    - **S 1/2008 (N 1), IMDA copy:** item 3 reads "57 dBµ/Vm @ 3m" (`TA1999-N1-S1-2008.txt:24`) where the Gazette reads "57 dBµV/m @ 3m" (`TA1999-N1-S1-2008-GAZ.txt:30`); the decimal point is lost in four band edges, "240 15", "300 00", "10 50" and "72 130" (`:43, 45, 49, 67`) for 240.15, 300.00, 10.50 and 72.130 (`-GAZ.txt:54, 56, 61, 81`).
    - **S 265/2006 (N 1), IMDA copy:** "240 15" and "10 50" (`TA1999-N1-S265-2006.txt:33, 38`) for 240.15 and 10.50 (`-GAZ.txt:43, 51`).
    - **S 179/2011 (N 1), IMDA copy:** item 8 reads "All other frequencies 25 W" (`TA1999-N1-S179-2011.txt:29`) where the Gazette reads "25 µW" (`-GAZ.txt:36`), as S 1/2008 and S 252/2013 do.
    - **S 414/2014 (Rg 6), IMDA copy:** "1605 – 1,800 kHz" and "40.500 – 41.00 MHz" (`TA1999-RG6-S414-2014.txt:36, 47`) where the Gazette prints "1,605-1,800 kHz" and "40.500-41.000 MHz" (`-GAZ.txt:39, 49`): the same two values, spelled differently.
    - **S 210/2010 (Rg 6), a difference of wording:** clause 8 inserts the new words after "regulation 20" "wherever they appear" in the IMDA copy (`TA1999-RG6-S210-2010.txt:140`) and "in paragraphs (1) and (2)" in the Gazette (`-GAZ.txt:145-146`).
      It changes nothing the encoding states: regulation 21 as S 478/2005 substitutes it has two paragraphs, and "regulation 20" appears once in each (`TA1999-RG6-S478-2005-GAZ.txt:177-184`).
    - **S 461/2009 (Rg 5), a difference of wording:** clause 9 deletes "or a network (spectrum) licence" "in the following provisions" in the IMDA copy (`TA1999-RG5-S461-2009.txt:133`) and "in the following regulations" in the Gazette (`-GAZ.txt:166`); the list that follows ("Regulations 10(d), 11(2) and 12(1)") is the same.
      Nothing else in the instrument turns on the word.
    - **S 685/2011 and S 686/2011:** IMDA's PDFs are page images, and the OCR text of them carried errors that I had quoted: "No. S 000" for the number, "J." for "1.", "74.-(1)" for "7A.-(1)", "(6)" for "(b)", "Gi)" for "(i)", "S$" for "S", and in clause 6(a) of S 685/2011 "reference and inserting" for "references and substituting" (`TA1999-RG3-S685-2011-OCR.txt` against `TA1999-RG3-S685-2011.txt:94-99`).
      The Gazette's PDFs have text layers (`pdftotext -layout`, no OCR); they replace the OCR text as `TA1999-RG3-S685-2011.txt` and `TA1999-COMP-S686-2011.txt`, and the OCR text is kept as `-OCR.txt` for the record, not quoted.
      Every quotation of the two instruments in `sgta-i-rg3-amendments.l4`, `sgta-i-rg3-class.l4` and `sgta-i-comp.l4` was re-pointed at the aligned Gazette lines by script (`scratchpad/tools/remap-ocr.py`) and passes `srcrefs --strict`; the encoded rules did not change, because every fee, amount and date is the same in both texts (the Ninth Schedule's "$200" and "No fee" rows, the commencement day 28 December 2011, S 686/2011's regulation 2).
    - **Everything else agrees**: no other number, date, amount or item differs; the rest is hyphenation at line ends, page furniture, capital letters ("(B)" for "(b)" in the IMDA copies of S 591/2003 and S 651/2004), the order of words that a table's column layout moves, and the footnote lists.
      The IMDA copies of S 20/2011 and S 100/2016 are word for word the Gazette's (zero differences).
    What I changed: the values keyed in `sgta-i-n1-bands.l4` for S 1/2008 item 3 and S 179/2011 item 8 now follow the Gazette ("57 dBµV/m", "25 µW"); they had been kept as the IMDA copy printed them, defects included (the earlier note called them "kept as printed", and that was wrong for an extraction defect); and the band keys of the S 414/2014 vintage in `sgta-i-rg6-amendments.l4` follow the Gazette's spelling.
    The `-- src:` quote lines of the other IMDA copies stay the IMDA lines as they are (`srcrefs --strict` checks them against the IMDA text), with each module saying where the Gazette differs.
24. **S 525/2001 is the Schedule of the 2002 Revised Edition, and it fills the N 1 gap from 17 October 2001 to 31 December 2002.**
    S 525/2001 (first published and in operation 17 Oct 2001) deletes the words "in-building or" from paragraph 2(b) of the Notification of 2001 (S 115/2001) and substitutes a Schedule of 16 items (`TA1999-N1-S525-2001.txt:21-34`).
    The Revised Edition 2002's history line reads "[G.N. Nos. S115/2001;S 525/2001]" (`TA1999-N1.txt:166`), and the two Schedules were compared on 2026-11-04 as sequences of words and figures: the same 16 items, bands and limits; only the way item 7's sub-items wrap across the page differs, and the footnote is word for word the same.
    Before this, `sgta-i-versions.l4`, `sgta-i-n1-exemption.l4` and `sgta-i-n1-bands.l4` answered NOTHING for conduct before 1 January 2003 (the earlier comment "already incorporates two earlier amendments (S 115/2001, S 525/2001)" was a mistake: S 115/2001 is the Notification as made).
    Now they answer from 2 March 2001, the day S 115/2001 came into operation (finding 27), and from 17 October 2001 on S 525/2001's Schedule, including item 11(e) "TV Receivers/ Radio Systems" (`TA1999-N1-S525-2001.txt:114`) and item 15, "Communication Receivers (excluding scanning devices) and MMDS Receivers" (`:148-153`).
    What the seat does with those days is in `TV-QUESTION.md`.
    N 1 before 2 March 2001 stays NOTHING (the Notification had not begun).
25. **The extra instruments, read in full.**
    - S 525/2001: finding 24.
    - S 78/2017 (first published 1 Mar 2017, in operation 1 Apr 2017): inserts item 18, "Intelligent Transport System", in N 1's First Schedule, a 5.9 GHz vehicle-to-roadside radio (`TA1999-N1-S78-2017.txt:28-45`); it amends no other item.
      Encoded (`sgta-i-n1-exemption.l4`, `sgta-i-n1-bands.l4`, the new `N 1 schedule item` `Intelligent Transport System` in `sgta-nouns.l4`; assertions at 31 Mar and 1 Apr 2017).
    - S 485/2016 (Rg 3, deemed in operation 1 Oct 2016): deletes the definition of "Authority" from regulation 2 (`TA1999-RG3-S485-2016.txt:26-28`); S 685/2011 had inserted it on 28 Dec 2011.
      Rg 3 is the class-licence regulations; the amendment concerns that definition only.
      It is retrospective: first published 3 Oct 2016 at 5.00 pm, "deemed to have come into operation on 1 October 2016" (`TA1999-RG3-S485-2016.txt:3, 21-23`), so a reader on 1 or 2 Oct 2016 still sees the definition that S 685/2011 inserted.
      Encoded as a function of both days (`sgta-i-rg3-s485-2016.l4`; Rg 3 has no version table in `sgta-i-versions.l4`).
    - S 23/2011 and S 24/2011 (in operation 21 Jan 2011): delete a reference to subsection 10.2 of the Code of Practice for Competition in the Provision of Telecommunication Services 2005 from paragraph 2 of three notifications that designate licensees (facilities-based and services-based operators) under s 32A(3) (`TA1999-DTL-S23-2011.txt:28-33`; `TA1999-DTL-S24-2011.txt:30-47`).
      They concern designated licensees only.
      First published 17 Jan 2011, in operation 21 Jan 2011; encoded as functions of both days (`sgta-i-dtl-notifications.l4`); the notifications they amend (S 86/2005, S 233/2005, S 390/2007) were deposited from the second list (finding 27); the Code (S 87/2005) is not deposited.
    - S 76/2007 (Rg 3), which IMDA lists and the Gazette copy of which was also fetched: its Gazette copy differs from the IMDA copy only in a line-end hyphenation; already encoded.
    - S 76/2005, the commencement notification of Act 10 of 2005: brings the whole Act into operation on 16 Feb 2005 except sections 10 and 11 (`TA1999.S76-2005.txt:23-25`).
      Section 10 repeals s 19 and section 11 amends s 20(5) (`TA1999.ACT10-2005.txt:267-271`); their own commencement day is not in a deposited text.
      It agrees with the Act's own history entry, and it settles the commencement question that was open (`sgta-ta-versions.l4`).
26. **Every published day in `sgta-i-versions.l4` is now read from the Gazette.**
    The 29 index dates the team lead gave agreed with the "First published in the Government Gazette, Electronic Edition, on" line inside each PDF, and each effective day agreed with the commencement clause of the Gazette text.
    Twelve rows of that file have a published day earlier than the effective day, so they answer differently for a reader between the two days (S 100/2016, S 20/2011, S 263/2006, S 707/2005, S 252/2013, S 651/2004, S 478/2005, S 210/2010, S 251/2013, S 726/2014, S 725/2014, S 78/2017); one has a published day later than its effective day, the Rg 5 row for S 374/2001 (first published 1 Aug 2001, deemed in operation 9 Jul 2001; finding 28).
    CORRECTED 2026-11-04 (independent review, D9): this finding first said that no row of the file is retrospective.
    Measured by script over the file's 30 rows that carry both days (2026-11-04): 12 have the published day earlier than the effective day, 17 the same day, 1 later (S 374/2001, `sgta-i-versions.l4:58`).
    The retrospective instruments are therefore S 374/2001 (Rg 5; 23 days), S 549/2012 of the Broadcasting Act and, under this Act, S 485/2016 (Rg 3), first published 3 Oct 2016 and deemed in operation on 1 Oct 2016, which `sgta-i-rg3-s485-2016.l4` models with both days (S 263/2006 has a retrospective element inside it, finding 21).
    `sgta-tests-i-versions.l4` has 171 assertions (143 when this finding was written; the Rg 5 table grew by the 2001 rows, finding 28), each computed from the rule as the module states it and not read back from the L4.
27. **The second list of exact URLs (team lead, 2026-11-04): N 1 as made, the two 2016 Acts, and the designation notifications.**
    Eleven PDFs fetched, one GET each, 5 seconds apart, commons User-Agent, each 200 with a text layer; the date the team lead gave agreed with the "First published" line inside every PDF (`scratchpad/gazette-dl3/log.tsv`).
    - **S 115/2001, N 1 as made** (first published 2 Mar 2001 at 5:00 pm, in operation 2 Mar 2001; `TA1999-N1-S115-2001.txt:30-32`).
      Paragraph 2(b) reads "the in-building or localised on-site installation or operation"; the Schedule has 15 items (no Short Range Radar), limits printed in "dB", and para 2(a) names the Telecommunications (Radio-communication) Regulations 2001 (G.N. No. S 114/2001), the Rg 5 as made, which the third list supplied (finding 28).
      Item 11(e) is "TV Receivers and Radio Systems" and item 15 "Communication Receivers (excluding scanning devices) and MMDS Receivers".
      Encoded as a vintage of N 1 (`sgta-i-n1-exemption.l4`: para 2 as made and the 20-entry list; `sgta-i-n1-bands.l4`: all 62 band lines as printed; `sgta-i-versions.l4`: the first N 1 row), so N 1 now answers from 2 Mar 2001.
    - **Act 22 of 2016** (the Info-communications Media Development Authority Act 2016; Acts Supplement No. 19 of 2016, first published 29 Sep 2016 5:00 pm; `TA1999.ACT22-2016.txt`) and its commencement notification **S 461/2016** (first published 29 Sep 2016 5.00 pm): the Act is in operation on 1 Oct 2016 except sections 89, 90(1) and 96(v) (2 Oct 2016).
      Its section 100 amends the Telecommunications Act (2000 Ed.): replaces the definitions of "Authority" and "Chief Executive", deletes that of "Media Development Authority of Singapore", deletes ", after consultation with the Media Development Authority of Singapore," in ss 21(1A) and 27(1A), inserts s 59A, deletes s 64(3) and amends s 69C(2)(a) (`TA1999.ACT22-2016.txt:3626-3716`); it touches none of ss 33 to 36, 65, 72 or 73, nor "equipment".
    - **Act 30 of 2016** (the Telecommunications (Amendment) Act 2016, "No. 30 of 2016" on its face; Acts Supplement No. 2 of 2017, first published 9 Jan 2017 5 pm, though the supplement's own date line reads "FRIDAY, JANUARY 13"; `TA1999.ACT30-2016.txt`) and **S 14/2017** (first published 13 Jan 2017 5 pm), which brings it into operation on 1 Feb 2017.
      Its sections 1 to 20 are word for word clauses 1 to 20 of Bill 30/2016 as introduced (compared by script, ratio 1.0).
      Section 2 adds five definitions and the leasing words in "telecommunication service"; **section 18 amends s 33(1) (now s 53(1)) by inserting ", or during the suspension of the person's licence under section 8"** (`TA1999.ACT30-2016.txt:1063-1068`), which the 2026 consolidation prints with the marker [30/2016]; it does not touch ss 34, 35, 65, 72 or 73.
      The numbers the team lead's mapping gives are confirmed on the faces: Act 22 of 2016 is the IMDA Act (Acts Supplement No. 19 of 2016), Act 30 of 2016 the Telecommunications (Amendment) Act (Acts Supplement No. 2 of 2017); the only mismatch is the supplement's date line.
      Both are versions in `sgta-ta-versions.l4`; the first Act after Act 30 of 2016 on the Legislative History, Act 15 of 2017 (s 53(6), 23 May 2017), was deposited later the same day (finding 28).
    - **The designation notifications** under s 32A: S 86/2005 (facilities-based operators; published 18 Feb 2005, in operation 4 Mar 2005), S 233/2005 (Pacific Internet Limited; 7 Apr 2005), S 390/2007 (Syniverse Technologies Private Limited; 20 Jul 2007 at 11:00 am), S 35/2012 (a single Notification that cancels those three; published 31 Jan 2012, in operation 1 Feb 2012), S 192/2012 (10 May 2012, in operation 11 May 2012) and S 521/2017 (20 Sep 2017, in operation 22 Sep 2017; made by the Info-communications Media Development Authority).
      Encoded with S 23/2011 and S 24/2011 as functions of both days in `sgta-i-dtl-notifications.l4` (109 assertions in `sgta-tests-more-notifications.l4`, computed from the stated rule).
      The Code of Practice S 87/2005 is still not deposited.

28. **The third list of exact URLs (team lead, 2026-11-04): Rg 5 as made and its 2001 amendments, the 2001 Composition Regulations, and the Companies (Amendment) Act 2017.**
    Seven PDFs fetched, one GET each, 5 seconds apart, commons User-Agent, each 200 with a text layer; the date the team lead gave agreed with the "First published" line inside every PDF (`scratchpad/gazette-dl4/log.tsv`).
    - **S 114/2001, the Telecommunications (Radio-communication) Regulations 2001** (47 pages; first published 2 Mar 2001 5:00 pm, in operation 2 Mar 2001; `TA1999-RG5-S114-2001.txt`), which is Rg 5 before the 2002 Revised Edition.
      Compared by script with `TA1999-RG5.txt`, regulation by regulation (80 on each side), after setting aside case, punctuation other than the parentheses of paragraph labels, hyphenation and page furniture: **59 regulations are the same words**; 21 differ (regs 1, 9, 20, 26, 28, 29, 36, 38, 40, 53, 54, 60, 61, 66, 67, 70, 72, 74, 76, 79 and 80).
      Regs 26 and 28 differ because S 450/2001 amends them; reg 20 only reorders its paragraphs; reg 60 only labels its two limbs; reg 9 divides paragraph (1) into limbs and changes "persons engaged" to "person engages"; regs 1, 79 and 80 are the citation, a heading, and the revocation of the Radiocommunication Regulations (Rg 3 of the 2000 Edition), which the Revised Edition drops; regs 53, 61, 67, 70, 72 and 74 drop "or its"; reg 40 says "one year" as made and "12 months" in the Revised Edition; reg 29 cites the Ship Station Operators Regulations as Rg 2 as made and Rg 1 in the Revised Edition; reg 76 as made has no "2000 (G.N. No. S 412/2000)".
      Regs 36(b) ("in exceptional circumstances"), 38, 54, 66 and 74 differ in words that neither S 374/2001 nor S 450/2001 changes, and the Revised Edition's history line names only S 114/2001, S 374/2001 and S 450/2001 (`TA1999-RG5.txt:1512`); I take those to be the revision's own wording and have not verified that.
      The First Schedule differs only in layout and in what S 374/2001 and S 450/2001 do; the Second and Third Schedules are the same words.
      The table is in `sgta-i-rg5-as-made.l4`, with every line of S 114/2001 quoted (1,636 quote lines in that module).
    - **S 339/2001** (Minister; first published 9 Jul 2001, in operation 9 Jul 2001) inserts Part II item 11, "Fixed Wireless Broadband Network"; **S 373/2001** (a Corrigendum, 1 Aug 2001) says S 339/2001 "which have been published in error are to be treated as cancelled"; **S 374/2001** (made by the Authority; 1 Aug 2001) makes the same insertion and is "deemed to have come into operation on 9th July 2001".
      So S 374/2001 is retrospective by 23 days, and a reader between 9 and 31 Jul 2001 saw S 339/2001's insertion that was then cancelled; both are in the version rule (`sgta-i-versions.l4`) with their two days.
      **S 450/2001** (Amendment No. 2; 18 Sep 2001, in operation 18 Sep 2001) substitutes reg 26(4) (the fees the Authority may reduce now include the licence fees of paragraph (1)), adds reg 28(1)(d) "Fixed Wireless Network Licence", deletes "Broadband" in Part I item 4 and Part II item 11 and "Ground" in Part II item 7(c), and inserts Part II item 12 "Special Purpose Station" ($50).
      None of the four touches reg 65 or any other provision the seat reads.
    - **What changed in the encoding.**
      Rg 5 now has a version from 2 Mar 2001 (before: from 1 Jan 2003, Fork B), so the dispatcher answers for conduct from 2 Mar 2001.
      Rg 5 functions that take a date now start on 2 Mar 2001 where the regulation has the same words as made (regs 24, 57, 64, 65, 78) or differs only in the order of its paragraphs (reg 20), and reg 65A answers FALSE from 2 Mar 2001 until S 461/2009 (it did not exist as made); reg 76 answers with its as-made wording before 1 Jan 2003.
      Functions of the other Rg 5 modules take no date and answer on the Revised Edition's words; `sgta-i-rg5-as-made.l4` says, regulation by regulation, whether those are the 2001 words.
      Two case expectations at 31 Dec 2002 changed from NOTHING to an answer.
    - **S 516/2001, the Telecommunications (Composition of Offences) Regulations 2001** (first published and in operation 15 Oct 2001; `TA1999-COMP-S516-2001.txt`), made under s 64 of the Act, revoking the Composition Regulations 2000 (S 260/2000, not deposited).
      Reg 2(a) names ss 29(1) and (3), 31(1), 32, 33(1), (3) and (4), 34(2), 35(1) and (3), 39, 40(1), 45, 48, 49(1), (2) and (3) and 52 of the Act (2000 Edition numbers); reg 2(b) names regs 24, 31, 32, 33, 35(2), 36, 54, 56(2), 57, 63(1), (2) and (3), 64, 67, 68, 69 and 70 of S 114/2001.
      The 2005 Regulations (S 706/2005) replace it from 11 Nov 2005 and name instruments as wholes.
      Encoded in `sgta-i-comp.l4` as a vintage from 15 Oct 2001 to 10 Nov 2005; before 15 Oct 2001 the answer is NOTHING, because S 260/2000 is not deposited.
    - **Act 15 of 2017, the Companies (Amendment) Act 2017** ("No. 15 of 2017" on its face; Acts Supplement No. 17 of 2017, first published 30 Mar 2017 5 pm, 114 pages; `TA1999.ACT15-2017.txt`).
      Section 1: it "comes into operation on a date that the Minister appoints by notification in the Gazette"; the notification is not deposited, so 23 May 2017 is the Legislative History's day (`TA1999.txt:7181-7190`) and the published day is assumed to be the same.
      A search of the whole text for "Telecommunications Act" finds one place, **section 53(6)**: it inserts "or 211I" after "section 210" in sections 32J(3)(a) and 32L(1)(b) and (2)(a) (`TA1999.ACT15-2017.txt:4217-4219`).
      The consolidation prints the marker 15/2017 three times and nowhere else (`TA1999.txt:4581`, `:4704`, `:4728`, each beside 19/2011 and 40/2018), which is the same number of places.
      It touches none of ss 2 "equipment", 33 to 36, 65, 72 and 73 (2020 numbers 2, 53 to 56, 85, 95 and 96).
      So `sgta-ta-versions.l4` now has Act 15 of 2017 as a version whose flags equal Act 30 of 2016's, on the printed text, and the texts answer for conduct up to 15 May 2018; the row after it stands for Act 26 of 2018 (16 May 2018) and the Acts after, which are not deposited ("Acts and instruments whose source was not obtained", under Coverage).

29. **Correction (team lead, 2026-11-04): S 333/2004 is a version of Rg 1, not a footnote to it.**
    My earlier account of the Broadcasting Act folder's deposits listed S 333/2004's replacement of reg 27(1) and (2) without saying what it did, and the Rg 1 table in `sgta-tv-ba-schedule.l4` had no row for it, so the seat treated Rg 1 as one unit from 29 Feb 2004.
    Read again from `BA1994-S333-2004.txt` (made 11 Jun 2004, first published 15 Jun 2004 5:00 pm, in operation 21 Jun 2004; the PDF's sha256 begins 68bf17f881f90e33, as the team lead's did): cl 12(a) deletes reg 27(1) and (2) and substitutes a paragraph about where to apply; cl 11(a) does the same to reg 23(1) and (2); cl 14 inserts reg 29A; cl 2 replaces the definitions of the two receivers; cl 3, 8 and 10 delete regs 3, 4, 12, 14 and 16 to 22.
    The Rg 1 table now has three rows, on both axes, and a function says what each version says in terms about a licence for a kind of receiver in a place; the text of the corrected account, the table and what does and does not change are in `TV-QUESTION.md` section 12.
    This file records only that the correction was made, that every quoted fragment of the new function is checked against the deposited files by script, and that the Telecommunications Act provisions and their tests are untouched.

30. **Independent review D11 (2026-11-04): `s 2: this is equipment` returns a BOOLEAN, not a MAYBE BOOLEAN, and I left it.**
    The review's point is right: "equipment" is defined by "includes", and an inclusive definition never says no, so FALSE for an item that is not used for telecommunications (a paperweight) is a "no" the Act does not give; the Broadcasting Act encoding returns MAYBE BOOLEAN for such definitions.
    Measured 2026-11-04 over `sgta-*.l4` (non-comment lines, the definition heads excluded): the function has 1 caller (`s 2 (composed): the equipment is radio-communication equipment`); that has 2 callers in `sgta-part6-offences.l4` (`s 54(1)(b): the person contravenes` and `s 55(1): the person is guilty of an offence`), which feed the two outcomes of s 54(2) (Readings A and B) and, through the seat's helpers, every answer the seat gives.
    Before today's 2000-Edition module the chain was 8 rule call lines in 3 modules and 32 assertion lines in 2 test files; with the mirror functions and dispatchers of `sgta-part6-2000ed.l4` it is 18 rule call lines in 4 modules and 392 assertion lines in 3 test files (360 of them the equivalence grid added today).
    The change is not local: the outcomes are an `Offence outcome` with no way to say "the Act does not say", so the type of every seat function that returns one, the seat's ten exports and the 360 case assertions would carry the new case.
    No TV answer turns on it: the receiver is used for reception, which is a telecommunication (`s 2: the equipment is used or intended to be used for telecommunications` is TRUE for it), so the function is TRUE for every kind of receiver the seat asks about, whichever type it returns.
    So the change would move no TV answer and would touch a layer that states the answer; I left it and recorded it here.
    What it does leave wrong: for equipment not used for telecommunications the encoding says FALSE where the Act is silent (`sgta-tests-s2-s5.l4` asserts `a paperweight` is not equipment).
31. **Independent review G1 (2026-11-04): the Revised Edition 2000's ss 34, 35 and 36 are now quoted and encoded, and the seat picks them by version.**
    `sgta-part6-2000ed.l4` quotes `TA1999.20001230.txt:1246-1287` and encodes the same rules as ss 54, 55 and 56 on the 2000 words (the words differ only in drafting form: "No person shall" for "A person must not", "shall be deemed" for "is deemed", "It shall be a defence" for "It is a defence", "dwelling-house").
    No deposited Act amends these sections (a search of Acts 10 of 2005, 19 of 2011, 22 of 2016, 30 of 2016 and 15 of 2017 for any amendment of section 34, 35 or 36 finds none), and the 2020 consolidation prints their former numbers alone, with no Act number beside them (`TA1999.txt:4907, 4931, 4949`), so the 2000 words are the text printed for every version from 30 Dec 2000 to 15 May 2018.
    Three dispatchers (`s 34(2) or s 54(2): the outcome, on Reading A, in the text the version prints`, the same for Reading B, and `s 35(1) or s 55(1): ...`) pick the words by `Act text version`; the seat calls them.
    The outcomes still name "section 54(2)" and "section 55(1)", the 2020 numbers, because the seat answers in the numbers of the Act as it is today.
    Tests: `sgta-tests-part6-2000ed.l4`, 545 assertions: the hand-written expectations of ss 54 to 56 repeated for ss 34 to 36, a grid on which each 2000 function must give the 2020 function's answer (3 pieces of equipment, 6 holdings, the Boolean facts), and the dispatchers for all eight versions.
    Effect on the seat: none (the 360 case assertions pass unchanged, measured after the wiring).
32. **Independent review D10, D8, D9, G2 (2026-11-04): locators and labels.**
    The review found 17 locator-level mismatches of 8 kinds; those on the TA side are fixed: M5 (`sgta-i-rg5-licences.l4`, reg 30 ended on reg 31's heading: now 741-742), M6 and M7 (N 1 item 16 cut mid-row in `sgta-i-n1-exemption.l4` and `sgta-i-n1-bands.l4`: the rest of the row is now quoted, `TA1999-N1:157-158` and `TA1999-N1-S525-2001:159-161`), M8 (labels: an enacted Act prints "28. Section 65 ... is amended", so "Act 10 of 2005 clause 28" is now "section 28", and likewise for Acts 19 of 2011 and 30 of 2016, in the modules, this file and TV-QUESTION.md; a Bill's clause is still a clause).
    M1 to M4 are in the Broadcasting Act encoding (`sgba-i-rg1.l4`) and are the Broadcasting Act encoder's.
    G2: `srcrefs-all.sh` now runs `srcrefs.py --strict` on the three `sgta-tv-*` modules, but they carry no `src:` quote lines or `@ref` locators (they cite deposited texts in comments as FILE.txt:N), so that run finds 0 lines in each and checks nothing; the check that does bear on them is the new `check-tv-citations.py` (every FILE.txt:N locator in them and in TV-QUESTION.md must exist, and every quoted fragment of the Rg 1 table must be in the deposits), which `srcrefs-all.sh` also runs.
    It does not check that a locator names the right provision.
    D8 and D9 are the CORRECTED notes in findings 16 and 26.

33. **Follow-up Part 2 (a), 2026-11-04: the TAS-era Order O 3, and the fork on what section 30 of the TAS Act said.**
    The Telecommunication Authority of Singapore (Exemption in respect of Specified Equipment) Order (Cap. 323, O 3) is deposited twice: S 549/1998 as made (made 11 Nov 1998 under s 130 of the TAS Act, first published 11 Nov 1998 5:00 pm, "shall come into operation on 12th November 1998") and the 1999 Revised Edition (1 Jul 1999).
    Paragraph 2 exempts "all persons" from "section 30 (1) to (5) of the Act" in respect of equipment approved for sale under reg 24(1) of the Dealers Regulations (Rg 7), and of Fifth Schedule equipment that meets the published standards.
    It survives by TA s 98(2) ("until it is revoked or repealed by subsidiary legislation made under this Act", `TA1999.txt:7097-7102`), and the 2010 Subject Index lists it (`TA1999-AID-INDEX2010.txt:9717-9721`, deposited as an aid and quoted in `sgta-i-o3-1998.l4`; an index as at 1 June 2010, finding 40); no revocation has been found, which is the result of a search and not proof.
    The text of section 30 of the TAS Act is not held (the source-not-obtained table above), so `sgta-i-o3-1998.l4` carries a fork, `What section 30 of the TAS Act provided`, with three values.
    On "approval-before-use" the Order is an exemption from an approval requirement and does not reach possessing or operating equipment; on "the prohibition on possessing or operating equipment" limb (a) would exempt every person in respect of equipment whose type was approved for sale under reg 24(1); with the text not held both functions answer NOTHING.
    The evidence in hand for the first branch is extrinsic and was read by the independent reviewer, not by this encoder: clause 6 of the Telecommunication Authority of Singapore (Amendment) Bill 1998 would have amended "section 30(1) of the principal Act" by replacing "public telecommunication" with "telecommunication system", the wording of s 9(1) of the 2000 Edition of this Act.
    One trap is recorded in the module header: the Order's "Fifth Schedule" is the Fifth Schedule of Rg 7 (1999 Ed.), "TELECOMMUNICATION EQUIPMENT NOT REQUIRING APPROVAL"; in Rg 6, which replaced Rg 7, the counterpart is the FIRST Schedule (`TA1999-RG6.txt:413-420`), and Rg 6's Fifth Schedule is a fee table (`TA1999-RG6.txt:581-584`).
    The seat does not consult O 3, no answer changed, and the reservation is named in `TV-QUESTION.md` section 8.
    Tests: `sgta-tests-1999-regs.l4`.

34. **Follow-up Part 2 (b), 2026-11-04: the 1999 Revised Editions of Rg 7 (Dealers) and Rg 3 (Radio-communication), as vintages before the Rg 5 and Rg 6 tables.**
    Both are the e-Gazette's copies of the Revised Edition of 1 Jul 1999 (Rg 7: 865 lines; Rg 3: 1,381 lines), quoted in full, one block per regulation and schedule, with a function for each operative regulation: `sgta-i-rg7-1999.l4` (34 regulations and 5 Schedules) and `sgta-i-rg3-1999.l4` (60 regulations and 4 Schedules).
    The name "Rg 3" in this encoding is the Class Licences Regulations of the 2002 Revised Edition; the 1999 text is always "Rg 3 (1999 Ed.)" and its stem is `RADIO99`, its folder `telecommunications-radio-communication-regulations-1999`.
    Start: both answer from 1 Dec 1999, the day the Telecommunications Act 1999 came into operation (s 3(1)); s 98(2) continues them.
    End of Rg 3 (1999 Ed.): 1 Mar 2001, read from reg 80(1) of S 114/2001, "The Radio-communication Regulations (Cap. 323, Rg 3) are revoked" (`TA1999-RG5-S114-2001.txt:1548-1549`), in operation 2 Mar 2001, so the Rg 5 table (NOTHING before 2 Mar 2001) and the new table tile; a test pins both sides of 1 and 2 Mar 2001.
    End of Rg 7 (1999 Ed.): 1 Apr 2003, now READ (Part 3, finding 39): reg 26 of S 185/2003 says "The Telecommunication (Dealers) Regulations (Rg 7) are revoked." and reg 1 puts those Regulations in operation on 2nd April 2003 (`TA1999-RG6-S185-2003.txt`).
    When this finding was first written the end day was an assumption (the 2004 Revised Edition of Rg 6 prints `[2nd April 2003]`, `TA1999-RG6.txt:66`, and contains no provision revoking Rg 7, and S 185/2003 was not deposited); the assumption is withdrawn and the module and the version row say so.
    The version rows are `Rg 3 (1999 Ed.): ...` and `Rg 7 (1999 Ed.): ...` in `sgta-i-versions.l4`; the published day is the Edition's, 1 Jul 1999, assumed.
    Amendments after 1 Jul 1999: S 362/2001 is held for Rg 7 (finding 39); any other is unknown (source-not-obtained table).
    NOT wired into the seat: wiring them would change the seat's output for conduct from 1 Dec 1999 to 1 Mar 2001 (finding 36 says what).
    Tests: `sgta-tests-1999-regs.l4` (178 assertions with O 3 and the classes of licence), and the evaluation differential `sgta-tests-eval-1999-2024.l4` (494 assertions on 143 boolean wrapper functions: see the Functions paragraph in the Modules section).

35. **Follow-up Part 2 (c), 2026-11-04: the 2023 and 2024 instruments.**
    S 588/2023 (N 1): first published 28 Aug 2023, in operation 1 Sep 2023 except paragraphs 2 and 3(a), which rename the sections the Notification names as "sections 53, 54(1)(b) and 55" and are deemed in operation on 31 Dec 2021; deletes "localised on-site"; replaces First Schedule items 2, 3, 5 and 8 to 15 and Second Schedule items 1 to 3.
    Item 11(e) is still "TV Receivers/ Radio Systems"; item 14 is now "Global Navigation Satellite Systems Receivers" and item 13 "Wireless LAN, RFID or Low Power Devices"; a new two-date function gives the sections the Notification names; new vintages in `sgta-i-n1-exemption.l4` and `sgta-i-n1-bands.l4`; a new row in the N 1 version table.
    S 589/2023 (Rg 6): first published 29 Aug 2023, in operation 1 Sep 2023 except paragraph 5 (statute citations), deemed from 31 Dec 2021; new Fifth Schedule item 1 vintage and a function of the words replaced; a new Rg 6 version row.
    S 560/2024 (Composition): first published 28 Jun 2024, in operation 1 Jul 2024; reg 2(f) now ends "as in force before 1 July 2024" and new reg 2(h) names reg 6 of the Wiring Work Regulations 2024; a new vintage in `sgta-i-comp.l4`.
    S 381/2024: in operation 30 Apr 2024; it exempts the sale, offer for sale and possession for sale of an ERP 2.0 "in-vehicle unit" from s 54(1)(a) and from the Dealers Regulations, with an exception for sales to the Land Transport Authority; it says nothing of possession or use by a purchaser and names no broadcast receiver; new module `sgta-i-erp-s381-2024.l4`.
    S 559/2024 and S 852/2024: the Wiring Work Regulations 2024 (first published 28 Jun 2024, in operation 1 Jul 2024) and their amendment (first published 8 Nov 2024, in operation 11 Nov 2024; adds a qualification to the First Schedule); new module `sgta-i-ww-2024.l4`.
    They REPLACE the Internal Wiring Regulations 2005 (S 479/2005) from 1 Jul 2024: reg 10(1) reads "Revoke the Telecommunications (Internal Wiring) Regulations 2005 (G.N. No. S 479/2005)", and the module records the 2005 Regulations' end.
    Reg 10 has only the revocation and a saving for optical fibre experience; the text has no provision continuing a licence granted under the 2005 Regulations, and none is encoded.
    The minimum specified period in reg 3(6), "a cumulative period of at least one year", is read as 365 days (assumed, not ruled; a leap year has 366).
    None of the six moves an answer: the seat consults N 1 only for whether item 11(e) is named, which it still is.
    Tests: `sgta-tests-2023-24.l4` (159 assertions).

36. **Follow-up Part 2 (d), 2026-11-04: the Acts after Act 15 of 2017, and what the seat would have to change to use them.**
    Seven Acts amend the Telecommunications Act and were deposited and encoded in Part 2 (the table in the Acts subsection): `sgta-i-acts-after-2017.l4`, 94 assertions in `sgta-tests-acts-after-2017.l4`; Part 3 added Act 31 of 2022 and G.N. No. S 26/2022 (finding 38), and the test file now has 131.
    None amends s 34, 35, 36, 65, 72 or 73 of the 2000 Edition (ss 54, 55, 56, 85, 95 and 96 today) or the definitions of "equipment", "radio-communication" or "broadcasting apparatus"; Acts 4 of 2021 and 12 of 2020 amend s 2 but other definitions ("owner", "common property"); Act 25 of 2021 changes "leave" to "permission" in s 33(7), now s 53(7), the one provision on the chain.
    The decision NOT taken: the seat's version table (`sgta-ta-versions.l4`) still has the one row `as amended by Acts after Act 15 of 2017 that are not deposited`, whose flags are the same as the consolidation's for the days it covers.
    Replacing it by rows for the seven Acts would make the seat's tier "on the texts deposited" answer, from the Acts' own texts, the days 16 May 2018 to 1 Oct 2026 that it now answers NOTHING for (the tier "also on the markers" already answers them from the consolidation's margin markers; I have not run the wiring, so I do not claim the two tiers would then agree on every case), and would change the exported "what the answer rests on" text for those days.
    That is a change of the seat's output and of what two case assertions expect, so it was NOT made; it is the team lead's call.
    The same holds for the 1999 Rg 3 and Rg 7 and the 2023 and 2024 instruments: the seat does not consult them.
    The statement "no text of the Acts after Act 15 of 2017 is deposited" was false from the moment the seven were deposited, so its three places were corrected in wording only (finding 37).
    Act 31 of 2022 and G.N. No. S 26/2022, not obtained in Part 2, were obtained in Part 3 (finding 38).
    Act 15 of 2019's own repeal of s 45 and Act 40 of 2018's insolvency references are encoded as strings of what each changes, not as rules: they do not bear on any question the encoding answers.

37. **Written claims corrected in the quarantined files, 2026-11-04 (wording only; no answer moved).**
    `sgta-tv-seat.l4` (the header comment on the days from 16 May 2018 and the `what the answer for the case rests on` string for the bucket row), `sgta-tv-cases.l4` (the two assertions that expect that string) and `TV-QUESTION.md` section 8 said "not deposited" of the Acts after Act 15 of 2017; they now say that seven are deposited but not wired in, and say which two are not obtained.
    The same statement stood in comments of `sgta-ta-versions.l4` (the row comment and the comment on the s 33(1) flag) and of `sgta-tests-act-versions.l4` (a section title and a comment); those are corrected too, comments only, and the constructor name is left as it is because the seat uses it.
    `TV-QUESTION.md` still says, in section 5 ("What I cannot exclude is an Act in between that changed one of them and was changed back") and in section 9 ("The risks are an exemption instrument I could not see, an Act after Act 15 of 2017 that the markers do not show, ..."), that such an Act is a risk: that is still true of any exemption instrument not yet seen and of an Act the Legislative History does not list; Act 31 of 2022 and S 26/2022, which were the two not obtained, were read in Part 3 (finding 38) and the sentences were left as written.
    `TV-QUESTION.md` section 8 also gained a bullet on O 3 (finding 33).
    The 360 case assertions all still pass with their yes/no answers unchanged (the gate numbers in the Checks block).

38. **Follow-up Part 3 (a), 2026-11-04: Act 31 of 2022 with S 850/2022, and G.N. No. S 26/2022.**
    Act 31 of 2022, the Statutes (Miscellaneous Amendments) Act 2022 (Acts Supplement No. 30 of 2022, first published 28 Oct 2022 at 5 pm; passed 3 Oct 2022, assented to 25 Oct 2022), amends the Telecommunications Act in one place, section 21(7): "In the Telecommunications Act 1999, in section 46(3)(b), delete \"Part 7\" and substitute \"Parts 7 and 9\"" (`TA1999.ACT31-2022.txt:1080-1081`), the Parts being those of the Insolvency, Restructuring and Dissolution Act 2018 (`TA1999.txt:4510-4511`, with the marker `[Act 31 of 2022 wef 01/11/2022]` at `:4516`).
    S 850/2022 (first published 31 Oct 2022 at 5 pm, made 28 Oct 2022) says in paragraph 2 that the Act, "except sections 4(1)(a) to (d) and (f), 10, 12(2) to (6), 16(b), 20(2) and 22(3), comes into operation on 1 November 2022"; section 21 is not an exception (`TA1999.S850-2022.txt:18-20`).
    So the effective day is 1 Nov 2022, as the Legislative History says (`TA1999.txt:7276`), and the day a reader could see it is READ, 31 Oct 2022, and no longer assumed.
    Bill 24/2022 (the Bill as introduced, first read 12 Sep 2022) is deposited as EXTRINSIC material only (`TA1999.BILL24-2022.txt`); its subsection (7) has the same words (`:1044-1045`), and nothing in the encoding rests on it.
    G.N. No. S 26/2022, the Variable Capital Companies (Consequential Amendments to Other Acts) Order 2022, made under s 167(1) of the Variable Capital Companies Act 2018 (first published 12 Jan 2022 at 7 pm), says in paragraph 1 that "except for paragraph 12" it "comes into operation on 13 January 2022" (`TA1999.S26-2022.txt:19-22`).
    Paragraph 22 amends the Telecommunications Act in three places (`:702-715`): (a) inserts "(including a VCC)" after "to a company" in the definition of "securities" in section 2; (b) inserts the definitions "VCC" and "VCC Act" after that of "Town Council" in section 2; (c) in sections 40(7)(a) and 41(7)(a) replaces "and the Trustees Act 1967" by ", the Trustees Act 1967 and the VCC Act".
    These match the five markers `[S 26/2022 wef 13/01/2022]` of the consolidation (`TA1999.txt:469`, `:546`, `:550`, `:3833`, `:4115`): the first on "securities", the second and third on "VCC" and "VCC Act", the last two on ss 40(7)(a) and 41(7)(a).
    None is on the chain: "securities", "VCC" and "VCC Act" are not among the three definitions the chain uses ("equipment", "radio-communication", "broadcasting apparatus"), and ss 40 and 41 are the Authority's powers to issue directions about the control of designated telecommunication licensees and to enforce conditions of its approvals (Part 5A).
    The earlier reading that both were consequential amendments and not amendments of ss 2 "equipment", 54 to 56, 85, 95 or 96 rested on the markers; it now rests on the texts and is confirmed.
    Encoded in `sgta-i-acts-after-2017.l4`, whose enum is renamed `Instrument amending the Telecommunications Act after Act 15 of 2017` and has nine values (S 26/2022 is an Order and not an Act); 37 new assertions in `sgta-tests-acts-after-2017.l4`, which has 131 in all.
    The published day of the other seven stays ASSUMED equal to the effective day (their commencement notifications are not deposited).
    The seat does not consult the module; no answer moved.

39. **Follow-up Part 3 (b), 2026-11-04: the Dealers chain, S 362/2001, S 185/2003, S 48/2004 and S 593/2004.**
    S 362/2001, the Telecommunication (Dealers) (Amendment) Regulations 2001 (first published 30 Jul 2001 at 5:00 pm, made 27 Jul 2001), comes into operation on 1 Aug 2001 "with the exception of regulation 4 (a)", which "shall be deemed to have come into operation on 21st January 2000" (`TA1999-DEAL99-S362-2001.txt:22-26`).
    It substitutes reg 15 (inspection of the Dealer's Individual Licence), substitutes reg 32 (the offence, now listing regs 4(1) and (4), 6(2), 12(2), 14, 15, 17, 18, 19 and 20(3) and (4) instead of every provision), and amends the First Schedule: item 3 is deleted (deemed from 21 Jan 2000), item 6 is replaced by "Radio-communication Equipment operating in frequency bands 890-915 MHz and 935-960 MHz except Cellular Mobile phones or such other equipment approved by the Authority", and item 7 is deleted.
    So the 1999 text is NOT the text of Rg 7 from 1 Aug 2001: `sgta-i-versions.l4` has a row for S 362/2001 (published 30 Jul 2001, effective 1 Aug 2001), and `sgta-i-rg7-1999.l4` has two-date functions for reg 32 and the First Schedule and a function for the substituted reg 15.
    Reg 15 has no dispatcher, because the 1999 function is the officer's entitlement and the 2001 function is the holder's duty (different subjects); the version row says which text governs.
    The deemed-retrospective item 3 deletion is modelled like S 549/2012: a reader on 30 Jul 2001 or later sees item 3 gone from 21 Jan 2000, a reader before that sees it.
    S 185/2003, the Telecommunications (Dealers) Regulations 2003 (first published 2 Apr 2003 at 5:00 pm), comes into operation on 2 Apr 2003 (reg 1) and reg 26 revokes Rg 7 (`TA1999-RG6-S185-2003.txt`); that FIXES the end of Rg 7 (1999 Ed.) at 1 Apr 2003, which was assumed until now.
    S 48/2004 (first published and in operation 3 Feb 2004) replaces "$400" by "$250" in reg 9 and in reg 10(1)(a) and (b); S 593/2004 (first published 27 Sep 2004, in operation 1 Oct 2004) replaces paragraph 5 of the Second Schedule.
    The Rg 6 version table therefore has three new rows (2 Apr 2003, 3 Feb 2004, 1 Oct 2004) and no longer answers NOTHING from 2 Apr 2003 to 31 Dec 2004; for those days the Revised Edition 2004's words stand for the as-made words in 25 of 31 blocks, and `sgta-i-rg6-as-made.l4` says, for each of the 31 blocks (26 regulations and 5 Schedules), whether the words are the same and, for the 6 that differ (regs 1, 3, 9, 10, 26 and the Second Schedule), how.
    The comparison was run by script against `TA1999-RG6-GAZ-RevEd2004.txt` after setting aside case, punctuation other than the parentheses of paragraph labels, hyphenation, running heads and page furniture, and the tail of the block for reg 25 (the heading of reg 26) and for the Fifth Schedule (the signature block against the Revised Edition's history line); the difference stated for reg 3 (the word "any" in paragraph (11)) is in neither amending instrument and is the Revised Edition's own.
    The seat reads the Rg 6 version table only through reg 22(1), whose function answers NOTHING for an effective day before 21 Jul 2005 (`sgta-i-rg6-dealers.l4:116-120`), so the new rows move no seat answer; the 360 case assertions all pass.
    The seat does not consult Rg 7 at all.
    Tests: `sgta-tests-dealers-chain.l4` (105 assertions) and new assertions in `sgta-tests-i-versions.l4` (185 in all) and `sgta-tests-1999-regs.l4` (one expected value changed from the assumed end to S 362/2001's effective day).
    O 3 (finding 33) refers to "the Fifth Schedule to the Telecommunication (Dealers) Regulations", which S 362/2001 does not amend and which S 185/2003 revokes with Rg 7 from 2 Apr 2003; the module header's note on the reference stands, and O 3 is not consulted by the seat.

40. **Follow-up Part 3 (c), 2026-11-04: the 2010 Subject Index, deposited as an AID.**
    `TA1999-AID-INDEX2010.txt` under `telecommunications-tas-exemption-specified-equipment-order-1998/registers/source-bundle/`, with a `.meta.json` (URL, retrieval time, sha256 of the PDF `4cbc65168fb2d5eaaef88bd3a51575684b51685a265d93cbe18605d8c52aaa86` and of the text), a note appended to `SOURCE-LICENSE-GAZETTE.md`, and an `aids` entry in `subject.json` (it is not in `files`, which lists instruments).
    It is the e-Gazette's "Subject Index to Subsidiary Legislation", whose title line reads "Incorporating all Subsidiary Legislation enacted before 1.6.2010" (`:53`): an index AS AT that date, which says nothing of the years after and is not law.
    My fetch (one GET, 2026-11-04) gave the same PDF and the same text as the independent reviewer's copy (the sha256 of the text, `a5a865ad765d13a6a056ae2e3e35f7efe62da9b3516e379aef5dd40771529aa4`, is equal), so the line numbers the reviewer cited are the deposit's: under "equipment, telecommunication" it lists the Order O 3 and the Telecommunications (Dealers) Regulations (Cap 323, Rg 6) (`:9717-9721`).
    Every citation of the reviewer's scratchpad path was repointed to the deposit: the header of `sgta-i-o3-1998.l4` now quotes the entry (a quote run and an `@ref`, checked by `srcrefs.py --strict`) and finding 33 cites the deposit.
    `gen-coverage.py` skips files with `-AID-` in the name (an aid is not an instrument).

41. **Follow-up Part 3 (d), 2026-11-04: rulings of the team lead recorded as ASSUMED, NOT RULED, and the wording corrections.**
    These are design calls of the team lead's, not Meng's rulings.
    - **The 1999 Rg 3 and Rg 7 stay layer 1 only and are not wired into the seat.** The seat's tier "on the texts deposited" needs the Act's own printed text for the day, and none is held before 30 Dec 2000; `TV-QUESTION.md` Date (1) (lines 195-202) now says what the 1999 Rg 3 text says (a "station" includes a "receiver", reg 4(1)), that it governed 1 Dec 1999 to 1 Mar 2001, which modules hold it, and that the seat answers NOTHING for those days (measured on six pairs of days). For 30 Dec 2000 to 2 Mar 2001 the Act is held but the seat's tables for N 1 and Rg 5 begin on 2 Mar 2001 and that for Rg 6 on 2 Apr 2003, which is why the measured answer is NOTHING there too (the team lead's stated reason covers only the days before 30 Dec 2000). To revert: add the two modules as a tier in `sgta-tv-seat.l4`; the Act's text for 1 Dec 1999 to 29 Dec 2000 would still be missing.
    - **The nine amending instruments after Act 15 of 2017 stay a parallel version rule; the bucket row is not split.** What splitting would change is stated under the Acts table above. To revert: split the row in `sgta-ta-versions.l4`.
    - **Published day of the two 1999 Revised Editions: 1 Jul 1999** (the Editions' own date), assumed. To revert: change the two rows of `sgta-i-versions.l4` (comment `Rg 3 (1999 Ed.)` and `Rg 7 (1999 Ed.)`).
    - **Published day of each of the seven Acts without a deposited commencement notification = its effective day**, assumed. To revert: deposit the notification and change the row in `sgta-i-acts-after-2017.l4` (the function `the day a reader could see its date of effect`).
    - **"At least one year" in the Wiring Work Regulations 2024, reg 3(6), is 365 days**, assumed. To revert: change the constant in `sgta-i-ww-2024.l4`.
    - **Rg 6 as made against the 2004 Revised Edition** rests on a script comparison (finding 39). To revert: delete `sgta-i-rg6-as-made.l4`; the version rows would then return a date for the as-made days and the as-made words would be unquoted.
    - Withdrawn: the end day 1 Apr 2003 of Rg 7 (1999 Ed.) is no longer assumed (finding 39).
    Wording-only corrections to the QUARANTINED files in Part 3, no answer moved (`sgta-tv-cases.l4` all 360 assertions pass): `sgta-tv-seat.l4` lines 32 and 331; `sgta-tv-cases.l4` lines 131, 247 and 381; `TV-QUESTION.md` lines 195-202 (the new paragraph), 226, 271, 272, 276 and 283-284.
    They replace "seven are deposited" and "Act 31 of 2022 and S 26/2022 are not obtained" with the truth that eight Acts and one Order are deposited; `sgta-tv-cases.l4` line 131 had said that Act 26 of 2018 was "not deposited" and had been missed in Part 2.
    The same claims in comments of `sgta-ta-versions.l4` (lines 41, 42 and 204) were corrected too.

42. **S 22/2011, the Telecommunications (Cancellation) Notification 2011, found by the independent reviewer and obtained after Part 3 (2026-11-04).**
    Made 6 Jan 2011 by the Info-communications Development Authority of Singapore under "section 26(5) of the Telecommunications Act", first published 17 Jan 2011 at 5:00 pm, in operation 21 Jan 2011 (paragraph 1); paragraph 2 cancels thirteen notifications, items (a) to (m) (`TA1999-CANC-S22-2011.txt:34-80`).
    Deposited as its own subject (text, `.meta.json`, licence notes, `subject.json`; the wording of the provenance is that the orchestrating session read the URL off a result in the e-Gazette index and passed it to the encoder).
    Encoded in `sgta-i-canc-s22-2011.l4` as a small module and not as a table of which notification stood cancelled on which day: all thirteen are cancelled on the one day, and whether each was in operation before it is a fact of each notification, which is not held.
    The module has the day the Notification begins, the thirteen G.N. numbers by item and as a list, and the two-date rule (conduct on or after 21 Jan 2011, read on or after 17 Jan 2011); 44 assertions in `sgta-tests-canc-s22-2011.l4`.
    The thirteen notifications are named in items (a) to (m), were not searched for, and are off the receiver question: items (a) to (j) are titled exemptions from the Telecom Competition Code or its Dominant Licensee Provisions and items (k) to (m) exemptions for named services, and none of the titles names a receiver (the row in the source-not-obtained table).
    The Notification cites "section 26(5)"; section 26 of the deposited Revised Edition 2000 (`TA1999.20001230.txt:971-990`) runs from (1) to (4) and has no (5), and which text of the Act the citation reads was not determined.
    The seat does not consult the module; no answer moved.

## Fork register

Forks on the provisions the television question runs through are in `TV-QUESTION.md` section 4 (one pointer each; the same five are `fork` rows in `COVERAGE.md`):
- FORK 1, whether "radio-communication equipment" is the composition of two definitions: `TV-QUESTION.md` section 4.
- FORK 2, whether s 53(1)'s closing words carry the extra verbs of s 3(2)(a) into the offence: `TV-QUESTION.md` section 4.
- FORK 3, the reach of s 95 for broadcasting apparatus (Reading A or B): `TV-QUESTION.md` section 4.
- FORK 4, what Rg 6 reg 22(1)'s "approval" is (Reading X or Y): `TV-QUESTION.md` section 4.
- FORK 5, N 1 item 11(e) (with the item's bands): `TV-QUESTION.md` section 4.
- FORK 6, whether s 2 "equipment" before 1 Feb 2012 ("telecommunication purposes") covers a receiver of broadcasts: `TV-QUESTION.md` section 4.

Forks not on the question's path, with the readings I saw, the one I took and the text that licenses each:

| Fork | Readings | Taken | Text |
| --- | --- | --- | --- |
| A. Where the 2000 Edition numbering of an instrument lands today | (i) the Comparative Table in the deposit (column-garbled); (ii) the margin markers | the markers | `TA1999.txt:4884` ("[33"), 4907, 4931, 5937, 5950, 6994, 7003, 7104 |
| B. The start of a Revised Edition's text | the PDFs do not print it | I took 1 January 2003 (Rg 3, Rg 5, N 1) and 1 January 2005 (Rg 6) as the day a Revised Edition row begins; for N 1 and Rg 5 the rows before it are now the instruments as made and amended in 2001 (findings 24, 27 and 28), so the assumption bears there only on 1 January 2003 itself; Rg 3 and Rg 6 earlier dates answer `NOTHING` | the instruments' own headers ("2002 Ed.", "2004 Ed."), their bracketed commencement dates and the amendments' own dates |
| C. A vintage of the Act's text for a date before 2 October 2026 | strict (nothing deposited) or markers (inference) | both, kept apart | `sgta-ta-vintage.l4` |
| D. "telecommunication equipment" in s 54(1)(a) | the Act has no definition; Rg 6 reg 2 defines it | s 2 "equipment" (an appliance, apparatus or accessory used or intended to be used for telecommunications) | `TA1999.txt:325-329`; Rg 6 reg 2 |
| E. s 54(1)'s exception and s 56, s 96 | the exception names a s 5 licence or regulations; s 56 and s 96 are separate carve-outs | the offence outcome applies all three; `s 54(1)(b): the person contravenes` is the exception alone | `TA1999.txt:4899-4902, 4935-4947, 7000-7001` |
| F. s 5(7) | "no person is to question whether the grant ... was ... with the consent of ... the Minister" | the Authority's grant is conclusive; consent is not an input | `TA1999.txt:693-703` |
| G. Printed values in N 1's Schedule that the PDF extraction renders defectively | keep the extraction as printed, or key the value the neighbouring vintages print | where the extraction keeps all the digits but looks wrong ("57 dBµ/Vm @ 3m" in S 1/2008 item 3; "25 W" in S 179/2011 item 8, where the vintages either side print "25 µW"), kept as printed; where it loses the decimal point (S 265/2006 and S 1/2008, "240 15" and "10 50"), keyed as 240.15 and 10.50 as the neighbouring vintages print them | `sgta-i-n1-bands.l4:12-17` |

## What the stable binary does not accept (found in this work; the binary governs)

- A one-line `CONSIDER m WHEN NOTHING THEN a WHEN JUST x THEN b` does not parse; each `WHEN` goes on its own line.
- A form with `THEN JUST` at the end of a line and the argument in parentheses on the next did not parse as written (seat line 112 in an earlier draft); I restructured to keep `JUST (` on one line and did not isolate the cause.
- Positional record construction with list literals needs each list in parentheses: `OF "x", (LIST a, b), (LIST c)`; without them the commas extend the first list.
- `APPEND` is the string operator; for lists use the prelude's `append xs ys`.
- A multi-line parenthesised `IF ... THEN ... ELSE` as an argument after another argument does not parse ("unexpected ("); give it a name as a function and call that.
- `NOT a OR b` parses as `NOT (a OR b)`; write `(NOT a) OR b`.
  `l4 check` also warns when an `AND` and an `OR` sit at the same indentation column.
- No section `GIVEN`, no `REFUSE`, no `#ASSERT REFUSED`, no `YMD`; dates are `Date day month year` (`IMPORT daydate`).
  Rules with no input (`GIVETH A Penalty` then a name) and heads that omit their `GIVEN` names both worked.

## Checks (pasted, main columns included)

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.98 (main, 7689b0d, 2026-10-19)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
sgta-i-acts-after-2017.l4                      0         0       0        0         0 |      0         0       0        0  same
sgta-i-canc-s22-2011.l4                        0         0       0        0         0 |      0         0       0        0  same
sgta-i-comp.l4                                 0         0       0        0         0 |      0         0       0        0  same
sgta-i-dtl-notifications.l4                    0         0       0        0         0 |      0         0       0        0  same
sgta-i-erp-s381-2024.l4                        0         0       0        0         0 |      0         0       0        0  same
sgta-i-iw-wiring.l4                            0         0       0        0         0 |      0         0       0        0  same
sgta-i-n1-bands.l4                             0         0       0        0         0 |      0         0       0        0  same
sgta-i-n1-exemption.l4                         0         0       0        0         0 |      0         0       0        0  same
sgta-i-o3-1998.l4                              0         0       0        0         0 |      0         0       0        0  same
sgta-i-resell.l4                               0         0       0        0         0 |      0         0       0        0  same
sgta-i-rg1-ship.l4                             0         0       0        0         0 |      0         0       0        0  same
sgta-i-rg3-1999.l4                             0         0       0        0         0 |      0         0       0        0  same
sgta-i-rg3-amendments.l4                       0         0       0        0         0 |      0         0       0        0  same
sgta-i-rg3-class.l4                            0         0       0        0         0 |      0         0       0        0  same
sgta-i-rg3-licences.l4                         0         0       0        0         0 |      0         0       0        0  same
sgta-i-rg3-s485-2016.l4                        0         0       0        0         0 |      0         0       0        0  same
sgta-i-rg4-cable.l4                            0         0       0        0         0 |      0         0       0        0  same
sgta-i-rg5-amendments.l4                       0         0       0        0         0 |      0         0       0        0  same
sgta-i-rg5-as-made.l4                          0         0       0        0         0 |      0         0       0        0  same
sgta-i-rg5-definitions.l4                      0         0       0        0         0 |      0         0       0        0  same
sgta-i-rg5-duties.l4                           0         0       0        0         0 |      0         0       0        0  same
sgta-i-rg5-licences.l4                         0         0       0        0         0 |      0         0       0        0  same
sgta-i-rg5-radio.l4                            0         0       0        0         0 |      0         0       0        0  same
sgta-i-rg5-schedules.l4                        0         0       0        0         0 |      0         0       0        0  same
sgta-i-rg5-spectrum.l4                         0         0       0        0         0 |      0         0       0        0  same
sgta-i-rg6-amendments.l4                       0         0       0        0         0 |      0         0       0        0  same
sgta-i-rg6-as-made.l4                          0         0       0        0         0 |      0         0       0        0  same
sgta-i-rg6-dealers.l4                          0         0       0        0         0 |      0         0       0        0  same
sgta-i-rg6-definitions.l4                      0         0       0        0         0 |      0         0       0        0  same
sgta-i-rg6-licensing.l4                        0         0       0        0         0 |      0         0       0        0  same
sgta-i-rg7-1999.l4                             0         0       0        0         0 |      0         0       0        0  same
sgta-i-trusts.l4                               0         0       0        0         0 |      0         0       0        0  same
sgta-i-versions.l4                             0         0       0        0         0 |      0         0       0        0  same
sgta-i-ww-2024.l4                              0         0       0        0         0 |      0         0       0        0  same
sgta-nouns.l4                                  0         0       0        0         0 |      0         0       0        0  same
sgta-part3-ss15-22.l4                          0         0       0        0         0 |      0         0       0        0  same
sgta-part3-ss23-29.l4                          0         0       0        0         0 |      0         0       0        0  same
sgta-part4-ss30-32.l4                          0         0       0        0         0 |      0         0       0        0  same
sgta-part5-ss33-36.l4                          0         0       0        0         0 |      0         0       0        0  same
sgta-part5a-s37.l4                             0         0       0        0         0 |      0         0       0        0  same
sgta-part5a-s38-39.l4                          0         0       0        0         0 |      0         0       0        0  same
sgta-part5a-s40.l4                             0         0       0        0         0 |      0         0       0        0  same
sgta-part5a-s41-43.l4                          0         0       0        0         0 |      0         0       0        0  same
sgta-part5b-5c-ss44-52.l4                      0         0       0        0         0 |      0         0       0        0  same
sgta-part6-2000ed.l4                           0         0       0        0         0 |      0         0       0        0  same
sgta-part6-more.l4                             0         0       0        0         0 |      0         0       0        0  same
sgta-part6-offences.l4                         0         0       0        0         0 |      0         0       0        0  same
sgta-part7-international-and-directions.l4       0         0       0        0         0 |      0         0       0        0  same
sgta-part8-more.l4                             0         0       0        0         0 |      0         0       0        0  same
sgta-part8-penalties.l4                        0         0       0        0         0 |      0         0       0        0  same
sgta-part9-general.l4                          0         0       0        0         0 |      0         0       0        0  same
sgta-part9-s89-90.l4                           0         0       0        0         0 |      0         0       0        0  same
sgta-part9-s91-92.l4                           0         0       0        0         0 |      0         0       0        0  same
sgta-part9-s93-94-97.l4                        0         0       0        0         0 |      0         0       0        0  same
sgta-s11-14-approval-and-residual.l4           0         0       0        0         0 |      0         0       0        0  same
sgta-s11-approval.l4                           0         0       0        0         0 |      0         0       0        0  same
sgta-s2-definitions.l4                         0         0       0        0         0 |      0         0       0        0  same
sgta-s2-more-definitions.l4                    0         0       0        0         0 |      0         0       0        0  same
sgta-s3-5-privilege-licensing.l4               0         0       0        0         0 |      0         0       0        0  same
sgta-s5-licence-terms.l4                       0         0       0        0         0 |      0         0       0        0  same
sgta-s6-8-spectrum-orbit-designation.l4        0         0       0        0         0 |      0         0       0        0  same
sgta-s9-10-conditions-and-sanctions.l4         0         0       0        0         0 |      0         0       0        0  same
sgta-ta-versions.l4                            0         0       0        0         0 |      0         0       0        0  same
sgta-ta-vintage.l4                             0         0       0        0         0 |      0         0       0        0  same
sgta-tests-1999-regs.l4                        0       178       0        0         0 |      0       178       0        0  same
sgta-tests-2023-24.l4                          0       159       0        0         0 |      0       159       0        0  same
sgta-tests-act-defs.l4                         0       187       0        0         0 |      0       187       0        0  same
sgta-tests-act-part2.l4                        0       152       0        0         0 |      0       152       0        0  same
sgta-tests-act-part3.l4                        0       150       0        0         0 |      0       150       0        0  same
sgta-tests-act-part4-5c.l4                     0       226       0        0         0 |      0       226       0        0  same
sgta-tests-act-part6-8.l4                      0       194       0        0         0 |      0       194       0        0  same
sgta-tests-act-part9.l4                        0       158       0        0         0 |      0       158       0        0  same
sgta-tests-act-versions.l4                     0        70       0        0         0 |      0        70       0        0  same
sgta-tests-acts-after-2017.l4                  0       131       0        0         0 |      0       131       0        0  same
sgta-tests-canc-s22-2011.l4                    0        44       0        0         0 |      0        44       0        0  same
sgta-tests-dealers-chain.l4                    0       105       0        0         0 |      0       105       0        0  same
sgta-tests-eval-1999-2024.l4                   0       494       0        0         0 |      0       494       0        0  same
sgta-tests-i-versions.l4                       0       185       0        0         0 |      0       185       0        0  same
sgta-tests-instr-more.l4                       0        81       0        0         0 |      0        81       0        0  same
sgta-tests-instruments.l4                      0       217       0        0         0 |      0       217       0        0  same
sgta-tests-more-notifications.l4               0       109       0        0         0 |      0       109       0        0  same
sgta-tests-n1-bands.l4                         0        47       0        0         0 |      0        47       0        0  same
sgta-tests-part6-2000ed.l4                     0       545       0        0         0 |      0       545       0        0  same
sgta-tests-part6-part8.l4                      0       113       0        0         0 |      0       113       0        0  same
sgta-tests-rg3.l4                              0       110       0        0         0 |      0       110       0        0  same
sgta-tests-rg5-amend.l4                        0       122       0        0         0 |      0       122       0        0  same
sgta-tests-rg5-as-made.l4                      0        65       0        0         0 |      0        65       0        0  same
sgta-tests-rg5-b.l4                            0       287       0        0         0 |      0       287       0        0  same
sgta-tests-rg5.l4                              0        73       0        0         0 |      0        73       0        0  same
sgta-tests-rg6.l4                              0       229       0        0         0 |      0       229       0        0  same
sgta-tests-s2-s5.l4                            0        67       0        0         0 |      0        67       0        0  same
sgta-tests-small-instruments.l4                0       175       0        0         0 |      0       175       0        0  same
sgta-tv-ba-schedule.l4                         0         0       0        0         0 |      0         0       0        0  same
sgta-tv-cases.l4                               0       360       0        0         0 |      0       360       0        0  same
sgta-tv-seat.l4                                0         0       0        0         0 |      0         0       0        0  same
TOTAL (95 modules)                             0      5033       0        0           |      0      5033       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`l4 check` on every `sgta-*.l4` printed no warning on the final run (no unknown annotation, no `@ref` at the end of a file or after code).

`./srcrefs-all.sh` (which runs `python3 -I srcrefs.py check --strict <raw> <module>` on each module against the text deposited for it, so that `src:ID:N` resolves beside the raw file):

```
srcrefs check: 61 src: lines, 18 runs, 19 locators, 0 problems
srcrefs check: 51 src: lines, 7 runs, 7 locators, 0 problems
srcrefs check: 27 src: lines, 2 runs, 2 locators, 0 problems
srcrefs check: 98 src: lines, 18 runs, 19 locators, 0 problems
srcrefs check: 49 src: lines, 6 runs, 6 locators, 0 problems
srcrefs check: 22 src: lines, 4 runs, 4 locators, 0 problems
srcrefs check: 253 src: lines, 34 runs, 34 locators, 0 problems
srcrefs check: 369 src: lines, 42 runs, 42 locators, 0 problems
srcrefs check: 137 src: lines, 14 runs, 14 locators, 0 problems
srcrefs check: 141 src: lines, 13 runs, 13 locators, 0 problems
srcrefs check: 389 src: lines, 24 runs, 24 locators, 0 problems
srcrefs check: 149 src: lines, 17 runs, 17 locators, 0 problems
srcrefs check: 249 src: lines, 11 runs, 11 locators, 0 problems
srcrefs check: 265 src: lines, 18 runs, 18 locators, 0 problems
srcrefs check: 253 src: lines, 28 runs, 28 locators, 0 problems
srcrefs check: 36 src: lines, 9 runs, 9 locators, 0 problems
srcrefs check: 257 src: lines, 34 runs, 34 locators, 0 problems
srcrefs check: 126 src: lines, 16 runs, 16 locators, 0 problems
srcrefs check: 162 src: lines, 20 runs, 20 locators, 0 problems
srcrefs check: 91 src: lines, 16 runs, 16 locators, 0 problems
srcrefs check: 433 src: lines, 29 runs, 29 locators, 0 problems
srcrefs check: 180 src: lines, 9 runs, 9 locators, 0 problems
srcrefs check: 97 src: lines, 16 runs, 16 locators, 0 problems
srcrefs check: 155 src: lines, 22 runs, 22 locators, 0 problems
srcrefs check: 52 src: lines, 12 runs, 12 locators, 0 problems
srcrefs check: 157 src: lines, 24 runs, 24 locators, 0 problems
srcrefs check: 118 src: lines, 15 runs, 15 locators, 0 problems
srcrefs check: 75 src: lines, 5 runs, 25 locators, 0 problems
srcrefs check: 806 src: lines, 16 runs, 16 locators, 0 problems
srcrefs check: 291 src: lines, 12 runs, 12 locators, 0 problems
srcrefs check: 649 src: lines, 7 runs, 7 locators, 0 problems
srcrefs check: 1636 src: lines, 5 runs, 5 locators, 0 problems
srcrefs check: 91 src: lines, 1 runs, 1 locators, 0 problems
srcrefs check: 133 src: lines, 15 runs, 15 locators, 0 problems
srcrefs check: 408 src: lines, 46 runs, 46 locators, 0 problems
srcrefs check: 62 src: lines, 8 runs, 11 locators, 0 problems
srcrefs check: 157 src: lines, 7 runs, 7 locators, 0 problems
srcrefs check: 219 src: lines, 16 runs, 16 locators, 0 problems
srcrefs check: 1016 src: lines, 11 runs, 11 locators, 0 problems
srcrefs check: 693 src: lines, 3 runs, 3 locators, 0 problems
srcrefs check: 48 src: lines, 7 runs, 8 locators, 0 problems
srcrefs check: 18 src: lines, 5 runs, 5 locators, 0 problems
srcrefs check: 430 src: lines, 28 runs, 29 locators, 0 problems
srcrefs check: 297 src: lines, 7 runs, 7 locators, 0 problems
srcrefs check: 9 src: lines, 2 runs, 2 locators, 0 problems
srcrefs check: 252 src: lines, 21 runs, 21 locators, 0 problems
srcrefs check: 7 src: lines, 1 runs, 1 locators, 0 problems
srcrefs check: 119 src: lines, 8 runs, 8 locators, 0 problems
srcrefs check: 91 src: lines, 4 runs, 4 locators, 0 problems
srcrefs check: 224 src: lines, 15 runs, 15 locators, 0 problems
srcrefs check: 167 src: lines, 15 runs, 15 locators, 0 problems
srcrefs check: 196 src: lines, 17 runs, 17 locators, 0 problems
srcrefs check: 21 src: lines, 1 runs, 1 locators, 0 problems
srcrefs check: 10 src: lines, 1 runs, 1 locators, 0 problems
srcrefs check: 38 src: lines, 3 runs, 3 locators, 0 problems
srcrefs check: 622 src: lines, 46 runs, 46 locators, 0 problems
srcrefs check: 1034 src: lines, 66 runs, 66 locators, 0 problems
srcrefs check: 70 src: lines, 4 runs, 4 locators, 0 problems
srcrefs check: 262 src: lines, 11 runs, 11 locators, 0 problems
srcrefs check: 380 src: lines, 32 runs, 32 locators, 0 problems
srcrefs check: 65 src: lines, 3 runs, 3 locators, 0 problems
tv srcrefs check (sgta-tv-ba-schedule.l4): 0 src: lines, 0 runs, 0 locators, 0 problems
tv srcrefs check (sgta-tv-cases.l4): 0 src: lines, 0 runs, 0 locators, 0 problems
tv srcrefs check (sgta-tv-seat.l4): 0 src: lines, 0 runs, 0 locators, 0 problems
tv citations check: 199 locators in 4 files (sgta-tv-seat.l4 0, sgta-tv-cases.l4 53, sgta-tv-ba-schedule.l4 33, TV-QUESTION.md 113), 22 quoted fragments of the Rg 1 table, 0 problems
```

Total: 61 modules, 14,973 quote lines in 927 runs, 954 locators, 0 problems.
The test and seat files carry no quotation and are not checked by srcrefs.

## Independent review

After both encoders had finished, one separate Claude session (Opus 5.5) reviewed this encoding and the Broadcasting Act encoding (`../../../broadcasting-act-1994/encodings/legalese-sonnet-5.5/`).
It is not a domain expert, so the status at the top of this file stands.
The record is in `review/`: `README.md` says who reviewed, what the reviewer was shown, what leaked, the numbers, and where each source the reviewer fetched is now deposited; `REVIEW.md`, `DISAGREEMENTS.md`, `MISSED-INSTRUMENTS.md`, `CITATION-CHECK.md` and `REQUESTS.md` are the reviewer's own files, unedited; `DISPOSITIONS.md` says what each encoder did about each item.
`REVIEW.md` holds the reviewer's own answer to the question; this file keeps to the quarantine stated above and does not repeat it.
The reviewer's `file:line` citations into this file are to the copy it was shown, which has changed since, so find a passage by its finding number, fork identifier or heading.

**What was independent.**
The method, set by the project owner, was Sonnet 5.5 encoders and then one independent Opus 5.5 reviewer who is not shown the encoders' conclusion.
The reviewer worked in a read-only copy of the repository without `TV-QUESTION.md`, `TV-QUESTION-BA.md`, the `sgta-tv-*` and `sgba-tv-*` modules, any `PROGRESS.md` and the forward-looking row `unstable-multitemporal-2026-11`.
It was told to re-derive its answer from the deposited texts before it opened any encoding file, to look for instruments the encoders had missed, to check the citations on the decisive chain and a random sample, and to run each `check.sh`.

**What was not.**
When the reviewer's context was compacted, at 2026-11-03T19:53:49Z, the harness attached four files to it.
One was its own brief, which it had read once; the other three it had not opened, and one of those stated both encoders' preliminary answers.
The reviewer reported this itself and opened none of the three.
Only section 1 of `REVIEW.md`, last written 14 minutes before the compaction (sha256 `dd6325a0943dd1744ecb76027edca414c6e32b2884d876fd5ad8d5a9b8d36176`), is blind.
Everything after it is not, and should not be counted as a further independent confirmation of it.

**What it found about this encoding.**
Eleven items of difference between the reviewer and an encoding (D1 to D11; 6 marked B, identified in the blind section, and 5 marked P, noticed later), of which seven concern this encoding.
- D2: the weight to give the pre-2012 wording of "equipment". No change; the reviewer and the encoder differ in weight and not in outcome, and FORK 6 in `TV-QUESTION.md` section 4 already carries the old words as a fork.
- D4: the TAS-era exemption order O 3. S 549/1998 and the 1999 Revised Editions of Rg 3 and Rg 7 are deposited, the Order is encoded with an explicit fork on what s 30 of the TAS Act said (that text is not held), and the 2010 Subject Index is deposited as an aid (findings 33, 34, 40 and 41).
- D7: the N 1 and Rg 6 version tables were stale for today. S 588/2023 and S 589/2023 are deposited and encoded, and the Rg 6 gap from 2 April 2003 is filled (findings 35 and 39).
- D8 and D9: findings 16 and 26 carry a CORRECTED note.
- D10: locator defects M5 to M8 and G2 are fixed, `srcrefs-all.sh` now runs the three `sgta-tv-*` modules (which quote no source text, so that run checks nothing in them), and `check-tv-citations.py` checks that each locator in them exists, not that it names the right provision (finding 32).
- D11: "equipment ... includes" is an inclusive definition. The encoder agrees and left the BOOLEAN return type on purpose (finding 30).

For the quotations the reviewer found all 15,530 quote lines of the 97 quoting modules it checked, in both folders, to be verbatim substrings of the lines they name.
By hand it found 17 locator-level mismatches of 8 kinds and 2 coverage gaps in the two folders together; none is in a quotation's words, and a random sample of 64 had 1.
The reviewer's own run of this folder's `check.sh` on its copy gave 76 modules and 3,003 assertions satisfied; its copy lacked the `sgta-tv-*` modules, so that is lower than the figures under "Checks", which are for the whole folder.
It also found S 22/2011, which the encoders had not deposited; it is now deposited and encoded (`sgta-i-canc-s22-2011.l4`, finding 42).

**What the project owner ruled that touches this file.**
- Scope (Meng, 2026-11-03): the whole Acts and every instrument found, encoded; an instrument that could not be obtained is a row marked `source not obtained`.
- Instruments hosted by IMDA are deposited with their full text, and each `SOURCE-LICENSE.md` says that this relies on the text being legislation and is not a clearance.
- A text from an unofficial mirror could be used for the First Schedule before 2011 only if the Singapore Statutes Online route, the Gazette, the Bills and Hansard all failed; none was used.
- A second blind review was permitted if a point first noticed after the leak could change a headline answer; none could, so it was not run.

## Open questions for a domain expert

1. Is IMDA's listing current, and are there Minister's exemption notifications under s 96 other than N 1 that bear on equipment people own?
2. What do the earlier versions of the Act say (no attempt on Singapore Statutes Online was made: the gate, the Broadcasting Act encoder's attempt, ended in a 403 at robots.txt on 2026-11-04), and what did the Broadcasting Act's First Schedule list before 1 January 2011 and between 1 January 2011 and the notification (S 549, commencing 1 January 2011) that replaced it?
3. Has the Authority published standards under Rg 6 reg 22(1) that apply to receivers of broadcasts, and is Rg 6 reg 22(1) read as an authorisation to possess?
4. Does Singapore Statutes Online show any amendment of N 1, Rg 5 or Rg 6 after those IMDA lists?
5. ANSWERED for Act 22 of 2016 (section 100: "Authority", "Chief Executive", "Media Development Authority of Singapore"; finding 27) and for Act 15 of 2017 (section 53(6) inserts "or 211I" in ss 32J(3)(a) and 32L(1)(b) and (2)(a) only; finding 28) from the printed Acts; still open for Act 4 of 2021 (section 22(9)): which definitions of s 2 did it change, and when? and for every other Act after Act 15 of 2017 (the table "Acts and instruments whose source was not obtained").
6. ANSWERED 2026-11-04 for every amending notification of N 1, Rg 5 and Rg 6 and for the commencement notification of Act 10 of 2005, from the e-Gazette copies (`sgta-i-versions.l4`, finding 26); what remains open is the day each Revised Edition began, which no deposited text prints (Fork B).
7. Was the First Schedule to the Broadcasting Act amended between the Revised Edition 2003 and the Revised Edition 2012 (assumed not, because both print the same three items)?
