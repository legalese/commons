# PROGRESS (keel agent br-g0, Lei 6.404/1976)

Kept current as I go.
If my context is compacted, re-read this file, `NOTES.md` and the text, not a summary.

## State (2026-10-22)

- Written and green: `br-core.l4`, `br-core-tests-prazo.l4`, `br-core-tests-vocabulario.l4`, `NOTES.md` (the eight required headings).
- `check.sh` with `L4_TARGET=unstable`: 3 modules, 0 errors, 68 satisfied, 0 failed, 0 refused.
- `srcrefs.py check --refs`: 40 src lines, 10 runs, 40 locators, 0 problems.
- Each module was imported by a three-line throwaway file, run, and the files deleted.
- Not done and not owed: the coverage table has zero rows because the keel's range is empty.

## What the last verification pass changed (so a reader can tell the file is not the first draft)

- The quote for `a instituição financeira` pointed at line 262, which is Art. 39; the article named was Art. 27, at line 190.
  The `srcrefs` gate does not compare the article in the label with the heading above the quoted line, so it passed.
  Fixed in `br-core.l4`; NOTES instruction 12 tells the pieces to check their own labels.
- Art. 140, § 2º (conselheiro independente) was cited at line 1266, which is struck; the live text is line 1267.
- "Investimento relevante" was marked scoped to its own article through Art. 248, § 1º (line 2201); that paragraph belongs to Art. 248 and uses the phrase for itself.
- The claim that all 58 dialect probes fail was wrong as stated: 56 exit non-zero from `l4 check`, and probes 49 and 50 exit 0 with a `Module not found` warning.
  The same holds for any misspelt `IMPORT`; `check.sh` counts it as errors, `l4 check` does not.
- A claim that Art. 239 states a percentage threshold was removed from fork F5 (it says "a minoria" and defines nothing).
- A vote-count record (`Votação em assembleia`), licensed by Arts. 125, 129 and 136, was added to the core, with tests.

## Findings about the text that every piece will trip on

1. `⟦STRUCK: ...⟧` spans can run over several lines (501 open, 501 close, 67 multi-line); a filter that drops only lines beginning `⟦STRUCK` shows their insides as live text.
2. Eight article numbers have no live opener: 32, 33, 60, 181, 185, 241, 242, 254.
3. Two SECTION-INDEX rows point into struck spans: Art. 289 at line 2452 and Art. 294 at line 2516.

## Left

- Final advisor review, then the final report.
