# PROGRESS: Companies Act 1967 (Singapore), wave 1

Written by the lead agent at the merge, 2026-11-18. The agents' own progress files are `notes/keel-PROGRESS.md` and `notes/<agent>-PROGRESS.md`.

- keel written and verified; 11 parts written in parallel and verified one by one (check.sh on both builds, srcrefs --refs and --strict, NOT-precedence sweep, keel files identical to the keel's, traces read against their EXPECT words).
- merged with `merge_sg.py` (not shipped): 88 non-test modules, 85 test modules, the concatenated seat and cases.
- merged gate: 173 modules, 10,470 satisfied, 0 failed, 0 refused, same on the main build.
- not done: the later waves, the independent test pass, a seat audit, a check against a later consolidation.
