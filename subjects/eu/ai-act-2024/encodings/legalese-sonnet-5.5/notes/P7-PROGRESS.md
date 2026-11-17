# PROGRESS (P7, run dst-aia-P7)

Status at the end of the run, 2026-11-17: every deliverable is written and checked; nothing is in progress.

Method: generator scripts in `DEPOSIT/../work/` (`lib.py`, `build.py <name>`, `m_<name>.py` for layer 1; `seatlib.py`, `seatgen.py`, `s_<slug>.py` for the seats; `parse.py` and `notes.py` for this file and NOTES.md) write the `.l4` files from the consolidated text and the registries in `state_*.json`.
After a compaction: re-read this file, NOTES.md, the work folder's `m_*.py` and `state_*.json`, and the text.

## Done (checked on 1.6.110 and 1.6.109 with check.sh, srcrefs --refs and --strict, traces compared on both builds)
- Layer 1: `P7-gates` (two group gates, the gate that calls the keel's `Art 2(2)`), `P7-sandboxes` (Articles 57 to 59), `P7-testing` (Articles 60, 60a, 61), `P7-sme` (Articles 62, 63), `P7-governance` (Articles 64 to 70), `P7-database` (Article 71), each with `P7-tests-<name>.l4`.
- check.sh: 29 modules, 1497 assertions satisfied, 0 failed, 0 refused, 0 errors, on both builds.
- Seat layer: 73 questions and 273 cases in 6 seats (person, provider, deployer, rep, manufacturer, notified); no seat for importer, distributor or general-purpose AI model provider (reasons in NOTES.md, Seats).
- Coverage: 316 rows (263 encoded, 37 fork, 16 inert, 0 repealed), 0 lines of 843 to 1112 uncovered.
- NOTES.md: coverage, fork register, FALSE and NOTHING reading, marginal readings, split sites, jural relations, seams, versions, rules with no breach path, seats, findings, what the stable binary does not accept, traces, srcrefs and check.sh output.

## Follow-up pass (2026-11-17, FOLLOWUP-1.md): done
- Seat audit, second pass: 73 questions read, 4 retitled (direction 0, subject 4); each retitled assertion carries a RECONCILED line in its case file.
- Fork lines at split sites: 19 fork entries now name the Guide line they rely on (the new entry F-duty-gates, which groups 28 duties and powers with a "where", "whenever", "upon" or "as appropriate" gate, is one of them); one answer changed (Article 65(6) second sentence, "Where appropriate": `NOTHING` to `JUST FALSE`, rule (b) of the periods ruling), with its test restated in place.
- Seam S14 is a call to the keel's `Art 2(2)` in 13 functions; the two Section B facts are plain BOOLEAN inputs with their own `@desc`; fork F-60a-1 is replaced by what the call returns for Article 60a (Seams).
- Gate re-run: check.sh, srcrefs --refs and --strict, and all `#TRACE` outcomes on both builds (numbers in the sections at the end of NOTES.md).

## Decisions (the licence for each is in the NOTES.md fork register)
- BRIEF.md governs over inputs/PLAN.md (the differences are listed at the top of NOTES.md).
- A function named for a grant answers `NOTHING` when a gate fails; a duty unmet answers `JUST FALSE`; a limit closed with "only" answers `JUST FALSE`; split sites (ii) are listed one by one.
- Versions: the as-enacted function quotes the base file, the as-amended function quotes the consolidated text, and a dispatcher behind the group gate picks the version in force.
- Article 2(2) is a call to the keel's `Art 2(2)` in 13 functions (seam S14); each fork entry at a split site names the Guide line it relies on, and Article 65(6) second sentence ("Where appropriate") answers `JUST FALSE` by the periods ruling, rule (b).

## Files written
- Layer 1 and tests: `P7-gates`, `P7-sandboxes`, `P7-testing`, `P7-sme`, `P7-governance`, `P7-database`, `P7-tests-gates`, `P7-tests-sandboxes`, `P7-tests-testing`, `P7-tests-sme`, `P7-tests-governance`, `P7-tests-database` (all `.l4`).
- Seats: `P7-seat-<slug>.l4` and `P7-cases-seat-<slug>.l4` for person, provider, deployer, rep, manufacturer, notified.
- `NOTES.md`, `PROGRESS.md`. No `NEEDS-CORE.md`: no type or constructor the core lacks was needed.
