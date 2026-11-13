# PROGRESS (coa24: ss 1092C-1133, lines 15485-16189)

Re-read this file, NOTES.md and the text after any compaction, not a summary.

## Paths

- DEPOSIT folder: <scratchpad>/runs/dst-coa24/deposit/encodings/legalese-sonnet-5.5/
- scratch: .../runs/dst-coa24/work/
- text: .../runs/dst-coa24/inputs/ukpga-2006-46.txt
- L4 = <scratchpad>/bin/l4-main-110 ; L4_MAIN = <scratchpad>/bin/l4-main-109
- check: `L4=<L4> L4_MAIN=<L4_MAIN> ./check.sh`
- srcrefs: `python3 -I srcrefs.py check --refs <text> <files>` and `--strict`

## Module plan (layer 1), dependency order

1. coa24-officers.l4      ss 1121, 1122, 1123
2. coa24-penalty.l4       ss 1125, 1131 (+ penalty tables used by other sections)
3. coa24-identity.l4      ss 1110A-1110D
4. coa24-register.l4      ss 1092C-1098 (self-incrimination, notices, removal, court orders, public notice)
5. coa24-acsp.l4          ss 1098A-1098H
6. coa24-index.l4         ss 1099-1101
7. coa24-language.l4      ss 1102-1110
8. coa24-disclosure.l4    ss 1110E-1110G
9. coa24-delivery.l4      ss 1111, 1113-1120
10. coa24-false-statements.l4  ss 1112-1112B
11. coa24-prosecution.l4  ss 1124, 1126-1130, 1132, 1132A, 1133
Tests: coa24-tests-<module>.l4. Seat: coa24-seat.l4, coa24-cases-seat.l4.

## Status

(updated as work proceeds)

- [ ] read text, PLAN, guides, skills: DONE (context 1)
- [ ] modules written: none yet

## Status (updated context 1, after 6 of 11 modules)

Tools in work/: coverage.py (+ dispositions.py, hand-written map), build.py (expands @@Q N M@@ quote markers from work/tpl/*.l4 into this folder; EDIT THE TEMPLATES in work/tpl, never the built files), chk.sh NAME... (build + srcrefs --strict + l4 run counts), traces.sh FILE (trace outputs on both builds).

DONE (module + tests, srcrefs --strict 0 problems, all assertions satisfied, main-109 same):
- coa24-officers (ss 1121-1123): 50 asserts
- coa24-penalty (ss 1125, 1131): 33
- coa24-identity (ss 1110A-1110D): 63
- coa24-register (ss 1092C-1098): 141 (+3 #TRACE of s 1093(3): day 13 FULFILLED, day 14 BREACH, never BREACH; same on main-109)
- coa24-acsp (ss 1098A-1098H): 119 (+3 #TRACE of s 1098E(1))
TODO: coa24-index (1099-1101), coa24-language (1102-1110), coa24-disclosure (1110E-1110G), coa24-delivery (1111, 1113-1120), coa24-false-statements (1112-1112B), coa24-prosecution (1124, 1126-1130, 1132, 1132A, 1133); then seat + cases; NOTES.md (coverage via coverage.py, forks, jural, marginal, FALSE/NOTHING section, seams, findings, binary), NEEDS-CORE.md, final check.sh, srcrefs --refs/--strict on ALL files, FALSE/NOTHING comment quote check.

## Decisions taken (with the licensing section)
- NOT precedence: tests caught `a AND NOT b AND NOT c` in s 1098A (reads NOT (b AND NOT c)); every NOT in a conjunction is now parenthesised. Finding for NOTES.
- "if" grants/duties: failed "if" => JUST FALSE (brief rule a), EXCEPT where another provision of the sources shows other routes (s 1098F(1) vs (2)) => NOTHING.
- "must" not done => JUST FALSE in a function named "meets the requirement of s N" (fork lines).
- "unless"/"only if"/"except" once MET => NOTHING (the bar lifts; the grant is elsewhere): ss 1122(1), 1094(3), 1096(3), 1097(5), 1126.
- s 1093(1)(b) / 1098E(1): "14 days beginning with" => last day = day + 13; WITHIN 13 in traces.
- s 1093(4): two versions of the daily default fine run together in the text: both encoded + third constructor "does not say which" => NOTHING (fork F1).
- General limit in a magistrates' court is an INPUT (MAYBE Period); s 1131(2) substitutes 6 months for offences before 2 May 2022.
- Level amounts are INPUTS (record `s 1125 amounts the Act leaves to other instruments`).
- Diamond import of coa-definitions measured OK on main-110 (no multiple definitions). acsp imports it for s 1173(1) firm.
- Traces cannot be #ASSERTed (DEONTIC not comparable): decision functions carry the same duties.

## Status update (context 1, all 11 layer-1 modules written and tested)
DONE (module + tests, srcrefs strict clean, all asserts satisfied): officers 50, penalty 33, identity 63, register 146, acsp 119, index 23, language 88, disclosure 35, delivery 76, false-statements 47, prosecution 129 (+ traces in tests-register, tests-acsp, tests-delivery).
s 1103 takes MAYBE BOOLEAN inputs (the answers of ss 1104(1), 1105(1)); NOTHING = no exception made out => general rule stands.
Composite functions added so the seat does not restate: s 1094(1) and (3); s 1096(1),(5A),(6); s 1097(1)-(5); s 1098E(1)-(3); s 1121 the person is an officer in default.
NEXT: coa24-seat.l4 + coa24-cases-seat.l4 (questions begin "Under section N,"; §-grouped in text order; @export + @desc on every input); then NOTES.md (build with work/build-notes.py from work/notes/*.md + coverage.py), NEEDS-CORE.md, dispositions.py, FALSE/NOTHING quote checker, final check.sh + srcrefs on all files, cleanup (remove tpl-only files? no: tpl is in work/, not shipped).

## Status update (context 1, seat written)
DONE: all layer-1 modules + tests; coa24-seat.l4 (70 @export questions, each with @ref, @export, @desc per input, grouped under §§ headings in text order); coa24-cases-seat.l4 (186 cases, generated from work/gen_cases.py with hand-written expectations; every question has >= 1 case, NOTHING cases asserted); full check.sh: 26 modules, 998 assertions satisfied, 0 failed, same on main-109 (work/check-full-1.txt); srcrefs --refs and --strict: 456 quote lines, 167 runs, 209 locators, 0 problems; checkquotes.py: every quoted piece in 319 FALSE/NOTHING comments is in the text, NOTHING reasons all among the six.
Coverage script: 713 rows (673 primary + 40 defined terms), 705 non-blank lines all covered once; dispositions: encoded 387, fork 38, inert(1) 83, inert(2) 198, repealed-or-blank 7 (work/dispositions.py maps every key; names validated).
NEXT: NOTES.md (work/build-notes.py + work/notes/*.md), NEEDS-CORE.md, final re-run of check.sh, final report. Re-run `python3 -I work/build.py` is NOT needed unless templates change; deposit files are built outputs of work/tpl.

## Final status (2026-11-13)
DONE: NOTES.md (built by work/build-notes.py from work/notes/*.md, coverage.py, branches.py, the jural table and the brief's rulings), NEEDS-CORE.md (4 items: 2 real gaps, 2 naming/convenience), final check.sh on both builds: 26 modules, 1001 assertions satisfied, 0 failed, 0 refused, every module "same" on 1.6.109 (work/check-full-final.txt); srcrefs --refs and --strict: 456 src lines, 167 runs, 209 locators, 0 problems; checkquotes: 319 FALSE/NOTHING comments (132 FALSE, 187 NOTHING), 0 quotation misses; 9 traces read on both builds; every NOT parenthesised; no REFUSE/YMD/BECAUSE (outside LEST BREACH BY); coverage 713 rows, 705 non-blank lines each in exactly one primary row.
Late changes: s 1094(1) and s 1098(1) take the s 1074 and s 1078 seam inputs as MAYBE BOOLEAN (so NOTHING passes through); s 1096(3) answers JUST TRUE once its condition is met (a sentence that grants the power, fork F3 exception); s 1093(1)(a)-(b) function added.
Scratch: no binaries were copied into the scratchpad; work/ holds only scripts, templates and text outputs.

## Seat audit of 2026-11-12 (lead's request)
70 seat questions read against the functions they return; 6 retitled (1 direction: s 1132A(5); 5 subject: s 1094AB(1), s 1128(1), (2), (3), s 1132A(4)); 17 assertions in coa24-cases-seat.l4 restated in place with `-- RECONCILED 2026-11-12: was ...`. check.sh TOTAL before and after: 26 modules, 1001 satisfied, 0 failed, 0 refused, every module same on 1.6.109. srcrefs --refs and --strict: 0 problems. NOTES.md has a seat list and a "Seat audit of 2026-11-12" note.

## Name-test sweep of 2026-11-12 (lead's request)
Swept the layer-1 functions named with may/permitted/power/entitled/authorised: 4 flipped to NOTHING (F19 s 1098B(1), F20 s 1113(3) may-apply, F21 s 1110C(1), F22 s 1132(2)), 18 kept JUST FALSE (text closes the gate, or not a grant), 0 listed "where/when/upon", 0 listed "entitled". 15 assertions restated (10 tests, 5 seat cases). check.sh TOTAL before and after: 26 modules, 1001 satisfied, 0 failed, 0 refused, all same on 1.6.109; srcrefs --refs and --strict 0 problems.
