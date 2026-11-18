# PROGRESS (sgo) -- part agent sgo, Companies Act 1967 (Singapore), lines 27070-28513

Read this first after any compaction, then NOTES.md, then the text.

## How I work (tooling, all under work/ which is not shipped)
- Templates: `RUN/work/src/*.l4` hold the L4 with `@@SRC <label> N-M ...` and `@@REF <label> N-M` directives.
  `python3 RUN/work/tools/expand.py [file.l4 ...]` expands them mechanically from inputs/CoA1967.txt into this folder
  (quote lines `-- src:N | text`, page furniture, blank lines and amendment marks left out). EDIT THE TEMPLATE, NEVER the expanded file.
- Coverage: `RUN/work/tools/coverage.py` holds the coverage rows (start line, label, disposition, names); it checks that the
  rows tile 27070-28513 without gap and writes the NOTES.md coverage section.
- RUN = <scratchpad>/runs/dst-sgo

## Plan (modules, in this folder, all `sgo-` prefixed)
- sgo-service.l4      ss 386A, 387, 387A, 387B, 387C, 387D (interpretation, service, electronic transmission)
- sgo-court.l4        ss 388-392, 394, 399, 409A, 409C (costs, witnesses, disposal of shares, relief, irregularities, production, compel, injunctions, appeal)
- sgo-records.l4      ss 393, 395-398 (privilege, form of records, falsification, inspection, accounts not kept, translations, certificate)
- sgo-penalties.l4    ss 407, 408, 409, 409B (general penalty, default penalty, proceedings, composition) + sch 1 table
- sgo-offences.l4     ss 401-406 (offences)
- sgo-tests-*.l4      one per module
- sgo-seat.l4, sgo-cases-seat.l4

## Decisions taken (with the text that licenses each)
- Offence provisions: an unmet element answers NOTHING (the section says "shall be guilty" and says nothing of the person who fails an element); an "unless"/"except" gate that is MET answers JUST FALSE (s 405(1) "unless at that time the business was duly incorporated").
- "may" + "where"/"when"/"upon" gate fails: JUST FALSE (periods ruling (b)), listed as split site (ii) with the other reading; "may" + "if"/"on application"/"with" gate: NOTHING (grant rule).
- Period counting only through sg-periods (P2 for "within N days after": same-day act is NOT within).
- s 402 and s 408 seams answered by BOOLEAN functions (see NOTES Seams).

## Status (updated after the seat layer and the first full check.sh)
- [x] templates written (work/src/sgo-{penalties,service,court,records,offences}.l4), expanded into this folder by work/tools/expand.py
- [x] modules check clean (0 errors, 0 warnings on main-110 and main-109)
- [x] tests: sgo-tests-{penalties 78, service 97, court 145, records 107, offences 149}; every `-- EXPECT` trace matches on both builds (work/tools/traces.py: 45 traces)
- [x] seat + seat cases: work/seat/{questions,desc*}.txt -> work/tools/mkseat.py -> sgo-seat.l4 (120 questions) and sgo-cases-seat.l4 (279 cases, 279 satisfied)
- [x] coverage: work/tools/rows.py tiles 27070-28513 (243 rows) and work/tools/coverage.py checks it and writes work/notes/gen-*.md
- [x] check.sh run: 20 modules, 855 satisfied, 0 failed, same on main-109 (log: work/check-run1.log)
- [x] srcrefs.py --refs and --strict: 0 problems on sgo-*.l4
- [x] NOTES.md: built by work/tools/mknotes.py from work/notes/template.md and the gen-*.md tables (re-run it after any change to a module); reviewed 2026-11-18
- [x] final check.sh run after NOTES.md (work/check-final.log: 20 modules, 855 satisfied, 0 failed, same on main-109; srcrefs --refs and --strict 0 problems; 45 traces 0 mismatches on both builds)
- [ ] the final report (sent as the last message)
