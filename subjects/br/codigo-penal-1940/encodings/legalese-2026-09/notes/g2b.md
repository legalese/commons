# g2b — arts. 138–154-B: notes for the reviewer

**Status (2026-09-29): in progress.**
Parte Especial, Título I, Capítulo V (crimes contra a honra, arts. 138–145) and Capítulo VI (crimes contra a liberdade individual, arts. 146–154-B).

## PROGRESS

- [x] Read BRIEF, PLAN, the skills, `cp-dominio.l4`, `cp-pena.l4`, `cp-g3-furto*.l4`, source lines 856–1087, sweep-b entries and proposed forks for 138–154-B.
- [x] Vigência of every law that wrote a current wording in the range: read at its own vigência clause on Planalto (§ 5 below).
- [x] `cp-g2b-comum.l4` — nouns shared by g2b's modules (checks clean).
- [x] Cap. V — `cp-g2b-honra.l4` + tests: 150 asserts, 150 satisfied, 0 failed, 0 refused (before mutation control). Roadmap arts. 138–145 → encoded; validator ok.
- [x] Cap. VI Seção I — `cp-g2b-constrangimento-ameaca.l4` (146–147-C) + tests: 112/112 satisfied. Roadmap → encoded. Mutation control started (`scratchpad/g2b/mutate.sh`): 4 mutations, each caught.
- [x] Cap. VI Seção I — `cp-g2b-sequestro-escravidao.l4` (148–149-A) + tests: 96/96 satisfied; 6 mutations, each caught. Roadmap → encoded.
- [ ] Cap. VI Seção II — `cp-g2b-domicilio.l4` (150) + tests.
- [ ] Cap. VI Seção III — `cp-g2b-correspondencia.l4` (151–152) + tests.
- [ ] Cap. VI Seção IV — `cp-g2b-segredos.l4` (153–154-B) + tests.
- [ ] Forks file, roadmap, nlg check, check.sh numbers.
