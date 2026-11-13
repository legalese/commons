# PROGRESS (coa27: lines 17518-18348, ss 1239-1273)

Final state at 2026-11-13. After any compaction re-read this file, NOTES.md and the text, not a summary.

## Done (all green on 1.6.110 and 1.6.109: `check.sh` prints 0 errors, 1026 satisfied, 0 failed, 0 refused on both; `srcrefs.py check --strict` 0 problems)
- Layer 1: `coa27-definitions.l4` (ss 1260-1262), `coa27-ch4-register.l4` (ss 1239, 1240(3), 1240A(3)), `coa27-ch5-third-country.l4` (ss 1241-1246), `coa27-ch6-second-audit-offences.l4` (ss 1248-1250, 1255-1257), `coa27-ch6-administration.l4` (ss 1251-1254, 1258, 1259), `coa27-transfer.l4` (ss 1253A-1253F), `coa27-part43.l4` (ss 1265-1271, FSMA ss 89A-89O, 90A, 100A as inserted).
- Tests: one `coa27-tests-*.l4` per module (868 assertions, 6 #TRACE runs).
- Layer 2: `coa27-seat.l4` (58 questions, all "Under section N,") and `coa27-cases-seat.l4` (158 assertions).
- Seat audit of 2026-11-12: all 58 seat questions read against the bodies of the functions they call; 1 retitled (s 1257(2), a subject mismatch), 0 direction mismatches; the totals above are unchanged (no assertion added or removed; four restated in place with `-- RECONCILED 2026-11-12`). Details in NOTES.md, "Seat audit of 2026-11-12".
- NOTES.md (coverage of 781 units, fork register, Hohfeld table, marginal readings, reading of FALSE and NOTHING, seams, findings, binary notes, check.sh output), NEEDS-CORE.md.

## Decisions taken (and the text that licenses each: see the fork register in NOTES.md)
- Part 43: shells inert (reason 2); inserted rules a person in the seat can be asked about are encoded under the Companies Act number with the FSMA label as a sub-label; rule-making powers inert (F-H).
- s 1248(8)(b): two extents of the text run together; both encoded; a combining function answers NOTHING when they differ (F-G).
- Name-test sweep of 2026-11-12 (F-Q1 to F-Q13): 13 more functions named for a power whose plain "if" gate failed now answer NOTHING; 8 keep JUST FALSE because the text closes the gate; 6 are listed, not flipped (where/when/upon and time conditions, including s 1245(2), "on an application ... the court decides"). The seat question under s 1253D(1) turns an unmet route into JUST FALSE itself, so its answer is unchanged. 24 assertions changed in place with `-- RECONCILED 2026-11-12`, and 2 (s 1245(2)) changed back with the same marker; the totals above are unchanged. Details in NOTES.md, "Name-test sweep of 2026-11-12".
- s 1268 FSMA 89L(1) and (2), the name test of 2026-11-12 (F-P): 89L(1) answers NOTHING outside its scope (a scope limit with no "only", ruling "Periods, where and scope limits" (c)); 89L(2), named for a power, answers NOTHING when the "reasonable grounds" gate fails. The other reading of each is in F-P and in the marginal readings.
- Regulative rules: #TRACE pair plus a twin decision function that check.sh counts (`#ASSERT EQUALS` on a deontic is "unsupported-equality" on the stable binary: measured).
- "within 21 days beginning with the date": last day = date + 20; "within 28 days following the date": last day = date + 28 (F-B).

## Tools (not shipped, in ../work relative to the deposit's run folder)
units.py (unit parser and orphan check), spec.txt and jural.txt (coverage and Hohfeld specs), build-notes.py (writes NOTES.md), expand.py and src/*.l4.in (sources with quote macros), gen1262.py (the s 1262 table and its tests), run1.sh.

## Not done
Nothing is left deferred. Not tested: deployment of the seat questions to the Interact form (nothing was deployed).
