# PROGRESS (wra3)

Paths (do not retype from memory):
- R = <the lead's scratchpad>/runs/iaw-wra3
- D = $R/deposit/encodings/legalese-sonnet-5.5   (deposit; check.sh runs every .l4 here, so NO scratch files here)
- W = $R/work                                      (scratch, probes, coverage.py)
- RAW = $R/inputs/ukpga-2012-5.txt  (3959 lines; my range ends "3960" which does not exist)
- L4 = .../scratchpad/bin/l4-stable-98 ; L4_MAIN = .../scratchpad/bin/l4-main-108

My ranges: 1344-1519 (Part 4 ss 77-95), 2475-2629 (Parts 6-7 ss 135-151), 3001-3049 (Sch 4), 3237-3959 (Sch 9-14).

## References read (do not re-read)
- BRIEF, PLAN, KEEL-NOTES, ENCODING-GUIDE, COMMONS-CLAUDE, both SKILL.md, dialects.md, source-locators.md, builtins daydate table, ea-seat.l4 first 170 lines (shape: @export Q / GIVEN ... @desc / GIVETH / DECIDE name IS ... WHERE records built from inputs).
- NOT yet read: drafting-patterns.md, regulative.md, source-patterns/*.

## Module plan (order of work)
1. wra3-pt4-pip.l4 (ss 77-90, 95) + wra3-tests-pt4-pip.l4
2. wra3-seat.l4 + wra3-cases-seat.l4 (Part 4 first)
3. wra3-pt6-misc.l4 (ss 135-146), wra3-pt7-final.l4 (ss 147-151)
4. wra3-sch9..., sch10 (para 1(2) only), sch11, sch12
5. wra3-sch4.l4 (housing credit)
6. sch13/sch14: coverage rows only (inert 2)
7. extend seat

## Decisions
(see NOTES.md fork register)

## Status
- [ ] nothing written yet

## Log
- Tooling (all in W): gen.py expands {{QR label | N M}} markers in W/tpl/NAME.l4 into src: quote lines + @ref and writes D/NAME.l4; `python3 t.py NAME [main]` generates, runs l4, prints counts, then srcrefs strict. EDIT THE TEMPLATE in W/tpl, never the generated D file.
- DONE (stable+main): wra3-pt4-s95 (+tests 20), wra3-pt4-s77-84 (+tests 164).
- Decisions: "not barred" = JUST TRUE means only that provision's bar does not apply (PLAN shape). Helper `s 78(6) the conjunction of the results` is the three-valued AND used by 78(6), 79(6), 79(1), 79(2). Month periods: `s 81(3) the last day of the months beginning with the day` (calendar months, clamped); previous 3 months = (D+1) less 3 months through D.
- Forks to record: F-81-1 (required period condition: limbs as the test vs NOTHING), F-81-2 (month-end counting), F-82 (12 months), F-83 (day of reaching relevant age counts as reached).
- DONE (stable): wra3-pt4-s85-90 (+tests 73; 2 TRACEs: FULFILLED day 730, BREACH day 731), wra3-pt6-misc (+tests 79; 2 TRACEs 911/912), wra3-pt7-final + wra3-sch10 (+tests-pt7-sch10 15), wra3-sch4 (+tests).
- TODO next: wra3-sch9 (list-limb functions: SSAA 73(6), SSA1998 Sch3 para 3(h)(i), SSFA 6A(1)(ca) x2, SSFA 10(3)(be), SSCBA 64(1A), SSAA 187(1)(ad), IAA 115(1)); wra3-sch11 (6 host Acts, seam-8 shared reading + purported-appeal-as-application); wra3-sch12 (definitions appeal tribunal/Commissioner + supersession list limbs); wra3-sch13-14 (definitions: the Commission, Minister of the Crown, appointed day for NI; rest inert 2); then SEAT (wra3-seat, wra3-cases-seat); then coverage table (work/units + audit script) and NOTES.md sections; NEEDS-CORE.md; check.sh run.
- Sch 9 ITEPA insertion (lines 3355-3356) is blank in this text -> 'repealed or blank'. Sch 14: Act column lost; inert 2 per group; Parts 3,5,10 headings only.
- DONE (stable): wra3-sch9 (+tests 16), wra3-sch11 (+tests 49), wra3-sch12 (+tests 26), wra3-sch13 (+tests 16; definitions CPA 8(1)/18(1) the Commission, 18(1) Minister of the Crown, 18(3) appointed day for NI; rest of Sch 13 inert 2 as amendments of other Acts / body staffing). Sch 14: coverage rows only (inert 2 per group).
- Sch 12 srcref lesson: a narrower @ref must follow the MOST RECENT quote run that covers it; otherwise repeat a {{QR}} for those lines.
- TODO next: SEAT (wra3-seat, wra3-cases-seat), then coverage table (work/units + audit script), NOTES.md sections, NEEDS-CORE.md, cleanup check, full check.sh run in background.
- PROBE (stable 1.6.98, work/probe/p5.l4) 11-04: diamond import of wra3-pt4-s77-84 + sch4 + sch13 + sch10 works; comma inside a backtick DECIDE name works; `@desc` line directly above `@export` on a top-level function raises no warning; `@export` with a MAYBE BOOLEAN GIVEN passes `l4 check`. Skill table: `@export <description>` exports, `@desc` on GIVEN params (function-level @desc is "internal only").
- Added layer-1 helper `s 78(6) the disjunction of the results` (wra3-pt4-s77-84, tests now 169): a section's own result = OR of 78(1), 78(2) (and 82(2) displacing) so the seat composes without logic of its own. gen.py now strips a duplicated (src:..) from QR labels (regenerate all modules at the end).
- SEAT DESIGN (fixed): every layer-1 MAYBE input becomes TWO plain inputs, "I can say whether X" + "X (ignored if you cannot say)", assembled in WHERE by helper `wra3 seat a yes or no the person may be unable to give` / `wra3 seat a number the person may be unable to give` / `... a date ...` (IF can-say THEN JUST x ELSE NOTHING). Questions: `@export Under section N, ...` + DECIDE `Under section N, ...` IS <layer-1 call>, GIVETH MAYBE BOOLEAN, return unchanged; @desc on every GIVEN. Person built in WHERE with placeholders. Composites: DL and mobility entitlement (call s 78(6)/79(6) with LIST of layer-1 results + disjunction). No seat for: s 77(2) (trivial list), s 78(4)/79(4)/85(3)-(7) (content of regulations), s 88(3),(4), s 89, s 141 (official-only), s 135(2)-(3), s 139, Sch 13, Sch 14. Sch 12 names carry derived para numbers; Sch 13 names cite the CPA section (paragraphs unnumbered): state both in findings.
- Seat generator: work/seatgen.py (specs -> wra3-seat.l4 + wra3-cases-seat.l4). Cases: #ASSERT count must equal satisfied.
- SEAT DONE 11-04: work/seat/{engine,specs_p4,specs_rest,seatgen}.py -> wra3-seat.l4 (65 questions) + wra3-cases-seat.l4 (259 #ASSERT = 259 satisfied on stable and main; mutation check: flipping 37 expectations made exactly 37 fail). Layer-1 additions: `s 78(6) the disjunction of the results`, `s 82(3) the required period condition limb ..., as it stands for the person` (wra3-pt4-s77-84 tests now 174). Regenerate with `python3 work/seat/seatgen.py` then `python3 work/t.py wra3-cases-seat [main]`.
- TODO next: coverage table (work/units.py + audit), NOTES.md sections, NEEDS-CORE.md, regenerate all templates (gen.py label fix) + rerun all tests, cleanup, full check.sh in background.
- 11-04 later: added layer-1 `s 92(3)` module (wra3-pt4-s92 + tests 8), `s 81(2)`/`s 81(3)(a)` definitions, `s 82(2) the result under section 78(1), section 82 displacing section 78(1)`, `sch 9 para 47 SSFA 10(3)(be)`; seat now 69 questions / 283 asserts (adds standard/enhanced composites for both components). work/cov.py builds + audits the coverage table (580 rows, 1103 non-blank lines, 0 problems; writes work/coverage.md). work/all.sh [main] reruns every module (4.5 min). Stable totals: 283+184+73+8+20+79+15+49+26+16+36+20 = 809 satisfied, 0 failed.
- TODO next: jural relations table (work/jural.py), fork register + marginal readings + seams + findings text, assemble NOTES.md (work/notes_build.py), NEEDS-CORE.md, main-binary rerun (all.sh main), cleanup (D has only wra3-*, NOTES, PROGRESS, supplied files), full check.sh in background, paste exact output into NOTES.
- FINAL 2026-11-04 (wra3 closed).
- Every layer-1 module imports `wra-definitions` (the brief governs over PLAN.md section 1); every template was regenerated and rerun on stable after that change: all clean.
- Added late: `sch 9 para 31 SSAA 187(1)(ad) the benefit is within the limb` (+3 tests; Schedule 2's (za) universal credit is the other limb, so it is a seam), FALSE-kind comments on three computed `JUST FALSE` branches (s 79(1)(a), s 79(2)(a), s 150(3)), and labelled fixture names in the two test files that had unlabelled ones.
- Decided against NEEDS-CORE.md: this part needed no type or constructor the core lacks (the three Child Support Act terms are asked as facts); the header of `wra3-pt6-misc.l4` says so.
- Final gate: `L4=<stable 1.6.98> L4_MAIN=<main 1.6.108> ./check.sh` exited 0, 27 modules, 812 satisfied on both builds, every module "same"; srcrefs `--refs` and `--strict` report 0 problems over 279 src lines.
- Coverage audit: 580 rows over 1103 lines (568 units before 12 splits), 0 problems; the sixth check (a row that is neither `encoded` nor `fork` names nothing) was added at the end.
- TRACEs (check.sh cannot see them): the four traces give the same FULFILLED and BREACH outcomes on stable and main; recorded in NOTES.md.
- NOTES.md is assembled by `work/notes_build.py` from the prose in it, `work/coverage.md`, `work/jural.md` and the check log; the work directory is not part of the deposit.
- Scratch and probe files live under work/ only; D holds wra3-*.l4, NOTES.md, PROGRESS.md and the supplied files.
