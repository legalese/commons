# PROGRESS (iaw-mc97, encoder: single Sonnet 5.5 agent)

Written to disk first so a compaction costs little.
After a compaction: re-read this file, NOTES.md, BRIEF.md and the extract (not a summary).

## Fixed facts

- DEPOSIT dir: this directory.
- RAW (in the run's inputs, now `../../registers/source-bundle/aep-Edw1cc1929-25-9-extract.md`); the table of status entries was `status-entries.tsv` in the run's inputs and is not shipped.
- L4_BIN = `.../scratchpad/bin/l4-stable-98` (1.6.98 main 7689b0d, sha256 82ea44ad...263e); L4_MAIN = `.../bin/l4-stable-102`.
- Source text lines in the extract: 22-49 (labels, preamble 1 at 23, preamble 2 at 26, c.1 at 29, c.9 at 32, c.29 at 35, heading 37, note 38, wrapper1 41, wrapper2 44, wrapper3 47, scans note 49).
  Status table 57-84; variants table 92-112.
- Build 98 facts probed: `#ASSERT deontic EQUALS deontic` gives "assertion failed" (never satisfiable); `#TRACE` prints no assertion line.
  `SHANT` with no WITHIN stands for ever; doing the act gives DEONTIC BREACHED.
  Vertical `LIST` of strings, `CONSIDER ... FOLLOWED BY`, `MAYBE/NOTHING`, `FLOOR n EQUALS n` all work.
  srcrefs accepts `|`-bearing table rows and sub-line slices of a long raw line.

## Build order and state

1. gen-status.py -> mc97-status.l4 + mc97-tests-status.l4 ........ DONE (56 assertions; --verify diff against tsv passes)
2. gen-coverage.py (manifest -> coverage table in NOTES.md + audit) ... DONE (stage 1 = 119 rows, 0 problems on the first run; stage 2 adds 28 limb + 45 term rows (192 in all); also checks fork ids and curly-quoted passages)
3. mc97-nouns.l4 ............................................... DONE (add constructors only with care: tests depend on them)
4. layer 1: mc97-preamble, mc97-c01, mc97-c09, mc97-c29, mc97-saving + a tests file for each ... DONE
   (27 + 20 + 28 + 62 + 78 assertions; 19 traces, all as expected, builds 98 and 102 agree; check-traces.py reads them back)
5. mc97-seat.l4 (15 @export questions), mc97-cases-seat.l4 (61 assertions) ... DONE
6. check.sh (both builds; the FIRST full run, superseded by 'Latest numbers' below): 15 modules, 0 errors, 332 satisfied, 0 failed, 0 refused, main columns identical; srcrefs --refs 0 problems (72 quote lines); traces 19/19 as expected, 98 and 102 agree ... DONE (rerun after any edit)
7. encoding.json, SOURCE-LICENSE.md, NOTES.md ........................ DONE (NOTES.md has all brief sections; check.sh output spliced verbatim)
8. positive controls: coverage audit (4 mutations caught), check-traces.py (flip + removed expect caught) ... DONE
9. advisor (second call), final report ... TODO

## Decisions taken (and the text that licenses each)

- Party = the King / an Heir of the King / a Man of the Realm. "We" is NOT identified with Henry or Edward in rules (F-WE); only preamble 1 and 2 name a speaker.
- Passive limbs of c.29, c.9 "shall have", wrapper 2 "shall be observed": decision functions only, no PARTY invented; an explicit NOTHING function says the text names no actor.
- c.29: exception ("but by lawful judgment of his Peers, or by the Law of the Land") read as governing ALL limbs (F-C29-SCOPE); "nor will We not" read as a plain negative (F-C29-NEG); the two exception limbs are alternatives (F-C29-OR); "sell" takes Justice or Right (F-C29-SELL); "man" is a separate input from "Freeman" (F-C29-MAN); variant "deal with him" not encoded (F-C29-VAR).
- c.9: bracketed "[which it hath been used to have]" taken as text (F-C9-BRACKET); "free" read as qualifying Customs only (F-C9-FREE).
- Subsidy "have given" = stated fact + ratio (1/15), not a duty (F-SAVING-GIFT).
- Regulative rules are TRACED (check-traces.py, `-- expect:` markers), not asserted; every duty also has a decision twin that IS asserted. Evidence: `#ASSERT rule EQUALS rule` -> "assertion failed" on 98.
- Rule names are prefixed with the chapter/paragraph so no two modules collide.

## Files written

BRIEF.md, check.sh, srcrefs.py, fetch-main-l4.sh (copied), PROGRESS.md, gen-status.py, check-traces.py,
mc97-nouns.l4, mc97-status.l4, mc97-preamble.l4, mc97-c01.l4, mc97-c09.l4, mc97-c29.l4, mc97-saving.l4,
mc97-tests-status.l4, mc97-tests-preamble.l4, mc97-tests-c01.l4, mc97-tests-c09.l4, mc97-tests-c29.l4, mc97-tests-saving.l4,
mc97-seat.l4, mc97-cases-seat.l4, gen-coverage.py, NOTES.md, encoding.json, SOURCE-LICENSE.md.

Latest numbers (2026-10-29, after the team lead's FALSE-vs-NOTHING refinement): check.sh 15 modules, 0 errors, 340 satisfied (= 340 #ASSERT lines in the 7 test/case files), 0 failed, 0 refused, main columns identical (332 on the first full run; later additions: NOTHING functions for chapters 1 and 9, the consideration-clause rule, and the status-table helper with its 5 extra tests); srcrefs 76 src lines 0 problems; traces 19/19; coverage rows 192 (119 first); 30 forks registered (F-NOTCOVERED added).

NEXT: advisor (second call), fix what it finds, re-run check.sh / srcrefs / check-traces / gen-status --verify / gen-coverage after any edit, delete probe-mc97/ (not bin/, which is the GM's), final report (items 1-8).

DONE 2026-10-29: refinement applied (the only JUST FALSE is in 'status table: words are shown for chapter'; 'not a chapter of this text' renamed 'outside the cc. 1-37 the extract names'; reason comment on every not-covered branch). Remaining: final report only; probe-mc97/ to delete.

DONE 2026-10-30: lead's fix list applied. Effect has `not made void by the first unnumbered paragraph` (F-SAVING-VOID; the unused `not covered by the first unnumbered paragraph` removed); 3 assertions in mc97-tests-saving.l4 and 1 in mc97-cases-seat.l4 restated with -- RECONCILED 2026-10-30 comments; F-SAVING-APPERTAIN, F-SAVING-INTHEM, F-SAVING-WHEREBY registered as marginal readings (answers unchanged). check.sh 15 modules, 0/340/0/0 on 98 and on 102; srcrefs --refs and --strict 0 problems; traces 19/19; 34 forks registered. Files changed: mc97-nouns.l4, mc97-saving.l4, mc97-tests-saving.l4, mc97-cases-seat.l4, gen-coverage.py, NOTES.md, encoding.json, PROGRESS.md.


Note added 2026-10-30, after the run: `gen-status.py`, `gen-coverage.py` and `check-traces.py` are named above as they were during the run and are not shipped with this folder; NOTES.md, "Generators and checkers used and not shipped", says what stands in for them.
