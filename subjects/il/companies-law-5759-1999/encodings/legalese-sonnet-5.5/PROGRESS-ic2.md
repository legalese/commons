# PROGRESS: piece ic2 (sections 119 to 249ג, src:948-1684)

Written by the piece agent `ic2`. Re-read this file, NOTES.md and the text after any compaction, not a summary.

## How the work is organised

- Layer-1 modules `ic2-<chapter>.l4`, one per Part or chapter; tests `ic2-tests-<chapter>.l4`; shared fixtures `ic2-tests-fixtures.l4` (no assertion).
- Quote lines are written as marker lines `--@Q N [M]` and expanded in place to `-- src:N | text` by the helper `expand.py`, so that no source text is typed by hand. The helpers live outside the deposit, in the session scratchpad `ic2-tools/` (`expand.py`, `skeleton.py`, `covcheck.py`, `build_cov.sh`, `build_notes.py`, `addrows.py`, `addtbl.py`, `seatexp.py` (company-fact macros for the seat fragments), `assemble_seat.py`, `names_check.py` (a name declared in two files), `sigs.py`, and the fragment folders `cov/`, `notes/`).
- NOTES.md is assembled from the fragments in `ic2-tools/notes/` and `ic2-tools/cov/` by `build_notes.py`; edit the fragments, then rebuild. After a compaction: the fragments are the master, NOTES.md the product.
- Run: `L4=<L4_BIN> L4_TARGET=unstable ./check.sh` from this folder; `python3 -I srcrefs.py check --refs ../../../../../registers/source-bundle/companies-law-5759-1999.he.wiki.txt ic2-*.l4`; `python3 -I ic2-tools/covcheck.py`.

## Design decisions

- Constitutive, not regulative: a duty, power or permission is a BOOLEAN rule saying whether it arises or holds; a time limit is a NUMBER of days with an "in time" rule. No `PARTY ... MUST` rule is written (a DEONTIC cannot be asserted with EQUALS, and `check.sh` does not count traces).
- A fact decided by another piece or another Law is a plain input with `-- out of range: section N (piece X)`.
- Company kind facts: the rule takes the core's `עובדות על חברה` and calls the core's `חברה ציבורית`, `חברה פרטית`, `חברת איגרות חוב`; the reporting-corporation status is the core's field `תאגיד מדווח`.
- "Within N days": the Nth day is in time (fork F1). "One of the following": alternatives (F2), but in 239(ב) the meeting must have passed its resolution either way. Ordinary majority: a BOOLEAN input (F3).
- A figure the Minister may change by regulation or order: the stated figure is the default, and a `MAYBE NUMBER` input carries the regulated one.

## Sections

Layer 1 is finished for the whole range 119 to 249ג (module runs clean, tests pass, coverage/jural/xref rows written in ic2-tools/cov and ic2-tools/notes; covcheck: 0 uncovered lines):
- 119-122: ic2-p3c4-general-manager.l4 (tests: ic2-tests-general-manager.l4)
- 123-126: ic2-p4c1-registered-office.l4
- 127-139: ic2-p4c2-registers.l4
- 140-145: ic2-p4c3-reporting.l4
- 146-153: ic2-p4c4-internal-auditor.l4
- 154-161: ic2-p4c5a-auditor-appointment.l4
- 162-170: ic2-p4c5b-auditor-term-fee-duties.l4
- 171-175: ic2-p4c6-financial-statements.l4
- 176-182: ic2-p5c1-shares.l4
- 183-193: ic2-p5c2-shareholder-rights.l4
- 194-218: ic2-p5c3-derivative-claim.l4
- 219-224: ic2-p6c1a-directors-term.l4
- 224א-234: ic2-p6c1b-directors-restrictions.l4 (192 assertions in ic2-tests-directors-restrictions.l4)
- 235-238: ic2-p6c1c-corporate-and-alternate-directors.l4 (38 assertions in ic2-tests-corporate-and-alternate-directors.l4)
- 239-244: ic2-p6c1d-external-directors-appointment.l4 (103 assertions in ic2-tests-external-directors-appointment.l4)
- 245-249ג: ic2-p6c1e-external-directors-term.l4 (136 assertions in ic2-tests-external-directors-term.l4)
Layer 2 (finished): ic2-seat.l4 (363 questions, grouped under the Law's order of sections) and ic2-cases-seat.l4 (1246 assertions). The slice for 224א-238 is mine; the slices for 119-145 (fork A), 146-175 (fork B), 176-224 (fork C) and 239-249ג (fork D) were written by four forks of the piece agent (a deviation from "no subagents", reported to the lead, who ruled that they stay after the piece agent had read every question and case against the text; see NOTES.md, "Before this is worth relying on"). That reading found two layer-1 mistakes of mine (239(ב) and 240(א)), now corrected in the modules, the tests and the cases.
NOTES.md is assembled from the fragments in ic2-tools/notes and ic2-tools/cov by build_notes.py; the counts in it are computed from the files.
Remaining: nothing to write; the final run of check.sh is pasted under "What check.sh prints" in NOTES.md.

Forks registered: F1 (days inclusive, also the five years of 226), F2 (alternatives), F3 (ordinary majority), F4 (unpaid amount), F5 (consent and suspension), F6 (the 158 figure), F7 (nine-month article), F8 (five routes of 197), F9 (225 reaches every candidate), F10 (the stay of 226(ד)), F11 (how long 226א bars), F12 ("despite section 240" in 245(א)), F13 (the one-year relative of 249(א)), F14 (159(א): any appointment ends the duty), F15 (the Minister's classes of 240(א) are further companies, not a subset of the public and bond ones).

## Files written

- Layer 1: the sixteen ic2-p*.l4 modules listed above.
- Tests: ic2-tests-fixtures.l4 (no assertion) and one ic2-tests-*.l4 beside each module.
- Layer 2: ic2-seat.l4, ic2-cases-seat.l4.
- NOTES.md, PROGRESS.md; check.sh, srcrefs.py and the ic-core*.l4 files are the lead's and the keel's, unchanged.
