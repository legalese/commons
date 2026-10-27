# PROGRESS -- dg6: Subchapter IX, 8 Del. C. §§ 251-254 (src:1058-1171)

Written for the stable `l4` 1.6.98. Read this first after any compaction; then NOTES.md; then the text (sed -n on the source), not a summary.

## Working method (so a resumed session can continue)

- The `.l4` quote lines (`-- src:N | ...`) of the six layer-1 modules are produced mechanically from templates in the scratchpad, not typed:
  templates `scratchpad/dg6-work/tpl/<module>.l4` contain `@@Q N "start" ~ "end"@@` lines; `python3 -I scratchpad/dg6-work/gen.py` expands them into this folder.
  EDIT THE TEMPLATE, never the generated module (a re-run overwrites it). The test files (`dg6-tests-*.l4`) and `dg6-cases-seat.l4` are written directly here.
  `dg6-seat.l4` is the concatenation of the chunks `scratchpad/dg6-work/seat/s*.l4` (`scratchpad/dg6-work/mkseat.sh` rebuilds it): edit the chunks, not the file.
- `scratchpad/dg6-work/run.sh [files]` = expand, `l4 run`, count satisfied lines (each assertion prints twice), srcrefs check.

## State: everything written; last full run green

| item | status |
| --- | --- |
| layer 1: `dg6-s251a-agreement.l4`, `dg6-s251f-no-vote.l4`, `dg6-s251h-tender-offer.l4`, `dg6-s252-foreign-corporation.l4`, `dg6-s253-parent-subsidiary.l4`, `dg6-s254-joint-stock.l4` | done |
| tests of layer 1: `dg6-tests-s251a` (118 assertions), `-s251f` (78), `-s251h` (69), `-s252` (106), `-s253` (93), `-s254` (105) | done, all satisfied |
| layer 2: `dg6-seat.l4` (109 `@export` questions), `dg6-cases-seat.l4` (255 assertions, at least one per question) | done, all satisfied |
| `NOTES.md` | all ten sections written; coverage table 68 rows, no non-blank line of 1058-1171 unnamed |
| `check.sh` (L4_TARGET=unstable) | 0 errors, 824 satisfied, 0 failed, 0 refused over 15 modules |
| `srcrefs.py check --refs` over dg-core.l4 and dg6-*.l4 | 0 problems |

## Decisions taken (with the text that licenses each)

See the Fork register in NOTES.md (F1 to F26) and the numbered findings; the short list:
1. Sections 252, 253, 254 IMPORT `dg6-s251a-agreement` (the type `s 251 Kind of combination` and the composing rule); 251(f),(g) import it for the type.
2. A nonstock corporation is not covered by the § 251 stockholder-vote rule (`NOTHING`): § 114(b)(2).
3. "at least 20 days prior" (§ 251(c)) and "after 20 days' notice" (§ 253(a)): inclusive.
4. § 251(d) limits (1) and (3) protect the constituent whose stockholders adopted; limit (2) protects against any alteration of the survivor's certificate once any adopted.
5. § 251(f): the certificate exception governs the first sentence only.
6. § 251(h)(3): "equals at least such percentage" = enough to have carried the vote; "more than 2,000": strict.
7. § 252(d): fee paid exactly as prescribed; retention inclusive through 5 years after receipt.
8. § 253(a) is silent on a vote of the subsidiary's stockholders; 90% per class on votes; a class with no voting shares is not tested.
9. § 254(d)(8): needed for a surviving joint-stock association formed outside this State.
10. The "facts" sentences (251(b), 252(b), 253(a), 254(c)) are encoded, not inert: the list is open (fork F26); an event or a determination or action by any person or body is a fact, anything else `NOTHING`. No commencement or enactment date in the range.

## Files written (all in this folder)

dg6-s251a-agreement.l4, dg6-s251f-no-vote.l4, dg6-s251h-tender-offer.l4, dg6-s252-foreign-corporation.l4, dg6-s253-parent-subsidiary.l4, dg6-s254-joint-stock.l4, dg6-tests-s251a.l4, dg6-tests-s251f.l4, dg6-tests-s251h.l4, dg6-tests-s252.l4, dg6-tests-s253.l4, dg6-tests-s254.l4, dg6-seat.l4, dg6-cases-seat.l4, NOTES.md, PROGRESS.md (and the keel's dg-core.l4, check.sh, srcrefs.py, not mine, unchanged).

## Next

Only the final report (the last message), after a last `check.sh` and `srcrefs.py check --refs` run.
