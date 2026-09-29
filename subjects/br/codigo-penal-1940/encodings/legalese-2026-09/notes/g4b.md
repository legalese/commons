# g4b — arts. 250–288-A: notes for the reviewer

**Status (2026-09-29): in progress.** This file is the resume point; PROGRESS below says where the work stands.

## PROGRESS

- [x] Read BRIEF.md, PLAN.md, the writing-l4-rules skill (SKILL.md, gotchas, drafting-patterns, all eleven source-pattern pages), encoding-a-subject, cp-dominio.l4, cp-pena.l4, cp-g3-furto.l4 and its tests.
- [x] Read source lines 1771–2011 (arts. 250–288-A), and arts. 18, 19, 121 § 3º, 129 §§ 1º–2º, which my range cites.
- [x] Read sweep-c: the entries on my range are M-sweep-c-03 (binding, art. 273 § 1º-B, I), M-sweep-c-04 (binding, art. 287), M-sweep-c-08 (interpretive, art. 268, fork F-sweep-c-04) and M-sweep-c-25 (no-effect). I also read the searches S-sweep-c-03, -04 and -09.
- [x] Vigência of every law that amended my range, from the laws' own texts fetched from Planalto on 2026-09-29 (table in § 7).
- [x] Messaged sweep-c about Lei 8.072/1990, art. 8º (a special penalty for art. 288 that the compiled text does not show), and three unverified leads (§ 6).
- [x] `cp-g4b-comum.l4` (shared nouns: `Dados comuns do fato`, `Elemento subjetivo`, `Imputação do resultado`, `Perigo criado`, `Ação do agente`, `Profissão de saúde`) and `cp-g4b-comum-testes.l4` (shared test fixtures + 22 assertions).
- [x] Capítulo I, arts. 250–259: `cp-g4b-perigo-comum.l4` (art. 258 lives here) and its tests, 143/143. Six single mutations each caught (§ 4).
- [x] Capítulo II, arts. 260–266: `cp-g4b-transportes-e-servicos.l4` and its tests, 100/100. Roadmap: arts. 250–266 `encoded`, validator ok.
- [ ] Capítulo III, arts. 267–285: four modules planned — `cp-g4b-saude-publica-forma-qualificada.l4` (art. 285, imported by the other three; art. 267's exclusion and fork F-g4b on art. 282 live there), `cp-g4b-saude-publica-epidemia-e-agua.l4` (267–271), `cp-g4b-saude-publica-alimentos-e-medicamentos.l4` (272–281), `cp-g4b-saude-publica-exercicio-ilegal.l4` (282–284).
- [ ] Título IX, arts. 286–288-A: `cp-g4b-paz-publica.l4` and its tests.
- [ ] Forks file, roadmap, nlg check, mutation check, final report.

## 1. What is encoded, and what is not

(to be written as each Capítulo lands)

## 2. The forks, in prose

## 3. Proposed shared nouns (PROPOSTO-COMUM)

## 4. What `check.sh` prints

## 5. Sweep entries acted on

## 6. Open questions for a Brazilian criminal lawyer

## 7. Vigência of the laws that amended arts. 250–288-A

Every row was read from the law's own text on Planalto, fetched with curl on 2026-09-29. The fetched files are in g4b's private scratch directory. The publication dates come from each text's "não substitui o publicado no DOU de …" line, and agree with the Senado XML.

| law | what it did in my range | vigência clause | in force |
| --- | --- | --- | --- |
| Lei nº 5.346/1967 | added art. 265, parágrafo único | art. 4º: "entra em vigor 30 dias após a sua publicação" (DOU 7.11.1967, Senado XML) | 7.12.1967 |
| Lei nº 8.072/1990 | art. 6º: new penas for arts. 267 and 270 caput; art. 8º: 3–6 years for art. 288 with hediondos | art. 12: "Esta lei entra em vigor na data de sua publicação" (DOU 26.7.1990, Senado XML) | 26.7.1990 |
| Lei nº 9.677/1998 | re-wrote arts. 272–277 | art. 2º: in force on publication; DOU 3.7.1998 | 3.7.1998 |
| Lei nº 12.720/2012 | added art. 288-A | art. 5º: in force on publication; DOU 28.9.2012 | 28.9.2012 |
| Lei nº 12.737/2012 | added art. 266 §§ 1º and 2º (§ 2º then only "por ocasião de calamidade pública") | art. 4º: "após decorridos 120 (cento e vinte) dias de sua publicação oficial"; DOU 3.12.2012 | 2.4.2013 (counting under LC 95/1998, art. 8º, § 1º) |
| Lei nº 12.850/2013 | re-wrote art. 288 (caput, pena, parágrafo único) | art. 27: "após decorridos 45 (quarenta e cinco) dias de sua publicação oficial"; DOU 5.8.2013 (edição extra) | 19.9.2013 |
| Lei nº 14.197/2021 | added art. 286, parágrafo único | art. 5º: "após decorridos 90 (noventa) dias de sua publicação oficial"; DOU 2.9.2021 | 1.12.2021 |
| Lei nº 15.181/2025 | re-wrote art. 266 § 2º | art. 6º: in force on publication; DOU 29.7.2025 (also S-sweep-c-04) | 29.7.2025 |
| Lei nº 15.245/2025 | art. 288: added § 2º, "numerando-se o atual parágrafo único como § 1º" | in force on publication; DOU 30.10.2025 | 30.10.2025 |
| Lei nº 15.397/2026 | art. 266: new pena, new § 2º with incisos I–II | art. 4º: in force on publication; DOU 4.5.2026 | 4.5.2026 |
| Lei nº 15.425/2026 | art. 282: new caput and pena, §§ 2º–5º added, "numerando-se o atual parágrafo único como § 1º" | art. 3º: in force on publication; DOU 8.6.2026 | 8.6.2026 |
