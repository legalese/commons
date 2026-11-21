# PROGRESS (sgd): the Companies Act 1967 (Singapore), ss 210 to 215K, lines 20183-21697

Status at 2026-11-18, end of the pass: layer 1, its tests, the seat layer, the seat cases, `NOTES.md` and `NEEDS-CORE.md` are written; the final gates are recorded at the end of `NOTES.md` ("What check.sh prints").
After any compaction: re-read this file, `NOTES.md` and the text (`inputs/CoA1967.txt` 20183-21697), not a summary.

## Paths

- RUN = <scratchpad>/runs/dst-sgd
- DEPOSIT folder = RUN/deposit/encodings/legalese-sonnet-5.5.
- L4 = RUN/../../bin/l4-main-110 (1.6.110); L4_MAIN = RUN/../../bin/l4-main-109 (1.6.109).
- Generated files (edit the source, never the output):
  - layer 1 (`sgd-compromise.l4`, `sgd-acquisition.l4`, `sgd-amalgamation.l4`, `sgd-amalgamation-solvency.l4`) from `RUN/work/tpl/<name>.l4t` by `python3 -I RUN/work/gen.py <name>`;
  - `sgd-seat.l4` from `RUN/work/tpl/sgd-seat-{a,a2,b,c,d,e}.l4t` by `cd RUN/work && python3 -I seatgen.py tpl/sgd-seat-a.l4t tpl/sgd-seat-a2.l4t tpl/sgd-seat-b.l4t tpl/sgd-seat-c.l4t tpl/sgd-seat-d.l4t tpl/sgd-seat-e.l4t`, then `python3 -I seatmap.py`;
  - `sgd-cases-seat.l4` from the layer-1 tests and `tpl/sgd-cases-seat-hand.l4t` by `python3 -I seatcases.py`, then `python3 -I addtrailer.py` (the closing line "Assertions written ... satisfied");
  - `NOTES.md` by `python3 -I mknotes.py` from `work/notes/*.tpl`, `coverage.py` (coverage table), `forks.py` (fork register), `marginal.py`, `deontic.py`, `seattable.py`.
- Hand-written: the four `sgd-tests-*.l4`, `check.sh`, `srcrefs.py`, `fetch-main-l4.sh` (the last three are supplied).
- Gates: `check.sh` (both builds), `RUN/work/gates.sh` (srcrefs `--refs` and `--strict`, `kindcheck.py`, `trace_compare.py` on both builds).

## Files

| file | covers | state |
| --- | --- | --- |
| sgd-compromise.l4 | ss 210, 211, 212 (and the repealed 211A-211J, 213, 214) | done; tests pass |
| sgd-acquisition.l4 | ss 215, 215AA, 215AB | done; tests pass |
| sgd-amalgamation.l4 | ss 215A to 215H, 215K | done; tests pass |
| sgd-amalgamation-solvency.l4 | ss 215I, 215J | done; tests pass |
| sgd-tests-*.l4 | tests, one per module | done; every assertion satisfied on both builds |
| sgd-seat.l4 | seat layer, 150 questions | done; `l4 check` clean |
| sgd-cases-seat.l4 | seat cases | done; every assertion satisfied on both builds |
| NOTES.md, NEEDS-CORE.md | notes, needed core types | done |

## Decisions taken (with the text that licenses each)

- Counting: only `sg-periods` (P1 to P9). "within N after X" uses `period: the date is within a period after` (the window opens the day after X); "within N of X" and "not later than the end of N after X" use `period: the date is not later than the end of a period after`; "not less than N before X" uses `period: the date is at least a period before`.
- "Before the general meeting": days only; an earlier day is before, a later day is not, and the day of the meeting is `NOTHING` (F-215C-1). Trace deadlines use the day before.
- A grant ("may") with an "if" gate that fails answers `NOTHING` (grant ruling of 2026-11-12, limit 1); a "where", "when", "upon" or application gate on a "may" answers `JUST FALSE` (periods ruling (b), ruling (c) of the second 2026-11-05 ruling), listed in the fork register and counted in "Split sites (sgd)".
- An offence function's own question, with an element unmet, answers `JUST FALSE` (split site (i), Guide line 98).
- Official Receiver party: `s 210(10B) the Official Receiver` (sgd-compromise); board of directors party: `s 215C the board of directors of an amalgamating company` (sgd-amalgamation); both in `NEEDS-CORE.md`.
- Penalty record `s 210(9) penalty` is declared once in sgd-compromise and reused for ss 211(5), 212(3), 215I(6), 215J(5).
- s 215AB(1): an unmet "if" answers `NOTHING` because s 215AB(3)(a) says so (finding 7).
- s 215(6): "received by the person" is read as received by the company holding it (finding 3); s 215K(1) is unambiguous.
- No "associate" in the range (finding 4); s 5B and s 5(1) are not called, and the wholly-owned status is a plain input (NOTES.md, "The brief governs over PLAN.md").

## Changes made at the end of the pass

- Added the `split site (ii)` tag and a fork id to the layer-1 comments that lacked them, and three fork lines (F-210-12, F-215H-2, F-215I-3) for grant functions that answer `NOTHING` without a fork line of their own; the fork register now has 42 entries.
- Tagged every branch that rests on a failed "if" with `marginal reading (a)` (19 branches, listed in NOTES.md).
- Moved the s 215K questions of the seat to the end of the file so that the `§` headings are in the text's order (215I, 215J, then 215K).
- Wrote `work/mknotes.py`, so that every table and count in `NOTES.md` is computed from the files.
- Known gap, recorded as finding 9: the manner of the s 215(3)(a) notice ("in the prescribed manner") is not asked.

## To do

Nothing is open. A reviewer's list is in `NOTES.md`: "Marginal readings for a lawyer (sgd)", "Split sites (sgd)", findings 2, 3, 6, 9, and "What the stable binary does not accept" (the brief and the two builds disagree about `REFUSE` and `YMD`).
