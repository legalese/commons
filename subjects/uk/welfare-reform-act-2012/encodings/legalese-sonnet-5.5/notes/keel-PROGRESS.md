# PROGRESS (keel agent, row iaw-wra-k, Welfare Reform Act 2012 (UK))

State on 4 November 2026: finished.
Re-read this file, NOTES.md and PLAN.md after any compaction, not a summary of them.

## Paths

- DEPOSIT = <the lead's scratchpad>/runs/iaw-wra-k/deposit/encodings/legalese-sonnet-5.5
- Raw text = .../runs/iaw-wra-k/inputs/ukpga-2012-5.txt (3959 lines; plain-text rendering by a converter script, not the official text); from DEPOSIT it is ../../../inputs/ukpga-2012-5.txt
- Stable binary = .../scratchpad/bin/l4-stable-98 (1.6.98); main build = .../scratchpad/bin/l4-main-108 (1.6.108)
- Run: `cd DEPOSIT; L4=<stable> L4_MAIN=<main> ./check.sh` and `python3 -I srcrefs.py check --strict ../../../inputs/ukpga-2012-5.txt wra-*.l4`
- zsh note: an unquoted `$var` is not word-split in this shell.

## Files written (all in DEPOSIT)

- wra-core.l4 (271 lines, DECLARE only; its `-- src:` lines were produced by `srcrefs.py quote`, never retyped)
- wra-core-tests.l4 (163 lines, 38 assertions)
- wra-definitions.l4 (imports and a header; defines nothing: no definition falls in line 1)
- PLAN.md, NOTES.md, PROGRESS.md
- (check.sh, fetch-main-l4.sh, srcrefs.py were supplied)

## Result

check.sh target main: 3 modules, 0 errors, 38 satisfied, 0 failed, 0 refused, every module "same" on the main build.
srcrefs --strict: 58 src lines, 15 runs, 29 locators, 0 problems.

## Decisions taken (with the text that licenses each)

- No shared numeric constants in the core: every number the Act states belongs to one provision (s 96(5A) amounts are wra4's; "child under 16" is stated in s 40 for UC and again in the ESA text s 57 inserts, each part encodes its own).
- `Person` is used for every natural person including children (s 40 "child" = under 16, raw line 432, is a rule in wra1, not a type).
- `Benefit` splits JSA and ESA into the two bases the Act itself names (s 33(2)(a), (b)).
- `Provision that reduces an award` lists exactly what Sch 5 para 1(3) (raw 3059-3062) and Sch 6 para 5(4) (raw 3163-3167) name.
- Schedule paragraph numbers are not printed in the raw text; derived by counting cross-headings, consistent with s 43(3)(l), (m) and Sch 5 para 4 (so the "sanction" list is Sch 6 para 5(4), not 6(4)).
- `Authority` limited to actors that carry a power or duty toward the individual and appear in more than one place.
- Seams are by reading, not by regex (the regex found 357 hits, nearly all sections of other Acts).
- wra-definitions.l4 kept as a defines-nothing module so the file name in the brief resolves.

## Housekeeping

- Scratch (a `_scratch/` directory in DEPOSIT and a `work/` directory beside it under runs/iaw-wra-k/, outside DEPOSIT) was used for probes, the quote generator and the PLAN template; both were deleted before the final check.
