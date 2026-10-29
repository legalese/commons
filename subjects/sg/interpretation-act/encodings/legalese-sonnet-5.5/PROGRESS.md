# PROGRESS (iaw-sg, Interpretation Act 1965 Singapore, whole + seat layer)

Re-read this, NOTES.md and the text (../../registers/source-bundle/IA1965.txt) after any compaction, not a summary.

## Paths
- INPUTS = /Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/ca81f332-162b-4c52-8cc3-57ed15b3f6fa/scratchpad/runs/iaw-sg/inputs
- RAW text = $INPUTS/IA1965.txt (3046 lines). Operative text = lines 149-2208 (long title to s 55). Lines 1-148: cover + arrangement of sections (inert, reason 1). Lines 2210-3046: legislative history, "not part of the Act" (inert, reason 1).
- DEPOSIT dir = .../runs/iaw-sg/deposit/encodings/legalese-sonnet-5.5 (flat; all .l4 are sgia-*.l4)
- L4_BIN = .../scratchpad/bin/l4-stable-98 (1.6.98), L4_MAIN = .../scratchpad/bin/l4-stable-102
- Experiments only in .../runs/iaw-sg/exp (scratch, not deliverable)

## Stable-binary facts measured (1.6.98)
- `YMD` absent: local shim `YMD y m d MEANS Date d m y` (needs GIVETH A DATE).
- `Day date` = day count (2026-01-04 -> 739984, a Sunday; (Day d) MODULO 7 == 0 iff Sunday, with epoch 2026-01-04). Independent: `date -j` says 2026-01-04 and 2025-12-28 are Sundays.
- daydate `add months` / `add years` CLAMP (2024-01-31 +1m = 2024-02-29; 2025-12-31 +2m = 2026-02-28; 2024-02-29 +1y = 2025-02-28). The Act does NOT say this: finding only.
- Date PLUS n works (2026-01-01 + 30 = 2026-01-31).

## Design decisions (with licensing section)
- s 50(a): "from" an event: day of event excluded, N days -> last day = start + N (inclusive). "after" is not named in s 50(a): NotCovered (fork F2).
- s 50(b): excluded days = Sunday or public holiday (exactly those two). Chosen reading: (b) applies to the last day of ANY period (text says "the last day of the period", chapeau says "in computing time"); alt reading R-days-only is also encoded as a function so both outcomes are tested (fork F4).
- Months / years / weeks: text defines "month" = calendar month, "year" = Gregorian year; NO counting convention; "week" and "day" undefined. Unadjusted last day of an N-month/N-year period = NotCovered. Person may supply the last day they worked out; s 50(b) then applies. daydate clamping recorded as finding only.
- s 50(c): act directed on an excluded day is in due time if done next non-excluded day; other act days -> NotCovered.
- s 50(d): period "not exceeding 6 days": excluded days not reckoned.
- Office closed days: not an excluded day (s 50 names exactly Sunday and public holiday).
- s 10: comes into operation "on the expiration of the previous day" = first instant of the specified day, standard time (s 51: +8h on UTC unless President notifies). Act silent on default if no day specified: NotCovered.
- s 2(5): post service deemed effected on proper addressing+prepaying+posting; time = when letter would be delivered in ordinary course of post (INPUT, not in Act); rebuttable.

## Files plan (flat folder, ASCII)
layer 1: sgia-nouns.l4 (if needed), sgia-interpretation-time.l4 (imports ONLY prelude, daydate), sgia-p1-definitions.l4 (+generated term table), sgia-p1-other.l4 (2(2)-(5), 2A), sgia-p2-written-law.l4 (3-18 except time), sgia-p3-subsidiary.l4 (19-26A), sgia-p4-powers.l4 (27-37), sgia-p5-penal-court.l4 (38-41E), sgia-p6-misc.l4 (42-55 except 50,51,52,53 which live in time module)
layer 2: sgia-seat.l4, sgia-cases-seat.l4
tests: sgia-tests-*.l4
other: check.sh (+ extras), srcrefs.py, NOTES.md, PROGRESS.md, encoding.json, SOURCE-LICENSE.md, BRIEF.md

## Policies decided (advisor review 1)
- "unless the contrary intention appears"/"unless the context otherwise requires": public rule takes plain Bool input `a contrary intention appears` (or `the context otherwise requires`), answers NOTHING when TRUE. Applied to s 50, 53, 2(2), 2(2A), 2(3)(b). Apply to EVERY later section carrying the phrase.
- F4 pinned: time-module public fns use `every period`; alt reading fn `...if it reaches periods of days only`. Seat calls the pinned one.
- List-of-DATE input on @export passes `l4 check`; NOTES must say Interact form needs to accept a list of dates.
- Deleted subsections (2(4), 2(6)) are stub constants quoted with @ref; machinery (2A(7), s 1, etc.) = inert reason 2, NO stub.
- Test expected values hand-written (calendar facts from `date -j`); definitions tests generated from gen-defs.py DATA, tied to text by `gen-defs.py --verify`.

## Conventions in modules
- every module: `--@Q label @ N M` macro above each rule, expanded with qx.py (run ONCE per new macro); locators must end on non-blank text lines (use --@R with exact text-line ends).
- Rules under "unless contrary intention" return MAYBE BOOLEAN; JUST x = Act's answer; NOTHING = Act does not say / default displaced.
- Fork candidates noticed so far (to put in NOTES fork register): F1 from counts?; F2 "after"; F3 last day inside; F4 reach of 50(b); F5 office-closure day not excluded; F6 s 23(2) "or" read as both limbs; F7 s 2A(4) "2 medical practitioners" AT LEAST 2; F8 s 2A(2) "subject to (5)" standards still apply; F9 s 2(3)(e) "the Chief Justice" bare; F10 s 14 after substitution in force -> Act silent; F11 s 36 etc "not exceeding 6 days" (d) uses stated N; F12 2(5) vs 48A both on post; F13 s 32A(1) majority = more than half of ALL persons; F14 2(4)/(6) deleted rows; F15 s 10: neither limb -> NOTHING; F16 s 20(a)(i) "or both".

## Tooling written
- qx.py RAW FILE : expands `--@Q label @ N M [N2 M2]` macros (quote lines from RAW + `@ref label (src:a-b)`) and `--@R label @ N M` in place. Run once per new macro; srcrefs.py check --refs must say 0 problems.
- exp/q.sh FILE : quiet runner (stable-98): prints satisfied/failed/other errors. check.sh needs L4=... L4_MAIN=... env (see brief).

## State
- [x] read brief, guide, commons notes, both SKILL.md, dialects.md, source-locators, canon-deposit, example seat
- [x] read whole source text
- [x] sgia-interpretation-time.l4 DONE (typechecks, srcrefs 0 problems) + sgia-tests-time.l4 (103 satisfied, 0 failed; check.sh same on main 102)
- [x] gen-coverage.py + coverage-dispositions.py WRITTEN (reads gen-units.py tiling, @ref locators, #ASSERT lines; run: python3 -I gen-coverage.py ../../registers/source-bundle/IA1965.txt . [--write NOTES.md]; NOTES.md needs the markers <!-- COVERAGE-TABLE:BEGIN --> / END). 496 rows, audit gaps 0, dups 0. FORKS table inside coverage-dispositions.py maps unit labels to F-ids.
- [x] sgia-p1-definitions.l4 + sgia-tests-definitions.l4 GENERATED by gen-defs.py (92 entries; 297 asserts) ; sgia-p1-other.l4 + sgia-tests-p1-other.l4 (2(1) chapeau, reading rules, 2(2), 2(2A), 2(3) table, 2A; 107 asserts). YMD shim lives ONLY in sgia-interpretation-time.l4 (diamond import verified OK).
- [x] sgia-p2-written-law.l4 (+tests-p2 119 asserts), sgia-p3-subsidiary.l4 (+tests-p3 61), sgia-p4-powers.l4 (+tests-p4 128) DONE, srcrefs 0 problems
- [x] sgia-p5-penal-court.l4 (+tests-p5 102) and sgia-p6-misc.l4 (+tests-p6 80) DONE. LAYER 1 COMPLETE (all modules typecheck; srcrefs 0 problems). Fork added: F18 s 41D/41E (41E displaces 41D(1) only for matters it lists).
- [x] seat layer sgia-seat.l4 (30 @export questions, all params @desc) + sgia-cases-seat.l4 (147 asserts, 0 failed) DONE. Tests-time now 122 asserts (helpers, non-monotonic 6 vs 7 days, daydate clamp as library behaviour).
- [x] NOTES.md (all sections, coverage table generated), encoding.json, SOURCE-LICENSE.md WRITTEN
- [x] final: check.sh 18 modules 0 errors 1165 satisfied 0 failed same on main 102; srcrefs 288 locators 0 problems; gen-defs --verify 92 entries 0 problems; coverage 496 rows gaps 0 dups 0; q.sh over all 18 files: no Error/Warning; advisor consulted (items done)

## Forks (ids used in code comments and coverage-dispositions.py)
F1 s50(a) day of event, F2 'after', F3 last day inside, F4 reach of 50(b), F5 office-closure day not excluded, F6 s23(2) 'or', F7 s2A 'two medical practitioners' = at least 2, F8 s2A(2)/(3) 'subject to' = standards still apply, F9 s2(3)(e) construed-as words as stated, F10 s14 silent after substitution, F11 s50(d) 'not exceeding 6 days' = stated number, F12 s2(5) vs s48A post, F13 s32A(1) majority of all persons, F14 s2(1) feminine gender silent, F15 s10 other ways of fixing the day -> NOTHING, F16 s20(a)(i) 'or both', F17 s45(1)(a)/(b) estimate stands in for fee, F18 s41D/41E.

## Next
- NOTES.md (write now), encoding.json, SOURCE-LICENSE.md, final check.sh over ALL files, srcrefs on all, advisor, tidy scratchpad.

## ROUND 2 (fix list from team-lead, after the independent test pass; snapshot of round-1 files in runs/iaw-sg/exp/orig)
Items: 1 s48(6),(7) loser = JUST FALSE (+seat question); 2 s2(3)(l) pairing; 3 s2(1) list members (gen-defs EXTEND table); 4 forks to register (F19+); 5 Known limits; 6 srcrefs --strict at time module line 255.
Rules: keep round-1 files byte-identical unless listed in NOTES `## Changes to existing modules`; edit NOTES.md by heading anchors; coverage rows must stay 496; check.sh 'same' on main; target stable.

### Round 2 state
- [x] 1 s 48(6),(7): loser JUST FALSE in sgia-p6-misc.l4; tests-p6 101; seat question 31; cases-seat 161
- [x] 2 s 2(3)(l) respectively: `Paired replacement`, `each construed as`, `the words section 2(3) prints for` in sgia-p1-other.l4; tests-p1-other 116
- [x] 3 list members: gen-defs.py EXTEND (21 entries) / UNLISTED / LEFT (21 printed items) + sweep; tests-definitions 440 (+143)
- [x] 4 forks F19 to F26 in NOTES.md; F4, F6, F10, F13 cross-referenced; FORKS in coverage-dispositions.py (15 rows encoded -> fork; 496 rows unchanged); two F23 asserts added to tests-p4 (130)
- [x] 5 `## Known limits` and `## List members in the s 2(1) table` and `## Changes to existing modules` in NOTES.md
- [x] 6 srcrefs --strict 0 problems (time module quote re-cut)
- [x] final: check.sh 18 modules, 0 errors, 1352 satisfied, 0 failed, 0 refused, same on main 102; srcrefs --refs and --strict 289 locators 0 problems; gen-defs --verify 0 problems; coverage 496 rows gaps 0 dups 0 (encoded 351, fork 53, inert 89, repealed or blank 3)
- ids F19 s36 delegates, F20 s46(2) parenthesis, F21 s41A(6)(e), F22 s32 vs s30(3), F23 s32A(1) vs (2)(b), F24 s2(1) written law qualifier, F25 s9A(3) includes, F26 s20(c)/26A/29/37 provisos


Note added 2026-10-29, after the run: the date shim described above no longer exists. Every module writes dates as `Date day month year`, and this encoding defines no `YMD` or `YearMonthDay`.
