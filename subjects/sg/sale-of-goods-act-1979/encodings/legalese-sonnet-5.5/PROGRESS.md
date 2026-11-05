# PROGRESS (iaw-soga, Sale of Goods Act 1979 (Singapore), 2020 RE, informal consolidation in force from 1/4/2022)

Re-read this file, NOTES.md and the text after any compaction, not a summary.

## Paths
- DEPOSIT = <run>/deposit
- ENC = DEPOSIT/encodings/legalese-sonnet-5.5   (flat folder; all soga-*.l4)
- TEXT = .../runs/iaw-soga/inputs/SGA1979.txt   (raw; line numbers in src: locators are this file's)
- WORK = DEPOSIT/work   (templates, generator, coverage script; not a deliverable; deleted at the end of the run)
- L4 = <bin>/l4-main-109 (1.6.109, sha256 eeb12f1e...); L4_MAIN = <bin>/l4-main-108

## Build chain (WORK; the folder was deleted at the end of the run, so this is a record of how the .l4 files were made, not instructions)
- `work/tpl/<module>.l4.tpl`  --gen.py-->  ENC/<module>.l4.  A template line `@@QR <label> | <N-M>[, <N-M>...]` expands to mechanical quote lines (`-- src:N | text`, furniture lines skipped) and an `@ref <label> (src:N-M)` line.  Everything else is copied verbatim.
- `work/cov.py TEXT` parses the text into coverage rows (line ranges); `work/rows.py` holds dispositions; `work/mknotes.py` writes the generated tables of NOTES.md.
- While WORK existed: edit templates, never the generated .l4; run `python3 -I work/gen.py` then `L4=... L4_MAIN=... ./check.sh`.  After deletion the .l4 files here are edited directly.

## Conventions (decided; do not re-litigate)
- Layer 1 = flat modules `soga-nouns`, `soga-part1-application`, `soga-part2-formation`, `soga-part3-effects`, `soga-part4-performance`, `soga-part5-unpaid-seller`, `soga-part6-actions`, `soga-part7-supplementary`, `soga-interpretation` (s 61), `soga-schedule`.  Layer-1 tests: `soga-cases-partN.l4`, each imports only its module(s); the seat never imports case files.  Layer 2: `soga-seat.l4`, `soga-cases-seat.l4`.
- Every top-level name and every enum constructor is unique across the whole import closure of soga-seat (script: work/dups.py).
- Function names start with the section: ``s 14(2) there is an implied condition that the goods are of satisfactory quality``.  Schedule: ``sch para 5 ...``.
- Results: `MAYBE BOOLEAN` (JUST TRUE = text says yes; JUST FALSE = text says no in its words; NOTHING = not covered) or `MAYBE <enum/NUMBER>`.  Every JUST FALSE / "no" branch carries `-- FALSE-kind (the text says no in its own words): "<quote>"`; every NOTHING branch carries `-- NOTHING-kind (<why>)`, why in: silent, list not closed, includes, undefined term, points outside the text, limited by its own wording.
- "Where ..." (not in the brief's list of if-variants) fails to NOTHING (limited by its own wording).  "if / only if / unless / except / save / provided that / so long as / while / until" fail to JUST FALSE, and every such branch is listed under "Marginal readings for a lawyer".  "Unless otherwise agreed" over a VALUE (who bears risk) fails to NOTHING; over a yes/no default it fails to JUST FALSE (marginal).
- Inputs: plain BOOLEAN / NUMBER / DATE / enum facts.  Open-textured judgments (reasonable time, reasonable price, fault, good faith ...) are BOOLEAN inputs worded as facts.
- Borrowed terms (Unfair Contract Terms Act 1977 "deals as consumer", Factors Act 1889 "document of title", "other enactment", "bankruptcy rules", "common law") are inputs.
- Dates: `Date day month year`, never YMD.  No REFUSE / ASSERT REFUSED / BECAUSE (except LEST BREACH BECAUSE).  Parenthesise every NOT.  One-line #ASSERT.  Lists vertical LIST blocks.
- Duties (regulative): `PARTY .. MUST/MAY/SHANT ..` with `#TRACE` for illustration plus a twin decision function (asserted), since a DEONTIC cannot be asserted.  Where the party is an input, compare in `PROVIDED`.
- Each case file ends with `-- assertions written: N`.
- Also run: grep Warning in l4 run of every file; grep 'is at the end of the file|follows code on its line'; srcrefs `check --refs`; work/dups.py.

## Status (updated 2026-11-05)
- [x] read brief, skills, dialects, text
- [x] coverage parser: 385 script rows, every non-blank line covered; 22 overlapping defined-term rows added (407 rows in NOTES.md)
- [x] layer 1: soga-nouns, part1 to part7, interpretation, schedule, routes, duties: all written, all tested (case files soga-cases-*.l4)
- [x] layer 2: soga-seat.l4 (88 questions, 12 groups, after the revision of 2026-11-05; 70 at first) and soga-cases-seat.l4 (275 assertions, all satisfied; 219 at first)
- [x] soga-cases-findings.l4 (16 assertions): findings that cross Parts and the main binary's behaviour
- [x] check.sh with both builds: 25 modules, 0 errors, 1492 satisfied, 0 failed, 0 refused, same on 1.6.108 (1324 before the revision of 2026-11-05; 1445 before the "until" bars)
- [x] srcrefs.py check and check --strict over every layer-1 module: 0 problems
- [x] NOTES.md, encoding.json, SOURCE-LICENSE.md written
- [x] optional second encoding on unstable: written after the main row was complete (see NOTES.md, Unstable dialect)

## Decisions taken (with the text that licenses each)
See NOTES.md, Fork register (the rulings of 2026-11-05 beside E1 and N2; F1 to F13), the hand-gathers G1 to G9 (E1 option B) and the list of marginal readings.
Flat negatives are `JUST FALSE` (N2); the prohibition is derived only where the text names the bearer (s 57(4)).

## Files written
All soga-*.l4 in this folder, check.sh, srcrefs.py, fetch-main-l4.sh, BRIEF.md (a copy), NOTES.md, PROGRESS.md, encoding.json, SOURCE-LICENSE.md.
The build scripts (templates, generator, coverage and notes writers) lived in DEPOSIT/work and are not part of the deliverable; the .l4 files here were generated in the first pass and edited directly in the revision of 2026-11-05 (NOTES.md, Changes of 2026-11-05, item 8); they are the artefact.

## Revision of 2026-11-05
- [x] ruling on periods, "where" and scope limits applied across layer 1, the Schedule and the seat (NOTES.md, Changes of 2026-11-05)
- [x] gaps filled: seat questions for ss 8(1), 10(2), 14(1), 30(3); s 35(6) inputs; s 14(2) and s 61(1) "business" by date; s 48(4) damages limb; 18 yes/no twins and 10 companion seat questions
- [x] NOTES.md: Dependencies section; encoding.json: "dependencies" key
- [x] ruling typed 06:04: "when", "upon" and "whenever" are "where" (fork F10); the "until" bars are their own yes/no functions: `s 18(b) Rule 2: the property cannot yet pass`, `s 18(c) Rule 3: the property cannot yet pass`, `s 29(4) delivery is not yet possible`, and by extension `s 16 property in unascertained goods cannot yet be transferred` and `s 19(1) the property cannot yet pass because the right of disposal is reserved`; 4 seat questions; 47 assertions
