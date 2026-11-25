# Brief: the 2023 Merger Guidelines (U.S. DOJ and FTC)

Written 2026-11-25 by session Commons for one builder session.
The common rules for both DOJ/FTC guideline encodings are in a common brief (`BRIEF-COMMON.md`) that session Commons wrote outside this repository.
This file is this row's part of the brief, with the common rules that shaped the work restated briefly.

## Target

`main`: the stable `l4` 1.6.112.
`main` has no `REFUSE`, so an answer the text does not give is `NOTHING` from a `MAYBE`.
Run with the unstable build as well, and compare the two with `check.sh`.

## The question

Given the facts of a merger, what do the 2023 Merger Guidelines say the Agencies presume, infer, examine, credit or accept?
The Guidelines are AGENCY ENFORCEMENT POLICY, NOT LAW: they say they create no independent rights or obligations.
No result may be named as lawful or unlawful.

## Scope

- Guideline 1: HHI; the change in HHI (2ab); more than 1,800; more than 100; over 30 percent; both limbs of the table; rebuttable, with stronger evidence needed the higher the metrics. Fixtures: 2,000, 1,667 and 200 from footnotes 13 and 14. Footnote 15's history: 1,000, 1,800 and 100, with concentrated meaning over 1,000.
- Guidelines 2 to 6 as their stated tests; indicator lists taken from the caller and reported, never weighed.
- Guidelines 7 to 11 as settings.
- Section 3: failing firm requirements A, B and C with footnote 62 (above liquidation value is reasonable; a rejected reasonable offer bars the claim); the failing division with footnote 64's two conditions; entry (timely, likely, sufficient; the repositioning exclusions); efficiencies.
- Section 4: the HMT, the five percent SSNIP (footnote 84: not a threshold of harm), critical loss, shares. The evidence discussion goes in the coverage table as inert.
- Forks to record at least: the merged firm's share; shares that do not sum to 100; "creates or further consolidates" read as a post-merger HHI over 1,800; the rounding of 1,667.

## Sources

- The deposited text, `../../registers/source-bundle/2023-merger-guidelines.txt` (28,710 words, with `[pdf page N of 51]` markers), and its `.meta.json`.
- Nothing is to be fetched from the web. A fact the text does not give goes into NOTES.md as an open question.
- Withdrawn and superseded guidelines go into NOTES.md, not into the encoding, each marked as read at source or only reported: the 2000 Collaboration Guidelines (withdrawn 11 December 2024, reported); the 2020 Vertical Merger Guidelines (FTC approval withdrawn 15 September 2021, reported; a December 2023 DOJ notice reported as ambiguous); the 2023 text's own "consolidates, revises, and replaces" (read at source); the memoranda of 18 February 2025 keeping the 2023 Guidelines in force (reported) and the DOJ index page listing them on 2026-11-25 (read by the parent session).

## Deliverables

In `encodings/legalese-2026-11/`: a nouns module, rule modules in the Guidelines' order, test modules from the text with both sides of every threshold, a `-red` module of positive controls counted in `expected_red`, `NOTES.md` (status, checks on both builds, scope, coverage table, fork register, open questions, withdrawn guidelines, the label), `encoding.json`, `check.sh`, `fetch-main-l4.sh` and this file.

## Rules that matter

- Work only in the worktree; commit locally; never push or open a pull request.
- Every commit ends with the `Co-Authored-By:` and `Claude-Session: Commons (3f25eec7-e29b-4460-907f-7016392f6838)` trailers.
- Nouns first; one provision, one recognisable place in the L4; inputs as `GIVEN` records; impossible input gives `NOTHING`.
- Percentages in percent points; HHI on the 0 to 10,000 scale.
- A failing assertion is a finding, not something to fix by editing the expected value.
- Quote only short passages of the Guidelines; encode, do not reproduce.
- Run `check.sh` after every unit and report the counts it prints.
