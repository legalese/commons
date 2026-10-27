# PROGRESS -- piece dg8 (Subchapter IX, 8 Del. C. §§ 263-268, lines 1277-1385)

State at the last update: all deliverables written and checked; the final report is the last message of the session. After any compaction: re-read this file, NOTES.md and the text, not a summary.

## Tools (outside DEPOSIT, in the session scratchpad)

- `scratchpad/dg8-tools/build.py` expands the quote directives of the templates `scratchpad/dg8-tools/src/*.l4t` into verified `-- src:N | ...` lines and writes the `.l4` files into DEPOSIT. The `.l4` files here are generated: edit the template, rebuild with `b.sh`, never hand-edit a quote line.
- `scratchpad/dg8-tools/mkseat.py` (with `seatlib.py`, `seat263.py`, `seat265_268.py`) generates `src/dg8-seat.l4t`; `mkcases.py` generates `src/dg8-cases-seat.l4t` (expected values written by hand in that script, from the text); `notes/*.md` and `notes/coverage.rows` are assembled into NOTES.md by `mknotes.py`; `final.sh` runs the whole chain and `check.sh`.
- No probe files remain in DEPOSIT (they were `dg8-zz-probe*.l4`, deleted).

## Sections

| section | state |
| --- | --- |
| 263 | done: `dg8-s263-merger-with-partnerships.l4`; tests `dg8-tests-s263.l4` (142 assertions) |
| 264 | done: `dg8-s264-merger-with-llcs.l4`; tests `dg8-tests-s264.l4` (134) |
| 265 | done: `dg8-s265-conversion-to-a-corporation.l4`; tests `dg8-tests-s265.l4` (92) |
| 266 | done: `dg8-s266-conversion-to-other-entities.l4`; tests `dg8-tests-s266.l4` (162) |
| 267 | done: `dg8-s267-parent-and-subsidiary-merger.l4`; tests `dg8-tests-s267.l4` (108) |
| 268 | done: `dg8-s268-certificate-amendments-and-disclosure-schedules.l4`; tests `dg8-tests-s268.l4` (23) |
| shared noun | done: `dg8-nouns.l4` (the form of a combination, §§ 263 and 264) |
| seat layer | done: `dg8-seat.l4` (121 `@export` questions, 320 inputs, every input with `@desc`) |
| cases | done: `dg8-cases-seat.l4` (286 assertions, at least one for every question) |
| NOTES.md | done: all ten headings; 132 coverage rows (83 encoded, 27 fork, 21 inert, 1 repealed) |

## Decisions taken (with the text that licenses each)

- Every section its own module and its own rules, though 263 and 264 read as twins: they differ (263(c) second sentence on stockholders who become general partners; 263(c)(1) "type of entity"; certificate signed "by a general partner" against "by an authorized person"; "partner" against "member"; 263(b)(7) and (d) wording).
- Definitions ("partnership" 263(a), "limited liability company" 264(a), "other entity" 265(a), "entity" 267(d)(2)) are predicates over the core `Kind of entity` (keel instruction 12).
- The five "facts" sentences are encoded as rules over four kinds of thing (an event, a determination, an action: JUST TRUE; something else: NOTHING; fork F26), not left inert (the brief's list of reasons for `inert` does not include them).
- Binary quirks found: `WHEN `ctor` WITH field` is rejected, bind positionally; `at least` needs a bracketed percentage; a nested `ELSE IF` on one line needs `BRANCH`.
- Seat: 121 questions in six groups; an entity is chosen from one list of fifteen descriptions; one class stands for "each class" in § 267(a)(1) (assumed, not ruled).
- Forks: see the Fork register in NOTES.md (F1 to F26).

## Files written (all in DEPOSIT/encodings/legalese-sonnet-5.5/)

dg8-nouns.l4, dg8-s263-merger-with-partnerships.l4, dg8-s264-merger-with-llcs.l4, dg8-s265-conversion-to-a-corporation.l4, dg8-s266-conversion-to-other-entities.l4, dg8-s267-parent-and-subsidiary-merger.l4, dg8-s268-certificate-amendments-and-disclosure-schedules.l4, dg8-seat.l4, dg8-cases-seat.l4, dg8-tests-s263.l4, dg8-tests-s264.l4, dg8-tests-s265.l4, dg8-tests-s266.l4, dg8-tests-s267.l4, dg8-tests-s268.l4, NOTES.md, PROGRESS.md.
