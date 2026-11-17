# PROGRESS (P2): Article 4a, Articles 8 to 15, Annex IV

Ranges: lines 156-169, 262-373, 1755-1782 of the consolidated text. Read BRIEF.md (runs/dst-aia-P2/BRIEF.md) and inputs/PLAN.md first after a compaction.
Work area (not shipped): runs/dst-aia-P2/work/ holds the generator (`gen_lib.py`, `spec_*.py`, `gen.py`) that writes the P2-*.l4 files; re-run `python3 -I gen.py` after editing a spec. Hand-written files are marked below.

## Design decisions (each licensed by the text or the brief)
- Layer 1 modules: P2-section-2-gate.l4 (hand-written: gate on Art 113 / Art 2(2) / Art 2(13), the combinator of answers = seam S8), P2-art-4a.l4 (Art 4a and the as-enacted Art 10(5)), P2-art-8 ... P2-art-15, P2-annex-iv.
- Every requirement function of Arts 8-15 and Annex IV: first arg `the date asked`, then `the AI system` (core record), `the harmonisation facts` (my record), then facts. Gate: NOTHING when not applicable (Art 113 + 111(2), keel reading), JUST FALSE when Art 2(2) cuts it off (S14), NOTHING when Art 2(13) says it may be limited (S15).
- Bare "shall" not done = JUST FALSE (case by case; fork F-bare-shall). Duty whose "where" gate fails = NOTHING (fork F-duty-where; rests on Guide line 95 alone, and the brief's limit (2) can be read the other way: flagged). Grant limited by "to the extent" or in its own wording = NOTHING (six sites, split site ii); a power gated by the word "where" (11(3)) = JUST FALSE since the follow-up pass (Guide line 93 item (b), brief limit (3)); grant with "shall be met in order for" = JUST FALSE.
- Versions: Art 10(1), 10(6), 11(1) second subparagraph (SMC, form), Art 4a (hand-over from Art 10(5)); each text in its own function without gate, dispatcher gated + versioned (the as-enacted branch of a Chapter III dispatcher is dead: tested through its own function).
- Seats: provider, deployer, person, notified, gpai, manufacturer (6 files); none for importer, distributor, rep (the text of my ranges does not address them).

## Status (final, after follow-up pass 1)
- DONE: every module, test file, seat file and case file written and clean; NOTES.md written by work/notes_gen.py (reads work/check4.log, runs work/coverage.py); P2-proto.l4 deleted.
- Follow-up pass 1 (FOLLOWUP-1.md), both tasks done: (1) second seat-question audit, 121 questions read, 3 retitled (deployer 13(1) first sentence, 14(1), 15(1); subject), assertions restated in place in P2-cases-seat-deployer.l4; (2) the fork entries at the split sites name the Guide line or ruling they rely on, with the Guide's words and the file and line; one answer changed because the Guide's line gives the other (11(3), NOTHING to JUST FALSE, restated in P2-tests-art-11.l4); the stale fork id F-8-2-where in a layer-1 comment now reads F-duty-where.
- Regenerate everything: `cd work && python3 -I gen.py`; then check.sh -> work/check4.log; `python3 -I coverage.py --check`; `python3 -I traces.py <tests files with traces>`; `python3 -I notes_gen.py`.
- Verified at the end of the follow-up pass: check.sh on 1.6.110 with 1.6.109 as main, exit 0, TOTAL 39 modules, 0 errors, 1946 satisfied, 0 failed, 0 refused, every module `same` (the same TOTAL as before the pass); srcrefs --refs and --strict 0 problems (180 src lines, 87 runs, 94 locators) over every P2 file; 24 traces agree on 1.6.110 and 1.6.109 (none changed); coverage 154 of 154 non-blank lines (29 inert reason 1, 42 fork, 81 encoded, 2 repealed or blank).
- Hand-written files: P2-section-2-gate.l4, P2-tests-versions.l4. Everything else is generated from work/spec_*.py.
- The final report (the last message) is the nine items of the brief; its numbers are in NOTES.md (Files, Coverage, Fork register, Split sites, check.sh output).
