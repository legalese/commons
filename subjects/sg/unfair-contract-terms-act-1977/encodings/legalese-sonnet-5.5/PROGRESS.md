# PROGRESS (UCTA 1977, Singapore, whole encoding, main target)

Re-read this file, NOTES.md and the text (INPUTS_DIR/UCTA1977.txt) after any compaction, not a summary.

Paths
- DEPOSIT dir: <run>/deposit/encodings/legalese-sonnet-5.5
- Source text: .../runs/iaw-ucta/inputs/UCTA1977.txt (697 lines, sha256 852b81e6...)
- L4 = <bin>/l4-main-109 (1.6.109, sha256 eeb12f1e...); L4_MAIN = <bin>/l4-main-108 (1.6.108, sha256 4159128d...)
- Check: `L4=<l4-main-109> L4_MAIN=<l4-main-108> ./check.sh`
- srcrefs: `python3 -I srcrefs.py check --refs <UCTA1977.txt> ucta-*.l4`

Plan (module order = import order, text order recorded in encoding.json)
1. ucta-nouns.l4 (DECLARE only)
2. ucta-logic.l4 (three-valued helpers over MAYBE BOOLEAN; reading rules)
3. ucta-schedules.l4 (First Schedule paras 1-4, Second Schedule (a)-(e))
4. ucta-part3.l4 (ss 26-30)
5. ucta-p1-explanatory.l4 (ss 11-14)
6. ucta-p1-introductory.l4 (s 1)
7. ucta-p1-avoidance.l4 (ss 2-4)
8. ucta-p1-goods.l4 (ss 5-7)
9. ucta-p1-other.l4 (ss 8-10)
10. ucta-effects.l4 (hand-gathered routes, option B; says so in the fork register)
11. ucta-seat.l4, ucta-cases-seat.l4
12. tests: ucta-tests-<module>.l4 per module
13. NOTES.md, encoding.json, SOURCE-LICENSE.md, coverage.py + coverage-rows.tsv

Status (updated after compaction #1)
- [x] coverage rows and script (196 rows, all 476 non-blank lines covered)
- [x] nouns
- [x] logic
- [x] schedules (+ tests 38)
- [x] part3 (+ tests 67)
- [x] explanatory (+ tests 109)
- [x] introductory (+ tests 130)
- [x] avoidance (+ tests 98)
- [x] goods (+ tests 132)
- [x] other ss 8-10 (+ tests 16)
- [x] effects: NO gatherer module (E1 option C; reach aggregator in the s 1 module is the only hand-gathering, option B guidance, say so in the fork register)
- [x] seat + cases (58 questions, 159 cases)
- [x] NOTES.md, encoding.json, SOURCE-LICENSE.md
- [x] check.sh green on both builds (19 modules, 775 satisfied); srcrefs 0 problems (496 src lines, 77 runs, 79 locators)

Decisions taken (with licence)
- D1 QA at the six "reasonableness" sites: follow the text's own spelling. "cannot ... except in so far as" (ss 2(2), 3(2), 4(1), 7(4)): NOTHING when the term is shown reasonable (lifted bar grants nothing; QA default). "can be excluded ... but only in so far as" (ss 6(3), 7(3)): JUST TRUE when shown reasonable. Both: JUST FALSE when not shown reasonable, "not shown" including "nobody has shown it" (fix round, s 11(5), fork F13). Recorded as a finding and one fork line per site.
- D2 No SHANT: the Act's effects are disabilities ("cannot") and immunities, not prohibitions; no provision names a party who must act by a deadline. Jural relations table records the kinds. Burden of proof (ss 11(5), 12(3)) is a decision function (who must show), not a MUST.
- D3 Dependencies: none copied (no period counted; s 30(2) is a date compared to 12 Nov 1993). Interpretation Act not used.
- D4 s 30(2) encoded (not inert): Date 12 11 1993; the "except in so far as s 5 Civil Law Act 1909" is an input (outside the text).
- D5 Layer 1 inputs: plain BOOLEAN for what a witness could state; MAYBE BOOLEAN for court judgments and borrowed legal characterisations (reasonableness, "appears to the court", goods of a type ordinarily supplied for private use, Minister's order).

Files written so far (all under DEPOSIT)
- BRIEF.md, PROGRESS.md
- _src/ (quote-expansion templates and build.py) REMOVED from the deposit at the end (deposit must be flat); the built .l4 files are now the source of truth. NOTES.md says so.
- ucta-nouns.l4, ucta-logic.l4, ucta-fixtures.l4
- ucta-schedules.l4, ucta-part3.l4, ucta-p1-explanatory.l4 (built)
- ucta-tests-schedules.l4, ucta-tests-part3.l4, ucta-tests-explanatory.l4
Next: seat generator (script in scratchpad, not shipped) -> ucta-seat.l4 + ucta-cases-seat.l4; then coverage.py/TSV, NOTES.md, encoding.json, SOURCE-LICENSE.md, check.sh run, final advisor call.
Seat design: two-tier: Part 3 question (14 facts) -> scope question (9 facts + Part 3 answer, per section) -> section questions take one My answer 'scope rules take my case out of this section'.
Design: ss 2-7 functions take `Reach of a section` (computed by s 1 aggregator from Scope facts, Part 3 outcome, Section of Part 1). Consumer unknown: evaluate both, NOTHING if they differ. Notices: ss 3,4,6,7 contract term only; ss 2, 5 any term or notice.

Fix round (2026-11-05, from an independent review: 156 assertions, 144 satisfied, 12 failed)
- Item 1 (F15): a flat negative that takes a section out of the case makes the six "requirement of reasonableness applies" twins answer JUST FALSE (ahead of their scope limits); the "can exclude / rely / be made to" functions stay NOTHING there.
- Item 2 (F6): per-site list. Real "where" on a negative at ss 2(3), 5(1), 9(2), 27(1): four new own-words twins (JUST TRUE inside, JUST FALSE outside); ss 10, 26, 28(2), 29(1) are not a "where" (checked, no change).
- Item 3 (F13, F14): unproved reasonableness is JUST FALSE for the claimant (s 11(5)); the seat's "I am not sure" there means "not shown". s 12(3): "no evidence" is not a state either layer holds (fork).
- Judgment calls: F16 (time of the judgment; Misrepresentation Act 1967), F17 (who prescribes under s 28(2)), F18 (s 5(2)(b)), F3 (First Schedule paras 2(c) and 4) all "checked, no change". F19 (reviewer gaps 138 and 140, as the lead explained them: offence for a void exclusion clause; incorporation of a term) checked, no change, no function added.
- Pre-existing assertions changed: 12 (avoidance 6, goods 5, seat cases 1); every other pre-existing assertion is unchanged and still passes.

Final state (this file is the record after the last compaction)
- Deposit is flat: 19 .l4 files + check.sh, fetch-main-l4.sh, srcrefs.py, coverage.py, coverage-rows.tsv, NOTES.md, encoding.json, SOURCE-LICENSE.md, PROGRESS.md, BRIEF.md.
- NOTES.md is generated from the built files by a scratchpad script (not shipped); its file:line cells match the built files as of the final check.sh run. Do not edit a .l4 file without regenerating NOTES.md.
- Added during the work: First Schedule para 1(d)(i) 'company' definition (nouns `Kind of entity`, `sch 1 para 1(d)(i) the entity is a company`).
- Optional second (unstable) encoding: not written; NOTES.md ## Unstable dialect says why.
- Remaining: final advisor call, final report as the last message.
