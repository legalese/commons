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
