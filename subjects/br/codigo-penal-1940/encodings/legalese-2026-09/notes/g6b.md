# g6b — arts. 337-E–359-H: notes for the reviewer

**Status (2026-09-29): in progress.** Parte Especial, Título XI, Capítulos II-B (crimes em licitações e contratos administrativos), III (crimes contra a administração da justiça) and IV (crimes contra as finanças públicas).

## PROGRESS

- [x] Read BRIEF.md, PLAN.md, the writing-l4-rules skill (SKILL.md, gotchas, drafting-patterns, all eleven source-pattern pages), encoding-a-subject, cp-dominio.l4, cp-pena.l4, cp-g3-furto*.l4.
- [x] Read source lines 2253–2256 (art. 327) and 2344–2563 (arts. 337-E–359-H); sweep-c entries and proposed forks; the Senado XML rows for my articles.
- [x] Fetched the amending laws from Planalto for their vigência clauses (scratch `g6b/laws/`); § 7 below.
- [x] `cp-g6b-comum.l4` (group nouns and helpers) and tests: 20/20.
- [x] Capítulo II-B, arts. 337-E–337-P: `cp-g6b-licitacoes.l4` and tests: 94/94; eight mutations each caught; `nlg --lang en` read (no module rule bare); roadmap units 337-E–337-P moved to encoded, validator ok.
- [x] Capítulo III, arts. 338–344: `cp-g6b-justica-reingresso-a-coacao.l4` and tests: 110/110; ten mutations each caught; `nlg --lang en` read; roadmap units moved.
- [x] Capítulo III, arts. 345–359: `cp-g6b-justica-exercicio-arbitrario-a-desobediencia.l4` and tests: 113/113; fourteen mutations each caught; `nlg --lang en` read; roadmap units moved.
- [ ] Capítulo IV, arts. 359-A–359-H: `cp-g6b-financas-publicas.l4` and tests.
- [ ] Forks file `registers/parts/g6b.forks.json`, validated.
- [ ] Roadmap `registers/parts/g6b.roadmap.json`, every unit moved, validated.
- [ ] `nlg --lang en` read for every tests module.
