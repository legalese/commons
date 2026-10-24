# PROGRESS (the encoder's memory across compactions)

Row `legalese-sonnet-5.5`, subject `us/ca` interpretation cluster, file prefix `usca`.
Re-read after a compaction: this file, `NOTES.md`, the six statute `.txt` files in INPUTS_DIR, and `BRIEF.md`.

## Fixed facts

- Target: `unstable` (the brief requires `REFUSE` and `@lang en`, which `main` rejects). Run `L4_TARGET=unstable L4=<L4_BIN> ./check.sh`; the default target of this copy of `check.sh` is `unstable`.
- L4_BIN `/Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-9afd0288/bin/l4`, sha256 `2d912dd2a61ba36b3fb8c1e02dcbd445ba1143c3b8ecb931462c01050cd607d7`, `l4 --version` prints `dev`.
- `JL4_LIBRARY_PATH` stays UNSET.
- The `.txt` files are a converter-made rendering, not the official text; nothing here was checked against the official text.

## Status

- [x] Coverage plan: 159 sections, every one has a row in the coverage table of `NOTES.md`.
- [x] `usca-interpretation-time.l4` (prelude + daydate only), `usca-holidays.l4`, `usca-operation-of-statutes.l4`, `usca-general-provisions.l4`: all compile with no diagnostics; `srcrefs.py check --refs` (the encoding skill's tool, /Users/mengwong/src/legalese/l4-ide/skills/encoding-a-subject/assets/srcrefs.py) reports 0 problems on each.
- [x] Tests: `test-usca-time.l4`, `test-usca-rules.l4`, `test-usca-holidays.l4`, `test-usca-operation.l4`, `test-usca-general.l4`, `test-usca-worked.l4`: all assertions satisfied (counts in the check output in `NOTES.md`).
- [x] `tests-red.l4`: 8 assertions meant to fail; counted in `check.sh` (`expected_failed`) and `encoding.json` (`expected_red`).
- [x] Answer table: 63 evaluations of the worked cases, 0 differences from the values written down before the first run.
- [x] `check.sh`, `encoding.json`, `SOURCE-LICENSE.md`, `BRIEF.md`, `NOTES.md`.
- [x] Mutation check of the four modules (scratch script, not shipped): 366 mutants, 357 killed, 9 survivors, all read as equivalent; result in `NOTES.md`.
- [x] Final `check.sh` (2026-10-22, target `unstable`, exit 0): 11 modules, 8 errors, 1696 assertions satisfied, 8 failed (all in `tests-red.l4`, expected 8), 0 refused. Verbatim in `NOTES.md`.
- [ ] Not run: the skill's independent test pass (step 8; the brief allowed no subagents) and any run against `main`.

## Peeked

Nothing opened from the forbidden list.
Names of files and directories only, none opened: one `ls` of the scratchpad root early in the task, and one `ls` of the scratchpad root and of `interp-wave/` near the end (these listed other rows' directory names and loose files such as `BRIEF.template.md`, none of which was read).
Writes outside the row: a stray directory `scratchpad/us-ca-probe`, made outside DEPOSIT by mistake and removed with `rmdir`; a copy `scratchpad/ops-before.l4`, made outside DEPOSIT for a diff and removed; a stray output file `deposit/check-run-1.txt` in the DEPOSIT root, removed.
