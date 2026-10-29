# PROGRESS (iaw-nz, Legislation Act 2019 (NZ), encoding `legalese-sonnet-5.5`)

Read this and NOTES.md and the text again after any compaction; do not trust a summary.

Paths (absolute):
- DEPOSIT = /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/ca81f332-162b-4c52-8cc3-57ed15b3f6fa/scratchpad/runs/iaw-nz/deposit
- ENC = DEPOSIT/encodings/legalese-sonnet-5.5   (all deliverables here, `.l4` files flat)
- RAW = /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/ca81f332-162b-4c52-8cc3-57ed15b3f6fa/scratchpad/runs/iaw-nz/../../registers/source-bundle/act_public_2019_58.txt (1430 lines, 1430 non-blank)
- L4 = .../scratchpad/bin/l4-stable-98 ; L4_MAIN = .../scratchpad/bin/l4-stable-102
- Probe dir DEPOSIT/_probe : DELETE BEFORE FINISHING.

## Facts about the deposited text (measured)
- Converter dropped subsection numbers and paragraph labels; tables are flattened. Row key = raw line range.
- s 54 (lines 380-389): the table's rule cells are GONE; only the lead-in (381) and the Examples Items 1-7 (383-389) survive. Do not reconstruct the rules from memory.
- Blank/headings only: Part 4 (ss 101-112, lines 762-773), s 148 (1029), Sch 1 cll 30-31 (1262-1263), Sch 1A (1288), Sch 4 (1428-1430), Sch 3 tables (1327-1427, only "Exemption applies" cells and some grounds survive).
- Year, week, day are NOT defined anywhere; `month` = calendar month (s 13); `working day` (s 13); `sitting day` (s 5(1)).
- U+FEFF appears inside cross-references; srcrefs.py handles it (probe passed).
- Stable 98 and 102 both lack `YMD`; shim `YearMonthDay y m d MEANS Date d m y` (first written as `YMD`, renamed so that it cannot collide with the library's `YMD`) compares fine with AT LEAST / EQUALS / PLUS on both.
- daydate: `add months` clamps; `Date 31 6 2025` rolls to 1 July 2025; `Day (Date 5 1 2026)` = 739985 and is a Monday (checked with macOS date). Weekday index = (Day d MINUS 739985) MODULO 7, 0 = Monday (MODULO is floored: (0 MINUS 3) MODULO 7 = 4).

## Plan: modules (layer 1) -- placement of each section is in the coverage table
- nz-nouns.l4 (shared nouns only)
- nz-interpretation-time.l4 (imports ONLY prelude, daydate): YearMonthDay shim, working day s13, ss 17, 25-28, 39, 54-58, answers for day/week/month/year
- nz-part1-preliminary.l4 (ss 5-7), nz-part2-principles.l4 (8-12), nz-part2-definitions.l4 (13-23), nz-part2-commencement-repeal.l4 (24, 29-38), nz-part2-powers.l4 (40-53), nz-part2-revision-incorporation.l4 (59-66)
- nz-part3-publication.l4 (67-83A), nz-part3-editorial-revision.l4 (84-100), nz-part5-oversight.l4 (113-127), nz-part6-7-pco-regulations.l4 (128-147A), nz-schedules.l4
- tests: nz-tests-*.l4 beside each module; seat: nz-seat.l4, nz-cases-seat.l4

## Decisions taken (with the licensing line)
- D1 "from"/"after" a day: period starts the NEXT day (s 54 Item 2 at 384; s 56 example 3 at 400 equates "after" with item 2).
- D2 "within N days of" an event: anchor day excluded, last day = anchor + N, ends at the close of that day (Item 3, 385).
- D3 "starting on" a day counts it (s 56 examples at 398-399); Items 1, 4, 5: begins-on / ends-on / until include the named day; Item 6 "before the start of D": last day = D - 1; Item 7: neither end day counted.
- D4 months: s 56 (393-396); commencement by months s 28 (224-228) differs (in force ON the corresponding/last day).
- D5 years, weeks, days: undefined => NOTHING / explicit not-covered value, asserted. 12N-months reading recorded in the fork register as NOT chosen.
- D6 s 55 (391) says "within a limited period of time": applies to periods of any unit, so also months. Permissive ("may ... be done on the next working day").
- D7 named holidays (Waitangi, Good Friday, Easter Monday, Anzac, Sovereign's birthday, Matariki, Labour Day) are NOT dated in the Act: inputs.

## Order of work
1. [ ] PROGRESS/NOTES skeleton (this file)  2. [ ] coverage.py + coverage-spec  3. [ ] nouns  4. [ ] time module + tests + seven worked cases
5. [ ] rest of Part 2  6. [ ] seat layer + cases  7. [ ] Parts 3-7 + schedules  8. [ ] Hohfeld table, forks, findings, NOTES  9. [ ] check.sh run, srcrefs check, encoding.json, SOURCE-LICENSE.md  10. [ ] delete _probe

## Status log (update as each unit lands)
- LANDED (compiles, 0 errors): src/nz-interpretation-time.l4t -> nz-interpretation-time.l4 ; src/nz-tests-time.l4t -> nz-tests-time.l4 (144 assertions satisfied, 0 failed on stable 98; negative control: 27 mutated expectations all failed)
- TOOLS: expand.py (src/*.l4t -> *.l4 with `--@Q a-b` markers expanded to quote lines; EDIT THE .l4t, never the .l4), coverage.py (700 rows, all 1430 non-blank lines covered once; fill coverage-spec.tsv: keys s56 | s56#2 | s5:def:term | s5:ex:78 | s54:tbl:383 | h:LINE | h | x:LINE|sNNN for heading-only), run helper DEPOSIT/_probe/r.sh FILE [98|102] (delete _probe at the end)
- LANDED 2026-10-29 (all compile 0 errors, tests all satisfied on 98; not yet run on 102): nz-nouns, nz-part1-preliminary (20 asserts), nz-part2-principles (38), nz-part2-definitions (97), nz-part2-commencement-repeal (84; F8 same-day re-exercise, F9 same-day offence), nz-part2-powers (87; ss 40-53), nz-part2-revision-incorporation (51; ss 59-66). Each has src/<name>.l4t + src/nz-tests-<x>.l4t. srcrefs check: 0 problems at that point.
- Convention learned: GIVEN order must equal mixfix head arg order; `--@Q N-M` markers put quote lines directly before the `@ref`; never leave an @ref src:N without a quote line covering N.
- LANDED (later same day): nz-part3-publication (150 asserts, ss 67-83), nz-part3-editorial-revision (121, ss 85-99), nz-part5-oversight (93, ss 114-127; sitting days are a supplied LIST OF DATE). s 83A, s 100, ss 84/92/93 left for inert (1 or 2). srcrefs 0 problems after these.
- LANDED (3rd batch): nz-part6-7-pco-regulations (44 asserts; ss 131,133,134,146,147,147A encoded; rest inert 2), nz-schedules (222 asserts; Sch 1 cll 2-10,13-18,19(5)(6),20-22,23,24,25-29,32,33,33A,34,27B; Sch 2 cll 1-6; Sch 3 opening rule + grounds). srcrefs 0 problems before schedules; recheck.
- STILL TO WRITE (in order; modules above are all done; remaining = glossary, seat, cases, coverage-spec, NOTES, encoding.json, SOURCE-LICENSE.md, check.sh, srcrefs, delete _probe): nz-part3-publication (ss 69-83A), nz-part3-editorial-revision (ss 84-100), nz-part5-oversight (ss 114-127), nz-part6-7-pco-regulations (ss 131,133,146,147,147A), nz-schedules (Sch 1 cll 3-10,13,15-16,18,20,22,25-29,32,33,33A,34,27B; Sch 2; Sch 3 intro), nz-glossary (gen_glossary.py), nz-seat, nz-cases-seat, coverage-spec.tsv (700 rows), NOTES.md, encoding.json, SOURCE-LICENSE.md, check.sh run, delete DEPOSIT/_probe
- (superseded) NEXT: nz-nouns, nz-part1-preliminary, nz-part2-principles, nz-part2-definitions, nz-part2-commencement-repeal, nz-part2-powers, nz-part2-revision-incorporation (each + nz-tests-*), glossary (gen_glossary.py -> nz-glossary.l4 + independent tests), Parts 3,5,6-7, schedules, seat, cases, NOTES, encoding.json, SOURCE-LICENSE.md
- Spec for coverage-spec.tsv is NOT started: fill it after each module (disposition E/I1/I2/I3/F/B + target).

## Files written
- BRIEF.md, check.sh, srcrefs.py, fetch-main-l4.sh (copied from the skill), PROGRESS.md

## LANDED (seat layer, 2026-10-29, after the 2nd compaction)
- gen_seat.py generates src/nz-seat.l4t and src/nz-cases-seat.l4t (EDIT gen_seat.py, then `python3 -I gen_seat.py && python3 -I expand.py`). 43 questions, 131 cases, all satisfied on stable 98, 0 errors. Not yet run on 102.
- Seat questions dropped as official-only (layer 1 only): Sch 1 cl 15 lodging (the maker lodges), s 131 privilege (a PCO client instructing). Questions about secondary legislation are phrased for a person who RELIES ON it ("the secondary legislation I rely on"), not the maker.
- Two expectations of mine were wrong first time and corrected from the text (s 54 Item 7 gives 18 Feb 2026, not 17 Feb; word cases use the constructors `a day` ... `a sitting day`). Finding for NOTES: the typed-by-hand expectation caught my own arithmetic slip; the encoding was right.
- STILL TO DO: (1) Schedule 3 grounds --@Q markers in src/nz-schedules.l4t (6 srcrefs problems); (2) coverage-spec.tsv (700 rows); (3) NOTES.md; (4) encoding.json, SOURCE-LICENSE.md; (5) check.sh on 98 and 102; (6) negative-control mutations on newer tests; (7) delete DEPOSIT/_probe and gen scratch; (8) final report.

## FIRST-PASS FINAL STATE (2026-10-29; superseded by the second-pass state at the end of this file)
- DONE: all layer-1 modules and tests, the glossary (85 entries), the seat (43 questions, 131 cases), coverage-spec.tsv (702 rows, 502 encoded, 14 fork, 88 inert 1, 80 inert 2, 18 blank), NOTES.md (generated by gen_notes.py from src/NOTES.tail.md and the tree), encoding.json, SOURCE-LICENSE.md.
- check.sh (98 with 102 as main): 29 modules, 0 errors, 1720 assertions satisfied, 0 failed, 0 refused, every module `same` on 102. srcrefs: 0 problems. Warning scan on both builds: none. Negative control: 639 mutated expectations in 14 test files each failed once.
- Rules added late (after the first full pass) because the brief does not let "addresses an official" or "refers to another Act" stand as inert reasons: ss 5(3), 6, 17(5), 71(2), 72(1)(b), 73(1)-(2), 80(1), 82(1),(3), 83A, 86(3), 95(1), 96(1), 100, 116(1), 119(1), 120(2), 125(1)(b)-(c), 133(1),(5), s 13 writing (Part 4 CCLA as an input); Schedule 1 cll 3(2), 13(4), 14(3), 21(1), 27A, 32(3); Schedule 2 cl 4(3); Schedule 3 cl 2. Glossary: Inland Revenue Bills, responsible Minister, Consumers Price Index, union, list deadline, and the "unless the context otherwise requires" lead-in.
- Seat questions dropped as official-only (kept in layer 1): Schedule 1 cl 15 lodging, s 131 privilege of a PCO client.
- Cleanup: DEPOSIT/_probe and __pycache__ deleted at the end. Nothing was copied into the scratchpad root.

## SECOND-PASS FINAL STATE (2026-10-29, after the independent test pass)
- Version 0.2.0. check.sh (stable 98, main build 102): 29 modules, 0 errors, 2217 assertions satisfied, 0 failed, 0 refused, every module `same` on the main build; no warning-severity diagnostic on either build.
- srcrefs: `check --refs` 0 problems and `check --strict` 0 problems (551 locators). coverage.py: 703 rows (503 encoded, 14 fork, 88 inert 1, 80 inert 2, 18 blank), 1430 of 1430 lines covered once. sweep_lists.py: 0 problems (108 multi-thing constructors: 75 split, 33 whole; 32 definitions: 27 look-ups, 5 whole). expand.py reproduces every `.l4` byte for byte.
- Glossary: 86 entries (publication deadline now its own); seat: 46 questions, 148 cases; forks F1 to F23.
- Negative control (mutate_tests.py, one run): 2,206 of 2,217 mutated, 2,201 failed exactly once, 0 missed, 5 ill-typed (an expected NOTHING whose type no replacement fits), 11 not mutated; the 548 assertions added or changed since the first pass: 548 of 548 detected.
- NOTES.md has 17 headings (14 before; added: Known limits, Lists, Changes to existing modules). It is generated: `python3 -I gen_notes.py <saved check.sh output> <mutation summary text>` after the generators; edit src/NOTES.tail.md or gen_notes.py, never NOTES.md.
- Judgment calls left to the lead, in NOTES: polarity of s 40(2), s 52 and s 146 (protection: NOTHING taken); s 46, ss 48 to 50 and s 53 (extensions of a power with its own terms: NOTHING taken).
- Dates are written `YearMonthDay`; `YMD` is not used anywhere in the code. The shim stays until the lead converts it to the library's `YMD`. The paths in this file's first lines and in BRIEF.md and encoding.json (`l4_bin`, `l4_main`) are from the first pass; nothing added in the second pass names an absolute path.
- Cleanup: DEPOSIT/_probe, scratch mutation copies and __pycache__ deleted at the end.


Note added 2026-10-29, after the run: the date shim described above no longer exists. Every module writes dates as `Date day month year`, and this encoding defines no `YMD` or `YearMonthDay`.
