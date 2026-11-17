# PROGRESS (P1): Articles 5 to 7, Annexes I, II, III

State on 2026-11-17: finished. Nothing is pending except what the lead rules on (the fork register in NOTES.md) and what needs the core (NEEDS-CORE.md).
Sandbox: this folder (flat). Scratch: `work/` beside the run's `deposit/` folder, not shipped (generators `work/build.py`, `work/gen_*.py`, `work/coverage.py`, `work/gen_notes.py`; sources `work/src/*.l4` with `@@QR ... @@` quote directives).
To rebuild a layer-1 file: edit `work/src/<file>.l4` (or its generator), run `python3 work/build.py <file>.l4`, then `work/check-all.sh`. The seat and case files are generated whole by `python3 work/gen_seats.py`; the Article 3 terms and their facts are the `TERMS` table in that script.
After a compaction: re-read this file, NOTES.md and the text lines 170-261 and 1671-1754, not a summary.

## Follow-up pass (2026-11-17)
- Seat audit, second pass: 86 questions read, 0 retitled (NOTES.md, Seats).
- Fork entries at split sites name their authority; one new entry for the duty to stop the use when the authorisation is rejected (F-5-3-rejection-if); no answer changed.
- Seam S14 decided: no function wired (F-S14-reach). The person and manufacturer seat headers and NEEDS-CORE.md no longer say `aia-scope.l4` was missing.
- The person and manufacturer role questions through `Art 2(1)(g)` and `Art 2(1)(e)` of `aia-scope.l4` are not written (outside the follow-up).

## What exists
- Layer 1: `P1-annex-ii`, `P1-annex-i`, `P1-annex-iii`, `P1-art5` (points (a) to (h), (ba), (bb), 1a, 1b), `P1-art5-rbi` (paragraphs 2 to 8), `P1-art6`, `P1-art7`, each with a `P1-tests-*.l4`.
- Layer 2: seats person, provider, deployer, importer, product manufacturer (`P1-seat-*.l4` and `P1-cases-seat-*.l4`); no seat for distributor, authorised representative, general-purpose AI model provider or notified body (NOTES.md, Seats). A seat question that reaches an Article 3 term asks the facts of the keel's definition and works the term out in a `WHERE` by calling the keel's function (fork F-5-3-defined-terms); the table under Seats in NOTES.md lists which.
- NOTES.md (all sections the brief names), NEEDS-CORE.md.

## Last verification (2026-11-17)
- `check.sh`: 29 modules (5 keel + 24 P1), 0 errors, 1,194 satisfied (856 in the layer-1 tests, 338 in the seat cases), 0 failed, 0 refused, every row `same` on the main build (1.6.109). The five keel modules have no assertions of their own.
- `python3 -I srcrefs.py check --refs` and `--strict` over every `P1-*.l4`: 217 quote lines, 98 runs, 123 locators, 0 problems.
- 43 traces, 0 mismatches against their EXPECT comments, identical on both builds (`python3 work/trace-compare.py`).
- Coverage: `work/coverage.py` finds every non-blank line of the two ranges (176) in exactly one of 79 rows, and every L4 name the rows cite in a `P1-*.l4` file.

## Assumed, not ruled
Every entry of the fork register in NOTES.md. The largest: layer 1 takes the Article 3 terms as BOOLEAN inputs and the seat layer works them out from facts by calling the keel (F-5-3-defined-terms; the other reading is that layer 1 calls the keel); an unmet element of a prohibition answers NOTHING (F-5-1-element, 13 sites); the "may" gated by "where" answers JUST FALSE as the guide's ruling (b) gives (5 sites) and the grants of Article 5(5) answer NOTHING (2 sites). No function of P1 calls the keel's `Art 2(2)` (F-S14-reach, seam S14). Each split-site fork entry names the Guide line or ruling it relies on; two sites (5(2) and 5(3) urgency) fit those lines only by a reading, and the Article 111(2) saved-system answer follows the keel's convention against the Guide's "only if" (F-111-2-nothing); all are under Marginal readings.
