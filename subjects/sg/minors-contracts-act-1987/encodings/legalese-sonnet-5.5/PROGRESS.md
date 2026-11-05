# PROGRESS (Minors' Contracts Act 1987, Singapore; main row; single encoder Sonnet 5.5)

Updated as I go; after any compaction re-read this file, NOTES.md and the text (INPUTS_DIR/MCA1987.txt), not a summary.

## Paths
- DEPOSIT = .../runs/iaw-mca/deposit ; encoding folder = DEPOSIT/encodings/legalese-sonnet-5.5
- INPUTS_DIR = .../runs/iaw-mca/inputs ; source = INPUTS_DIR/MCA1987.txt (154 lines, 663 words)
- L4_BIN = scratchpad/bin/l4-main-109 (1.6.109, sha256 eeb12f1e...); L4_MAIN = scratchpad/bin/l4-main-108
- scratch probes live in DEPOSIT/probe-scratch (DELETE before the final report)

## Plan (modules)
- mca-nouns.l4        the nouns: contract record, band s 4 puts a contract in, effects of the IRA 1874, defined-term record, party/property/transferee types
- mca-act.l4          ss 1-4 in text order, one section heading per section (s 4 last, but ss 1-3 read it); regulative MAY for s 3(1)
- mca-reading.l4      Interpretation Act reuse ("he" includes females; "person" includes company etc.), via the copied sgia-p1-definitions.l4
- mca-cases.l4        layer-1 tests (both sides of every boundary, every branch)
- mca-seat.l4         layer 2: the seat's questions (@export, @desc, grouped under section headings)
- mca-cases-seat.l4   layer 2: worked cases, one per question at least
- sgia-p1-definitions.l4  COPIED UNCHANGED (blob ca5e2607..., header added), keeps its own name (brief line 109 over line 167)
- coverage.py, NOTES.md, encoding.json, SOURCE-LICENSE.md, BRIEF.md (copy), check.sh, srcrefs.py, fetch-main-l4.sh

## Decisions taken (with the text that licenses each)
- Naming: each function is named for what the section DOES (e.g. "s 2 the guarantee is saved from unenforceability on that ground alone"), so a where-fail JUST FALSE never reads as a claim about the underlying state. (ruling of 2026-11-05, "where" unmet = JUST FALSE)
- s 4 is a gate on ss 1-3: band by date of making (after 9 Apr 1987 and before 12 Nov 1993 is the band); in band with CLA s 5 saving false: shut (JUST FALSE for the section); saving true (the exception is met): the section's own words operate, gate JUST TRUE and bar question JUST FALSE (QA, reversed from the first draft); saving unknown: NOTHING.
- The dates 9 April 1987 and 12 November 1993 are fixed in the text's own words: outside them JUST FALSE at all four sites (s 1 reaches, s 2(a), s 3(1)(a), s 4 bar); s 1's "made by a minor" limb stays a scope limit (NOTHING). Fork F2 (rewritten in the fix round).
- s 2(b)/s 3(1)(b) read the record's minority fact first: no minor -> JUST FALSE; minor and reason unknown -> NOTHING. Fork F1.
- "because he was a minor" scope over "(or he repudiates ...)": reading (i), both limbs tied to minority (s 2 tail "for that reason alone"). Fork F1.
- Age of majority is NOT in the sources: "minor" is a fact input. No number from memory.
- No unstable second encoding unless a shape appears (current view: none; only plain date comparisons).

## Status (fix round done)
- [x] layer 1 and layer 2 complete; fix round: dates agree at the four sites (F2), minority fact read in s 2(b)/s 3(1)(b) (F1), s 3(2) F5 cases, F11, gaps and findings 17-21 in NOTES
- [x] check.sh (final): 7 modules, 354 satisfied (251 + 103), 0 failed, 0 errors, 0 refused; main columns same (1.6.108); 4 traces identical on 108 and 109
- [x] srcrefs --refs and --strict: 0 problems; coverage.py: 37 primary + 37 sub rows, 0 problems; --verify-notes: 70 refs, 0 problems
- [x] scratch directories deleted
