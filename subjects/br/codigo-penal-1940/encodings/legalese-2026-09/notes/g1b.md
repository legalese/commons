# g1b — arts. 32–76: the penalties, their cominação and application, concurso, the limit of art. 75

**Status (2026-09-29): in progress.** This file is the reviewer's record and the resume point; PROGRESS is updated after each Capítulo.

## PROGRESS

- [x] Read BRIEF, PLAN, the skills (SKILL.md, gotchas, drafting-patterns, all eleven source-pattern pages, encoding-a-subject), `cp-dominio.l4`, `cp-pena.l4`, `cp-g3-furto*.l4`, source lines 157–357, sweep-a (all 40 entries) and its proposed forks, and the sweep-b/-c entries that touch arts. 32–76.
- [x] Vigência of every law that re-worded arts. 32–76, read from Planalto's texts of the laws (§ 7).
- [x] `cp-g1b-condenacao.l4` — the nouns of the sentencing (no rules).
- [x] `cp-g1b-circunstancias.l4` — arts. 61–67 (+ tests)
- [x] `cp-g1b-privativas-de-liberdade.l4` — art. 33 §§ 2º–4º, arts. 34–42 (+ tests)
- [x] `cp-g1b-restritivas-de-direitos.l4` — arts. 44–48 (+ tests)
- [x] `cp-g1b-multa.l4` — arts. 50–52 (+ tests)
- [x] `cp-g1b-cominacao.l4` — arts. 54–57, 58 parágrafo único (+ tests)
- [ ] `cp-g1b-aplicacao-da-pena.l4` — arts. 59, 60, 68 (+ tests)
- [ ] `cp-g1b-concurso-de-crimes.l4` — arts. 69–76 (+ tests)
- [ ] forks file, roadmap, nlg check, mutation run, final check.sh

## Design decisions (so far)

- Module dependency order: condenacao ← circunstancias ← privativas, restritivas ← cominacao, aplicacao; concurso and multa import only condenacao.
- Reincidência is COMPUTED (arts. 63–64) from the agent's prior convictions; `Agente`'s `reincidente` (g0, fork F-g0-05) is cross-checked against it in the tests.
- The first and second phases return RANGES (`Intervalo de duração`), never a chosen number; the third phase uses `cp-pena`'s cascade.
- TYPICALLY on a field typed by an own enum is rejected by this binary ("The TYPICALLY value … must be a literal"), although `writing-l4-rules` source-patterns entry 1.5 says a constructor of one's own ONE OF type is accepted. Probe: scratchpad `g1b/probe/p1.l4`, first run. So F-sweep-a-04's reading is materialised as a rule parameter with a named default, mechanism `encoded`, not `TYPICALLY`.

## Fork registry (ids in use; the forks file is written from this)

| id | article | question | taken |
| --- | --- | --- | --- |
| F-g1b-01 | 33 caput, § 2º a | detenção over 8 years: § 2º a (fechado) or caput (never starts closed) | caput: semi-aberto |
| F-g1b-02 | 33 § 2º | "pena": cominada or aplicada | aplicada (the sentence's) |
| F-g1b-03 | 33 § 3º; Súmula 269 | "favoráveis as circunstâncias judiciais" | none valued desfavorável |
| F-g1b-04 | 42 | days of custody: inclusive of both ends? | yes (art. 10) |
| F-g1b-05 | 33 § 4º | "crime contra a administração pública" | Título XI; delegated classification |
| F-g1b-06 | 44 I | does the violence bar reach the culposo limb | no |
| F-g1b-07 | 44 I | "violência": does reduction to impotence (violência imprópria) count | no (literal) |
| F-g1b-08 | 44 II | "reincidente em crime doloso" | both crimes dolosos |
| F-g1b-09 | 44 § 3º | "o mesmo crime" | same offence (article) |
| F-g1b-10 | 45 § 1º | which minimum wage | input; not fixed by the text |
| F-g1b-11 | 46 § 3º | "dia de condenação" | calendar days of the term (art. 10) |
| F-g1b-12 | 61 caput | "quando não constituem ou qualificam o crime" | delegated: the crime record lists them |
| F-g1b-13 | 61 II e | "cônjuge" and the companheiro | excluded (no analogy in malam partem) |
| F-g1b-14 | 61 II f | "prevalecendo-se" | relation + finding |
| F-g1b-15 | 65 I | does "salvo" reach both limbs | both (Lei 15.160's ementa) |
| F-g1b-16 | 63 | new crime on the day of trânsito | not "depois" |
| F-g1b-17 | 64 I | start and counting of the five years | probation start or cumprimento; art. 10 |
| F-g1b-18 | 67 | which circumstances preponderate | reincidência; motives 61 II a, b, 62 IV, 65 III a; personality 65 I, 65 III d |
| F-g1b-19 | 50 | "dentro de 10 dias depois de transitada" | ends on the tenth day after the trânsito |
| F-g1b-20 | 54 vs 44 I | "inferior a 1 (um) ano" (1984) against "não superior a quatro anos" (1998) | art. 44 governs the quantity |
| F-g1b-21 | 56, 57 | do arts. 56–57 condition interdições I–III, and are IV–V unconditioned | yes; yes |
| F-g1b-22 | 58 p.ú. | "parágrafo único do art. 44" no longer exists | read as art. 44 § 2º |
