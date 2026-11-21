# The independent readers' files

Three reader groups, each a fresh agent that read the Act's text before it opened any encoding, wrote its own answers to scenarios taken from the text, turned them into assertions, and ran them against the encoding.
A failing assertion was left failing; each failure was then triaged as `ENCODER` (the encoding departs from the text), `SCENARIO` (the reader's expectation was wrong), `AMBIGUOUS` (the text and the Guide read both ways) or `GAP` (no function answers the question).

| group | parts read | triage file | split-site (type (ii)) proposals |
| --- | --- | --- | --- |
| 1 | keel, sga1, sga2, sga3 | `reader-1-triage.md` | `reader-1-phase3-findings.md` (also the s 7(9)(ca) seam) |
| 2 | sgb1, sgb2, sgc1 | `reader-2-triage.md` | `reader-2-phase3-split-sites.md` |
| 3 | sgc2, sgd, sge, sgf, sgg | `reader-3-triage.md` | `reader-3-phase3-split-sites.md` |

**What these files refer to that is not shipped.**
The readers' own test modules (`tests-independent.l4`) and their answer files (`ANSWERS.md`) are not part of this folder, so a line number written `t:` or "L" in a triage or phase-3 file points at a file you do not have; the provision, the text line and the two answers in each line are enough to rerun the scenario by hand.
A line number written "text" or "l." is a line of the deposited source text, `../../registers/source-bundle/CoA1967.txt`.

**Counts** (the lead reran every reader's tests itself): 1,969 assertions, 1,884 satisfied, 85 failed, 0 refused; 122 triage lines: `ENCODER` 2, `SCENARIO` 38, `AMBIGUOUS` 46, `GAP` 36.
These counts are of the encoding as it stood before the changes listed in the top-level `NOTES.md`, section "Changes made after the independent review".

**The proposals in the phase-3 files are proposals.**
The only ones taken so far are the three listed in that section of `NOTES.md`.
The rest depend on a ruling that has not been made on how a "may" gated by "where", "when", "upon" or "on application" answers when the gate fails.
