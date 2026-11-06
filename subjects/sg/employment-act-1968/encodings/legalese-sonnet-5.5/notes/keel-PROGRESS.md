# PROGRESS (keel agent, row iaw-ea-k, Employment Act 1968 (Singapore))

Written for the keel's own memory across context compaction.
After a compaction: re-read this file, `NOTES.md`, `PLAN.md` and `inputs/EmA1968.txt` lines 1-784, not a summary.

## Brief and inputs
- Brief: `runs/iaw-ea-k/BRIEF.md`. Inputs: `runs/iaw-ea-k/inputs/`. Deposit: this folder.
- Binary: `scratchpad/bin/l4-main-109` (1.6.109 main), second main build `l4-main-108`.
- Keel range: EmA1968.txt lines 1-784 (title page, arrangement of sections, s 1-7, all of s 2(1)).
- Parts: ea1 785-2596, ea2 2597-4611, ea3 4612-6790.
- Probe/scratch work: `scratchpad/keel-ea-k/` (not part of the deposit): `ea-core.l4.in`, `ea-definitions.l4.in`, `ea-definitions-tests.l4.in` are the templates; `build.py` expands the `{{Q n m}}` markers into `-- src:` quote lines; `lint.py` checks every FALSE-kind / NOTHING-kind comment and quote.

## State
- [x] read brief, skills, Guide, example seat
- [x] read text: keel range in full; the parts' ranges for seams
- [x] ea-core.l4 (278 lines; srcrefs 0 problems)
- [x] ea-definitions.l4 + ea-definitions-tests.l4 (155 assertions, all satisfied on 109 and on 108; srcrefs --refs and --strict 0 problems; lint 0 problems; no warnings)
- [x] PLAN.md final (seams re-checked by grep against the text; function table generated from ea-definitions.l4)
- [x] NOTES.md final (coverage table checked: every non-blank line of 1-784 is in a row; E1 and N2 diffed against BRIEF.md: identical; 14 forks; marginal readings; jural relations; findings; unstable line)
- [x] final check.sh run after the last edit: 0 errors, 155 satisfied, 0 failed, 0 refused, same on 1.6.108; srcrefs --refs and --strict 0 problems; lint 0; no warnings on either build
- [x] advisor review done; fixes applied (F2 count, jural enumeration); report next

## Decisions taken (with licence)
- Parts see only ea-core.l4 (brief: "each with your core module as a read-only file"); a defined-term answer from ea-definitions is a seam INPUT for a part.
- Section GIVEN is not accepted on main (dialects.md): every rule has its own GIVEN.
- Unowned in PARTS.md: `EmA1968-S200-2019.txt` (the Retrenchment Reporting Notification 2019). Flag to lead; recommend ea2 (s 96A is in ea2's range).
- Policy P-INC for "means X and includes Y": JUST TRUE if X or Y, otherwise NOTHING (NOTHING-kind includes). Recorded as fork F2 in NOTES.md.

## Findings worth telling the parts (measured)
- On main 1.6.109 and 1.6.108 a long `PLUS` chain over locals defined in a `WHERE` block AFTER the expression that uses them makes `l4 check` run for minutes with no error and no output (killed after 60 s; the same function type-checks in under a second once the locals are defined first on 109, but still hangs on 108). Writing the sum as `sum (LIST ...)` over inline field projections is fast on both.
- `length` and `isEmpty` are not in the prelude: use `count` and `null`.
