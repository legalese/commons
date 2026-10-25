# PROGRESS -- piece dg2 (Delaware General Corporation Law, ss 121-147, src lines 240-464)

Started 2026-10-25. Written by the dg2 agent; the disk is my memory.

## State

Layer 1, layer 2, the tests and NOTES.md are written.
The last full run of `check.sh` (target unstable) printed 0 errors, 0 failed and 0 refused, with every file's assertions written equal to assertions satisfied; the exact output is in NOTES.md under "What check.sh prints".
`python3 -I srcrefs.py check --refs <raw text> dg2-*.l4` printed 0 problems.
`python3 -I _work/cov.py` (now deleted) found no non-blank line of 240-464 that no coverage row names.

## Files (all in this folder)

- Layer 1: `dg2-powers.l4` (ss 121-127), `dg2-registered-agent.l4` (ss 131-132), `dg2-registered-agent-changes.l4` (ss 133-136), `dg2-board.l4` (s 141(a), (b), (j)), `dg2-board-committees.l4` (s 141(c)), `dg2-board-action.l4` (s 141(d)-(i), (k)), `dg2-officers.l4` (ss 142-143), `dg2-interested-definitions.l4` (s 144(e)), `dg2-interested-transactions.l4` (s 144(a)-(d)), `dg2-indemnification.l4` (s 145), `dg2-board-approvals.l4` (ss 146-147), `dg2-support.l4` (helpers).
- Tests: `dg2-tests-<module>.l4` for each of the twelve.
- Layer 2: `dg2-seat.l4` (172 questions), `dg2-cases-seat.l4` (599 cases, at least one per question).
- `NOTES.md`, `PROGRESS.md`.

## Decisions taken (and the section that licenses each)

All forks are in NOTES.md, "Fork register", with the text that licenses each.

## Late changes

- `-- out of range:` comments added above every input that stands for a provision outside the range (the brief asks for them); no rule changed.
- Section 132(f)(1) (src:331) had no rule; `s 132(f)(1) the Court may make orders respecting the proceeding and enter orders granting interim or final relief` was added to `dg2-registered-agent.l4`, with two assertions and a seat question and two cases.

## Left over

Nothing is left in `_work/`, which has been deleted.
Not done: an independent test pass (the brief allows none), and checking anything against the official text.
