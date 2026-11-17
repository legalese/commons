# PROGRESS.md -- ccc26 (Criminal Code (Canada), lines 15171-15768: ss 716 to 736, Part XXIII first half)

Status 2026-11-17: every deliverable is on disk and checked (see "Done" below); nothing is open except the lead's merge.
Read this file, NOTES.md and the text again after any compaction; trust the deposit over this file where they differ.

## Paths

- DEPOSIT folder: `<scratchpad>/runs/dst-ccc26/deposit/encodings/legalese-sonnet-5.5/`
- work folder (not shipped): `.../runs/dst-ccc26/work/` (`units.py` parses the text into coverage units; `src/*.tpl` are the templates; `build.py` expands them).
- L4_BIN `<scratchpad>/bin/l4-main-110`, L4_MAIN `<scratchpad>/bin/l4-main-109`; JL4_LIBRARY_PATH unset.
- Baseline check.sh before any edit: 3 modules (keel's), 0 errors, 0 assertions, both builds the same (`work/check-baseline.log`).

## Method

Layer-1 templates live in `work/src/<module>.l4.tpl`. `work/build.py` expands `@@Q first last label@@` (quote lines `-- src:N | text` copied from the raw text, then `@ref label (src:A-B)`) and `@@R first last label@@` (only the `@ref`), and writes the module into the deposit. Nothing is quoted by hand. Marginal-note headings are folded into the quote run of the provision they head.

## Modules (text order, one tests file each)

| module | sections | tests |
| --- | --- | --- |
| `ccc26-interpretation.l4` | 716 (definitions), 717 to 717.4 (repealed), 729(2), 729.1(2), 732.1(1), 734.8(1) + the shared three-valued helpers (filed under `s 716`) and the period comparator | `ccc26-tests-interpretation.l4` |
| `ccc26-principles.l4` | 718 to 718.21 | `ccc26-tests-principles.l4` |
| `ccc26-punishment.l4` | 718.3, 718.4, 719 | `ccc26-tests-punishment.l4` |
| `ccc26-reports.l4` | 720 to 722.2 | `ccc26-tests-reports.l4` |
| `ccc26-hearing.l4` | 723 to 729.1 | `ccc26-tests-hearing.l4` |
| `ccc26-discharge.l4` | 729.2, 730 | `ccc26-tests-discharge.l4` |
| `ccc26-probation.l4` | 731 to 732.1 | `ccc26-tests-probation.l4` |
| `ccc26-probation-orders.l4` | 732.11 to 733.1 | `ccc26-tests-probation-orders.l4` |
| `ccc26-fines.l4` | 734 to 736 | `ccc26-tests-fines.l4` |
| `ccc26-seat.l4`, `ccc26-cases-seat.l4` | the accused's questions (213) and their cases (506) | (cases) |

## Decisions (each licensed by the section or the brief)

1. Inert: marginal-note headings and the Part title (reason 1, folded into the row of the provision they head); regulation-making and designation machinery: s 721(2), 732.1(8), (9), (12), 734(7), 734.51 (reason 2). Repealed rows (717 to 717.4, 718.3(8), 729(4) and (5), 731(3.1), 732.1(2)(a.1), (2.1), (2.2), 716 "alternative measures") are carried as string constants that quote what the text shows (disposition: repealed or blank in this text).
2. s 734.4 and s 734.5 are NOT machinery: refusal or suspension of a licence bites the offender.
3. `Length of time` has no order in the core. Every comparison of a term with a stated length (s 730(1), 731(1)(b), 732(1), 732.2(5)(e), 736(1)) goes through the stand-in `s 716 the first period is at most the second period` (month and day bounds, NOTHING where the calendar decides); caps stated in hours or months (s 732.1(3)(f)) take a NUMBER in the text's own unit. The wanted comparator is recorded in NEEDS-CORE.md, with the wanted `Party` for the minister of justice of a territory. s 734(5) turns a `Length of time` into days from an anchor date (the date of default).
4. s 734(5): term in default = the lesser of FLOOR((unpaid + costs) / (8 x provincial minimum hourly wage)) and the (b) ceiling; wage and costs are inputs (they point outside the text).
5. s 734.8(2) has no rounding rule in the text: fork line; tests on whole-day cases and one fraction.
6. Seams: `s 734.8 the fine and its penalty` (exactly that name, returns core `Fine`) for ccc27, over a NUMBER `s 734.8(1) the penalty`. Inputs taken: `s 2.2 the individual may act on the victim’s behalf, subject to subsection (2)` and `s 2 victim: the purpose is section 722` (s 722), `s 3.01 the offence counts as one in which violence is used, threatened or attempted` (s 726.21; s 718.3(8) is repealed in this text, so that half of the seam is dead), `s 320.11 the person is an analyst` (s 729.1(2)), `the punishment the offence charged is liable to` (core `Punishment`) for ss 718.2/718.3/730/731/734/735.
7. Every constructor and type is prefixed with the section label; constructors are unique across all enumerations of the part.
8. Three-valued helpers: `s 716 all of the answers`, `s 716 any of the answers` (Kleene logic over MAYBE BOOLEAN; they never turn NOTHING into FALSE).
9. Grant-named functions (may / permitted / power / entitled / authorised) carry a comment `-- gate: if | where | when | upon | only-if | with | none` so that the name-test sweep is a grep. Duties, bars and the provision's own question are not in the sweep.
10. Regulative rules (nullary action constructors under the part's prefix, `WAITUNTIL` in traces, results printed and not asserted): s 720(1), 721(5), 722(2), 722.1, 722.2(1.1), 722.2(5), 732.1(3)(a)(i), 732.1(11) and s 734.7(1) (SHANT). Each has a decision function beside it that carries the assertions.

11. Seat layer: generated by `work/seatgen.py` from the layer-1 signatures; a question is named from the layer-1 function it calls, in the same direction (bars asked as bars). A provision is left out of layer 2 only when its subject is a victim's, a community representative's or a government's own conduct, or an inquiry about victims (s 722(2), (4)-(7), 722.2(1.1), (2)-(4), 725(1.1), 726.3, 734.4(3)(a), (b)); what an official must or may do to, for or about the accused is asked. Cases are the layer-1 assertions whose arguments translate (a MAYBE input becomes a BOOLEAN passed as `JUST x`; a `Length of time` becomes three numbers), with one case per expected value per question, up to three, plus one with a "less a day" length where a layer-1 assertion has one.
12. Name-test sweep of 2026-11-12: one flip, `s 722(6)(b)` (F163); 43 "may" functions with a where, when, upon, on, after, with, during or in gate are listed in the fork register (S1 to S43) and keep JUST FALSE; no "entitled", "permitted" or "authorised" function name exists.

## Done (2026-11-17)

- Baseline `check.sh` at the second resume: 15 modules, 634 satisfied, 0 errors, same on both builds. Final: 23 modules, 1550 satisfied, 0 failed, 0 refused, same on both builds (output in NOTES.md).
- Modules and tests (satisfied of written): interpretation 89/89, principles 90/90, punishment 89/89, reports 116/116, hearing 178/178, discharge 76/76, probation 133/133, probation-orders 115/115, fines 158/158; seat cases 506/506.
- `srcrefs.py check --refs` and `--strict` over every `ccc26-*.l4` file: 0 problems; `work/lint.py`: 0 problems.
- #TRACE comparison, 1.6.110 against 1.6.109, `JL4_LIBRARY_PATH` unset: reports 128, probation 137, fines 160 `Evaluation` blocks (assertions included), identical.
- Second pass: seat audit (213 questions read, 0 retitled, 13 read and left) and the name-test sweep (1 flip, 43 listed); NOTES.md is generated by `work/gen_notes.py` from `work/notes/data_*.py`; NEEDS-CORE.md written.
- Helpers (not shipped): `work/build.py`, `work/lint.py`, `work/t.sh`, `work/mktests.py` + `work/tests/*.py`, `work/seatgen.py`, `work/gen_notes.py`, `work/notes/data_*.py`.
