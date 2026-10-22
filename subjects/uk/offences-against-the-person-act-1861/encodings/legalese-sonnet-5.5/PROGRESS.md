# PROGRESS (run porridge-uk-oapa-b, Sonnet 5.5 solo)

Re-read this, NOTES.md and the text after any compaction, not your summary.

## Orientation done (2026-10-22)
- Read: BRIEF.md, inputs/ENCODING-GUIDE.md, inputs/COMMONS-CLAUDE.md, inputs/SOURCES.md, the Act text (125 lines, one line per section), both SKILL.md files, dialects.md, source-locators.md, canon-deposit.md, drafting-patterns.md, gotchas.md, source-patterns index and entries 5.7, 7.1-7.2, 8.4-8.5, 9.1, 11.3, 11.5.
- l4 = 1.6.98 (main, 7689b0d), sha256 verified 82ea44ad...; JL4_LIBRARY_PATH unset.
- Stable binary confirmed: enums with HAS fields, LIST equality of such values, two records sharing a field name, WHERE-built records, `@export` with `@desc` on GIVEN all work.
- Pre-deposited in the folder: check.sh, srcrefs.py (same as the skill's assets).
- Probe files are named zz-probe*.l4 in this folder; DELETE before finishing.

## Text facts (checked against ukpga-Vict-24-25-100.txt)
- Operative sections with text: 4, 5, 9, 10, 16, 17, 18, 20-40, 42, 44, 45, 47, 57-60, 64, 65, 68, 76, 78.
- Blank (". . . .") sections: 1, 2, 6, 7, 11, 19, 41, 43 (title survives), 46, 48-50, 52-54, 56, 61, 66, 69-74, 77, 79.
- Numbers absent from the text: 3, 8, 12-15, 51, 55, 62, 63, 67, 75.
- No Schedules or tables.
- Penalties: many terms hidden by ". . ." (e.g. s 20, 24, 26, 27, 31, 47, 59 "penal servitude . . ."). Do not import.

## Plan
Layer 1 (flat folder): oapa-nouns, oapa-homicide (4,5,9,10), oapa-threats (16), oapa-danger-bodily-harm (17-25), oapa-danger-neglect-explosives (26-31), oapa-danger-railways-vehicles (32-35), oapa-assaults (36-47), oapa-bigamy (57), oapa-abortion-birth (58-61), oapa-gunpowder (64-65), oapa-other (66-79).
Layer 2: oapa-seat.l4, oapa-cases-seat.l4. Plus per-module tests (oapa-tests-*.l4 or cases within).

## Method notes (keep)
- Quotes: write a marker line `--@@ N M` in a .l4 file, then `python3 -I expand-quotes.py RAW file.l4` expands it into `-- src:` lines copied from the raw text (expand-quotes.py lives in this folder; keep or delete at the end, say which in NOTES).
- RAW = ../../../../../registers/source-bundle/ukpga-Vict-24-25-100.txt (relative to this folder). sha256 63920ce0... matches the meta file.
- Gate: `python3 -I srcrefs.py check --refs --strict $RAW file.l4` (strict passes on every module so far).
- check.sh was extended with warnings + written columns (written must equal satisfied+failed+refused).
- Positive control done (wrong assertions fail with "assertion failed").
- Stable binary facts probed: transitive imports work; diamond/duplicate imports fine; inert strings and `...`/`..` work; positional patterns `WHEN ctor x THEN` (NOT `WITH`) for constructor fields; CONCAT/TOSTRING work; zero-input `GIVETH A MAYBE BOOLEAN` rule is accepted with @export.
- Test files are named oapa-tests-<group>.l4; OF with ruler comment; every expected value hand-decided from the text.
- Naming: every layer-1 rule starts `s N: ...`; fact records `Conduct under section N`; per section: offence rule, `what the text calls the offence` (Classification), `the sentences the text states` (LIST OF Sentence), `how the text says the offence is tried` only where the text says (16, 39, 40, 42, 47).

## Status (update after every module)
DONE (2026-10-22). Layer 1 (12 modules + 11 test files), layer 2 (oapa-seat.l4, 55 @export questions; oapa-cases-seat.l4, 403 assertions), NOTES.md, encoding.json, SOURCE-LICENSE.md, BRIEF.md copy.
Final gates: check.sh unfiltered (L4_TARGET is a no-op): 25 modules, errors 0, warnings 0, written 933, satisfied 933, failed 0, refused 0. Strict srcrefs over all .l4 files: 0 problems. No zz-* or marker lines left.
The generators (gen-seat.py, gen-cases.py, seat-header.l4, expand-quotes.py, gen-notes.py, the check output) lived in the run's scratch folder, outside the deposit and not deposited; they were first written in the run folder shared by all the agents and moved at the end.
Files written in this folder: the 25 .l4 files listed in encoding.json (modules + tests), check.sh (extended), srcrefs.py (unchanged), NOTES.md, PROGRESS.md, encoding.json, SOURCE-LICENSE.md, BRIEF.md.
Decisions and the section that licenses each are in NOTES.md (fork register 4a ... U2).
Forks recorded so far (to go in NOTES fork register): s26 result-clause scope; s31 "whereby may" reading; s58 limb overlap (limb two says "any woman"); s57 timing of void declaration; s36 knowledge qualifier; s34 "wilful" scope; s5 manslaughter / ss1-2 murder not defined; s25 jury power; s18 four combos; s20 vs s18 verbs; s16 intent about fear; s42 heading says 5 l. but text says 200 pounds; s38 words missing ("shall assault any person" begins with ". . ."); s39 two limbs; s40 "unlawfully" first limb only; s44 justices' findings are inputs; s45 three alternatives; s47 elements; s64 felony derived from table; s65 justice's reasonable-cause judgment is an input and the powers borrowed from the 1860 Act are not encoded; s68 indictable derived or asked; s78 named input.
