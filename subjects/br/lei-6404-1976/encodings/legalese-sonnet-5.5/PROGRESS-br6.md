# PROGRESS: br6 (Lei 6.404/1976, Capítulos XVII a XX, lines 1958-2325, Arts. 206 to 264)

Written by the piece agent br6 on 2026-10-22; kept current as the work goes on, because the context may be compacted.
After a compaction, re-read this file, NOTES.md and the text (not a summary).

## State

Finished, apart from the final report, which is the agent's last message.
The last full run of `L4=<L4_BIN> L4_TARGET=unstable ./check.sh` printed 24 modules, 0 errors, 1,171 assertions satisfied, 0 failed, 0 refused (exact output in NOTES.md, "What check.sh prints").
No `.l4` file has changed since that run.

## Method

- Read: the brief, KEEL-NOTES.md, ENCODING-GUIDE.md, COMMONS-CLAUDE.md, both skills' SKILL.md, dialects.md, drafting-patterns.md, source-locators.md, the index of source-patterns.md and parts of its pages 05, 07 and 11 (not all of them), the example seat (ea-seat.l4) and br-core.l4.
- The text of my range was read through with struck spans removed (`perl` one-liner of KEEL-NOTES, instruction 1).
- Quote lines are made with `python3 -I srcrefs.py quote RAW A B`; every `@ref` has a locator inside a quoted run; checked with `--refs`.
- Duties and powers are encoded as compliance and entitlement predicates from facts (BOOLEAN, NUMBER, DATE or MAYBE), not as `PARTY ... MUST` rules, because an `#ASSERT` cannot compare a DEONTIC value, so a regulative rule could not be tested by assertion.
  This is a method decision, not a refusal by the binary and not a fork of the text; it is recorded in NOTES.md under "What the stable binary does not accept" and "Before this is worth relying on".
- Imports are flat: nouns, then cap18b, then cap20c, then cap17 (cap17 calls the subsidiária integral rule of Art. 251 for the ressalva of Art. 206, I, d).
  No piece imports another piece's module.
- Tests: `br6-tests-*.l4`, one per module, with expected values written by hand from the text before each run, never from the code's output.
- The seat: `br6-seat.l4` calls the layer-1 rules and builds their records in its `WHERE`; `br6-cases-seat.l4` has at least one case per question.
- The scripts that wrote the tests, the seat and NOTES.md live in the scratchpad of the session, in `br6gen/`, outside the deposit; the `.l4` files of the deposit do not depend on them at run time.
  NOTES.md is rendered from `br6gen/notes_data.py` and `br6gen/notes_more.py` by `br6gen/make_notes.py`, which fails if a jural row names a provision that has no coverage row, and which prints "Asserted." for a finding only if every rule or question it names occurs in an `#ASSERT` line.

## Modules (flat folder, ASCII names)

| module | articles | state |
| --- | --- | --- |
| br6-nouns | types shared by the modules | l4 check clean, srcrefs clean |
| br6-cap17-dissolucao-liquidacao-extincao | 206-219 | clean; tests 203 satisfied |
| br6-cap18a-transformacao | 220-222 | clean; tests 23 satisfied |
| br6-cap18b-incorporacao-fusao-cisao | 223-234 | clean; tests 163 satisfied |
| br6-cap19-economia-mista | 235-240 (241, 242 repealed) | clean; tests 48 satisfied |
| br6-cap20a-coligadas-participacao-reciproca | 243-246 | clean; tests 74 satisfied |
| br6-cap20b-demonstracoes-financeiras | 247-250 | clean; tests 50 satisfied |
| br6-cap20c-subsidiaria-integral | 251-253 | clean; tests 41 satisfied |
| br6-cap20d-alienacao-compra-de-controle | 254-A, 255, 256 (254 repealed) | clean; tests 54 satisfied |
| br6-cap20e-oferta-publica-de-controle | 257-263 | clean; tests 66 satisfied |
| br6-cap20f-incorporacao-de-controlada | 264 | clean; tests 35 satisfied |
| br6-seat.l4, br6-cases-seat.l4 | layer 2 | 111 questions, 326 plain inputs, 414 assertions satisfied |
| NOTES.md | all ten required headings | written; 161 coverage rows, 25 forks (cited by 27 fork rows), 177 jural rows, 24 cross-reference rows, 2 needs, 32 findings (30 asserted) |

## Files written

Layer 1: `br6-nouns.l4`, `br6-cap17-dissolucao-liquidacao-extincao.l4`, `br6-cap18a-transformacao.l4`, `br6-cap18b-incorporacao-fusao-cisao.l4`, `br6-cap19-economia-mista.l4`, `br6-cap20a-coligadas-participacao-reciproca.l4`, `br6-cap20b-demonstracoes-financeiras.l4`, `br6-cap20c-subsidiaria-integral.l4`, `br6-cap20d-alienacao-compra-de-controle.l4`, `br6-cap20e-oferta-publica-de-controle.l4`, `br6-cap20f-incorporacao-de-controlada.l4`.
Tests: `br6-tests-cap17.l4`, `-cap18a`, `-cap18b`, `-cap19`, `-cap20a`, `-cap20b`, `-cap20c`, `-cap20d`, `-cap20e`, `-cap20f`.
Layer 2: `br6-seat.l4`, `br6-cases-seat.l4`.
Reports: `NOTES.md`, `PROGRESS.md`.
Not mine, and not changed: `br-core.l4`, `check.sh`, `srcrefs.py`.

## Checks run

- `check.sh`, stable `l4` 1.6.98, target unstable: 24 modules, 0 errors, 1,171 satisfied, 0 failed, 0 refused.
- `python3 -I srcrefs.py check --refs <raw text> br6-*.l4`: 251 `src:` lines, 166 runs, 234 locators, 0 problems.
- Instruction 12 (the article of every `@ref` against the heading above its `src:` lines): 225 `@ref` lines, 346 non-blank source lines, 0 mismatches; a control with two wrong labels was caught.
- Negative controls (assertions known to be false, appended to copies of a layer-1 test file and of the seat cases) failed as they should.
- Every `Q.j` label of the seat resolves to a coverage row; every coverage row has a jural row.

## Decisions taken

- Method: predicates, not deontics (above).
- Counting convention: the core's F1 (event day is day 0) and F2 (months end on the last day of a shorter month).
- Votes thresholds: the live (2021) wording, in votes, for Arts. 215, § 1º, 243, § 5º and 252, § 2º.
- Seat: 111 questions, because the brief asks for a question for every provision that gives a claim, privilege, power or immunity, puts a duty or liability on the person, or decides something they would ask; three questions were added late (Art. 206, II, Art. 206, III and Art. 211) and the seat was then frozen.
- The 25 forks, with the reading taken, are in NOTES.md.

## Open points for the lead

- Whether to add a deontic layer with `#TRACE` tests (none was written).
- Whether to prune or order the 111 seat questions for the form.
- The two needs from the core: `prazo em horas`, and a canonical dissent fact.
- When br1, br3, br4 and br5 are merged, turn the cross-reference inputs into calls and re-run.
