# PROGRESS: piece pb3 (Lei 8.213/1991: arts. 59 to 80 and arts. 125 to 156)

Status at last update: layer 1 (seven modules and their tests), layer 2 (`pb3-seat.l4`, 152 questions, and `pb3-cases-seat.l4`, 449 assertions) and NOTES.md are written; `check.sh` prints 0 errors, 1164 assertions satisfied, 0 failed, 0 refused over 17 files; `srcrefs.py check --refs` reports 0 problems.
The advisor's review was taken (one seat prompt that asked the wrong date, three seat helper names that were too generic, and the generic constructor and field names were fixed and re-run), the throwaway scratch is deleted, and `check.sh` and `srcrefs.py` were re-run on the scratch-free folder with the same output as in NOTES.md.
Nothing is left except the final report; the lead writes `encoding.json` and `SOURCE-LICENSE.md` when it merges.

## Where the working files were

- The L4 files in this folder are the deliverable.
- The build material was in the session scratchpad, outside the deposit (templates `*.l4.in` with `@@Q a-b` quote macros, the generators of the seat and its cases, the data files behind the tables of NOTES.md, and probe copies of modules).
  It has been deleted: NOTES.md is now the master of its tables, and the L4 files are edited directly (the quotation lines are copies of the source and are checked by `srcrefs.py`).

## Plan (modules, in text order)

| module | provisions | status |
| --- | --- | --- |
| pb3-auxilio-doenca.l4 | arts. 59 to 63 (art. 64 is repealed) | done, tested in pb3-tests-auxilio-doenca.l4 |
| pb3-salario-familia.l4 | arts. 65 to 70 | done, tested in pb3-tests-salario-familia.l4 |
| pb3-salario-maternidade.l4 | arts. 71 to 73-A | done, tested in pb3-tests-salario-maternidade.l4 |
| pb3-pensao-por-morte.l4 | arts. 74 to 78 (art. 79 is repealed) | done, tested in pb3-tests-pensao-por-morte.l4 |
| pb3-auxilio-reclusao.l4 | art. 80 | done, tested in pb3-tests-auxilio-reclusao.l4 |
| pb3-recursos-e-acoes.l4 | arts. 125 to 133 | done, tested in pb3-tests-recursos-e-acoes.l4 |
| pb3-disposicoes-finais.l4 | arts. 134 to 156 | done, tested in pb3-tests-disposicoes-finais.l4 |
| pb3-seat.l4, pb3-cases-seat.l4 | layer 2 | done |

## Decisions taken (with the section that licenses each)

Forks F-P3-1 to F-P3-32 are in the fork register of NOTES.md. The conventions:
- Rule names begin with the citation (`art. 59, § 1º — ...`); inputs are plain `GIVEN`s on every rule that reads them; the head of a rule has no arguments (positional in GIVEN order).
- A call of a rule on several lines needs its argument lines indented further than the rule's name (a layout trap); `(NOT` on its own line then the call indented works.
- Deontic rules: `IF applicable THEN PARTY .. MUST .. HENCE FULFILLED LEST BREACH BY .. BECAUSE ".." ELSE FULFILLED`; where a deontic is the only statement of a duty the seat asks about, its condition is a BOOLEAN rule of its own that the deontic calls; no WITHIN unless the text states a period; `WAITUNTIL n` in traces.
- A BOOLEAN whose text says "não é devido" is TRUE when the exclusion applies.
- Art. 33 (pb2) is applied in arts. 61, 75 and 80 from the core's reference values (F-P3-9).
- Amounts in cruzeiros are inputs in reais with the Cr$ figure in a comment (arts. 66, 128, 133).
- The seat builds the core's records from plain inputs by three constructors at the head of `pb3-seat.l4`; a field no rule reads is a documented placeholder; the keel's exact input names are kept for the facts the other pieces share.
