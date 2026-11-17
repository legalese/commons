# PROGRESS.md -- part agent ccc16 (Criminal Code (Canada), lines 8719-9543, ss 483 to 487.04)

Status: COMPLETE on 2026-11-16 (resumed after the weekly-limit stop): first pass and both follow-up tasks done; final check.sh 20 modules, 1611 satisfied, 0 failed, 0 refused, the same on 1.6.109; srcrefs --refs and --strict 0 problems; lint 0 problems; #TRACE outcomes identical on both builds. After a compaction, re-read this file, NOTES.md and the text, not a summary.

## Workflow (scripts in `../../../work/`, outside the deposit; templates in `work/src/`)
- `python3 -I work/build.py [name.l4]` expands `@@Q`, `@@GEN` markers in `work/src/` and writes the deposit file; `work/run1.sh <file>` builds, runs and prints counts.
- `python3 -I work/gen_seat.py` writes `ccc16-seat.l4` and `ccc16-cases-seat.l4` from a question table (the question names and the RETITLED map are there); `work/gen_dnatests.py` writes `src/ccc16-tests-dna-rows.l4`.
- `python3 -I work/mkcov.py` (coverage.json), `work/nametest_table.py` then `work/classes.py` (name-test classes), `work/audit_dump.py a b` (seat questions against layer-1 bodies), `work/lint.py`, `work/gen_notes.py` (writes NOTES.md; asserts each section occurs once).
- Check: `L4=<l4-main-110> L4_MAIN=<l4-main-109> ./check.sh`; srcrefs: `python3 -I srcrefs.py check --refs|--strict <raw> <files>`.

## Done
- Layer 1: seven modules with tests (officials 77, open-court 236, publication-bans 185, search-warrants 86, preservation 111, production-orders 272, dna-definitions 156) and `ccc16-tests-dna-rows.l4` (247, one per list row of s 487.04, with controls).
- Layer 2: `ccc16-seat.l4` (79 questions in 6 groups) and `ccc16-cases-seat.l4` (241 cases, all satisfied).
- Baseline on resume (check.sh, 20 modules): 1600 satisfied, 9 failed, all nine in `ccc16-tests-dna-rows.l4`: the generated fixtures for the Cannabis Act (a.1) and Controlled Drugs and Substances Act (b) rows lacked the indictment and five-year conditions those paragraphs ask for; fixture fixed, no expected value touched.
- Follow-up 1 (seat audit, second pass): 79 questions read, 8 retitled (485(2) summons, 485(2) warrant, 485.1, 486(3), 486.4(2), 486.51(7), 487.01(5.1), 487.0192(5)), 71 read and left (and the export text of 485(3) changed without a change of name); table in NOTES.md.
- Follow-up 2 (name-test sweep): 90 functions named may / permitted / power / authorized; 0 flipped (the ruling was applied from the first pass), 27 kept JUST FALSE, 28 listed (4 literal "Where", JUST FALSE; 24 on-application / when kind, NOTHING kept; 2 more kept functions, s 486.5(1) and s 486.7(1), also carry an on-application NOTHING branch), 0 entitled, 0 "it is lawful"; 33 grant-named functions answer NOTHING on a failed "if" gate; 2 outside the class.

## Decisions taken (assumed, not ruled; each is in the fork register of NOTES.md)
- A power named "may" whose "if" gate fails answers NOTHING (ruling 2026-11-12); a literal "Where" gate on a power, and a period or maximum the text states, answer JUST FALSE (rulings (a) and (b) of 2026-11-05); a duty whose trigger or "unless" is unmet answers JUST FALSE (case by case, the maintainer 2026-11-05); a category outside the section's scope with no "only" answers NOTHING (ruling (c)).
- The on-application gates stay NOTHING (a question to team-lead was sent, no answer yet): flipping them to JUST FALSE would touch 26 sites and their tests and seat cases.

## Still to do
Nothing in this part's scope. The open question to team-lead (the on-application gates of the name-test sweep, 24 functions answering NOTHING plus 2) is in NOTES.md, Fork register, Name-test sweep; if the answer is JUST FALSE the sites, their tests and their seat cases are listed there.
