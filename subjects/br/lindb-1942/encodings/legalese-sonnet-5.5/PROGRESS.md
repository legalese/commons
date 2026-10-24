# PROGRESS: Decreto-Lei 4.657/1942 (LINDB), row legalese-sonnet-5.5

Re-read this file, `NOTES.md` and `../../registers/source-bundle/lindb-1942.pt.txt` after any compaction, not a summary of them.

Paths (all absolute):

- `BR` = `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/f0f88090-d3bb-4c2f-a86e-663d7b9acf93/scratchpad/interp-wave/br`
- `INPUTS` = `$BR/inputs`; raw text `$INPUTS/lindb-1942.pt.txt` (113 lines)
- `ENC` = `$BR/deposit/encodings/legalese-sonnet-5.5` (the only place I write)
- `L4_BIN` = `/Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-9afd0288/bin/l4`, sha256 `2d912dd2a61ba36b3fb8c1e02dcbd445ba1143c3b8ecb931462c01050cd607d7` (checked 2026-10-21)

## What the text is

The whole Decreto-Lei: art. 1 to 6 (life of a law), 7 to 19 (private international law, consular acts), 20 to 30 (public-law decision making, Lei 13.655/2018).
It answers must-encode item 1 (art. 1 caput, §1, §3, §4) and item 5 (art. 2 §1 to §3, art. 6).
It is SILENT on items 2 (general counting), 3 (rest days), 4 (service), 6 (meanings of day/week/month/year) and on subordinate legislation.
The answer for a silent item is a named REFUSE and a coverage row saying "the Act is silent on this", never a borrowed convention.

## Target and toolchain

- Target: `unstable`, because the brief requires `@lang en`, `REFUSE`, `#ASSERT REFUSED` and `YMD`, which `main` rejects (dialects.md probes 01, 02, 03, 05).
- Run: `L4_TARGET=unstable L4=$L4_BIN ./check.sh` (never tries fetch-main-l4.sh).
- Leave `JL4_LIBRARY_PATH` unset.
- Quotation: only through `quote-lines.py` (reads the raw file, strips Planalto's editorial notes), checked by `srcrefs.py check --refs` and `quote-lines.py check`.

## Decisions taken (with the text that licenses each)

1. Point "N days after D" is D + N (the Nth day after D, D not counted). Licence: art. 1 caput `quarenta e cinco dias depois de oficialmente publicada`. The text does not say it; it is the plain denotation of `depois de`. Fork register F1.
2. "N months after D" and "N years after D": calendar reading, same day number, only where the target month has it; otherwise REFUSE. Licence: art. 1 §1 (`três meses depois`), art. 7 §6 (`1 (um) ano da data da sentença`). Not defined by the text. daydate's clamp is NOT used. Fork F3.
3. "Counted from D" (art. 19 par. unico `contados da data da publicação`): whether D counts is open; membership answers only where every reading agrees, REFUSE on the two boundary days. Fork F2.
4. Weeks: the text never uses the unit: REFUSE.
5. Rest days, holidays, recess: the text has no rule: REFUSE (a rest-day LIST OF DATE input is taken and ignored).
6. Deemed service: no rule: REFUSE.
7. Moment of binding: art. 1 gives a day, not a moment: REFUSE.
8. Subordinate legislation: art. 1 says `a lei`: REFUSE.
9. Art. 1 caput `Salvo disposição contrária`: an enactment's own commencement provision (fixed day, or "to be fixed later") displaces the 45 days.
10. Art. 1 §3 restart: only a corrective republication strictly before the commencement day restarts the count; one after is a new law (§4); one on the commencement day itself is REFUSE (moment unknown).

## Files written (all in `ENC`)

- Modules: `br-interpretation-time.l4`, `br-lindb-life-of-a-law.l4`, `br-lindb-conflict-of-laws.l4`, `br-lindb-public-law.l4`.
- Tests: `tests-time.l4` (180), `tests-life-of-a-law.l4` (73), `tests-conflict-of-laws.l4` (141), `tests-public-law.l4` (119), `tests-rejected-readings.l4` (8, expected red).
- Tools and records: `check.sh` (expected_failed 8 for the rejected-readings file), `srcrefs.py`, `quote-lines.py`, `BRIEF.md`, `NOTES.md`, `PROGRESS.md`, `encoding.json`, `SOURCE-LICENSE.md`.
- `_probe/` has been deleted.

## Working method (read after any compaction)

- Quotes are never typed: put a marker line `-- @@N@@` or `-- @@N-M@@` in a .l4 file and run `python3 -I quote-lines.py expand ../../../../../registers/source-bundle/lindb-1942.pt.txt FILE`.
- Strict locators: each article's quote run must be followed by ALL of that article's rules before the next quote run (nearest run above is what a later @ref is checked against).
- GIVEN parameters of a mixfix rule must be listed in the order the arguments appear in the pattern; one GIVEN per line when a LIST OF type is involved.
- A trailing mixfix keyword after the last argument does not parse: use a prefix name instead.
- Constructor names must not collide with field names or other rules (`day`).
- `#ASSERT REFUSED e` passes for ANY refusal; add BECAUSE where the reason matters.
- check.sh counts one satisfied per #ASSERT line (180 asserts -> 180 satisfied, checked).

## Status (2026-10-21, final pass)

- [x] all modules and tests written; `L4_TARGET=unstable L4=$L4_BIN ./check.sh`: 513 satisfied, 8 failed by design, 0 refused, 0 other errors, exit 0
- [x] every `#ASSERT REFUSED` carries BECAUSE
- [x] `srcrefs.py check --strict` over all `*.l4`: 0 problems; `quote-lines.py check`: 0 problems
- [x] NOTES.md (coverage table, fork register, answer table, check.sh output, open questions, the two disclosed test edits), encoding.json, SOURCE-LICENSE.md
- [x] `_probe/` deleted
- [ ] last advisor call, then the 8-point final report (peeked: nothing)
