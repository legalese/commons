# PROGRESS.md -- roc8 (Orders 34 to 38, lines 5051-5510)

Status: ALL DELIVERABLES WRITTEN; only the final report remains.
Re-read this, NOTES.md and the text after any compaction, not a summary.

## Done

- Layer 1: roc8-nouns, roc8-order-34 .. 38 (generated from work/src/*.l4.in by `cd work && python3 -I build.py <name>`; order-37 and order-38 from work/mk37.py and mk38.py).
- Tests: roc8-tests-order-34 .. 38 (work/src/*.in; 37 and 38 from mk37t.py and mk38t.py).
- Seat: roc8-seat.l4 (64 questions) and roc8-cases-seat.l4 (122 assertions), written by `python3 -I mkseat.py`.
- NOTES.md: written by `python3 -I mknotes.py` (needs L4 and L4_MAIN in the environment, or uses the scratchpad bins); it runs check.sh and srcrefs itself and embeds their output.
- check.sh (L4=l4-main-109, L4_MAIN=l4-main-108): 15 modules, 0 errors, 1097 satisfied, 0 failed, 0 refused, every line `same`.  trace-check.py: 72 traces, 0 problems.  srcrefs --refs and --strict: 0 problems.  No Error or Warning diagnostics on either build.

## Decisions taken (with the text or ruling that licenses each)

1. The brief governs over PLAN.md on periods: a stated period answers JUST FALSE outside it (ruling of 2026-11-05 (a)).
2. The count of a period is O 3 r 3 (another part): every "in time" function takes `o 3 r 3 the last day for doing the act` as a DATE (S-T1); the bars take the first day (S-T1b).
3. Quotes are mechanical: build.py expands `@@REF label|a b@@` markers by reading the raw text.
4. DECIDE names in the seat are the @export sentences ("Under Order N, rule M, ...").
5. Layer 1 is frozen: NOTES.md cites file:line from the built modules.

## Findings worth keeping

- `NOT a AND b` is `NOT (a AND b)` on both builds (work/probe6.l4); found at 3 sites by failing tests.
- A MAY with no LEST lapses to FULFILLED on both builds (work/probe5.l4).

## Update 2026-11-05 (lead): the six questions are judgment calls

- NOTES.md heading `### Judgment calls` (was `Open convention questions`) under the Fork register.
- Every QA/QB/QD site re-read on its own text; no answer changed; basis QA-1, QB-1, QD-1 stated once and cited per line (QB-1 = O 3 r 2(1) and (4)(a), raw lines 296-299).
- QD group 2 sites marked scope or trigger; no twin functions added.

## Fix round (after the update above)

- Period directions: O 38 r 14(1) and 14(3)(a) are now `Before the anchor`; 4 periods without a constant (O 34 r 6(2), 7(7)(a); O 38 r 10(a), 13(1)) now have one; every one of the 27 constants has length, unit and direction asserted.
- O 38 r 10(a): fewer than 4 clear days is JUST FALSE.
- New: O 34 r 2(1), 2(2), 3(2) way-of-application functions (a different way gets NOTHING); O 34 r 10(1) takes whether the Court gave permission (none: JUST FALSE); O 36 r 3(2) unpaid portion and an equality twin.
- Forks F21 to F26 added; seat 70 questions, 135 cases; check.sh 15 modules, 1203 satisfied on both builds; srcrefs 0 problems; trace-check 72 traces 0 problems.

## Remaining

- The final report (8 items) and the scratch tidy (nothing large in work/; no binaries copied).
