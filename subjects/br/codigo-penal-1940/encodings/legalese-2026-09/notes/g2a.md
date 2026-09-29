# g2a — arts. 121–137 (Parte Especial, Título I, Capítulos I–IV): notes for the reviewer

## PROGRESS

Resume from here, not from memory.

- 2026-09-29: read BRIEF, PLAN, the skills, `cp-dominio.l4`, `cp-pena.l4`, the furto pattern, the source (lines 590–855), sweep-b entries and forks-proposed.
- Asked sweep-b (message, 2026-09-29) for the vigência clauses of Leis 14.994/2024, 14.811/2024, 13.968/2019, 12.653/2012 and 9.777/1998. Until it answers, the gates use the DOU date from the Senado XML and say so.
- Module plan, in this order:
  1. `cp-g2a-comum.l4` — nouns shared by my modules (enums), no rules.
  2. `cp-g2a-homicidio.l4` — arts. 121, 121-A, 121-B (Cap. I, first part).
  3. `cp-g2a-lesao-corporal.l4` — art. 129 (Cap. II). Before Cap. I's second part, because art. 122 § 6º points at art. 129 § 2º.
  4. `cp-g2a-suicidio-infanticidio-aborto.l4` — arts. 122–128 (Cap. I, second part).
  5. `cp-g2a-periclitacao.l4` — arts. 130–136 (Cap. III).
  6. `cp-g2a-rixa.l4` — art. 137 (Cap. IV).
  Each with a `-testes.l4` beside it.
- DONE `cp-g2a-comum.l4` (nouns: `Elemento subjetivo`, `Circunstância do crime contra a pessoa`).
- DONE Cap. I first part, `cp-g2a-homicidio.l4` + tests: check.sh 0 errors, 158 satisfied, 0 failed, 0 refused, 158 asserts. Eight mutations each caught (scratchpad `g2a/mut/`). nlg --lang en read: heralds attach. Roadmap: arts. 121, 121-A, 121-B `encoded` (titles of 121-A, 121-B corrected to the Code's headings).
- Forks written in the module comments so far, NOT YET in `g2a.forks.json`: F-g2a-01 (§ 1º and qualifiers), -02 (§ 1º/§ 5º "pode"), -03 (§ 4º "menor de 14" vs § 2º IX), -04 (121/121-A/121-B specialty), -05 (§ 6º vs § 2º-D), -06 (3 months after birth), -07 (121-A § 3º knowledge), -08 (explosive in § 2º III), F-sweep-b-08.
- DONE Cap. II, `cp-g2a-lesao-corporal.l4` + tests: check.sh 0 errors, 126 satisfied, 0 failed, 0 refused, 126 asserts. Nine mutations; eight caught at once, the ninth (§ 10 reaching § 3º-A) exposed a missing test, now added and caught. nlg read. Roadmap: art. 129 `encoded`.
- More forks written in comments, NOT YET in `g2a.forks.json`: F-g2a-09 (§§ 9º/13 as forms of the slight injury), -10 (§ 7º sentence matching), -11 (grade from incisos), -12 (§ 10 and § 3º-A), -13 (§ 12 I c vs II), -14 (§ 11 "na hipótese do § 9º"), F-sweep-b-07 (ação penal).
- NEXT: write `g2a.forks.json` for Caps. I–II; then Cap. I second part, arts. 122–128.
