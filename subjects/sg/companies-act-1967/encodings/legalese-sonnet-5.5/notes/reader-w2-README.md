# The independent readers of wave 2

Three reader groups, each a fresh agent that read the Act's text before it opened any encoding, wrote its own answers to scenarios taken from the text, turned them into assertions, and ran them against the encoding of parts sgh to sgo (the wave-2 modules).
A failing assertion was left failing; each failure was then triaged as `ENCODER` (the encoding departs from the text), `SCENARIO` (the reader's expectation was wrong), `AMBIGUOUS` (the text and the Guide read both ways) or `GAP` (no function answers the question).

| group | parts read | words | triage file |
| --- | --- | --- | --- |
| a | sgh, sgi | 22,842 | `reader-w2a-triage.md` |
| b | sgj, sgk, sgl | 28,491 | `reader-w2b-triage.md` |
| c | sgm, sgn, sgo | 33,262 | `reader-w2c-triage.md` |

**What these files refer to that is not shipped.**
The readers' own test modules (`tests-independent.l4`) and their answer files (`ANSWERS.md`) are not part of this folder, so a line number written `L`, `t:` or "tests-independent.l4:N" in a triage file points at a file you do not have; the provision, the text line and the two answers in each line are enough to rerun the scenario by hand.
A line number written "text L" or "(L...)" is a line of the deposited source text, `../../registers/source-bundle/CoA1967.txt`.
The exception is the reader assertions that caught an `ENCODER` finding and now pass: they are in `sgh-tests-reader.l4`, `sgi-tests-reader.l4` and `sgj-tests-reader.l4`.

**Counts** (the lead reran every group's tests on the stable build): 1,929 assertions, 1,830 satisfied, 99 failed, 0 refused; 165 triage lines: `ENCODER` 5, `SCENARIO` 28, `AMBIGUOUS` 67, `GAP` 65.
These counts are of the encoding as it stood at commit d410f7a58, before the changes listed in the top-level `NOTES.md`, section "Changes made after the independent review".

**What the readers saw, and when.**
Groups a and c wrote their seat scenarios (33 and 48) after they had seen the seat questions' names and input types, and before they ran them; each group's report says so.
Group b's report does not say when it wrote its seat scenarios.
Group a read the bodies of a few functions (`sgh-part2-administration.l4`, `sgh-part2-inspection.l4`, one penalty in `sgi-alteration.l4`) after it had written its answers and before it ran them, and changed no expected value afterwards.
Group b read the encoders' comments for six provisions only after its expected values were written.
Group c read the modules for names and types, and again when judging verdicts after the run.
