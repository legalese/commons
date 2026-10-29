# PROGRESS (porridge-au-aia-b, legalese-sonnet-5.5)

Disk is the memory: re-read this file, NOTES.md and the text after any compaction.

Paths (all absolute):
- RUN = the run workspace (not kept)
- INPUTS = RUN/inputs   (text: RUN/../../registers/source-bundle/C1901A00002.txt, 1880 lines; body ends line 913, endnotes 915-1880)
- DEPOSIT dir = RUN/deposit/encodings/legalese-sonnet-5.5   (D below)
- L4 = l4  (1.6.98, sha256 82ea44ad...263e)
- scratch probes: RUN/scratch-probe (NOT part of the deposit; delete at the end)
- check: cd D && L4=<L4> L4_TARGET=unstable ./check.sh ; srcrefs: cd D && python3 -I srcrefs.py check --refs C1901A00002.txt <files>  (copy the raw text beside it? srcrefs RAW is a path; pass INPUTS path)

## Facts established by probes on the stable binary (1.6.98)
- `YMD` is NOT in daydate on stable: define the shim ONCE in au-interpretation-time.l4 (`YMD y m d MEANS Date d m y`); imports are transitive; diamond imports of prelude/daydate/shim are fine.
- `Date 31 2 2025` rolls to 3 Mar 2025 (lenient). `add months`/`add years` CLAMP. Do not use them: derive s 2G from the text.
- `DATE PLUS n` ok; dates compare with AT LEAST/AT MOST/EQUALS; `is weekend (d)` needs a DATE-typed argument (overloaded with NUMBER).
- `@export` accepts DATE, LIST OF DATE, enum inputs; MAYBE DATE output ok.
- `Message:` lines `assertion satisfied` are counted once per assertion by check.sh.

## Decisions taken (with licence)
- D1 s 36(1) items 5/6: a period "from"/"after" a day does NOT include it (Example 6: 28 days after 2 Aug begins 3 Aug). Period of N days starting S = S .. S+N-1 (Example 7).
- D2 s 2G: month(s) from start day S: ends immediately before corresponding day N calendar months later; if none, at end of that month. Written from text (examples 2G(1) ex1/2, 2G(2) ex1/2 are the gold tests).
- D3 s 36(2) applies to the last day of ANY period (no unit restriction); skips consecutive Sat/Sun/holiday ("next day that is not"). Holiday (s 36(3)) = union of public holidays at the place AND all-day office closures; both are caller-supplied date lists. Saturday/Sunday computed (named in the text). `business day` (s 2B) is NOT the same notion: no office closures.
- D4 "year" and "week" are NOT defined in the text (no "week" anywhere; "year" only in calendar year/financial year = "a period of 12 months", and s 37A anniversary). Text-only answer for N weeks / N years = NOTHING (the Act is silent on their length). The 7-day / 12-month readings are provided ONLY as separately named ALTERNATIVE functions, labelled as not stated by the Act.
- D5 s 3A(2): Act silent on commencement commences on the 28th day after the day of Royal Assent = assent + 28; s 3A(3) Constitution-altering: assent day. s 3: an Act/provision expressed to commence on a particular day does so at the START of that day (legal time in the place, s 37). "passed" read as the day of Royal Assent (input is the assent date).
- D6 Day to be fixed later (fixed 2026-06-01): s 3A(1) disapplies 3A; s 3 gives start of 2026-06-01 once fixed (reading: a fixed day is a "particular day"); recorded as a fork.
- D7 Subordinate legislation silent on commencement: the text is silent (3A speaks of Royal Assent of an Act; s 46(1) reaches only instruments that are not legislative/notifiable instruments and has no assent analogue; legislative instruments are sent to the Legislation Act 2003 by the Note to s 2(1)). NOTHING.
- D8 s 29: deemed service by post = ordinary-course delivery day (INPUT), unless the contrary is proved (INPUT: proved day). s 37A: anniversary day; 29 Feb birth in a non-leap year: Act silent (NOTHING).
- D9 Enactment date: endnote 3 (line ~975-978) Assent 12 July 1901, Commencement 12 July 1901 -> carried as values with @ref.
- D10 MAYBE/NOTHING (or an explicit constructor) for "not covered"; no REFUSE, no BECAUSE, no section GIVEN (stable rejects), parenthesise NOT, one-line #ASSERT.

## Module plan (all flat in D, names au-*.l4)
1. au-interpretation-time.l4  (prelude+daydate only) YMD shim; s 2B business day/calendar month/calendar year/financial year; s 2G; s 2M sitting day; s 3, 3A; s 29 (deemed day); s 36; s 37; s 37A.  [tests: au-tests-time.l4]
2. au-part1-application.l4 (ss 1, 1A, 2, 2A)   3. au-part2-definitions.l4 (2B rest, 2C-2F, 2H-2L)
4. au-part3-commencement.l4 (s 4, s 6)          5. au-part4-repeal.l4 (7, 10, 10A, 11, 11A, 11B)
6. au-part5-interpretation.l4 (12-25D)           7. au-part6-service.l4 (28A, 29 methods)
8. au-part7-powers.l4 (33-34C)                   9. au-part9-11-citation-instruments.l4 (35, 38-40A, 46-51)
10. au-seat.l4 + au-cases-seat.l4 (layer 2).  Tests per module: au-tests-*.l4.
Support files: check.sh (present), srcrefs.py (present), NOTES.md, PROGRESS.md, encoding.json, SOURCE-LICENSE.md, BRIEF.md (copy).

## Workflow (important, survives compaction)
- L4 modules are authored as TEMPLATES in RUN/tpl/NAME.l4 with `{{Q n}}` / `{{Q n-m}}` marker lines; `python3 -I RUN/build.py NAME...` expands them into D/NAME.l4 using srcrefs.py quote (mechanical quotes). EDIT THE TEMPLATE, never D/*.l4 for modules with quotes. (Tests files have no quotes but are also built from tpl/.)
- Gate per module: `L4=<L4> L4_TARGET=unstable ./check.sh` in D; `python3 -I srcrefs.py check --strict ../../../../../registers/source-bundle/C1901A00002.txt D/*.l4` must say 0 problems (strict passes for the time module: make each run's first @ref reach exactly the quoted lo-hi lines; later @refs narrower).
- GOTCHA found: `NOT (x) OR y` parses as NOT((x) OR y): write `(NOT (x)) OR y` everywhere. Constructor patterns bind fields positionally: `WHEN \`ctor\` d THEN`. `LIST a, b` with multi-line leading commas breaks layout: name fixtures first. Daydate defines `the day before/after`, `the later of`, etc.: avoid those names.
- coverage data: RUN/cov.tsv (section<TAB>title<TAB>disposition<TAB>where/reason) is the source of NOTES.md's coverage table; update when a module lands.

## Status (update after each module)
- [x] au-interpretation-time.l4 (time rules) + au-tests-time.l4 (134 assertions).
- [x] au-part1-application, au-part2-definitions, au-part3-commencement, au-part4-repeal, au-part5-interpretation, au-part6-service, au-part7-powers, au-part8-distance, au-part9-citation, au-part10-11-instruments, each with an au-tests-*.l4.
- [x] au-seat.l4 (31 questions) and au-cases-seat.l4 (every question, worked cases W1-W9, NOTHING cases). All 31 exports ran through `l4 batch`.
- [x] NOTES.md (generated by RUN/gen/gen_notes.py from RUN/gen/cov.py; check.sh output is pasted in by the generator), SOURCE-LICENSE.md, BRIEF.md, encoding.json.
- [x] final: D holds only the 31 deposit files; RUN/scratch-probe deleted. Build machinery (RUN/tpl, RUN/build.py, RUN/gen) is outside the deposit on purpose.

## Decisions added after D1-D10
- D11 seat: ONE list of holiday/closed days per question, placed last (l4 batch cannot re-print a LIST OF input that is not last); no lambda in the seat (batch cannot re-print it).
- D12 forks F1-F17 are in NOTES.md; F9 (days between the original and the shifted last day stay in time) arose from a failing seat case whose expected value was wrong, not the program.
- D13 two first-run failures (tests-part7 1983 date; seat case 2 Feb holiday) were my hand-written expected values; both are explained in NOTES.md under "What check.sh prints".

---
# PASS 2 (completion to "whole"), agent iaw-au, started 2026-10-29

Paths (absolute):
- RUN = /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/ca81f332-162b-4c52-8cc3-57ed15b3f6fa/scratchpad/runs/iaw-au
- D (deposit dir, the only place I write) = RUN/deposit/encodings/legalese-sonnet-5.5
- TEXT = RUN/../../registers/source-bundle/C1901A00002.txt (identical to RUN/deposit/registers/source-bundle/C1901A00002.txt, cmp-verified)
- L4 = SCRATCH/bin/l4-stable-98 ; L4_MAIN = SCRATCH/bin/l4-stable-102 (SCRATCH = /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/ca81f332-162b-4c52-8cc3-57ed15b3f6fa/scratchpad)
- check: cd D && L4=$SCRATCH/bin/l4-stable-98 L4_MAIN=$SCRATCH/bin/l4-stable-102 ./check.sh
- pass-1 template machinery (tpl, build.py) is gone: edit D/*.l4 directly; quotes via srcrefs.py

## baseline (before any change; check.sh target main, main build 1.6.102 (main, e4f2553, 2026-10-26))
- 24 modules, errors 0, satisfied 560, failed 0, refused 0; main columns identical (every module "same"); exit 0
- per module satisfied: au-cases-seat 124, au-tests-part1 8, part10-11 27, part2 62, part3 17, part4 30, part5 41, part6 15, part7 60, part8 5, part9 37, au-tests-time 134; layer-1 modules and au-seat 0 (no asserts in them)
- srcrefs (pass 1, as recorded in encoding.json): 425 src: lines, 80 runs, 108 locators, 0 problems
- l4 binary: 1.6.98 (main, 7689b0d, 2026-10-19) sha256 82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e

## Pass-2 facts established (probes on stable 1.6.98)
- units.py (in D) counts the units from the text: body 720 (11 Parts, 83 sections, 157 subsections, 267 paragraphs, 42 subparagraphs, 17 table rows, 95 defined terms = 77 in s 2B + 18 elsewhere, 31 Notes, 17 Examples) + apparatus 324 (front matter 23, 4 endnotes, 41 abbreviation-key entries, 79 endnote-3 rows, 177 endnote-4 entries) = 1044. Re-run: python3 -I units.py ../../registers/source-bundle/C1901A00002.txt
- The text has NBSP (U+00A0) in some lines (e.g. "subsection (6)"): use \s in patterns.
- Stable has: string LESS THAN (lexicographic), TOLOWER, TOUPPER, REPLACE s old new, SPLIT, TRIM, STRINGLENGTH, CHARAT, SUBSTRING, CONTAINS, INDEXOF, CONCAT, elem, count.
- probe/ (throwaway files) is inside D and MUST be deleted at the end.

## Pass-2 plan (module names; tests au-tests-<name>.l4)
- coverage.tsv (one row per unit; id, kind, first, last, disposition, reason, where, note) is the source of the NOTES.md coverage table (covtable.py renders).
- NEW layer-1 modules: au-part2-terms (s 2B 77 terms + 18 other defined terms: table of meanings), au-part2-more (2C(2), 2CA(2), 2F(2),(3),(7), 2K(2), 2L, 2M(3)), au-part3-more (4(3),(6)), au-part4-more (11A), au-part5-readings (12, 15A, 15AA, 15AB(2),(3), 15AC, 15AD, 15B(3),(3A),(4)(b), 16-18A, 18B(4)-(6), 20, 21, 23), au-part5-ministers (19-19E), au-part6-more (29(2)), au-part7-more (33*, 33A rest, 33AA, 33B, 34, 34AAA, 34AAB, 34AA, 34AB, 34B(1A),(2), 34C(5),(6)(b)), au-part8-more (37), au-part9-more (40A(4),(6)).
- Seat layer (au-seat, au-cases-seat): untouched unless a question is plainly owed.
- Order: audit (NOTES.md ## Re-disposition audit) BEFORE any new L4; then terms -> Part 5 -> 19-19E -> Part 7 -> residue; run check.sh after each module.

## Pass-2 status (update after each module)
- [x] NOTES.md: "## Re-disposition audit" and "## Coverage table" are GENERATED blocks between <!-- BEGIN audit/coverage --> markers: edit coverage.tsv (the seed was probe/seed.py; its dispositions are now authoritative in the TSV, hand-edit the TSV or re-run covtable.py) then `python3 -I covtable.py coverage.tsv NOTES.md`. NOTE: probe/seed.py regenerates the TSV from scratch (do not re-run it once rows are edited by hand).
- [x] au-part2-terms.l4 (generated by probe/gen_terms.py from probe/terms_data.py; 77 + 18 terms) + au-tests-part2-terms.l4 (257 asserts, from probe/gen_terms_tests.py). strict srcrefs 0 problems.
- [x] au-part5-readings.l4 (ss 12, 15A, 15AA, 15AB(2),(3), 15AC, 15AD, 15B(3),(3A),(4)(b), 16, 16A, 16B, 16BA, 16C, 17A, 18A, 18B(4)-(6), 20, 21, 23) + au-tests-part5-readings.l4 (122 asserts).
- [x] au-part5-ministers.l4 (19-19E), au-part2-more, au-part3-more, au-part4-more, au-part6-more, au-part7-more, au-part8-more, au-part9-more, each with its au-tests-<name>.l4 (done; see Final status).
- Mixfix lesson: a mixfix name may not END in a keyword segment (`what X says` t `means` fails: use a prefix name); GIVEN order must equal the order the args appear in the mixfix name.
- New forks so far: F18 (16C(2) date of commencement of s 16C not in text; endnotes give two dates for Act 79 of 1973: 19 June 1973 / s 4(2) 1 July 1973), F19 (33(2A) date not derivable), F20 (15AA tie), F21 (19 item 3(c) cumulative with (a)/(b)).

## Final status (pass 2)
- All modules and tests written; probe/ deleted. check.sh (target main, l4 1.6.98 and main build 1.6.102), after the review fixes below: 44 modules, errors 0, satisfied 1486 (1321 before them), failed 0, refused 0, every module "same" on main, exit 0. Baseline was 24 modules, 560 satisfied; every baseline number still holds (the 24 baseline modules are unchanged) and 20 modules and 926 assertions were added.
- srcrefs --refs and --strict over every au-*.l4: 913 src: lines, 280 runs, 314 locators, 0 problems (baseline 425 / 80 / 108 / 0). l4 check over every file: "Check succeeded." with no other output.
- coverage.tsv: 1044 units, 629 encoded, 42 fork, 299 inert (all reason 1), 74 repealed or blank in this text. Forks added in pass 2: F18 to F23.
- Existing modules and tests: none edited by me at the end of the first report (all still carried the staging time). Since then one comment was added to au-interpretation-time.l4 (review fix, below), and nine files were rewritten at 16:41:05 by someone else (see below).
- s 11A test: one expected value was my error, re-derived from the text ("Chairs" has the letters chairs, so it goes at position 3, after chairperson and before chairwoman, not position 1), and one comment mislabelled an equal-letters case; no assertion was changed to match program output.
- Mutation controls on au-tests-part7-more.l4 (a day boundary, the 3AA amend case, the 33(4) proviso scope, the 33B(5) place count): each mutation made at least one assertion fail, so the tests do check what they say.

## Review fixes (2026-10-29, after the test author's report)
- au-part2-terms.l4: the member lists of 15 terms are split into their items (the Act's printed phrase kept, each item added, article/singular and shared-head forms added; 215 members now, 150 printed and 65 derived). Found by a script sweep over every `members it names` / `members it leaves out` string, not by memory; each entry decided from the text. Left whole with reasons: AAO limb (b)(ii), record, coastal sea (a)(ii)/(b)(ii), holiday (a)/(b). Listed in NOTES.md, "Which printed lists are split into members".
- au-tests-part2-terms.l4: 165 assertions appended (257 -> 422): the printed phrase, each item, the article form, one unlisted thing still not named. Against the pre-fix module 147 of the 165 fail (the other 18 are the unlisted-thing controls, which pass either way).
- au-interpretation-time.l4: comment only, citing fork F9 at `the thing is done within the time allowed`. The days-between question the test author raised IS F9 (pass 1), so no new fork number was issued; F9's row now says where to change it.
- NOTES.md: new subsection "Reading a result: FALSE and NOTHING" (under Scope) and "Which printed lists are split into members" (under the findings); two headings added, none lost; coverage block still 1,064 table rows.
- coverage.tsv: the where cells of the 15 extended terms and the 2 checked-and-left terms updated; counts unchanged (629 / 42 / 299 / 74).
- Not mine: at 16:41:05 nine files (au-cases-seat, au-part1-application, au-part7-powers, au-tests-part1, au-tests-part3, au-tests-time, au-tests-part7, au-tests-part7-more, au-part5-ministers) were rewritten; eight changed size. No before-copy exists here, so what changed is unknown to me; assertion counts are unchanged and check.sh passes. Recorded in NOTES.md under "Changes to existing modules" with a request for the editor to list each change.


Note added 2026-10-29, after the run: the date shim described above no longer exists. Every module writes dates as `Date day month year`, and this encoding defines no `YMD` or `YearMonthDay`.
