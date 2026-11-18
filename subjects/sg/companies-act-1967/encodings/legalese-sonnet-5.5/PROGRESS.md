# PROGRESS: Companies Act 1967 (Singapore), waves 1 and 2

Written by the lead agent at the merge, 2026-11-18. The agents' own progress files are `notes/keel-PROGRESS.md` and `notes/<agent>-PROGRESS.md`.

- wave 1: keel written and verified; 11 parts written in parallel and verified one by one; merged; gate 173 modules, 10,470 satisfied, later 10,476 and 10,488 after the keel's core additions.
- an independent test pass on wave 1 (three reader groups; `notes/reader-README.md`) and three changes it led to (top-level `NOTES.md`).
- wave 2: 8 parts written in parallel against the hoisted keel and verified one by one (check.sh on both builds, srcrefs --refs and --strict, NOT-precedence sweep, keel files identical, every trace read against its EXPECT word); merged into the wave-1 folder with `merge_sg2.py` (not shipped).
- merged gate: 295 modules, 19,648 satisfied, 0 failed, 0 refused, same on the main build (292 and 19,642 before the changes that the wave-2 independent readers led to).
- 147 non-test modules, 145 test modules, one merged seat module and one merged cases module.
- not done: independent readers on wave 2, a seat audit of either wave, a check against a later consolidation.
