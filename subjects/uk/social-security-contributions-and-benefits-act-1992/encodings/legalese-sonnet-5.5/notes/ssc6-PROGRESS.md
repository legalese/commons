# PROGRESS -- ssc6 (ss 151-171ZT, lines 3095-3717 of ukpga-1992-4.txt)

Working log for part agent `ssc6` (run `iaw-ssc6`).
After a compaction: re-read this file, `NOTES.md` and the text, not the summary.

## Method

- `work/units.py` (not shipped) splits lines 3095-3717 into 585 units (headings, sections, subsections, paragraphs, sub-paragraphs, defined terms, dots lines, omission lines) and asserts that every one of the 623 lines is in exactly one unit.
- `work/build.py` expands `work/src/*.l4` into this folder; its `{{Q a b | CITATION}}` directive copies the quote lines from the raw file with `srcrefs.py quote` and writes the `@ref` with the matching locator, so no quotation is retyped.
- The dispositions of the 585 units are in `work/disp.tsv`; `work/coverage.py` joins them with the units and writes the coverage table into `NOTES.md`.

## Module plan (flat folder, `ssc6-` prefix, each starts `IMPORT prelude`, `IMPORT daydate`, ``IMPORT `ssc-core` ``; the exception is `ssc6-duties.l4`, which imports only `prelude`)

| file | holds | imports (of mine) |
| --- | --- | --- |
| `ssc6-smp.l4` | Part XII, ss 164-171 | none |
| `ssc6-ssp.l4` | Part XI, ss 151-163 | `ssc6-smp` (s 153(12) points at ss 165(1) and 171(1)) |
| `ssc6-spp.l4` | Part 12ZA, ss 171ZA-171ZK | none (employee/employer shapes are copied, not imported) |
| `ssc6-sap.l4` | Part 12ZB, ss 171ZL-171ZT | none |
| `ssc6-duties.l4` | the four payment duties as regulative rules (ss 151(1), 164(3), 171ZD(1), 171ZM(1)) | none |
| `ssc6-tests-*.l4` | one per module | the module under test |
| `ssc6-seat.l4`, `ssc6-cases-seat.l4` | layer 2 | all four modules |

The rate in s 157(1) reaches ss 166(3) and 171ZN(2G) as a `GIVEN` named for s 157(1), so that SMP and SAP need not import SSP (SSP imports SMP, and a cycle is impossible).

## Status

(updated after each step)

| step | state |
| --- | --- |
| units.py, build.py | done |
| ssc6-smp.l4 + tests | done: 205 assertions green; includes `s 164 the relevant week` (seam S30) |
| ssc6-ssp.l4 + tests | done: 194 assertions green |
| ssc6-spp.l4 + tests | done: 207 assertions green |
| ssc6-sap.l4 + tests | done: 219 assertions green |
| ssc6-duties.l4 | done: four DEONTIC rules, eight traces read by hand on stable and main; decision-function twins are the entitlement rules of each Part |
| ssc6-seat.l4 + ssc6-cases-seat.l4 | done: 42 `@export` questions, 115 cases satisfied; a two-value mutation of the cases gave 2 failed |
| coverage table in NOTES.md | done: 585 of 585 units (288 encoded, 20 fork, 63 inert reason 1, 191 inert reason 2, 23 repealed or blank) |
| NOTES.md sections | done (assembled from `work/notes/*.md` by `work/assemble.py`) |
| NEEDS-CORE.md | done: one item (`Labour` field) |
| final gates (check.sh, srcrefs --refs and --strict, placement grep, grep for absolute paths) | see NOTES.md, "What `check.sh` prints" |

## Decisions taken (assumed, not ruled), with the text that licenses each

(the fork register in `NOTES.md` is the durable copy)

- Sources for the four modules are `work/src/*.l4` (directives `{{Q}}`, `{{R}}`, `{{QQ}}`), expanded by `work/build.py` into this folder. Edit the source, never the expanded file.
- Seams: S29 and S30 are returned as `MAYBE Period` (the PLAN says `Period`): a week that regulations prescribe differently, or a duration above 52 weeks, answers NOTHING. Recorded in `NOTES.md`, Seams.
- `s 164 the relevant week` is not a defined term in s 164 (the text says "the week immediately preceding the 14th week before the expected week of confinement", src:3245); it is added in `ssc6-smp.l4` because S30 asks for it by that name.
- The duties module holds four regulative rules with no `WITHIN` and no `LEST`: the text gives no deadline and no consequence of non-payment (NOTES.md, finding 8).
  The stable binary does not compare the amount named in a `MUST` with the payload of the event, so the amount is asserted in the decision functions and the traces are read by hand (NOTES.md, "What the stable binary does not accept").
- The seat asks "Do regulations prescribe otherwise in your case?" wherever the Act says "except as may be prescribed"; the default is the Act alone, and "yes" returns `NOTHING`.
- Where PLAN.md and the brief differ (seams S29, S30, S32 are `MAYBE`), the brief governs; NOTES.md, Seams, says so.
- To change a module: edit `work/src/NAME.l4`, run `python3 -I build.py NAME.l4` from `work/`, then re-run `check.sh` and `srcrefs.py check --refs ... --strict`.
  `ssc6-seat.l4`, the four test files and `ssc6-cases-seat.l4` are not built from a source: edit them directly.
