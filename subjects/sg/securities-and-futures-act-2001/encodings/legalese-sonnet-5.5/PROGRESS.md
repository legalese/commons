# PROGRESS: Securities and Futures Act 2001 (Singapore), Cut A

Written by the lead agent at the merge, 2026-11-18. The agents' own progress files are `notes/keel-PROGRESS.md` and `notes/<agent>-PROGRESS.md`.

- keel written and verified; 4 parts written in parallel and verified one by one (check.sh on both builds, srcrefs --refs and --strict, NOT-precedence sweep, keel files identical to the keel's, traces read against their EXPECT words and compared across builds).
- merged with `merge_sfa.py` (not shipped): 49 non-test modules, 50 test modules, the concatenated seat and cases.
- merged gate: 99 modules, 6,290 satisfied, 0 failed, 0 refused, same on the main build.
- not done: the rest of the Act, the independent test pass, a seat audit, a check against a later consolidation.
