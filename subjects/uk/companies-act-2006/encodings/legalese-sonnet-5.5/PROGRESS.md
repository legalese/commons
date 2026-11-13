# PROGRESS: Companies Act 2006 (United Kingdom), 2006 c. 46

Written by the lead agent at the merge, 2026-11-13. The agents' own progress files are `notes/keel-PROGRESS.md` and `notes/<part>-PROGRESS.md`.

- keel written and verified; 30 parts written in parallel and verified one by one (check.sh on both builds, srcrefs --refs and --strict, core identical to the keel's).
- every part audited for seat-question direction and subject; a second pass for seven parts; the grant and power name test run over every part (NOTES.md).
- six independent readers wrote and ran tests from the text alone; their failures were repaired or restated (NOTES.md).
- merged with `merge_act.py` (not shipped): 231 non-test modules, 222 test modules, the concatenated seat and cases.
- merged gate: 453 modules, 40,076 satisfied, 0 failed, 0 refused, same on the main build.
