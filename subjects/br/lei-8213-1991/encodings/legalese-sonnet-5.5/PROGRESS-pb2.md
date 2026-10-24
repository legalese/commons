# PROGRESS (piece pb2, Lei 8.213/1991, lines 455-780)

State at the time of writing: all seven layer-1 modules, their seven test files, the seat and its cases are written and pass; `NOTES.md` is assembled from fragments. Re-read this file, `NOTES.md` and the text after any compaction, not a summary.

## Sections done

| module | articles | state |
| --- | --- | --- |
| `pb2-salario-de-beneficio.l4` | 28, 29, 29-A, 29-B, 29-C, 31, 32 (30 repealed, no rule) | done; tests `pb2-tests-salario-de-beneficio.l4` 137 satisfied |
| `pb2-renda-mensal.l4` | 33 to 40 | done; tests 108 satisfied |
| `pb2-reajustamento.l4` | 41-A (41 repealed, no rule) | done; tests 34 satisfied |
| `pb2-aposentadoria-por-invalidez.l4` | 42 to 47 | done; tests 82 satisfied |
| `pb2-aposentadoria-por-idade.l4` | 48 to 51 | done; tests 84 satisfied |
| `pb2-aposentadoria-por-tempo.l4` | 52 to 56 | done; tests 65 satisfied |
| `pb2-aposentadoria-especial.l4` | 57, 58 | done; tests 55 satisfied |
| `pb2-seat.l4` | all of the above, 98 questions | done |
| `pb2-cases-seat.l4` | one case at least per question | done; 201 satisfied, plus a `#TRACE` |

## Next

Nothing left to write. Remaining: capture the final `check.sh` output into `NOTES.md` (it is assembled by `inputs/_work/build_notes.py` from `inputs/_work/notes/*.md` and `checkout.txt`), and send the final report.

## Decisions taken (with the provision that licenses each)

- Layer-1 rules take the salário-de-benefício as the keel's NUMBER input `o salário-de-benefício em reais (art. 29)`, so the aposentadoria rules (arts. 44, 50, 53, 56, 57 § 1) do not thread the list of salários; the art. 29 rules compute it from the list, and the seat wires the two. (arts. 29, 44, 50, 53, 56, 57)
- Arts. 29-C and 34 take the results of arts. 52 and 29-A § 5 as BOOLEAN inputs that the seat supplies by calling those rules (they could be imported, but the modules stay independent).
- The seat never asks a list: the mean of the highest 80% is a number, the INPC is one accumulated variation, the last 12 salários are 12 numbers (art. 29 § 10), and two numbers stand for two concomitant activities (art. 32).
- Art. 33 has two rules: the floor and the cap (called by arts. 44, 50, 53, 56, 57 § 1, which say "observado ... o art. 33") and the same with the article's own condition.
- A row of the coverage table whose note points to a fork is `fork`: 24 rows, 25 forks, F-PB2-01 to F-PB2-25 (see NOTES.md).
- Art. 38 (a duty of the Previdência Social) is a regulative rule over `Parte`, exercised with `#TRACE`; every other duty with a time limit is a BOOLEAN over dates, using the core's `o dia em que termina ... contado de ...`.
- Inert rows (12): the nine headings, art. 38-A caput and § 1º, art. 38-B § 5º.

## Files written

All in `encodings/legalese-sonnet-5.5/`: the seven `pb2-<module>.l4`, the seven `pb2-tests-<module>.l4`, `pb2-seat.l4`, `pb2-cases-seat.l4`, `NOTES.md`, `PROGRESS.md`.
Scratch (not deliverable), under `inputs/_work/`: `expand.py`, `chk.sh`, `run4.sh`, `live.py`, `gen_cases.py`, `build_notes.py`, `src/*.l4.src` (the modules with `@@Q` quotation markers), `notes/*.md` (the fragments of NOTES.md), `seat/part*.l4`, `checkout.txt`.
