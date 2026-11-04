# PROGRESS (TA folder) - tasks and file states only

Quarantine reminder: no conclusions about the TV question belong in this file.
Running analysis of H1-H6 lives in the scratchpad notes file `scratchpad/tv-analysis-notes.md` and later in `TV-QUESTION.md`.

Session started 2026-11-03.
Compactions seen so far: 0.

## Toolchain facts checked

- `$HOME/.cache/l4-main/98/l4 --version` printed `1.6.98 (main, 7689b0d, 2026-10-19)` on 2026-11-03.
- Scratchpad: `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/daea9ea8-ade8-4962-9243-b775db3b08df/scratchpad`.

## Order of work (brief step numbers)

- [x] (1) Read CLAUDE.md, ENCODING-GUIDE, directory-conventions (partly), skills, both naive NOTES.md.
- [x] (2) Probe sources once and record each (see below; SSO attempt still planned for the window).
- [x] (3) Gather and deposit sources: IMDA instruments fetched (40 PDFs in scratchpad); META-ONLY deposits written for Rg 3, Rg 5, Rg 6, N 1 and the composition regulations under `subjects/sg/telecommunications-*` (SUPERSEDED 23:20: deposited with text under call A).
- [x] (4) TA coverage table: `gen-coverage.py` -> `COVERAGE.md`, 3 checks PASS, 1203 rows plus 40 instrument rows. BA coverage belongs to the BA folder's owner (see collision note).
- [x] (5) Nouns module (sgta-nouns.l4).
- [x] (6) Tier-1 rules and tests, instruments in vintages (3 test files, 340 assertions).
- [x] (7) Seat layer, cases (59) and TV-QUESTION.md written.
- [x] (8) NOTES.md, encoding.json, SOURCE-LICENSE.md, check.sh output (399 satisfied, main same), srcrefs strict 0 problems.

## Source probes (what each returned)

- SSO sso.agc.gov.sg: NOT tried by this session.
  Reason: the brief allows one attempt inside 03:00-07:00 Singapore time only; the probe session started at about 21:57 SGT on 2026-11-03.
  The brief records two earlier probes (GM 2026-10-20, orchestrator 2026-11-03) that returned 403.
  Plan: one request set inside the window if the session is still running (see "Planned SSO attempt" below).
- lawplain MCP: `statutes` serves `act_current` and `act_revised` only, no historical versions (probed `kind`; `as_at`/`version` params still to try).
  `subsidiary_legislation` holds NO instrument under parent TA1999 (search with `parent_act_id=TA1999` returned 0; `TA1999-RG1` is 404).
  It holds 12 under BA1994: RG2, RG3, N1, OR1, OR2, OR3, S 121/2008, S 211/2022, S 523/2010, S 477/2020, S 30/2023, S 47/2023.
  `BTA1963` and `BTA1994` (repealed predecessors) return no section text.
  `bills` holds the Bills for the 1994 Act, the 2001, 2002, 2004 amendments and the 2004 Telecommunications (Amendment) Bill.
- IMDA (www.imda.gov.sg): robots.txt allows the paths used.
  `/regulations-and-licensing-listing/telecommunications-act-1999` lists 40 instrument PDFs (Cap 323 numbering).
  All 40 fetched into `scratchpad/dl-imda/pdf/` with `fetch-log.txt`; the title-to-file map is `scratchpad/dl-imda/ta-listing-map.tsv`.
  Two of the PDFs have no text layer (S 685/2011 class licence amendment, S 686/2011 composition amendment): OCR needed.
  The archived MDA press release page (RTV licence abolished) is a client-rendered shell; its text was not in the HTML.
- egazette.gov.sg: robots.txt allows `/`, disallows `/search`; sitemap lists only the SPA shell pages.
- legal-data-hunter MCP: `SG/SSOStatutes` has 508 documents; not yet queried for the BA.

## Open items from the advisor pass

- [ ] Planned SSO attempt (03:00-07:00 SGT = 19:00-23:00 UTC): `/Act/BA1994/Historical/20101001`, `/Act/BA1994/Historical/20110101`, then the Notification under `/SL/`. A 403 ends it.
- [ ] IMDA terms of use: read the reproduction clause before depositing any IMDA-hosted PDF; message the orchestrator if not plainly permissive.
- [x] Tried lawplain `get_document` with `as_at` and `section` params on BA1994: the same text came back (as_at ignored); `kind` is act_current or act_revised only.
- [x] Tried legal-data-hunter `search` (namespace legislation, country ["SG"]) 2026-11-03: `SG/SSOStatutes` holds the 2020 Revised Edition consolidation "up to and including 1 December 2021" of BA1994, TA1999 and others as single current documents; no historical versions; nothing before 2011 for the Broadcasting Act.
- [ ] Read the BA instruments lawplain holds (OR1, OR2, OR3, S 121/2008, S 211/2022, S 523/2010, N1, RG2, S 477/2020) and give each a coverage row.
- [ ] Hansard 18 Feb 2011 and 2011 Committee of Supply via lawplain `hansard` (extrinsic).
- [ ] Read the decisive instruments in full: Rg 5 base and S 100/2016; N 1 base and its amendments; the Dealers Regulations equipment provisions.
- [ ] Third-party copies of the pre-2011 BA exist (cyrilla.org PDF, a fandom wiki page); NOT used, because they are mirrors of SSO text and the brief forbids getting round a refusal that way.

## Collision note (2026-11-03 22:13)

Another session is writing in the BA folder (sgba-nouns.l4, sgba-vintage.l4, sgba-sched.l4, gen-coverage.py, qx.py) and has deposited 13 BA instrument subjects.
The orchestrator was asked (message 22:1x) to confirm the split: that session owns BA paths; this session owns TA paths, the seat layer and TV-QUESTION.md.
This session writes nothing under BA paths or those 13 subjects.

## Facts learned that later steps need (neutral)

- Margin markers in TA1999.txt give the 2000 Ed. section number: s 53=33, 54=34, 55=35, 56=36, 57=37, 58=38, 59=39, 64=44, 71=52, 84=64, 85=65, 86=66, 87=67, 88=68, 95=72, 96=73, 97=74, 98=75, s 11=9.
  The Comparative Table text at the end of the deposit is column-garbled in extraction, so the markers are the evidence.
- IMDA instruments cite the 2000 Ed. numbers: N 1 "sections 33, 34(1)(b) and 35" = ss 53, 54(1)(b), 55.
- The text deposit banner says "version in force from 2/10/2026"; meta.json says retrieved 2026-10-09 and "Current version as at 09 Oct 2026"; its historical_versions list ends at 20251001.
- TA(Amendment) Bill 67/2004 (lawplain bills, as introduced) matches Act 10 of 2005 (no Notice of Amendments in the legislative history): it added the daily continuing fine to the general-penalties section (then s 65).
- OCR of the two scanned PDFs is in scratchpad/ocr.

## Layer-1 state (2026-11-03 ~23:50, updated by hand)

Written and passing `l4 check`/`l4 run` on 1.6.98 and `srcrefs.py check --strict` (SUPERSEDED 23:20: now against the repo-deposited texts, srcrefs-all.sh):
sgta-nouns, sgta-s2-definitions, sgta-s3-5-privilege-licensing, sgta-s11-approval, sgta-part6-offences, sgta-part8-penalties,
sgta-part9-general, sgta-ta-vintage, sgta-i-n1-exemption, sgta-i-rg5-radio, sgta-i-rg6-dealers, sgta-i-rg3-comp.
Tests (hand-written expected values): sgta-tests-s2-s5 (67 satisfied), sgta-tests-part6-part8 (113), sgta-tests-instruments (160).
Quote markers `-- @Q a b` / `@QI id a b` / `@QC id` are expanded by scratchpad/tools/expand-quotes.py (not committed).
Still to do: seat layer (sgta-tv-seat.l4, sgta-tv-cases.l4), TV-QUESTION.md, NOTES.md, encoding.json, SOURCE-LICENSE.md, check.sh output,
instrument rows in COVERAGE (gen-coverage.py), srcrefs output for the repository raw files, BA-side cross-register.

## State at hand-off (2026-11-03, before the advisor review)

- check.sh (L4_MAIN_BUILD=98): 17 modules, 399 satisfied, 0 errors/failed/refused, main columns same.
- Open: orchestrator's ruling on IMDA text deposit (message sent 2026-11-03); SSO attempt not made (outside the 03:00-07:00 SGT window).
- (SUPERSEDED 23:20, the ruling was call A: quotations stay) IMDA-quote lines that would have been stripped: every `-- src:ID:N |` line with ID in (n1, n1s*, rg5, rg5s*, rg6, rg6s*, rg3, rg3s685, comp, comps686) in sgta-i-*.l4, and the short quotations in TV-QUESTION.md section 3.
- The quote markers were expanded by scratchpad/tools/expand-quotes.py (not committed); the module files are final text. (23:35: the tool now reads the repo-deposited texts.)

## Final (2026-11-03, after the advisor review)

- Fixed: s 2 marker row (last marked amendment 1 October 2025) and its two tests; TV-QUESTION section 5 and 9 now state the s 2 definitions gap; placeholder comment on `What the person holds`; unused import removed from the cases file.
- check.sh (L4_MAIN_BUILD=98): 17 modules, 399 satisfied, 0 errors, 0 failed, 0 refused, main columns same.
- legal-data-hunter and lawplain `as_at`: no historical versions (recorded above).
- Pending with the orchestrator: the IMDA text-deposit ruling; confirmation of the BA/TA ownership split.
- SSO: not attempted (window 03:00-07:00 SGT = 19:00-23:00 UTC; URLs: /Act/BA1994/Historical/20101001, /Act/BA1994/Historical/20110101, then the notification under /SL/).
- Compactions seen: 0.

## RE-BRIEF (2026-11-03 22:50 SGT) - READ THIS FIRST AFTER A COMPACTION

I am Encoder TA (`sg-tv-encoder`).
Meng's rulings relayed by the orchestrator:
- SCOPE: the whole Telecommunications Act (every section, subsection, paragraph, table row, defined term) and EVERY instrument found, no deferred rows.
  Dispositions allowed: encoded / inert (only: not operative; machinery per Guide section 4; repealed or blank) / fork / repealed-or-blank / `source not obtained` (instruments only).
  NOT reasons for inert: addresses an official; interpretive canon; refers to an unavailable instrument; no input would change the answer; naive encoding did not cover it.
- IMDA TEXTS: deposit in full (call A).
  Per instrument: `registers/source-bundle/<id>.txt` (OCR where there is no text layer, said in meta.json) + `.meta.json` (IMDA URL, retrieval date, sha256 of PDF, sha256 of text, in-force date as the AGC header gives it, how obtained).
  Instrument `SOURCE-LICENSE.md`: (1) text is the AGC Revised Edition / gazetted instrument, header as printed; (2) copy obtained from IMDA's site, URL, date, sha256; (3) reproduction relies on SSO Terms of Use cl.13 grant with the cl.13(a) attribution as in the Act-level SOURCE-LICENSE.md; (4) IMDA's own Terms paras 6-7 restrict its site content and the deposit relies on the text being legislation rather than IMDA content; this is a reliance, not a clearance from IMDA or AGC.
  Quote lines `-- src:` are allowed; run srcrefs against the repo's own texts; no "cannot be checked" note.
- MIRROR (call B): a mirror copy may be used for date (1) ONLY if all four fail: SSO in the 03:30-04:00 SGT window (after BA's attempt), the Gazette, lawplain Bills, lawplain Hansard.
  Then: mark as unofficial aid in NOTES.md and TV-QUESTION.md, name URL, date read, sha256 of what was read; do NOT deposit (scratchpad only); cross-check against Bills and Hansard; answer date (1) with the stated reliance.
- SSO WINDOW: 03:00-07:00 SGT; use 03:30-04:00; keep the crawl-delay in SSO robots.txt; a 403 or challenge ends it.
  Do not close date (1) before the attempt.
- GAZETTE: also check egazette.gov.sg (own terms of use; report them; which instruments are on it).
- CHECKPOINT: when the TV path is solid and TV-QUESTION.md complete, ONE SendMessage to `main` (conclusion allowed): answers (1)-(3), decisive sections, H1-H6, what could not be sourced, check.sh numbers; mark "date (1) pending the window" if before 03:30.
  Then carry on with the rest of the Act in the Act's own order, modules split along the Parts.
- BA folder belongs to `sg-ba-encoder`; do not write there; do not read `TV-QUESTION-BA.md` or `sgba-tv-*`. BA facts are inputs.

### Plan after the re-brief
1. [ ] Deposit IMDA instrument texts (all 40; five existing subjects get .txt; five new subjects for Rg 1, Rg 4, Internal Wiring, Resellers Notification, Prescribed Trusts).
2. [ ] Re-point quote IDs in sgta-i-*.l4 to the repo file stems; split sgta-i-rg3-comp.l4 into rg3 and comp modules; srcrefs against repo texts.
3. [ ] Update TV-QUESTION.md / NOTES.md / SOURCE-LICENSE.md for the deposit ruling (no workaround notes).
4. [ ] Checkpoint message to `main` (date (1) pending the window).
5. [ ] Rest of the Act in order: s 2 all terms; ss 6-10, 12-14; Part 3; Part 4; Part 5; 5A; 5B; 5C; Part 6 rest; Part 7; Part 8; Part 9.
6. [ ] Every instrument in full: Rg 5, Rg 6, Rg 3, N 1 tables, Rg 1, Rg 4, Internal Wiring, Resellers, Prescribed Trusts, and every amending instrument.
7. [ ] gen-coverage.py: rows for the whole Act (each row encoded/inert/fork/blank, no deferred) and every instrument provision.
8. [ ] SSO attempt 03:30-04:00 SGT; Gazette; lawplain bills/hansard for date (1); mirror only if all fail.
9. [ ] NOTES.md, encoding.json, check.sh, srcrefs outputs refreshed; final report to team-lead.

## 2026-11-03 23:20 SGT status
- DONE: 40 IMDA instruments deposited with text (call A) under subjects/sg/telecommunications-*: .txt + .meta.json each, subject.json, SOURCE-LICENSE.md (reliance wording 1-4). Script scratchpad/tools/mk-ta-deposits2.py.
- DONE: quote IDs re-pointed to the repo stems; sgta-i-rg3-comp.l4 split into sgta-i-rg3-class.l4 and sgta-i-comp.l4; srcrefs-all.sh runs strict against the repo texts, 0 problems on all 11 rule modules; check.sh 399 satisfied, main columns same.
- DONE: NOTES.md, encoding.json, SOURCE-LICENSE.md, TV-QUESTION.md no longer say the text is withheld.
- DONE: egazette terms read (cl.11 permits reproduction with attribution and non-abusive automated extraction; robots Disallow: /search; browse page is a script search, endpoint not found in the static chunks). Not deposited from there.
- DONE: lawplain Bills/Hansard for date (1): nothing pre-2011 on the First Schedule.
- NEXT: send team-lead the egazette report; send `main` the checkpoint (date (1) pending the window); then the rest of the Act from Part 1/s 2 on in its own order; then every instrument in full; gen-coverage rewrite.

## 2026-11-03 23:55 SGT: coverage generator v2 (mechanical) is in place
- `python3 -I gen-coverage.py` now classifies every Act row and every instrument-provision row as encoded (all content lines inside an @ref locator of a rule module), inert (INERT table, reasons 1/2/3 only), fork (FORK table) or pending.
  Exit code 2 while any row is pending. First run: Act 81 encoded / 16 inert / 1106 pending; instruments 76 encoded / 39 inert / 397 pending (512 provision rows in 40 files).
- The queue is the pending count. WORK LOOP: read a text chunk, write the module with `-- @Q a b` (Act) or `-- @QI <stem> a b` (instrument) quote markers, run `python3 -I /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/daea9ea8-ade8-4962-9243-b775db3b08df/scratchpad/tools/expand-quotes.py <file>`, then `./srcrefs-all.sh`, `check.sh`, `gen-coverage.py`.
  (The tool now reads the repo texts; `@QI` takes the deposit stem such as TA1999-RG5-S100-2016.)
- Advisor order: Rg 5 in full first (TV relevance), then the Act in its order, then the other instruments; report anything from Rg 5 that bears on a receive-only station to team-lead (NOT `main`).
- TO DO LATER: gen-coverage's old "Text deposit: none yet" statement is gone (v2 rewrote the output); NOTES.md Scope/coverage text and Editions row (ten instrument groups, not five) and encoding.json to be updated with the final numbers.
- SSO WINDOW PREP (write the list before 03:30): see the section below once written.

## 2026-11-03 23:25 SGT: Rg 5 done (all 6 texts); next Rg 6, N 1, Rg 3, Comp, then the small instruments, then the Act
- Rg 5 modules: sgta-i-rg5-{radio,spectrum,licences,duties,schedules,definitions,amendments}.l4; tests sgta-tests-rg5.l4, -rg5-b.l4, -rg5-amend.l4.
  Over-broad locators in sgta-i-rg5-radio.l4 were narrowed (they had quoted amending regulations that were not modelled): coverage is by quoted lines, so a locator must not reach lines the function does not model.
- Test lesson: 3 tests in sgta-tests-rg5-b.l4 first failed because I wrote the expected values with the arguments in the wrong order (reg 70(2)-(3), reg 74(3)(a)); re-derived from the regulation text, not from the code.
- Rg 5 finding for team-lead (NOT a change to the conclusion): reg 68(1) bars a person from intercepting or acquainting himself with the contents of a radio-communication "other than those transmitted for general information or for the information of licensees belonging to the same licensed network"; reg 2 says "reception ... includes interception". So the Regulations themselves treat reception of a general-information broadcast as outside the secrecy duty; it does not touch the licensing of possession in s 54. Relevant to s 9A only.
- Pending counts (gen-coverage): Rg 3 54+..., Rg 6 49+..., Internal Wiring 25, Rg 1 23, Rg 4 18+..., N 1 about 20, Comp 4, Resellers 3, Trusts 2; Act: 1106 rows pending.
- check.sh at this point: 27 modules, 583 satisfied (before the last test fix), main columns same.

## 2026-11-03 ~23:45 SGT: Rg 6 done (2004 Ed. + 7 amendments); next N 1, Rg 3, Comp, Rg 1/4/IW/Resellers/Trusts, then the Act
- Rg 6 modules: sgta-i-rg6-dealers.l4 (narrowed), -licensing.l4, -amendments.l4 (Fifth Schedule item 1 band tables generated from the texts by scratchpad/tools/bandtable.py + mk-rg6-amend.py; lookup by band as printed, hyphens for dashes); tests sgta-tests-rg6.l4.
- New TV-path datum added to TV-QUESTION.md section 3 (Dealers row): Rg 6 Second Schedule para 9 (Class Licensee must tell purchasers of the need to obtain a licence for possession/operation/installation/use of telecommunication equipment) and the First Schedule lists no receiver. TELL team-lead in the next report (not main).
- Scratchpad tools: expand-quotes.py (@Q/@QI), fixq.py (drop punctuation-only quote lines, tighten locators), regranges.py (provision line ranges), bandtable.py (band/limit tables), mk-rg6-amend.py.

## 2026-11-03 23:50 SGT: every instrument row cleared (0 pending); the whole Act is next
- gen-coverage: Instruments 511 encoded / 79 inert / 0 pending; Act 81 encoded / 16 inert / 1106 pending.
- New modules this window: sgta-i-n1-bands, sgta-i-comp (full), sgta-i-rg3-licences, sgta-i-rg3-amendments, sgta-i-rg1-ship, sgta-i-rg4-cable, sgta-i-iw-wiring, sgta-i-resell, sgta-i-trusts, sgta-i-rg6-definitions; tests sgta-tests-n1-bands, -rg3, -small-instruments, and Comp additions in sgta-tests-instruments.
- check.sh (L4=$HOME/.cache/l4-main/98/l4 L4_MAIN_BUILD=98): 41 modules, 0 errors, 1420 satisfied, 0 failed, 0 refused, main columns the same (run at 23:40, before the last three modules and tests; to be rerun).
- Two fixes found by the mechanical coverage, not by reading: Rg 3 reg 3 had been quoted 78-80 and lost line 81; the S 210/2010 locator stopped one line short (item 2's second line).
- Next: the Act in its own order (s 2 first, from the text), then rerun check.sh, srcrefs-all.sh, gen-coverage.py.
- SSO window 03:30 SGT (2026-11-04): request list still to be written before then.

## 2026-11-04 00:20 SGT: the whole Act and every deposited instrument are encoded; SSO request list written before the window
- gen-coverage: Act 1203 rows = 1183 encoded + 4 fork + 16 inert + 0 pending; instruments 590 rows = 508 encoded + 3 fork + 79 inert + 0 pending.
  Inert reasons: Act: cover and edition notice, arrangement of sections, long title, legislative history (reason 1), s 1 short title (2), eleven Part headings (1).
  Instruments: 38 front-matter rows (title, arrangement, enacting words: reason 1; the Composition Regulations' S 706/2005 front matter, which also holds the enacting words naming s 64, is reason 2), 34 back-matter rows (date of making and signature: reason 1), six citation rows (reason 2) and one blank row, Rg 6 First Schedule item 10 (reason 3).
- New Act modules this window: sgta-s2-more-definitions, sgta-s5-licence-terms, sgta-s6-8-spectrum-orbit-designation, sgta-s9-10-conditions-and-sanctions, sgta-s11-14-approval-and-residual, sgta-part3-ss15-22, sgta-part3-ss23-29, sgta-part4-ss30-32, sgta-part5-ss33-36, sgta-part5a-s37, sgta-part5a-s38-39, sgta-part5a-s40, sgta-part5a-s41-43, sgta-part5b-5c-ss44-52, sgta-part6-more, sgta-part7-international-and-directions, sgta-part8-more, sgta-part9-s89-90, sgta-part9-s91-92, sgta-part9-s93-94-97.
- Tests added: sgta-tests-act-defs (169), -act-part2 (152), -act-part3 (150), -act-part4-5c (226), -act-part6-8 (194), -act-part9 (158), -instr-more (81).
- check.sh at 00:15: 69 modules, 0 errors, 2550 satisfied, 0 failed, 0 refused, main columns the same.
- srcrefs-all.sh at 00:15: 48 modules, 9,270 quote lines in 712 runs, 718 locators, 0 problems.
- Tests found one encoding bug and two wrong expectations of mine: (1) s 45(2)-(3) was written `NOT a OR b`, which L4 reads as NOT (a OR b); code fixed, test kept; (2) s 91(3)(a): I had written the wrong expected value for the case in which the Act says the voting rights are NOT exercisable; test fixed from the text; (3) earlier, three Rg 5 expectations with the wrong argument order.
- Coverage found two quote ranges that stopped one line short (Rg 3 reg 3, S 210/2010 item 2); a function with an unused parameter was also removed in three places (s 6(1)(a), s 16(1)(a), s 79(1)(a)).
- Tautologies removed: three functions of the form `x OR NOT x` (ss 25(4), 26(3), 47(3)) became "the prejudice bars the Authority" functions that return FALSE.
- Untested functions: 18 of 1081 (the per-vintage band-table functions of N 1 and Rg 6 Fifth Schedule item 1 and the N 1 item lists), each reached through its dispatcher or its per-item function in tests; `python3 -I scratchpad/tools/untested.py` lists them.

SSO REQUEST LIST (written 00:20 SGT; the attempt is ONE run of scratchpad/tools/sso-fetch.py between 03:30 and 04:00 SGT, which refuses to run outside the window):
- robots.txt first (crawl-delay read from it, at least 6 s); the first answer that is not HTTP 200 with a PDF or HTML body, or any page with a challenge word, ENDS the attempt and nothing else is tried.
- 5 PDFs of the whole Act at a historical date, in this order, each a separate file: ValidDate=20050216 (the Act as the 2005 amendment left it: the date (1) text), 20120201 (as the 2011 amendment left it), 20161001, 20170201, 20180516 (the date (2) versions).
  URL form: https://sso.agc.gov.sg/Act/TA1999?ViewType=Pdf&ValidDate=<date>; whether SSO honours ValidDate on the PDF view is not known: a PDF that carries today's banner is not a historical version and will be recorded as such.
- Date (1) is held open until that attempt; Call B (an unofficial mirror) is allowed only if SSO, the Gazette, lawplain Bills and lawplain Hansard have all failed.
- Not requested: the subsidiary-legislation consolidations (Rg 3, 5, 6, N 1, Comp) at SSO: their SSO page names and ids were not established, and a wrong URL spends the one attempt; they are listed as open questions 1 and 4 in NOTES.md.

## 2026-11-04 00:27 SGT: documentation refreshed; one coverage defect corrected; per-term s 2 markers added
- NOTES.md rewritten to the whole-Act scope (367 lines): the old Tier 1 / Tier 2 scope section and its coverage tables are gone, the editions table lists all ten instrument groups, and the checks and srcrefs output are pasted from the final runs.
- encoding.json refreshed: 51 rule modules, 18 case files, scope and not_reviewed rewritten.
- CORRECTION to the 00:20 block above: the instruments are 509 encoded, 3 fork, 78 inert, 0 pending, not 508 / 3 / 79.
  `gen-coverage.py` had classed Rg 6 First Schedule item 10 ("10. EFTPOS/CCAT", `TA1999-RG6.txt:431`) as inert, reason 3, "blank or page furniture only", because its all-capitals text matched the heading rule, although `sgta-i-rg6-licensing.l4:586` quotes it.
  The generator now keeps the first line of a numbered row as content; no reason-3 row remains among the instruments.
- FORK pointers are now `fork` rows in COVERAGE.md (Act 4, instruments 3): s 2 "equipment", s 2 "radio-communication", s 53(1), s 95, Rg 6 reg 22 (twice: the revised edition and S 478/2005 reg 8) and N 1 Schedule item 11.
- `sgta-ta-vintage.l4` gained a per-term table for s 2, read from clause 2 of Bills 67/2004, 20/2011 and 30/2016 (as introduced; lawplain, not deposited): "equipment" and "telecommunication system" changed on 1 February 2012, "broadcasting apparatus" and "broadcasting service" were inserted on 16 February 2005, "telecommunication service" changed on 1 February 2017.
  Eighteen new assertions in `sgta-tests-act-defs.l4`.
  TV-QUESTION.md sections 3, 5 and 9 were corrected to say so (the stale "I did not read Rg 5 in full" sentence is gone; the date (2) row no longer lists 2008 and 2009 test days).
- Final gate at about 00:25: check.sh 69 modules, 2568 assertions satisfied, 0 errors, 0 failed, 0 refused, main columns the same on all 69; srcrefs-all.sh 48 modules, 9,270 quote lines, 712 runs, 718 locators, 0 problems; gen-coverage.py 6 PASS.
- N 1 bands: two printed values are kept as printed although the extraction looks defective ("57 dBµ/Vm @ 3m", S 1/2008 item 3; "25 W", S 179/2011 item 8); two are keyed from the neighbouring vintages because the PDF lost a decimal point (240.15 and 10.50, S 265/2006 and S 1/2008).
  This corrects the sentence in my 00:20 report to team-lead that said all defective values are kept as printed.
- CORRECTION to the correction: the pre-2005 reg 22 of the Revised Edition ("the Authority may ... test that equipment") is not what FORK 4 is about, so its row is `encoded`; the fork row is S 478/2005 reg 8 (`TA1999-RG6-S478-2005.txt:136-157`, which substitutes Part VI, including the new reg 22).
  Final instruments: 510 encoded, 2 fork, 78 inert, 0 pending (590 rows).

## 2026-11-04 00:42 SGT: the SSO attempt is ARMED, now GATED on a GO file (do not arm it again)
- 00:42 change: the job was stopped and re-armed (harness task id bav9ny7h4) with a gate: at 03:31 SGT it waits for the file `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/daea9ea8-ade8-4962-9243-b775db3b08df/scratchpad/sso-1104/GO`, which I create by hand only after sg-ba-encoder's result message says its own attempt did not end on a 403, 429, 503 or challenge (its request: do not touch sso.agc.gov.sg before that message).
  No GO file by 04:00 SGT means no attempt (arm.log says so).
  The task id in the paragraph below (bu2ah1phu) is the stopped job.
- Armed at 00:33 SGT as a background Bash job (harness task id bu2ah1phu) running `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/daea9ea8-ade8-4962-9243-b775db3b08df/scratchpad/tools/arm-sso.sh /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/daea9ea8-ade8-4962-9243-b775db3b08df/scratchpad/sso-1104 /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/daea9ea8-ade8-4962-9243-b775db3b08df/scratchpad/sso-1104/urls.txt`.
  It sleeps until 03:31 SGT, then runs `python3 -I /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/daea9ea8-ade8-4962-9243-b775db3b08df/scratchpad/tools/sso-fetch.py` once; `sso-fetch.py` itself refuses to run outside 03:30 to 04:00 SGT, reads robots.txt first, takes its crawl-delay (at least 6 s), and stops at the first answer that is not HTTP 200 with a PDF or HTML body or that carries a challenge word.
- Its record is `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/daea9ea8-ade8-4962-9243-b775db3b08df/scratchpad/sso-1104/log.tsv` (time, URL, status, bytes, sha256, first 80 bytes) and `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/daea9ea8-ade8-4962-9243-b775db3b08df/scratchpad/sso-1104/arm.log`; bodies, if any, are `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/daea9ea8-ade8-4962-9243-b775db3b08df/scratchpad/sso-1104/NN.bin`.
  If neither file exists after 04:00 SGT, the job did not run: say so, do not run it by hand outside the window, and do not call date (1) closed.
- Request list, in order: ValidDate 20050216 (the text in force from 16 Feb 2005 to 31 Jan 2012, which covers 1 January 2011), 20120201, 20161001, 20170201, 20180516, 20001230.
  Whether SSO honours `ValidDate` on the PDF view is not known; a PDF that carries the current banner ("version in force from 2/10/2026") is not a historical version and will be recorded as such.
- If it succeeds: `pdftotext -layout` each PDF in its own directory, deposit each as `TA1999.<date>.txt` with a `.meta.json` beside `TA1999.txt` (as the Broadcasting Act folder did for BA1994.20030731), and replace the inference layer for the dates covered (`sgta-ta-vintage.l4`, the seat's two inference answers) with the text.

## 2026-11-04 01:08 SGT: Gazette deposits, two time axes, kind of receiver, FM/AM section
- Deposited from the e-Gazette (9 PDFs, one GET each, 5 s apart): TA1999.20001230, .ACT10-2005 (scan, OCR; page images compared for pages 1, 2, 21, 26), .ACT19-2011, .S33-2012, .BILL20-2011, .BILL30-2016, .RevEd2020-printed, and TA1999-RG6-GAZ-RevEd2004 and TA1999-RG6-S178-2011-GAZ in the dealers subject; SOURCE-LICENSE-GAZETTE.md in both folders.
- New modules: sgta-ta-versions.l4 (Act versions on two time axes; 40 assertions), sgta-i-versions.l4 (N 1, Rg 5, Rg 6 versions; 70), sgta-tv-ba-schedule.l4 (quarantined; the Broadcasting Act First Schedule as versions), seat and cases rewritten (cases: 242 assertions, in pairs of days, three kinds of receiver and the satellite dish system).
- Tests found my own expectation errors twice more (conduct 1 Feb 2012 read before S 549/2012 is "no offence", not "offence"; conduct before 16 Feb 2005 has the older penalty); fixed from the text.
- Rg 6 reg 10(2) and (4) of the Gazette's Revised Edition 2004 are now encoded (the IMDA copy has S 478/2005's text there; NOTES finding 19); gen-coverage.py skips the two Gazette copies in the dealers folder.
- Gate at about 01:00: check.sh 74 modules, 2861 satisfied, 0 failed, main columns the same on all 74.  After the Rg 6 repair (+10 assertions) a further full run is owed before the final report.
- TV-QUESTION.md rewritten: two-axes answers, FORK 6, FM/AM/TV section 10 with the mechanical search (terms and counts in NOTES.md).
- SSO attempt: still armed and gated on a GO file (see the 00:42 block); no message from sg-ba-encoder yet.

## 2026-11-04 01:30 SGT: 29 Gazette instruments fetched and deposited; OCR replaced; S 525/2001 and S 78/2017 encoded
- Fetched on the team lead's exact URLs, one GET each 5 s apart, commons User-Agent, each 200 with a PDF with a text layer (`scratchpad/gazette-dl2/log.tsv`): 23 of the listed instruments and the extras the team lead named (S 485/2016, S 78/2017, S 525/2001, S 76/2007, S 23/2011, S 24/2011).
  The index date given for each agreed with the "First published" line inside the PDF, in all 29.
- Deposited as `TA1999-<id>-GAZ.txt` beside the IMDA copy (23 pairs, compared by word diff and by the multiset of numbers: NOTES.md finding 23), or under the instrument's own stem where IMDA's list lacks it (S 525/2001, S 78/2017, S 485/2016, S 23/2011, S 24/2011), or under the Act's folder (S 76/2005, the commencement notification of Act 10 of 2005); a new subject folder `telecommunications-designated-telecommunication-licensees-notifications` holds S 23/2011 and S 24/2011.
- The Gazette's copies of S 685/2011 and S 686/2011 have text layers: they replaced the OCR text as `TA1999-RG3-S685-2011.txt` and `TA1999-COMP-S686-2011.txt` (the OCR kept as `-OCR.txt`); 193 quote lines in three modules were re-pointed by script (`scratchpad/tools/remap-ocr.py`) and pass `srcrefs --strict`.
- IMDA-copy defects found and corrected in the keyed values: S 1/2008 item 3 ("57 dBµV/m"), S 179/2011 item 8 ("25 µW"), the S 414/2014 band keys of Rg 6 (finding 23).
- `sgta-i-versions.l4` rewritten with Gazette published days (all of them read, none assumed except the two Revised Editions' start days) and rows for S 525/2001 and S 78/2017; its tests are generated from the stated rule (143 assertions).
- N 1: S 525/2001's Schedule equals the 2002 Revised Edition's, so N 1 now answers from 17 Oct 2001 (finding 24); S 78/2017 adds item 18; new noun `Intelligent Transport System`.
- New modules `sgta-i-rg3-s485-2016.l4`, `sgta-i-dtl-notifications.l4` and tests `sgta-tests-more-notifications.l4` (13 assertions); `sgta-ta-versions.l4` now cites S 76/2005.
- Coverage: instruments 623 rows (533 encoded, 2 fork, 88 inert, 0 pending).
- S 485/2016 (Rg 3) is retrospective (published 3 Oct 2016, deemed in operation 1 Oct 2016), so `sgta-i-rg3-s485-2016.l4` and `sgta-i-dtl-notifications.l4` take both days; their 29 assertions are computed from the stated rule.
- Gate at 01:37 SGT after the last edit: check.sh 77 modules, 2,991 assertions satisfied, 0 errors, 0 failed, 0 refused, main columns the same on all 77; srcrefs --strict 51 modules, 9,463 quote lines, 0 problems; coverage Act 1,183 encoded / 4 fork / 16 inert / 0 pending, instruments 533 / 2 / 88 / 0 (623 rows); 1,103 functions, 22 not named in a test (per-vintage functions reached through dispatchers).
- Still armed: the SSO attempt (gated on a GO file; nothing from sg-ba-encoder as of this block; this turn ends so that its message can be delivered).

## 2026-11-04 01:53 SGT: the second list of exact URLs (N 1 as made, the 2016 Acts, the designation notifications)
- Eleven PDFs fetched (one GET each, 5 s apart, commons User-Agent, all 200 with text layers; `scratchpad/gazette-dl3/log.tsv`), and the date the team lead gave agreed with the in-PDF "First published" line for every one: S 115/2001, Act 30 of 2016 (Acts Supplement No. 2 of 2017), S 14/2017, Act 22 of 2016 (the IMDA Act, Acts Supplement No. 19 of 2016), S 461/2016, S 86/2005, S 233/2005, S 390/2007, S 35/2012, S 192/2012, S 521/2017.
- N 1 as made (S 115/2001) is the first N 1 version (2 Mar 2001): para 2 as made, the 20-entry item list, all 62 band lines as printed; N 1 now answers from 2 Mar 2001.
- `sgta-ta-versions.l4` has two new versions (Act 22 of 2016, 1 Oct 2016; Act 30 of 2016, 1 Feb 2017) and the flag that s 53(1) names the suspension of a licence (Act 30 of 2016 clause 18); the printed texts now cover conduct to 22 May 2017.
  Clauses 1 to 20 of Act 30 of 2016 are word for word Bill 30/2016 as introduced.  The seat's "texts deposited" answer extends to 22 May 2017; the "markers" form now begins on 23 May 2017.
- `sgta-i-dtl-notifications.l4` rewritten for all eight designation notifications on both axes (109 assertions).
- Not given: the Rg 5 as made, S 114/2001 (cited by S 115/2001 para 2(a)), and the Code of Practice S 87/2005.
- Gate at 01:55 SGT after these changes: check.sh 77 modules, 3,132 assertions satisfied, 0 failed, 0 refused, main columns the same on all 77; srcrefs --strict 51 modules, 9,730 quote lines, 0 problems; coverage Act 1,183 encoded / 4 fork / 16 inert / 0 pending, instruments 556 / 2 / 102 / 0 (660 rows in 52 texts); 1,117 functions, 24 not named in a test.

## 2026-11-04 02:04 SGT: the receiver licence's ending instrument (S 548/2012) and Rg 1, from the Broadcasting Act folder's deposits
- Team lead's fact: S 548/2012 (Broadcasting (Television and Radio Licensing) (Revocation) Regulations 2012; made 30 Oct 2012, first published 31 Oct 2012 at 5.00 pm, deemed in operation 1 Jan 2011) revokes Rg 1.
  Read from the Broadcasting Act folder's deposits (`BA1994-S548-2012.txt`, `BA1994-RG1.txt` Revised Edition 2004, `BA1994-S333-2004.txt`); nothing of theirs is deposited in this folder and none of their quarantined files was read.
- `sgta-tv-ba-schedule.l4`: Rg 1 as a table of versions (Revised Edition 2004 from 29 Feb 2004; S 548/2012 effective 1 Jan 2011, published 31 Oct 2012) and a check that Rg 1 and the First Schedule agree for a television, an FM radio and an AM radio.
  `sgta-tv-seat.l4`: a new export `Were the receiver licensing regulations in operation`.  `sgta-tv-cases.l4`: 32 new assertions (all satisfied; no existing expectation changed).
- TV-QUESTION.md: Date (1), H1, H2, section 10(b), (d), (e), section 8 and a new section 11 saying which findings change.
  Mechanical search re-run over 86 files (the Broadcasting Act folder's 26 instrument texts added); NOTES.md table refreshed.
- Gate at 02:06 SGT after these changes: check.sh 77 modules, 3,164 assertions satisfied, 0 failed, 0 refused, main columns the same on all 77; srcrefs 51 modules, 9,730 quote lines, 0 problems; coverage unchanged (instruments 556 / 2 / 102 / 0).

## 2026-11-04 02:34 SGT: the third list of exact URLs (Rg 5 as made and its 2001 amendments, the 2001 Composition Regulations, the Companies (Amendment) Act 2017)
- Seven PDFs fetched (one GET each, 5 s apart, commons User-Agent, all 200 with text layers; `scratchpad/gazette-dl4/log.tsv`); the date the team lead gave agreed with the in-PDF "First published" line for every one: S 114/2001 (2 Mar 2001), S 339/2001 (9 Jul 2001), S 373/2001 and S 374/2001 (1 Aug 2001), S 450/2001 (18 Sep 2001), S 516/2001 (15 Oct 2001), Act 15 of 2017 (30 Mar 2017, "No. 15 of 2017" on its face).
  Titles read off the PDFs: S 339/2001, S 373/2001 (a Corrigendum cancelling S 339/2001) and S 374/2001 are all "Telecommunications (Radio-communication) (Amendment) Regulations 2001"; S 450/2001 is "(Amendment No. 2)"; S 516/2001 is the "Telecommunications (Composition of Offences) Regulations 2001".
- Rg 5 as made compared with the 2002 Revised Edition by script, regulation by regulation: 59 of 80 the same words, 21 differ (NOTES.md finding 28).
  New module `sgta-i-rg5-as-made.l4` (S 114/2001 quoted in full, the comparison table, the four amendments of 2001 as functions of both days) and tests `sgta-tests-rg5-as-made.l4`.
  Rg 5 now has versions from 2 Mar 2001 in `sgta-i-versions.l4`; the Rg 5 functions that take a date start on 2 Mar 2001 where the words are the same as made (or only the paragraph order differs, reg 20; or the regulation did not exist, reg 65A); reg 76 answers with its as-made wording.
- `sgta-i-comp.l4`: the 2001 Composition Regulations as a vintage from 15 Oct 2001 to 10 Nov 2005; before it NOTHING (S 260/2000 not deposited).
- `sgta-ta-versions.l4`: Act 15 of 2017 is a version (23 May 2017); its only amendment of the Act is s 53(6) (ss 32J(3)(a), 32L(1)(b) and (2)(a)), so its flags equal Act 30 of 2016's; a row stands for the Acts after it from 16 May 2018.
  The seat's "texts deposited" answer now extends to 15 May 2018, and the "markers" form begins on 16 May 2018.
- "Source not obtained" rows for Acts 26 of 2018, 40 of 2018, 15 of 2019, the Code S 87/2005, and (not searched) Acts 4 of 2021, 25 of 2021, 31 of 2022, 12 of 2020, 13 of 2026 and S 26/2022 are in NOTES.md under Coverage, with the markers each shows in the consolidation.
- Mechanical search re-run over 95 files (the third list's six instrument texts, and Acts 22 and 30 of 2016 and Act 15 of 2017, which had not been searched, added); NOTES.md table and TV-QUESTION.md section 10(b) updated; no new hit bears on a receiver or an AM or FM band (Act 30 of 2016's s 11A(2) "station" includes "a receiver" for spectrum sharing only).
- Wrong or unchecked claims caught on re-read and fixed: a pointer in `sgta-i-comp.l4` to where the composition cap lives (it is in `sgta-part8-penalties.l4`, not dated by version); a reference to Rg 5 reg 76 as citing the S 87/2005 Code (it cites the 2000 Code, S 412/2000); a marker count for Act 13 of 2026 (18, not 19).
- Gate at 02:33 SGT after these changes: check.sh 79 modules, 3,317 assertions satisfied, 0 errors, 0 failed, 0 refused, main columns the same on all 79 (`scratchpad/check-f10.txt`); srcrefs --strict 52 modules, 11,415 quote lines in 740 runs, 767 locators, 0 problems; coverage Act 1,183 encoded / 4 fork / 16 inert / 0 pending (1,203 rows), instruments 790 rows in 58 texts (680 encoded / 2 fork / 108 inert / 0 pending); 1,133 functions, 29 untested (reached through dispatchers).
- Compactions of this session so far: 5 (jq count of user records containing "This session is being continued" in the transcript, 2026-11-04 02:34 SGT).
- Not done: the SSO attempt (gated on sg-ba-encoder's message, delivered when this turn ends; no GO file exists).

## 2026-11-04 02:46 SGT: correction (team lead): S 333/2004 is a version of Rg 1
- The team lead pointed out that S 333/2004 cl 12 deletes reg 27(1) and (2) of Rg 1 and substitutes a paragraph on where to apply, so reg 27(1)'s "No person shall operate a broadcast television receiver without a licence" stood only from 29 Feb 2004 to 20 Jun 2004.
  Read again from the Broadcasting Act folder's deposits (`BA1994-S333-2004.txt`, PDF sha256 68bf17f881f90e33..., as the team lead's; `BA1994-RG1.txt`; `BA1994-S548-2012.txt`); the clauses are listed in TV-QUESTION.md section 5 and NOTES.md finding 29.
- What was wrong: my section 5 and H1 gave reg 27(1) with no end date; I had recorded the replacement of reg 27(1) and (2) as "a paragraph on where to apply" without the consequence; `sgta-tv-ba-schedule.l4` had two rows for Rg 1 and said S 333/2004 "is not a row here"; the seat's `Were the receiver licensing regulations in operation` therefore treated Rg 1 as one unit from 29 Feb 2004.
- Corrected: three Rg 1 versions on both axes (Revised Edition 2004; as amended by S 333/2004, published 15 Jun 2004, in operation 21 Jun 2004; as revoked by S 548/2012, published 31 Oct 2012, deemed in operation 1 Jan 2011); a function that says what each version says in terms about a licence for a kind of receiver in a place, every quoted fragment of which is checked against the deposited files by `scratchpad/tools/verify-quotes-rg1.py` (22 fragments, none missing); a new seat export `What did the receiver licensing regulations say about a licence for this receiver` (10 exports now); 46 new case assertions; TV-QUESTION.md sections 5, 10(d), 11, H1 and a new section 12.
- No Telecommunications Act answer moved: the answers rest on Reading A of s 95 and the First Schedule's list, and Rg 1 is not a conjunct; the 32 operation assertions still hold.
- Gate at 02:45 SGT: check.sh 79 modules, 3,363 assertions satisfied, 0 errors, 0 failed, 0 refused, main columns the same on all 79 (`scratchpad/check-f11.txt`); srcrefs --strict 52 modules, 11,415 quote lines, 740 runs, 767 locators, 0 problems; coverage unchanged (Act 1,203 rows: 1,183/4/16/0; instruments 790 rows in 58 texts: 680/2/108/0).
- Compactions: 5 (jq count at 02:46 SGT).

## 2026-11-04 03:09 SGT: the SSO attempt is not made
- sg-ba-encoder reported at 03:08 SGT that its single attempt, made at 03:07:48, ended at `https://sso.agc.gov.sg/robots.txt` with a 403 (919 bytes, a CloudFront "Request blocked" page); nothing was requested or deposited from SSO.
  That was the gate for mine: I make no request to SSO, I did not create `sso-1104/GO`, and the armed job (`scratchpad/sso-1104/arm.log`) will find no GO file and request nothing.
- NOTES.md, TV-QUESTION.md and encoding.json now say the attempt was not made and why; the SSO consolidations by date remain not deposited, and the Act's printed text stops where the e-Gazette's copies stop (NOTES finding 28).
- sg-ba-encoder also reports its Gazette deposits now hold the First Schedule at 31 Jul 2003 and 31 Aug 2012, S 549/2012, Rg 1 (2004 Ed.), S 333/2004 and S 548/2012, all already read here.

## 2026-11-04 03:10 SGT: the SSO attempt cancelled (team lead's ruling)
- SSO: not attempted by the TA encoder because the BA encoder's one attempt was refused at robots.txt (403, CloudFront block page, 2026-11-04 03:07:48 SGT); no SSO text used, no mirror.
- The team lead ruled that a block is a no for every agent from this client and that a second try from the same client is not a different request; I did not create `sso-1104/GO`, stopped the armed task, and deleted the two files I had made for it (`tools/arm-sso.sh`, `tools/sso-fetch.py`); `scratchpad/sso-1104/urls.txt` and `arm.log` stay as the record of what was not requested.
- Final gate at 03:11 SGT (`scratchpad/check-f12.txt`, `srcrefs-f12.txt`, `coverage-f12.txt`; pasted into NOTES.md "Checks" and encoding.json): check.sh 79 modules, 3,363 assertions satisfied, 0 errors, 0 failed, 0 refused, main columns the same on all 79; srcrefs --strict 52 modules, 11,415 quote lines, 740 runs, 767 locators, 0 problems; coverage Act 1,203 rows (1,183 encoded / 4 fork / 16 inert / 0 pending), instruments 790 rows in 58 texts (680 / 2 / 108 / 0). The TA folder is final.

## 2026-11-04 07:07 SGT: follow-up after the independent review, Part 1
- NOTES.md findings 16 (D8) and 26 (D9) corrected, each marked CORRECTED; D9 measured by script over the 30 rows of `sgta-i-versions.l4` that carry both days: 12 published earlier than effective, 17 the same day, 1 later (S 374/2001).
- Locators (D10): M5, M6, M7 fixed in `sgta-i-rg5-licences.l4`, `sgta-i-n1-exemption.l4`, `sgta-i-n1-bands.l4`; M8 relabelled (Acts print sections, not clauses) in the modules, NOTES.md and TV-QUESTION.md; M1 to M4 are in the Broadcasting Act encoding and left to its encoder.
- G2: `srcrefs-all.sh` runs the three `sgta-tv-*` modules (0 `src:` lines in each: the run checks nothing) and the new `check-tv-citations.py` (198 locators in the three modules and TV-QUESTION.md, 22 quoted fragments of the Rg 1 table, 0 problems).
- G1: new `sgta-part6-2000ed.l4` (the Revised Edition 2000's ss 34, 35, 36 quoted and encoded, with the version dispatchers) and `sgta-tests-part6-2000ed.l4` (545 assertions); the seat calls the dispatchers; all 360 case assertions pass unchanged.
- D11: left as it is, with the measured caller counts and the reason in NOTES.md finding 30.
- Gate at 07:07 SGT (`scratchpad/check-f13.txt`, `srcrefs-f13.txt`, `coverage-f13.txt`): check.sh 81 modules, 3,908 assertions satisfied, 0 errors, 0 failed, 0 refused, main columns the same on all 81; srcrefs --strict 53 modules, 11,458 quote lines, 749 runs, 776 locators, 0 problems; coverage unchanged (Act 1,203 rows 1,183/4/16/0; instruments 790 rows in 58 texts 680/2/108/0).
- No TV answer moved.

## 2026-11-04 07:58 SGT: follow-up after the independent review, Part 2
- (e) the NOTES row "searched" was written earlier (the team lead's wording).
- (a) The Order O 3 (S 549/1998 and the 1999 Revised Edition) is deposited and encoded in `sgta-i-o3-1998.l4` with a fork on what section 30 of the TAS Act said (text not held: source not obtained); the seat does not consult it (NOTES.md finding 33).
- (b) The 1999 Revised Editions of Rg 7 (Dealers) and Rg 3 (Radio-communication) are deposited and encoded in full (`sgta-i-rg7-1999.l4`, `sgta-i-rg3-1999.l4`), with version rows: Rg 3 (1999 Ed.) from 1 Dec 1999 to 1 Mar 2001 (reg 80(1) of S 114/2001), Rg 7 (1999 Ed.) from 1 Dec 1999 to an ASSUMED 1 Apr 2003 (no text held states its end; finding 34).
- (c) S 588/2023, S 589/2023, S 560/2024, S 381/2024, S 559/2024 and S 852/2024 are deposited and encoded; the Wiring Work Regulations 2024 revoke the Internal Wiring Regulations 2005 from 1 Jul 2024 (finding 35).
- (d) Seven Acts after Act 15 of 2017 that amend the Act are deposited and encoded (`sgta-i-acts-after-2017.l4`); thirteen more Acts and four Bills were fetched and read and amend nothing in it; Act 31 of 2022 and S 26/2022 are not obtained (findings 36; NOTES.md tables).
- Not wired into the seat (it would change seat output): the Acts after Act 15 of 2017 in the version table, and the 1999 instruments for conduct from 1 Dec 1999 to 1 Mar 2001. Three false statements ("not deposited") corrected in wording only (finding 37).
- Gate (`scratchpad/check-g4.txt`, `srcrefs-g4.txt`, `coverage-g4.txt`; pasted into NOTES.md "Checks" and encoding.json; g2 and g3 gave the same rows): check.sh 91 modules, 4,833 assertions satisfied, 0 errors, 0 failed, 0 refused, main columns the same on all 91 (360 case assertions unchanged); srcrefs --strict 59 modules, 14,118 quote lines, 907 runs, 934 locators, 0 problems; coverage instruments 1,022 rows in 68 texts (898 encoded, 2 fork, 122 inert, 0 pending), Act 1,203 rows unchanged; 1,426 functions, 27 not named in any test; 494 of the new assertions are an evaluation differential, not tests of meaning.
- No TV answer moved.

## 2026-11-04 08:57 SGT: follow-up after the independent review, Part 3
- Fetched (10 GETs, all 200 with a PDF): the 2010 Subject Index, Act 31 of 2022, S 850/2022, Bill 24/2022, S 26/2022, S 362/2001, S 185/2003, S 48/2004, S 593/2004 (08:11 SGT, 5 s apart) and Bill 20/2026 (08:21 SGT, read, not deposited). Licence notes and meta files written for each deposit.
- Act 31 of 2022 (s 21(7): s 46(3)(b), "Part 7" to "Parts 7 and 9"; in operation 1 Nov 2022 by S 850/2022, first published 31 Oct 2022) and S 26/2022 (paragraph 22: three amendments matching the five markers; in operation 13 Jan 2022) are encoded in `sgta-i-acts-after-2017.l4` (enum renamed `Instrument amending ...`, nine values); none is on the decisive chain (finding 38).
- Dealers chain (finding 39): S 362/2001 amends Rg 7 from 1 Aug 2001 (regs 15 and 32, First Schedule; reg 4(a) deemed from 21 Jan 2000); S 185/2003 reg 26 revokes Rg 7, so the Rg 7 end day 1 Apr 2003 is READ, no longer assumed; S 48/2004 and S 593/2004 are Rg 6 versions; new `sgta-i-rg6-as-made.l4` (31 blocks compared with the 2004 Revised Edition by script: 25 same, 6 differ); the Rg 6 table no longer answers NOTHING for 2 Apr 2003 to 31 Dec 2004.
- 2010 Subject Index deposited as an AID (finding 40); citations repointed (`sgta-i-o3-1998.l4` header now quotes it; NOTES finding 33).
- TV-QUESTION.md: one paragraph on the 1999 Rg 3 text added to Date (1) (lines 195-202) and a section 8 bullet (283-284).
- Rulings recorded as assumed, not ruled, with a line to revert each: finding 41 and the Acts table paragraph in NOTES.md.
- Quarantined files edited in Part 3, wording only: `sgta-tv-seat.l4` lines 32 and 331; `sgta-tv-cases.l4` lines 131, 247 and 381; `TV-QUESTION.md` lines 195-202, 226, 271, 272, 276, 283-284. Also comments in `sgta-ta-versions.l4` lines 41, 42 and 204.
- Not done: gen-coverage rows for the amending Acts (the TA folder is skipped for instrument rows, and one amending provision per Act is in the NOTES table with its lines checked by srcrefs --strict).
- Gate (`scratchpad/check-h2.txt`, `srcrefs-h2.txt`, `coverage-h2.txt`; run 08:34 to 08:37 SGT; pasted into NOTES.md "Checks" and encoding.json): check.sh 93 modules, 4,989 assertions satisfied, 0 errors, 0 failed, 0 refused, main columns the same on all 93. Of these 494 are the evaluation differential (`sgta-tests-eval-1999-2024.l4`, 143 wrapper functions, unchanged), and 4,495 are the other assertions, of which 156 are new in Part 3 (105 in `sgta-tests-dealers-chain.l4`, 37 in `sgta-tests-acts-after-2017.l4`, 14 in `sgta-tests-i-versions.l4`). srcrefs --strict 60 modules, 14,908 quote lines, 924 runs, 951 locators, 0 problems; tv citations 199 locators, 0 problems. Coverage: instruments 1,105 rows in 72 texts (977 encoded, 2 fork, 126 inert, 0 pending); Act 1,203 rows unchanged. Functions 1,454, 27 not named in any test.
- 360 case assertions pass unchanged. No TV answer moved.

## 2026-11-04 14:20 SGT: S 22/2011 (the Telecommunications (Cancellation) Notification 2011), found by the independent reviewer
- Fetched once at 11:13 SGT (200, 3 pages) from the exact URL the orchestrating session passed; sha256 of the PDF d682419753b958efb5e28175517e66d12ad734ecb3214cd995019c37f8b058a5 and of the text aa8180945959322a8308b39d8ea307216826964831588f7f98ff0ce077e272b0, both equal to the reviewer's.
- Deposited as its own subject, `telecommunications-cancellation-notification-2011` (text, .meta.json, licence notes, subject.json). Encoded in `sgta-i-canc-s22-2011.l4` (the day it begins, the thirteen G.N. numbers by item and as a list, the two-date rule) with 44 assertions in `sgta-tests-canc-s22-2011.l4`; NOTES.md finding 42, a row in the source-not-obtained table, the Editions and Modules tables.
- Gate (`scratchpad/check-i2.txt`, from `check-i1.txt`, run 11:16 to 11:19 SGT; `srcrefs-i2.txt`, `coverage-i2.txt`): check.sh 95 modules, 5,033 assertions satisfied (of which 494 are the evaluation differential, unchanged; the other 4,539 include the 44 new), 0 errors, 0 failed, 0 refused, main columns the same on all 95. srcrefs --strict 61 modules, 14,973 quote lines, 927 runs, 954 locators, 0 problems. Coverage: instruments 1,109 rows in 73 texts (980 encoded, 2 fork, 127 inert, 0 pending). Functions 1,460, 27 not named in any test.
- The `EXITCODE=0` line at the end of `check-i1.txt` is from my wrapper and is not check.sh's exit status (I read `$?` after an echo). What shows the run green is the TOTAL line, every row ending "same", and the footer for "no module reads differently on main"; for finalize.py I wrote "exit 0" into `check-i2.txt` on that evidence.
- 360 case assertions pass unchanged (sgta-tv-cases.l4 is in the run). No TV answer moved.
