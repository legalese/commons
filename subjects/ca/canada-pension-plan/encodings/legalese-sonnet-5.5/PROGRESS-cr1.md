# PROGRESS: piece cr1 (Canada Pension Plan Regulations: Parts I-IV, VIII, Schedules, Related Provisions)

Updated as work lands. After a compaction: re-read this file, NOTES.md and the text, not a summary.
Build tooling lives OUTSIDE the deposit, in `../../../work/` (relative to this folder: `tb/cpp/cr1/work/`): templates `src/*.l4.tpl` expanded by `build.py` (quote lines come from `srcrefs.py quote`; `@@INCLUDE@@` pulls `gen/schedules-data.l4`, which `gen_schedules.py` writes from the raw text); `cov_skeleton.py` + `cov_fill.py` feed the NOTES coverage table; `notes/*.md` are the NOTES fragments; `python3 work/mk_notes.py <deposit>/NOTES.md` regenerates NOTES.md. Never hand-edit a deposit .l4 that has a template; edit the template and run `python3 work/build.py <name>`.

## Layer 1 finished (each module: `l4 check` clean, `srcrefs.py check --refs` 0 problems, tests all satisfied)
- cr1-helpers.l4 (date helpers; no provision)
- cr1-interpretation.l4 (reg 2) + cr1-tests-interpretation.l4
- cr1-part1-contributions.l4 (regs 3-7) + cr1-tests-part1-contributions.l4
- cr1-part1-payment.l4 (regs 8-8.3) + cr1-tests-part1-payment.l4
- cr1-part2-returns.l4 (regs 9-14) + cr1-tests-part2-returns.l4
- cr1-schedules.l4 (Schedules III-IX as data and rules) + cr1-tests-schedules.l4
- cr1-part3-interpretation.l4 (reg 15), cr1-part3-outside-canada.l4 (reg 16), cr1-part3-transport.l4 (regs 17-21), cr1-part3-canada.l4 (regs 22-28), cr1-part3-election.l4 (regs 29-34.1) + their tests
- cr1-part4-interest.l4 (regs 35-36) + cr1-tests-part4-interest.l4
- cr1-part8-misc.l4 (79, 82-84.1, 86, 88), cr1-part8-mpe.l4 (85), cr1-part8-interest.l4 (87) + cr1-tests-part8.l4
- cr1-related-provisions.l4 + cr1-tests-related-provisions.l4
- Coverage table: 250 rows, no TODO left (work/cov_fill.py). Forks F1-F20 in work/notes/40-forks.md.

## Done (final)
- Layer 2: cr1-seat.l4 (113 questions, every one @export with @desc on every input) and cr1-cases-seat.l4 (215 assertions). Both generated from work/seat/ (gen_seat.py, gen_cases.py, build-seat.sh), outside the deposit.
- NOTES.md: all ten required headings filled, no TODO; coverage table 255 rows (encoded 162, fork 29, inert 50, repealed or blank 14), every non-blank line of the ranges covered (work/check_cov.py).
- check.sh: 35 modules, 0 errors, 1145 satisfied, 0 failed, 0 refused (exact output in NOTES.md).
- srcrefs check on the 16 layer-1 modules: 0 problems. l4 check warning scan on every cr1 file: clean.

## Left
Nothing in the brief. Open questions for a human are in NOTES.md "Before this is worth relying on".

## Seat-layer plan (superseded: the layer that landed has groups A to I; see NOTES.md ## Seat)
Seat: the individual (worker / self-employed / survivor / child / disabled person). Groups (§§) in the text's order: A. Contributions on my pay (regs 4-7, 3); B. When contributions are remitted, who is my employer (8-8.3); C. Information returns and my copies (10-14); D. Is my job pensionable (15-34.1) one question per route; E. Interest on my overpayment refund (35-36); F. Elections and deadlines (82-84.1); G. Interest on a debt I owe (87); H. SIN (88); I. The treatment of a spouse/partner under agreements (86); J. Year's maximum pensionable earnings (85) and Related Provisions. Each question: @export, @desc on every input in the person's words; builds layer-1 records from plain inputs; calls layer-1 rules; never restates.

## Decisions taken
- Rounding: round half up to the cent by FLOOR(x*100+0.5)/100, never prelude ROUND (half to even): reg 5(2).
- No DEONTIC rules: duties are encoded as dates, amounts and BOOLEAN predicates.
- "includes" definitions answer NOTHING outside the list (F1); a closed "means" list is a BOOLEAN.
- The Regulations file has no AMENDMENTS NOT IN FORCE section; no Part VI or VII.

## Disclosure for the final report (peeked)
While reading the Part VIII range I printed lines 817-821 of C.R.C.-c.-385.txt, which are the tail of reg 78.4 (piece cr2's range). I read nothing else of another piece.
