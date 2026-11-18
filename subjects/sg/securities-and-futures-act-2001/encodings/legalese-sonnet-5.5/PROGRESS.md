# PROGRESS: Securities and Futures Act 2001 (Singapore), Cut A

Written by the lead agent at the merge, 2026-11-18. The agents' own progress files are `notes/keel-PROGRESS.md` and `notes/<agent>-PROGRESS.md`.

- keel written and verified; 4 parts written in parallel and verified one by one (check.sh on both builds, srcrefs --refs and --strict, NOT-precedence sweep, keel files identical to the keel's, traces read against their EXPECT words and compared across builds).
- merged with `merge_sfa.py` (not shipped): 49 non-test modules, 51 test modules, the concatenated seat and cases.
- merged gate: 100 modules, 6,293 satisfied, 0 failed, 0 refused, same on the main build.
- independent readers: four groups, one per range (see NOTES.md, section "Independent readers of Cut A"); their triage files are notes/reader-sfa-g<n>-triage.md.
- not done: the rest of the Act, a seat audit, a check against a later consolidation.
