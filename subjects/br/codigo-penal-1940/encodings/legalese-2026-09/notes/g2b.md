# g2b — arts. 138–154-B: notes for the reviewer

**Status (2026-09-30): all 24 units encoded; forks register written; every module checks clean; 507 of 507 assertions satisfied.**
Parte Especial, Título I, Capítulo V (crimes contra a honra, arts. 138–145) and Capítulo VI (crimes contra a liberdade individual, arts. 146–154-B).

## PROGRESS

- [x] Read BRIEF, PLAN, the skills, `cp-dominio.l4`, `cp-pena.l4`, `cp-g3-furto*.l4`, source lines 856–1087, sweep-b entries and proposed forks for 138–154-B.
- [x] Vigência of every law that wrote a current wording in the range: read at its own vigência clause on Planalto (§ 5 below).
- [x] `cp-g2b-comum.l4` — nouns and readings shared by g2b's modules.
- [x] Cap. V — `cp-g2b-honra.l4` + tests: 150/150. Roadmap arts. 138–145 → encoded.
- [x] Cap. VI Seção I — `cp-g2b-constrangimento-ameaca.l4` (146–147-C) + tests: 112/112. Roadmap → encoded.
- [x] Cap. VI Seção I — `cp-g2b-sequestro-escravidao.l4` (148–149-A) + tests: 96/96. Roadmap → encoded.
- [x] Cap. VI Seção II — `cp-g2b-domicilio.l4` (150) + tests: 40/40. Roadmap → encoded.
- [x] Cap. VI Seção III — `cp-g2b-correspondencia.l4` (151–152) + tests: 32/32. Roadmap → encoded.
- [x] Cap. VI Seção IV — `cp-g2b-segredos.l4` (153–154-B) + tests: 77/77. Roadmap → encoded.
- [x] Roadmap: all 24 units encoded; validator ok.
- [x] Forks `registers/parts/g2b.forks.json`: 28 entries, built by `scratchpad/g2b/build_forks.py`; validated wrapped against sweep-b (§ 3).
- [x] Mutation control: 20 single mutations across the six modules, each caught (§ 8).
- [x] `nlg --lang en` on every tests module (§ 8); quotation check against the source (§ 8).
- [x] These notes.
- Last check.sh TOTAL (2026-09-30): `TOTAL (13 modules)                                 0       507       0       0     507`

## 1. What is encoded, and what is not

Every article in the range is encoded whole, caput and every paragraph and inciso: 24 roadmap units, all `encoded`.
For each punishing provision there is the predicate (consummated or attempted, via art. 14 in `cp-pena`, except the two habitual crimes), the `Pena cominada` constant compared in the tests with its preceito's words, each cause as a constant plus an `incide …` predicate and an exported list, the pena that applies to the case (the heaviest form where several are present), the outer limits with causes and attempt, and the ação penal wherever the article states one.

| module | articles | exported functions |
| --- | --- | --- |
| `cp-g2b-comum.l4` | — (shared nouns and readings) | none |
| `cp-g2b-honra.l4` | 138–145 | crime, pena, causes, limits, ação penal, exceção da verdade, the art. 140 § 1º option, retratação |
| `cp-g2b-constrangimento-ameaca.l4` | 146, 146-A, 147, 147-A, 147-B, 147-C | crime, pena / preceito, causes, limits, ação penal |
| `cp-g2b-sequestro-escravidao.l4` | 148, 149, 149-A | crime, pena, causes (of increase and decrease), limits |
| `cp-g2b-domicilio.l4` | 150 | crime, pena, causes, limits |
| `cp-g2b-correspondencia.l4` | 151, 152 | crime, pena, causes, limits, ação penal |
| `cp-g2b-segredos.l4` | 153, 154, 154-A, 154-B | crime, pena, causes, limits, ação penal |

**Not encoded, by design, each named where a rule reaches it:**

- Every earlier wording a later law replaced (none is in the source). Each rule that would read one checks the fact's date and refuses by name before the law's vigência: art. 140 § 3º before 11.1.2023; art. 141 IV before 9.7.2022 (where IV's people are the victims); art. 145 p.u. before 30.9.2009 (where it would decide); art. 147's ação penal before 10.10.2024; art. 148 § 1º I before 29.3.2005; art. 149 before 12.12.2003; art. 150 § 2º (revoked) before 3.1.2020 for an official acting as such; arts. 153 and 154's penalties before 13.1.1985 (M-sweep-b-07's arm); art. 154-A from 2.4.2013 to 27.5.2021.
- A paragraph or article a later law added does not apply before its vigência: that is the law's answer, not a refusal (arts. 141 §§ 2º–3º, 146-A, 147 §§ 1º–2º, 147-A, 147-B and its p.u., 147-C, 148 § 1º IV–V and § 3º, 149-A, 153 §§ 1º-A and 2º; art. 154-A before 2.4.2013).
- Three open forks refuse where they decide: a legal person as victim of a crime against honour (F-g2b-01); the ação penal of injúria real with slight injury (F-g2b-06); art. 151 where a special law may have displaced it (F-sweep-b-06). Art. 147-A § 1º II refuses from 1.4.2021 to 9.10.2024 where it would decide (F-sweep-b-24).
- Mental elements (dolo) are the Parte Geral's (arts. 18, 20), as in `cp-g3-furto.l4`; "falsamente" is read as the imputation's falsity (F-g2b-20).
- Art. 107 VI (extinction by retraction) and art. 100 (the default ação penal) are g1c's; the rules here cite art. 100 where an article lifts a condition and states nothing else.

**Where the source prints no heading.** Arts. 144 and 145 carry the roadmap's mechanical title "Retratação"; the source's only heading there is the one before art. 143.

## 2. Two findings about my own encoding, caught by the tests

1. **Arts. 153 and 154 merged the act with its object** (`divulgar conteúdo de documento particular …`, `revelar segredo …`). An interrupted disclosure of anything then counted as an attempt at *both* art. 153's caput and its § 1º-A. Two assertions failed on the first run (`a divulgação frustrada`'s limits). Repaired by splitting the act (`divulgação`, `revelação`) from the object; witnesses added (`o vazamento frustrado`, `a fofoca que não é segredo profissional`).
2. **Art. 151's conduct list** had the same shape: an interrupted execution with no conduct named counted as an attempt. The list is now "what the agent did, or set out to do"; `Execução do crime` says whether it was completed. Witness: `uma tentativa de nada`.

## 3. The forks, in prose

28 entries in `registers/parts/g2b.forks.json`: 21 of g2b's own and the 7 sweep-b reserved on these articles.
Validation (wrapped in a register envelope, sweep-b as peer): 19 rules checked, no finding on these entries; the 17 findings are sweep-b's reserved ids for other groups' articles (F-sweep-b-01–03, 07–09, 13–23), which resolve at merge.
F-sweep-b-08 (what "violência doméstica e familiar" is) spans arts. 121-A (g2a) and 141 § 3º / 147 § 1º (mine); g2a owns the lowest-numbered article and creates it. I read it through the noun `Razão da condição do sexo feminino`.

| id | question | status | taken |
| --- | --- | --- | --- |
| F-g2b-01 | Can a legal person be the "alguém" of arts. 138–140? | **open** | refused |
| F-g2b-02 | When is each crime against honour consummated? | resolved | calúnia, difamação: a third person learns; injúria: the offended learns |
| F-g2b-03 | Two tipos met at once (138/139, 147/147-C) | resolved | each reported; the judge resolves the overlap |
| F-g2b-04 | Vigência of art. 141 § 2º (vetoed, then promulgated DOU 30.4.2021) | resolved | 30.5.2021 (thirty days from the promulgation; Aras, on RE 85.950) |
| F-g2b-05 | "arma" (146 § 1º, 147-A § 1º III, 150 § 1º) | resolved | any weapon, proper or improper; one enough |
| F-g2b-06 | Ação penal of injúria real with slight injury | **open** | refused (serious injury or death: unconditional either way) |
| F-g2b-07 | Art. 141 II: does "em razão de suas funções" reach the Presidents? | resolved | no — first limb only |
| F-g2b-08 | Do arts. 141 and 146 § 1º's increases reach the fine? | resolved | yes (stated as TRUE constants; `Pena cominada` has no dias-multa) |
| F-g2b-09 | Art. 140 § 1º: every form of injúria? | resolved | yes |
| F-g2b-10 | Attempt in the habitual crimes 146-A, 147-A | resolved | none |
| F-g2b-11 | Art. 143: only the querelado of a queixa? | resolved | yes |
| F-g2b-12 | "se a conduta não constituir crime mais grave" (146-A, 147-B) | resolved | delegated to a finding |
| F-g2b-13 | Who counts toward "mais de três pessoas" / "duas ou mais pessoas" | resolved | everyone who took part, the agent included |
| F-g2b-14 | Art. 148 § 1º III: how the days are counted | resolved | delegated: art. 10's count, first day included |
| F-g2b-15 | Art. 149-A § 1º III: "parentesco", "autoridade" | resolved | kin by blood or affinity (not the spouse); every authority relation |
| F-g2b-16 | Art. 150 § 1º: violence against a thing? | resolved | yes |
| F-g2b-17 | Art. 151 § 2º: reaches § 3º? | resolved | no |
| F-g2b-18 | Art. 153 § 1º: reaches § 1º-A? | resolved | yes |
| F-g2b-19 | Art. 154-A § 2º: reaches § 3º? | resolved | no (§ 4º is § 3º's increase) |
| F-g2b-20 | Art. 138 "falsamente": knowledge an element of the caput? | resolved | no — the imputation's falsity; knowledge is dolo |
| F-g2b-21 | Art. 144 "responde pela ofensa" | resolved | may be prosecuted; proves nothing |
| F-sweep-b-04 | Art. 150 and the public agent (Lei 13.869 art. 22); "noite" | resolved | from 3.1.2020 the agent's entry is Lei 13.869 art. 22; "noite" a finding |
| F-sweep-b-05 | Art. 150 § 3º II: actual crime, or founded reasons? | resolved | split by the agent's status (a third reading, as the sweep allowed) |
| F-sweep-b-06 | Art. 151 displaced by Leis 6.538/1978 and 9.472/1997? | **open** | refused where it decides |
| F-sweep-b-10 | Art. 149: are the modes alternatives? | **settled** | yes — STF Inq 3412 |
| F-sweep-b-11 | Art. 140 and homotransphobic injúria | **settled** | Lei 7.716 art. 2º-A — STF MI 4733 ED (21.8.2023) |
| F-sweep-b-12 | Art. 145 p.u. and Súmula 714 | **settled** | concurrent queixa for the servidor offended for their functions |
| F-sweep-b-24 | Art. 147-A § 1º II's reference to the revoked art. 121 § 2º-A | resolved | inapplicable from 10.10.2024; refused before where it decides |

Where I looked for ambiguity: every preceito's species, bounds and conjunction against the source line; every "e/ou" joining limbs; every plural ("as penas", "armas"); every paragraph whose placement could limit its reach (§§ 2º of arts. 151 and 154-A, § 1º of arts. 140 and 153); every cross-reference out of the range (arts. 121 § 2º-A, 121-A § 1º, 327, 100, 10, 14); every "Vigência" marker in lines 856–1087.

## 4. Sweep entries acted on

Binding on my articles: only **M-sweep-b-07** (Lei 7.209/1984, art. 2º). Arts. 153 and 154 are written with "ou multa" as the alternative fine; the réis amounts are quoted in comments and inert; the proposed rule-version arm is implemented as a refusal of both penalties before 13.1.1985 (`a multa em réis anterior à Lei nº 7.209, de 1984, não está codificada`), since the encoding carries no pre-1985 wording.

| entry | class | what g2b did |
| --- | --- | --- |
| M-sweep-b-07 | binding | above |
| M-sweep-b-12 | interpretive | F-sweep-b-04 created and taken |
| M-sweep-b-13 | interpretive | F-sweep-b-05 created; a split reading taken |
| M-sweep-b-14 | interpretive | F-sweep-b-06 created, left open; art. 151 refuses where it decides |
| M-sweep-b-15 | no-effect | art. 142 I encoded as written; cited in the comment |
| M-sweep-b-16 | binding (art. 129) | cross-ref in F-g2b-06 (the art. 145 exception) |
| M-sweep-b-17 | interpretive | F-sweep-b-08 is g2a's; arts. 141 § 3º and 147 § 1º read its facts through the noun |
| M-sweep-b-19 | interpretive | F-sweep-b-10 created and settled |
| M-sweep-b-20 | interpretive | F-sweep-b-11 created and settled after I found and quoted MI 4733 ED; injúria racial displaced from 11.1.2023 |
| M-sweep-b-21 | interpretive | F-sweep-b-12 created and settled |
| M-sweep-b-39 | no-effect | cited at `com o emprego de arma` (toy guns); cross-ref F-g2b-05 |
| M-sweep-b-42 | no-effect | cited at art. 147 |
| M-sweep-b-43 | interpretive | membership and context of Lei 15.358 are certified facts (arts. 147-C, 148 § 3º) |
| M-sweep-b-44 | no-effect | art. 141 II as written for all three crimes; cross-ref F-g2b-07, F-sweep-b-12 |
| M-sweep-b-46 | interpretive | F-sweep-b-24 created and taken |
| M-sweep-b-47 | prospective | cross-ref F-sweep-b-24 |

## 5. Vigência — the searches

Every date is the publication date from `SOURCE/senado-dadosabertos-527942.xml`, with the law's own vigência clause read on Planalto (fetched 2026-09-29 into `scratchpad/g2b/leis/`, decoded as cp1252). Periods of vacatio are counted by LC nº 95/1998, art. 8º, § 1º: the day of publication included, in force the day after the last.

| law | provision in the range | DOU | clause | in force |
| --- | --- | --- | --- | --- |
| Lei 7.209/1984 | fines of arts. 153, 154 | 13.7.1984 | art. 5º, six months (from the sweep's quotation) | 13.1.1985 |
| Lei 9.983/2000 | art. 153 §§ 1º-A, 2º | 17.7.2000 | art. 4º, "noventa dias após a data de sua publicação" | 15.10.2000 |
| Lei 10.803/2003 | art. 149 | 12.12.2003 | art. 2º, on publication | 12.12.2003 |
| Lei 11.106/2005 | art. 148 § 1º I, IV, V | 29.3.2005 | art. 4º, on publication | 29.3.2005 |
| Lei 12.033/2009 | art. 145 p.u. | 30.9.2009 | art. 3º, on publication | 30.9.2009 |
| Lei 12.737/2012 | arts. 154-A, 154-B | 3.12.2012 | art. 4º, 120 days | 2.4.2013 |
| Lei 13.188/2015 | art. 143 p.u. | 12.11.2015 | on publication | 12.11.2015 |
| Lei 13.344/2016 | art. 149-A | 7.10.2016 | art. 17, 45 days | 21.11.2016 |
| Lei 13.869/2019 | revokes art. 150 § 2º | 5.9.2019 | art. 45, 120 days | 3.1.2020 |
| Lei 13.964/2019 | art. 141 § 2º (promulgated veto) | 30.4.2021 (promulgation) | art. 20, 30 days (F-g2b-04) | 30.5.2021 |
| Lei 14.132/2021 | art. 147-A | 1.4.2021 | on publication | 1.4.2021 |
| Lei 14.155/2021 | art. 154-A caput, pena, § 2º, § 3º pena | 28.5.2021 | on publication | 28.5.2021 |
| Lei 14.188/2021 | art. 147-B | 29.7.2021 | on publication | 29.7.2021 |
| Lei 14.197/2021 | art. 141 II | 2.9.2021 | art. 5º, 90 days | 1.12.2021 |
| Lei 14.344/2022 | art. 141 IV | 25.5.2022 | art. 34, 45 days | 9.7.2022 |
| Lei 14.532/2023 | art. 140 § 3º | 11.1.2023 | on publication | 11.1.2023 |
| Lei 14.811/2024 | art. 146-A | 15.1.2024 | art. 10, on publication | 15.1.2024 |
| Lei 14.994/2024 | arts. 141 § 3º, 147 §§ 1º–2º | 10.10.2024 | art. 10, on publication | 10.10.2024 |
| Lei 15.123/2025 | art. 147-B p.u. | 25.4.2025 | on publication (sweep-b, S-sweep-b-02) | 25.4.2025 |
| Lei 15.358/2026 | arts. 147-C, 148 § 3º | 25.3.2026 | on publication (S-sweep-b-02) | 25.3.2026 |

The "(Vigência)" link beside art. 141 § 2º in Planalto's HTML points at Lei 13.964's art. 20; the promulgation date and the 30.5.2021 reading come from Senado Notícias (30.4.2021) and Vladimir Aras in ConJur (10.10.2021). Lei 9.983/2000 predates LC 107/2001's counting rule; both counts give 15.10.2000.

Other sources read outside the bundle: the TJRJ Portal do Conhecimento's reproduction (24.8.2023) of the STF's news on MI 4733 ED (F-sweep-b-11); the STF's own site was unreachable.

## 6. Proposed shared nouns (PROPOSTO-COMUM) and helpers the conductor may hoist

In `cp-g2b-comum.l4`:

- **`Razão da condição do sexo feminino`** and `contra a mulher por razões da condição do sexo feminino (art. 121-A, § 1º)` — the facts art. 121-A § 1º reads. Arts. 92 II, 121-A, 129 § 13, 141 § 3º and 147 § 1º all cite it; g2a owns art. 121-A.
- **`com o emprego de arma`** — "arma" unqualified over `Meio empregado` (F-g2b-05). `cp-dominio`'s comment names arts. 146 § 1º, 147-A, 150 § 1º and 158 § 1º as the users.
- **`funcionário público para os efeitos penais (art. 327, caput e § 1º)`** — a reading of art. 327 over `Vínculo com a administração pública`, used by arts. 139 p.u., 141 II, 149-A § 1º I and 150. g6a encodes art. 327; a cross-check assertion at integration keeps the two in step (phrasebook entry 1.9).
- **`Cargo do ofendido`** — the offices of arts. 141 I–II and 154-A § 5º (art. 7 I a names the President too).
- Generic helpers duplicated from `cp-g3-furto.l4`'s local ones: `a causa se incide`, `as causas que incidem`, `a mais grave das penas`, `a mais grave de todas`. They belong in `cp-pena.l4`.
- **`Execução do crime`** — the two facts art. 14 II reads besides the result; any offence record can embed it.

## 7. Open questions for a Brazilian criminal lawyer

1. Can a legal person be the victim of difamação, or of calúnia for an environmental crime? (F-g2b-01)
2. Injúria real (art. 140 § 2º) whose violence caused a slight injury: public and unconditional (art. 100), or conditional on representação by analogy with Lei 9.099 art. 88? (F-g2b-06)
3. From when does art. 141 § 2º apply: 30.5.2021 (thirty days from the promulgation), 30.4.2021, or 23.1.2020? (F-g2b-04)
4. Are art. 151 caput and § 1º I still operative for postal correspondence, and § 1º IV for clandestine radio? (F-sweep-b-06)
5. Does art. 147-A § 1º II still apply after Lei 14.994/2024 revoked the paragraph it cites? (F-sweep-b-24)
6. In art. 141 II, does "em razão de suas funções" qualify the Presidents of the Senado, Câmara and STF? And does Súmula 714's concurrent queixa reach them? (F-g2b-07, F-sweep-b-12)
7. Do arts. 141's and 146 § 1º's increases reach the number of dias-multa? (F-g2b-08)
8. Art. 150 § 3º II for a private person: an actual crime, or founded reasons? (F-sweep-b-05)
9. Does art. 140 § 1º's perdão judicial reach injúria real and injúria qualificada? (F-g2b-09)
10. Does MI 4733 ED (2023) reach homotransphobic injúrias committed before 21.8.2023 but after 11.1.2023? The encoding reads art. 2º-A from 11.1.2023. (F-sweep-b-11)
11. May the defendant in a public action (art. 141 I–II) retract under art. 143? (F-g2b-11)
12. Was art. 147's parágrafo único before Lei 14.994/2024 "Somente se procede mediante representação" for every case? The encoding refuses the ação penal for earlier facts because that wording is not in its source.

## 8. What `check.sh` prints, and the other checks

`L4=/Users/mengwong/.claude/br-penal-toolchain/l4 ./check.sh . cp-g2b-`, from the encoding directory, 2026-09-30:

```
module                                        errors satisfied  failed refused asserts
cp-g2b-comum.l4                                    0         0       0       0       0
cp-g2b-constrangimento-ameaca-testes.l4            0       112       0       0     112
cp-g2b-constrangimento-ameaca.l4                   0         0       0       0       0
cp-g2b-correspondencia-testes.l4                   0        32       0       0      32
cp-g2b-correspondencia.l4                          0         0       0       0       0
cp-g2b-domicilio-testes.l4                         0        40       0       0      40
cp-g2b-domicilio.l4                                0         0       0       0       0
cp-g2b-honra-testes.l4                             0       150       0       0     150
cp-g2b-honra.l4                                    0         0       0       0       0
cp-g2b-segredos-testes.l4                          0        77       0       0      77
cp-g2b-segredos.l4                                 0         0       0       0       0
cp-g2b-sequestro-escravidao-testes.l4              0        96       0       0      96
cp-g2b-sequestro-escravidao.l4                     0         0       0       0       0
TOTAL (13 modules)                                 0       507       0       0     507
(a failed assertion also counts as an error; errors minus failed = everything else)
```

Exit 0. `grep -c '^#ASSERT'` equals the satisfied column in every tests module. No module has a non-import warning (one AND/OR same-column lint in `cp-g2b-domicilio.l4` was fixed by indentation). The refusals the tests expect are `#ASSERT REFUSED` and are counted as satisfied; every vigência gate is also asserted directly on its day and the day before (PLAN T5).

**Positive control.** 20 single mutations, each made to a copy (`scratchpad/g2b/mutate.sh`), each caught:

| module | mutation | failures |
| --- | --- | --- |
| honra | § 2º "em triplo" → "em dobro" | 3 |
| honra | § 2º vigência 30.5.2021 → 23.1.2020 | 3 |
| constrangimento-ameaca | 146 § 1º "mais de três" → "três ou mais" | 2 |
| constrangimento-ameaca | 147-A § 1º II applies after 2024 | 2 |
| sequestro-escravidao | 148 § 1º III "mais de quinze" → "quinze ou mais" | 1 |
| sequestro-escravidao | 148 § 1º I: ascendente → irmão | 2 |
| sequestro-escravidao | 149-A § 2º: organização criminosa → milícia | 2 |
| sequestro-escravidao | 149 vigência one day early | 2 (+2 errors) |
| sequestro-escravidao | 149 without "intensa e persistente" | 1 |
| sequestro-escravidao | 149-A § 1º fraction up to 2/3 | 3 |
| domicilio | § 4º II → taverna | 4 |
| domicilio | § 3º II founded reasons for anyone | 1 |
| domicilio | § 1º violence OR → AND | 2 |
| domicilio | Lei 13.869 vigência at publication | 3 (+1 error) |
| correspondencia | § 2º AND NOT § 3º → OR | 2 |
| correspondencia | F-sweep-b-06 refusal → FALSE | 2 errors (failed `#ASSERT REFUSED`) |
| segredos | Lei 14.155 vigência = 2013 | 2 (+3 errors) |
| segredos | 154-A § 2º AND NOT § 3º → OR | 10 |
| segredos | 154 "sem justa causa" dropped | 1 |
| segredos | 154-A § 5º fraction up to 2/3 | 1 |

**English.** `nlg --lang en` renders 150, 112, 96, 40, 32 and 77 lines for the six tests modules. No rule of mine renders bare; the backticked names in the output are test fixtures, plus one `cp-pena` constructor (§ 9).

**Quotations.** Every quoted fragment in my comments, split at clause and inciso boundaries (192 pieces), was checked against `SOURCE/codigo-penal-1940.txt`. All are verbatim except quotations of other laws (Lei 13.964 art. 20, Lei 7.716 art. 2º-A, Lei 7.209 art. 5º, the TJRJ report), which are not in the Code's text. One non-verbatim quote was found and fixed ("aplica-se a pena em dobro / em triplo" merged § 1º and § 2º of art. 141).

## 9. For the conductor

- **`cp-pena.l4`'s `com pena privativa de liberdade` renders bare** in `nlg --lang en` (witness: `o preceito secundário da intimidação sistemática (art. 146-A)` in `cp-g2b-constrangimento-ameaca-testes.l4`). Its herald sits below a constructor that has a `HAS` field, and may be attaching to the field. g0's file; not edited.
- **`check.sh` and a failed `#ASSERT REFUSED`**: on 2026-09-29 it showed as an error and UNACCOUNTED, not as "failed"; the conductor's later fix counts the results section. Exit status was non-zero either way.
- **Art. 145 returns a list of routes** (Súmula 714 makes two concurrent); every other ação penal here is a single `Ação penal`.
- **Enum constructors are global** in any module that imports several groups: mine include `calúnia`, `difamação`, `injúria`, `coação`, `abuso`, `entrar`, `permanecer`, `clandestinamente`, `astuciosamente`, `agenciar` … `acolher`, `governador`, `prefeito`. `coação` in particular may collide with a later Título's.
- **PROPOSTO-COMUM** items and the art. 327 cross-check: § 6.
- **Integration decisions**: F-sweep-b-08 (g2a) should confirm it reads the same two facts `Razão da condição do sexo feminino` names; F-g2b-08's reading (increases reach the fine) sits beside g0's F-g0-28 for the machinery.
