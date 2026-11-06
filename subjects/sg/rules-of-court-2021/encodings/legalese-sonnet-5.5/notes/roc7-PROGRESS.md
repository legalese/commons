# PROGRESS (roc7: O 28, 29, 29A, 30, 31, 32, 33; lines 4194-5050)

Paths (absolute):
- RUN = <run>
- DEP = RUN/deposit/encodings/legalese-sonnet-5.5   (deliverables)
- WORK = RUN/work   (not shipped: builder scripts, .in sources, unit lists)
- RAW = RUN/inputs/SCJA1969-S914-2021.txt
- L4 = l4 (main 1.6.109) ; L4_MAIN = .../bin/l4-main-108

## State
- [x] read BRIEF, PLAN, guide, skills (SKILL.md x2, dialects), text 4194-5050, keel core
- [x] plan agreed (advisor, once)
- [x] builder WORK/build.py (macros %%REF %%AT %%FN %%PERIOD; see header) ; WORK/run.sh FILE... = quick run with counts
- [x] WORK/units.py -> units.tsv (703 units, 0 uncovered lines)
- [x] O 28 DONE: roc7-order-28.l4 + roc7-tests-28.l4 (391 assertions satisfied, 0 failed), srcrefs --strict 0 problems; WORK/cov-28.tsv (coverage+jural), WORK/forks.md (F-28-1..10)
- [x] O 29+29A (roc7-order-29, 100 asserts), O 30+31 (roc7-order-30, 162), O 32 (roc7-order-32, 66) DONE at layer 1, all srcrefs --strict clean. cov-29/30/32 NOT YET WRITTEN.
- [ ] O 33 in 3 modules (33a r1-17, 33b r18-28, 33c r29-46)
- [ ] seat + cases, notes.py (assemble NOTES.md from units.tsv + cov-*.tsv + forks.md + open-q), NEEDS-CORE.md (Years unit), check.sh run, encoding.json is the lead's

## Decisions (with licence)
- Brief governs over PLAN.md section 2: a stated period -> outside it JUST FALSE (periods ruling 2026-11-05 (a)); PLAN said NOTHING.
- Timeliness takes `o 3 r 3 the last day for doing the act` as an input DATE (S-T1); act date is MAYBE DATE, NOTHING = not done (QB site).

## PLAN (draft before advisor call)
Scale: 100 rules (O28 17, O29 7, O29A 5, O30 15, O31 4, O32 6, O33 46), ~850 text lines. One context, no subagents.
Tooling: WORK/build.py expands `%%REF label | N[-M]` macros in WORK/src/*.l4.in into `-- src:N | text` quote lines (via srcrefs.py quote) + `@ref label (src:N-M)`, so my hand-written L4 stays short and quotes are mechanical.
          WORK/units.py: parse raw 4194-5050 into units (rule / subsection `(k)  ` / paragraph `( a )` / subpara `(i)` / defined term) with line ranges -> units.tsv; WORK/cov.tsv maps unit-id -> disposition|L4 name|fork (prefix inheritance); builder emits the NOTES.md coverage table and audits every non-blank line is in a row.
Modules (flat, DEP/): roc7-order-28.l4 ; roc7-order-29.l4 (29+29A) ; roc7-order-30-31.l4 ; roc7-order-32.l4 ; roc7-order-33a.l4 (r1-17) ; roc7-order-33b.l4 (r18-28) ; roc7-order-33c.l4 (r29-46)
Tests: roc7-tests-28.l4 etc. (one per module). Seat: roc7-seat.l4 + roc7-cases-seat.l4. NOTES.md generated in parts + hand-written sections.
Shapes: (F1) period -> function over MAYBE DATE done (NOTHING = not done, QB site) and input `o 3 r 3 the last day for doing the act` DATE: <= last day JUST TRUE, after JUST FALSE (periods ruling a);
        (F3) court power -> MAYBE BOOLEAN, JUST TRUE when conditions held else NOTHING; (F4) deeming -> function returning a Moment/DATE + yes/no twin; (F5) definition -> over small enum/STRING; (F6) required contents -> record of BOOLEANs;
        a handful of regulative rules (O33 r2(4),(5), r18(2),(9), r20(2), O30 r5(2)) with #TRACE; seat ~50 questions "Under Order N, rule M, ...".
Seams I own: S-F1 o 28 r 10 ; S-F2 o 28 r 11 ; S-S2 o 28 r 12 ; I take: o 3 r 3 last day (DATE), o 7 r 8 day service deemed effected (DATE), o 26 r 3, o 6 r 5/6/7/9, o 8, o 9 r 7/8/9/24/25, o 13 r 8, o 14, o 15 r 4/10/11, o 16 r 2, o 19 (O30), o 21, o 27 r 15, o 59 r 7, o 11 r 2 as inputs.
Unstable second encoding: decide at the end (probably "none found" unless time).

## RULES OF THE ROAD (set after advisor call)
- (working rule until delivery; superseded by the delivery note at the end) do not hand-edit DEP/roc7-*.l4 while WORK/build.py is in use: edit WORK/src/<name>.l4.in and run `python3 -I WORK/build.py [name]`. Macros: `%%REF label | N-M` (quote lines + @ref), `%%AT label | N-M` (@ref only).
- WORK/units.py -> WORK/units.tsv (703 units, audit: 0 missing lines, 0 blank). Re-run after any change to units.py.
- Timeliness helper semantics (resolves advisor point 1): inputs `done` MAYBE DATE, `last day` DATE (o 3 r 3), `as at` DATE. JUST d: d<=last TRUE else FALSE; NOTHING (not done): as at <= last -> NOTHING (period still running), as at > last -> FALSE (period ran out). All sites registered under periods ruling (a); QB only where a bare "must" has no period.
- O 28 r 1 "deemed means deemed until the contrary is proved": helper `o 28 r 1 a deeming under this Order stands` over BOOLEAN `the contrary is proved`: FALSE once proved (until-bar, delegated-definitions ruling (d)), TRUE before. Thread on deeming functions.
- Yes/no twin for each Moment/DATE/NUMBER result.
- O 29/29A: own `Court` type, prefixed. Dependencies: none needed (all periods via S-T1): say so in NOTES + encoding.json note for lead.
- Build order: O 28 end-to-end first (module, tests, cov, jural), then O 33, then small Orders, then seat + cases, then NOTES assembly, then check.sh + srcrefs checks.
- Regulative rules: each gets a decision-function twin that is asserted; run each #TRACE on both builds and record outcomes in NOTES.

## Macro conventions learned (keep)
- %%FN inputs: a leading ? marks an if/where condition (unmet -> JUST FALSE per rulings 2026-10-29 / 2026-11-05 (b)); other inputs are scope limits (unmet -> NOTHING). DEF/WHERE kinds: every input is ? . DUTY with ? inputs auto-adds companion `<name> (the duty arises)` (QD).
- NOT precedence: write ((NOT a) OR b) always. A heading like  §§ `Rule 10 -- x (seam S)`  must keep everything inside the backticks.
- Hand tests live in WORK/src/<mod>.t.in with %%TESTIMPORT <module> first line; generated tests are appended by build.py.
- L4 binary path in WORK/run.sh. Hand-written helper in O 28: `o 28 r 7(8)(a) the act is done by the last day`, `o 28 r 1 a deeming under this Order stands`, `o 28 r 11(3) the first working day on or after`.
- Open convention sites so far: QB (o 28 r 3(1), 6(6), 8(1), 8(5), 14, 15(2)), QD (r 8(1) hand-made companion + auto companions), QE (r 7(1) service bureau), QA-adjacent (r 8(4) judged a grant), QC none, QF n/a.

## State at O 33a done (update 2)
- DONE layer 1: roc7-order-28 (396 asserts), -29 (100), -30 (164), -32 (66), -33a (517 = r 1-17). All run clean on main 1.6.109; srcrefs --strict 0 problems.
- build.py macros now: %%REF %%AT %%FN(POWER DUTY BARE DEF WHERE DEEM) %%NEG (flat negative) %%PERIOD %%VALID (validity period). Marks on %%FN inputs: '?' trigger (DUTY: unmet -> NOTHING + auto companion "<name> (the duty arises)"; POWER: unmet -> JUST FALSE); '!' exception on a DUTY (unmet -> JUST FALSE); plain = scope (unmet -> NOTHING).
- QD pattern for hand-written duties: compliance fn NOTHING when the trigger is unmet + companion "(the duty arises)" JUST FALSE. QB marker "(open convention question QB)" and QD marker in the NOTHING comments; QA hand sites say "a lifted bar grants nothing" (add marker text "(open convention question QA)").
- Anchors offered by 33a: `o 33 r 4 a warrant of arrest is issued under this Rule`, `o 33 r 5 a caveat against arrest is issued under this Rule`, `o 33 r 13 an instrument of release is issued under this Rule`.
- cov-28.tsv written; cov-29/30/32/33a NOT yet; forks.md has F-28-*; add F-33-1 (r 11(1) and = both), F-33-2 (unless on a grant r 6, r 14(2): JUST FALSE), F-33-3 (r 7(3) both deemings: earlier day), F-33-4 (r 13(3) neither limb: JUST FALSE).
- NEXT: roc7-order-33b (r 18-28), roc7-order-33c (r 29-46), roc7-order-duties (regulative rules + #TRACE, both builds), seat, cases, NOTES via notes.py, NEEDS-CORE.md (Years unit), check.sh.

## State after the seat layer (update 3, 2026-11-05)
- DONE layer 1 (all on main 1.6.109, 0 errors, 0 warnings): roc7-order-28 (396), -29 (100), -30 (164), -32 (66), -33a (520), -33b (440), -33c (461), -duties (32 assertions + 32 recorded #TRACE outcomes; identical on 1.6.109 and 1.6.108; traces.tsv).
- DONE layer 2: roc7-seat.l4 ((at that time 386, now 392; see the delivery note) `@export` questions, generated by WORK/seatgen.py from WORK/seatspec.py + fns.json; each calls one layer-1 function; time questions take a year/month/day with 0 = not done) and roc7-cases-seat.l4 (1259 cases lifted from the layer-1 tests of the called function; expected values written from the text there). Both run clean.
- Regenerate (until delivery only): `python3 -I WORK/build.py <module>` (layer 1), `python3 -I WORK/listfns.py` (fns.json), `python3 -I WORK/seatgen.py` (seat + cases). Superseded by the delivery note at the end.
- NEXT: WORK/covgen.py -> cov-29/30/32/33a/33b/33c.tsv (with jural holder|bearer|kind), WORK/notes.py -> NOTES.md, NEEDS-CORE.md (Years unit), srcrefs --refs/--strict on all roc7 files incl. duties, full check.sh, fix 33c header comments (remove the O 19 seam line; anchor `o 33 r 36(1)`), final report.

## State at first delivery (update 4, 2026-11-05; superseded by updates 5 and 6, whose numbers are current)
- ALL DELIVERABLES WRITTEN: layer 1 (8 modules + 8 test files), layer 2 (roc7-seat.l4: 386 questions at that time, 392 at delivery; roc7-cases-seat.l4: 1259 cases then, 1280 at delivery), NOTES.md (assembled by WORK/notes.py from units.tsv, cov-28.tsv, covgen.py, forks.md, traces.tsv, check-out.txt, notes_static.py), NEEDS-CORE.md (Years unit).
- check.sh (L4 = main 1.6.109, L4_MAIN = main 1.6.108): TOTAL 20 modules, 0 errors, 3459 satisfied (3438 before the six amount-and-day questions were added to the seat), 0 failed, 0 refused, identical on both builds. Baseline it replaced: the keel alone, 2 modules, 0 satisfied (WORK/baseline-check.txt).
- srcrefs --refs and --strict: 967 src lines, 503 runs, 672 locators, 0 problems, over every roc7 file.
- Coverage: 703 units; encoded 695, inert-1 8 (7 Order headings + PART 2), inert-2 0, inert-3 0. RULE-INDEX rows before: 107.
- Regeneration order while WORK/ exists: build.py <module> (each) -> listfns.py -> seatgen.py -> traces.py > traces.tsv -> check.sh > work/check-out.txt -> notes.py. This is a record of how the row was made, not an instruction for a later session (see the delivery note).
- The headers of the .l4 files no longer say GENERATED (the builder is not shipped).
- Open items for the lead: encoding.json "dependencies": [] ; hoist `Years` (NEEDS-CORE.md); lawyer to confirm the Jural table rows marked `not typed` and the Order 29-33 holder/bearer typing (read off the function names).


## Delivery note (update 5, 2026-11-05)
- After delivery the DEP files are the source: the `roc7-*.l4` files carry the text, the `@ref` and the quote lines as shipped, and a later session edits them directly (they say so in their headers).
- WORK/ (build.py, seatgen.py, notes.py and the .in files) was a one-time scaffold; it is not shipped and must not be re-run over the shipped files, because it would overwrite any hand edit made after delivery.
- Seat: 392 `@export` questions and 1282 cases (1280 before update 6). Six questions return an amount or a day (the monthly fee, the fee for a number of months, the day a fee is due, the day service through the electronic filing service is deemed effected, the day an originating claim is deemed duly served, the interest on a sum).
- The 8 jural rows that were once marked `not typed` are now typed by hand (NOTES says which were inferred from the nature of the provision).

## Judgment calls (update 6, 2026-11-05, after the lead's message that the six open convention questions are decided case by case)
- Fork register heading is now "Judgment calls" (was "Open convention questions"): one line per site with question id, provision, function, file:line, the answer taken and the other reading.
- Changed from the brief's defaults, each on the text of the site: QB (133 sites, including O 28 r 8(5), a site I had missed) now JUST FALSE for the compliance question when a bare "must" is not met (comment kind "a requirement the text states, not met on these facts", reading (c) in Marginal readings); QA (14 sites): 7 answer JUST TRUE (the exception is a permission, order or direction), 6 are split (JUST TRUE for the Court's permission or order, NOTHING for a fact that only ends the bar), 1 stays NOTHING (O 32 r 5(1)); QC (10 sites): 4 lists closed by Rule 1's "specified in" are JUST FALSE, 6 stay NOTHING with the reason per site; QE (10 sites): O 33 r 25(1) and r 35(2) "except" are JUST FALSE, O 28 r 9(2)(b) JUST FALSE inside a "where", the other six stay NOTHING (scope limit); QD (115 sites) unchanged, companions kept because a party plainly asks "does this duty apply to me?".
- Tests changed with the functions: 39 QB assertions and 15 QA assertions flipped, 4 QC and 5 QE assertions flipped, 2 both-limbs assertions added.
- check.sh (main 1.6.109, L4_MAIN 1.6.108): 20 modules, 0 errors, 3467 satisfied, 0 failed, 0 refused, same on both builds. srcrefs --refs and --strict: 0 problems. Seat: 392 questions, 1282 cases. O 29 r 7: the three arms pairing a listed court with the wrong country are JUST FALSE ("where" not met, ruling (b)); both-limbs assertions added for all six split QA functions.
- Periods: no timeliness assertion answers NOTHING outside a stated period (PLAN.md correction already followed).

## Fix round after an independent review (update 7, 2026-11-05)
- Item 1: every QB compliance function (bare "must" not met) now answers NOTHING, like Orders 20 to 27 and 34 to 70 (O 3 r 2(1) and r 2(4)(a)); 134 sites (133 plus the second duty made when O 33 r 41(1) was split); comment kind `NOTHING-kind (a requirement not met; ...)`; the "(the duty arises)" companions and the consequence functions are unchanged; 40 assertions and the seat refund case flipped back; reading (c) in Marginal readings, the QB lines of Judgment calls and forks F-28-4, F-28-5, F-ALL-2 rewritten.
- Item 2: O 28 r 12(1) now answers JUST FALSE for an unmet "If" (F-28-11); `?` added to the "where"/"if"/"upon" inputs of O 28 r 8(8)(b), r 12(9)(b), O 32 r 5(2)(b), O 33 r 18(8) and O 33 r 41(2) (JUST FALSE when unmet); O 28 r 8(1) and r 8(4) checked, no change. NOTES paragraph 8 of "Specific readings" says what was checked and F-ALL-4 records the rule.
- Item 3: (a) `o 33 r 21(10) the interest on the sum` takes `the judgment is given under this Rule` and answers MAYBE NUMBER (NOTHING outside it), seat question updated; (b) O 33 r 41(1) split into `... the claiming party files the claim` and `... serves a copy of the claim on every other party` (the exception is its own input), two seat questions plus companions; (c) O 28 r 12(3) route: one line under "What the text does not answer"; (d) new `o 33 r 16(4) the earliest moment the bond may be filed without consent` and two seat questions (may the bond be filed at this time; from what time); (e) the r 7(3) seat question retitled to the Legal Profession Act applications it asks about (its @desc lines already asked what the inputs ask and are unchanged; only the title misled), and a new seat question for the search-only entity's monthly fee under r 7(2)(c); the r 41(1) exception input is worded "Is it so that the reference is not in a limitation action?" in the seat.
- Item 4: fork lines F-28-1 (A1), F-33-10 (A2), F-33-8 (A3), F-28-13 (A5), F-33-11 (A6, flipped to NOTHING), F-ALL-3 (A7), F-29-2 (A8), F-33-12 (A9), F-28-12 (A10), F-33-13 (A11).
- Item 5: the reviewer's numbered test list was not supplied, so #113, #174, #226, #245, #278, #295, #325, #389, #404, #452, #138, #358, #240, #286, #323b and #331 cannot be matched to rules and no gap line was added for them; #55 (O 28 r 7(1)) and #409 (O 33 r 26(1)) are the QE sites already under Judgment calls. Needs the number-to-rule map to add the gap lines.
- Numbers: check.sh (main 1.6.109 and 1.6.108): 20 modules, 0 errors, 3495 satisfied, 0 failed, 0 refused, same on both. Tests 28=396, 29=100, 30=164, 32=66, 33a=527, 33b=441, 33c=469, duties=32. Seat: 397 questions, 1300 cases. srcrefs --refs and --strict: 968 src lines, 504 runs, 675 locators, 0 problems. traces: 32, 0 differences between builds.
