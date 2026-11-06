# PROGRESS -- Terrorism Act 2000, Part III (iaw-ta), encoding legalese-sonnet-5.5

Read this first after any compaction.  Then NOTES.md (coverage table, fork register) and the text itself.

## Tools (in this folder)
- `coverage.py RAW [--audit] [--names] [--table] [--notes NOTES.md]`: rows from the text, map in `coverage-map.tsv`.
  RAW = .../runs/iaw-ta/inputs/ukpga-2000-11-part-3.txt (not copied here).
- `srcrefs.py check --refs RAW ta-*.l4` must print 0 problems.
- `check.sh` (L4=<l4-main-109> L4_MAIN=<l4-main-108>).
- Quote lines are generated, never retyped: marker line `--@Q a-b[,c-d] label` in a draft is expanded by a scratch script into
  `-- src:N | text` lines plus `@ref label (src:a-b)`.  (The script is in the session scratchpad, not here.)

## Plan (modules, in text order)
ta-nouns (types only) / ta-interpretation (s 14) / ta-offences (ss 15-18, 17A, 22) / ta-disclosure (ss 19-21ZC, 22A) /
ta-regulated-sector (ss 21A-21C, 21H) / ta-voluntary-disclosure (ss 21CA-21CF) / ta-tipping-off (ss 21D-21G) /
ta-information-orders (ss 22B-22F) / ta-forfeiture (ss 23-23B); ss 24-31 repealed (coverage rows only).
Layer 2: ta-seat.l4, ta-cases-seat.l4.  Tests of layer 1: ta-tests-<module>.l4 beside each module.

## Decisions taken (and the text that licenses each)
- Decision functions return MAYBE BOOLEAN; name carries the section ("s 15(1) ..."); FALSE-kind / NOTHING-kind comment on every no / not-covered branch.
- A failed "if" is the text's no (marginal reading (a)); a failed "where/when/which" limit is NOTHING (marginal reading (b)).  Both listed in NOTES.
- Borrowed terms (Sch 3A regulated sector, statutory maximum, level 5, bank holidays, Good Friday, group, EEA equivalence) are plain inputs.
- Good Friday and bank holidays: one input list of dates (the 1971 Act and Easter are not among the sources); Sat, Sun and 25 Dec are computed.
- s 14(1) "means" but s 14(2)(a),(b) "includes": no limb met -> NOTHING (fork F1, taken); the other reading is JUST FALSE.

## Working method (do not change)
- Draft module with `--@Q a-b[,c-d] label` marker lines; expand with the scratch script `<scratch>/ta-work/expand.py FILE` (replaces markers by quote lines + `@ref label (src:..)`).
  Regulative functions have NO GIVEN named like a constructor (`the person` clashes): use no GIVEN.
- Mixfix connectives in `ta-logic.l4`: `the conjunction` a `and also` b / `the disjunction` a `or else` b / `the negation of` a / `the fact` x.  Put each connective on ONE line (use WHERE names); a continuation line breaks it.
- NEVER turn a callee's NOTHING into FALSE: use `EQUALS JUST TRUE` only when the callee cannot return NOTHING, else propagate (ta-logic, or IF ... THEN callee ELSE JUST FALSE).
- Tests: `ta-tests-<module>.l4` (layer 1), `ta-cases-seat.l4` (layer 2).  Positional `OF` for records with a ruler comment; nested `OF` needs a named value.
- After each module: srcrefs check --refs; check.sh with L4=l4-main-109 L4_MAIN=l4-main-108; add rows to coverage-map.tsv (prefix pointers: `s 19(2)` = every rule named `s 19(2) ...`); `python3 -I coverage.py RAW --audit --names`; jural.tsv rows; `--notes NOTES.md` regenerates coverage + marginal readings + jural blocks.
- Keywords as constructor names fail (A, B ...): rename.  Names must not clash with prelude (`either`).

## Fork register (to be written into NOTES.md at the end; keep ids stable)
- F1 s 14(1) "means" vs s 14(2) "includes": no limb met -> NOTHING (taken); other reading JUST FALSE (closed "means").
- F2 s 19(2) "does not disclose (a) ... and (b) ...": failing either, or failing promptness = offence (taken); other reading: offence only if neither is disclosed.
- F3 s 21ZA(2),(3): notice period = calendar span from the first working day after disclosure to the 7th working day (counting that day as 1); a refusal received on any day from the disclosure day to that last day counts; on the last day the period has not yet ended.
- F4 s 21ZA(4): Good Friday and bank holidays are an input list (the 1971 Act and Easter are not among the sources); Sat, Sun and 25 Dec are computed.
- F5 E1: where the seat composes an offence (ss 15-18) with a protection (ss 21, 21ZA, 21ZB, 18(2), 21ZC, 21E-21G) that is option B hand-gathering; say where (to fill when the seat is written).
- F6 Mind record merges "may be used" (15(1),(2),16(2)) and "will or may be used" (15(3), 17): one field "reasonable cause to suspect that it will or may be used".
- F7 "sections 15 to 18" (and "16 to 18") include s 17A, which lies in the range: s 21(5), s 21CF(10), s 22B(14), s 23(1),(7).
- F8 s 21CA(1)(b) "where applicable": condition 5 is applicable in every case except the one s 21CA(7) names (a request by a constable).
- F9 s 21CC(4)(d): a report sent on the last day of the applicable period is sent "before the end" of it.
- F10 s 21CC(8): a constable's variation of the 28 days takes effect only by written notice to the person who made the required notification; without it the 28 days stand.
- Policy used in ss 21A-23B (M1/M2): a failed "if"/"where"/"applies" on an offence, protection, scope, content-"must", definition or duty-trigger = JUST FALSE (M1); a grant ("may"), "treated as", "includes", "so far as" without "only", and compliance with a sub-clause that does not apply = NOTHING (M2 / silent).  Ruling of 2026-11-05 06:04: a defence the person must "prove", when not proved, = JUST FALSE for that section only (F18); "when"/"upon"/"whenever" = "where" (F23).

## Status (2026-11-05, after the second ruling round)
- Layer 1: 10 modules + 9 test files.  Layer 2: ta-seat.l4 (55 `@export` questions in 8 groups, every input has `@desc`) and ta-cases-seat.l4 (181 assertions).
- Final check.sh (L4 1.6.109, L4_MAIN 1.6.108): 21 modules, 0 errors, 1054 satisfied (873 layer 1 + 181 seat), 0 failed, 0 refused, every module "same" on 108.  srcrefs: 635 src lines, 234 runs, 240 locators, 0 problems.  coverage --audit --names: 612 of 612 lines owned once, 615 rows, encoded 548, inert 22 (reason 1: 6; reason 2: 16), fork 37, repealed 8, deferred 0; 234 rule names checked; 0 problems.
- 14 #TRACEs read on both builds: same.
- Review round (ruling of 2026-11-05: (a) a period the text fixes in its own words, outside it JUST FALSE; (b) a "where" condition not met, JUST FALSE; (c) a scope limit with no "only", NOTHING): s 14(1) closed ("means"); s 19(4), 21CA(1),(8), 21CB(3),(4), 21CD(2),(5),(7),(8)(a),(10), 21CE(3), 21B(1), 21ZA(2), 22B(1),(1A),(8), 23(2)-(6) now JUST FALSE where their "if"/"where"/"only so far as"/period fails; new rule `s 21CC(8) the notice varies the period of 28 days`; stated gaps in coverage-map.tsv; `dependencies` key in encoding.json; forks F16-F22 in NOTES.md.
- Second ruling round (Meng, typed 2026-11-05T06:04:54.553Z): the "it is a defence ... to prove" sites s 18(2), s 19(3), s 19(4), s 21(5), s 21ZC now answer JUST FALSE for that section when the proof is not made ("this section gives no defence on these facts"), and keep NOTHING for a person not charged under the section (assumed, F18); no "when"/"upon"/"whenever" site needed a change, s 22F(5) is inert (F23); no "until" in the text; the definitions handed to a list were already JUST FALSE for a case in none of the heads, Schedule 3A is an input (F23).  The F18 "reviewer expected" line is gone, the answer is recorded as ruled.
- Left as they were, with "reviewer expected JUST FALSE; open question": the property clauses of s 23 and 23A(1) (F19), s 23A(2) (F20), s 21A(6)(b) (F21), s 21(2) and s 22B(12) (F22).
- To regenerate NOTES.md: the generator is in the session scratchpad (ta-work/mknotes.py), not in this folder; the generated blocks come from `python3 -I coverage.py <source> --notes NOTES.md`.
