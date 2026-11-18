# PROGRESS (sgb2): Companies Act 1967, ss 161 to 173I

State as of the last write to this file: every section of the range is encoded (layer 1), tested, and has seat questions (layer 2); `NOTES.md` is written; the last full `check.sh` run is reproduced at the end of `NOTES.md`.
How each claim here was checked is in the column `Verified by`.

| Unit | Module | Tests | Verified by |
| --- | --- | --- | --- |
| s 161 | sgb2-s161-issue-of-shares.l4 | sgb2-tests-s161.l4 (43) | `check.sh` (both builds), `srcrefs.py check --strict` 0 problems |
| s 162 | sgb2-s162-loans-to-directors.l4 | sgb2-tests-s162.l4 (91) | same |
| ss 163, 163A, 163B | sgb2-s163-loans-to-connected-persons.l4 | sgb2-tests-s163.l4 (104) | same |
| s 164 | sgb2-s164-register-of-shareholdings.l4 | sgb2-tests-s164.l4 (100, 17 traces) | same |
| ss 164A, 165 | sgb2-s164a-s165-disclosure.l4 | sgb2-tests-s165.l4 (86, 22 traces) | same |
| ss 166, 167, 170 | repealed rows only | none | coverage rows |
| ss 168, 169 | sgb2-s168-s169-payments-to-directors.l4 | sgb2-tests-s168.l4 (85, 8 traces) | same |
| s 171 | sgb2-s171-secretary.l4 | sgb2-tests-s171.l4 (56, 17 traces) | same |
| ss 172, 172A, 172B | sgb2-s172-liability-of-officers.l4 | sgb2-tests-s172.l4 (29) | same |
| s 173 | sgb2-s173-registers.l4 | sgb2-tests-s173.l4 (70, 2 traces) | same |
| ss 173A, 173B, 173C, 173H | sgb2-s173a-s173c-information-duties.l4 | sgb2-tests-s173a.l4 (52, 24 traces) | same |
| ss 173D, 173E, 173F, 173G, 173I | sgb2-s173d-s173i-transitional-and-notice.l4 | sgb2-tests-s173d.l4 (82, 5 traces) | same |
| seat (layer 2) | sgb2-seat.l4 (84 questions) | sgb2-cases-seat.l4 (260) | same; a swap-mutation run (90 swaps, 58 caught, 32 are swaps the functions cannot tell apart) |
| NOTES.md | all required sections | none | read against the text; every quoted phrase in a `FALSE-kind` or `NOTHING-kind` comment found in the text or the Guide by script |

Decisions taken, with the provision that licenses each, are the fork register in `NOTES.md` (58 entries); the two counts of split sites are in "Split sites (sgb2)".

Open items for a reviewer: the marginal readings (`NOTES.md`, "Marginal readings for a lawyer": a summary and a table of the 157 branches of layer 1 that rest on reading (a) or (b), each with the other reading, generated from the kind comments); the seam deviations (`NOTES.md`, "Seams": s 6 and the `s 4(1)` terms are plain inputs, not calls of the keel).

To resume: re-read this file, `NOTES.md` and the text (`inputs/CoA1967.txt` lines 13355 to 15410); run `L4=<l4-main-110> L4_MAIN=<l4-main-109> ./check.sh`.
