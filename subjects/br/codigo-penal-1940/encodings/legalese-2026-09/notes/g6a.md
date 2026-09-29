# g6a — arts. 312–337-D: notes for the reviewer

**Status (2026-09-29): in progress.** Parte Especial, Título XI, Capítulos I, II and II-A.

## PROGRESS

- [x] Read BRIEF, PLAN, the skills (writing-l4-rules SKILL, gotchas, drafting-patterns, all eleven source-pattern pages; encoding-a-subject), `cp-dominio.l4`, `cp-pena.l4`, `cp-g3-furto*.l4`.
- [x] Read arts. 312–337-D in the source (lines 2168–2343), sweep-c (entries and forks) and the sweep-b entry on LC 225/2026 (M-sweep-b-11).
- [x] Asked sweep-c (message, 2026-09-29) for the vigência clauses of the older laws that re-worded preceitos in range (Leis 13.964/2019, 10.763/2003, 13.008/2014, 9.983/2000, 10.467/2002, 8.137/1990, 9.127/1995, 11.466/2007, 6.799/1980) — S-sweep-c-04 covers only 2025–2026.
- [x] Art. 327 — `cp-g6a-funcionario-publico.l4`; shared machinery `cp-g6a-comum.l4` (the `Ato do agente` record, vigência constants, heaviest-penalty fold, cause lists); test fixtures `cp-g6a-casos.l4`.
- [x] Cap. I, arts. 312–316 — `cp-g6a-peculato-a-concussao.l4` + tests: 129/129 satisfied (first run).
- [x] Cap. I, arts. 317–326 — `cp-g6a-corrupcao-passiva-a-sigilo.l4` + tests: 109/109 satisfied (first run).
- [ ] Positive control (mutations) still owed: every test module passed on its first run.
- [ ] Vigência dates still marked A CONFIRMAR in `cp-g6a-comum.l4` and `cp-g6a-funcionario-publico.l4` (all but LC 225/2026) — awaiting sweep-c.
- [ ] Cap. II, arts. 328–333 — `cp-g6a-usurpacao-a-corrupcao-ativa.l4`
- [ ] Cap. II, arts. 334–337-A — `cp-g6a-descaminho-a-sonegacao.l4`
- [ ] Cap. II-A, arts. 337-B–337-D — `cp-g6a-administracao-estrangeira.l4`
- [ ] Forks file, roadmap, sweep entries acted on, check.sh output, nlg check.

## Plan of modules

| module | articles |
| --- | --- |
| `cp-g6a-funcionario-publico.l4` | 327 (caput, § 1º, § 2º) — imported by every other g6a module |
| `cp-g6a-peculato-a-concussao.l4` | 312, 313, 313-A, 313-B, 314, 315, 316 |
| `cp-g6a-corrupcao-passiva-a-sigilo.l4` | 317, 318, 319, 319-A, 320, 321, 322, 323, 324, 325, 326 |
| `cp-g6a-usurpacao-a-corrupcao-ativa.l4` | 328, 329, 330, 331, 332, 333 |
| `cp-g6a-descaminho-a-sonegacao.l4` | 334, 334-A, 335, 336, 337, 337-A |
| `cp-g6a-administracao-estrangeira.l4` | 337-B, 337-C, 337-D |

Each has a `-testes.l4` beside it.
