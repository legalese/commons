# g6b — arts. 337-E–359-H: notes for the reviewer

**Status (2026-10-08): complete, with ta-g6's four record-shape findings fixed (§ 10; their positive controls not yet run).** All 44 units encoded; check.sh `TOTAL (10 modules) 0 errors, 427 satisfied, 0 failed, 0 refused, 427 asserts`. Parte Especial, Título XI, Capítulos II-B (crimes em licitações e contratos administrativos), III (crimes contra a administração da justiça) and IV (crimes contra as finanças públicas).

## PROGRESS

2026-10-08, art. 337-M knowledge (fork F-g6b-24): caput and § 1º now require the new local field `o agente sabia que a empresa ou o profissional fora declarado inidôneo` (old: the verbs alone made the crime; new: verb AND knowledge; § 2º unchanged). Fixture `inidônea:` gained a `, sabendo` parameter. Tests +4 asserts, no existing #ASSERT changed. Positive control: removing the requirement fails 2. Positive controls of the four record-shape fixes (mut-fix4.py) run 2026-10-08: all seven mutants killed as expected.

2026-10-08, the conductor's four fixes (§ 10): code and tests done; positive controls not yet run. Last check.sh TOTAL (all ten g6b modules): `TOTAL (10 modules)                                 0       427       0       0     427`, exit 0; 411 earlier assertions unchanged, 16 new. Roadmap part and forks part (24 entries) validate. NEXT: the reply to the conductor.

- [x] Art. 351: record field `o fugitivo é o próprio agente`; the lone escape is not art. 351 (fork F-g6b-23). Tests +3.
- [x] Arts. 342, 343 (and 357): `parte no processo`, `pessoa sem função no processo` in `Pessoa que funciona no processo`; art. 357's list made positive. Tests +6.
- [x] Art. 344 (and 342): `nenhum processo ou procedimento` in `Processo ou procedimento`. Tests +3.
- [x] Art. 337-P: the combined check reads the crime (`Crime cuja multa se fixa`) and refuses one outside the chapter. Tests +5; four existing calls pass `crime do art. 337-E` where they passed `pena do art. 337-E`, same expected values.
- [ ] Positive controls: NOT RUN. Seven mutants are written in `~/.claude/br-penal-scratch/g6b/mut-fix4.py` (§ 10); the run was held behind the `cp-codigo-penal.l4` typecheck (one l4 at a time), and the conductor called for the report first.
- [x] Dependants re-checked: `cp-ind-g6-justica-exercicio-arbitrario-a-desobediencia.l4` no longer compiles (the new art. 351 field, § 10); the other three cp-ind-g6 modules and `cp-codigo-penal.l4` compile ("Check succeeded.").

Resumed 2026-09-30 after the usage-limit stop; the 2026-09-30 TOTAL was 411/411.


- [x] Read BRIEF.md, PLAN.md, the writing-l4-rules skill (SKILL.md, gotchas, drafting-patterns, all eleven source-pattern pages), encoding-a-subject, cp-dominio.l4, cp-pena.l4, cp-g3-furto*.l4.
- [x] Read source lines 2253–2256 (art. 327) and 2344–2563 (arts. 337-E–359-H); sweep-c entries and proposed forks; the Senado XML rows for my articles.
- [x] Fetched the amending laws from Planalto for their vigência clauses (scratch `g6b/laws/`); § 7 below.
- [x] `cp-g6b-comum.l4` (group nouns and helpers) and tests: 20/20.
- [x] Capítulo II-B, arts. 337-E–337-P: `cp-g6b-licitacoes.l4` and tests: 94/94; eight mutations each caught; `nlg --lang en` read (no module rule bare); roadmap units 337-E–337-P moved to encoded, validator ok.
- [x] Capítulo III, arts. 338–344: `cp-g6b-justica-reingresso-a-coacao.l4` and tests: 110/110; ten mutations each caught; `nlg --lang en` read; roadmap units moved.
- [x] Capítulo III, arts. 345–359: `cp-g6b-justica-exercicio-arbitrario-a-desobediencia.l4` and tests: 113/113; fourteen mutations each caught; `nlg --lang en` read; roadmap units moved.
- [x] Capítulo IV, arts. 359-A–359-H: `cp-g6b-financas-publicas.l4` and tests: 74/74; eleven mutations each caught; `nlg --lang en` read; roadmap units moved (44/44 encoded, validator ok).
- [x] Forks file `registers/parts/g6b.forks.json`: 23 entries (F-sweep-c-13, F-g6b-01 to -22); all 19 fork-register rules pass (wrapped in a register envelope); the validator's other 22 findings are forks sweep-c reserved for other groups.
- [x] Roadmap `registers/parts/g6b.roadmap.json`, every unit moved, validated.
- [x] `nlg --lang en` read for every tests module (no module rule renders bare); 271 record fields and enum constructors each have an own-line `@nlg:en` below, and a live render of three record literals shows them attaching.

## 1. What is encoded, and what is not

All 44 units of the range are `encoded` in `registers/parts/g6b.roadmap.json`: arts. 337-E–337-P, 338–359 (art. 350 as its revocation) and 359-A–359-H.
Every punishing provision has its case record, the predicate that its elements are made out (consummated and, where the execution can be stopped short, attempted), its pena cominada as a `Pena cominada` constant checked against the preceito's words, its causes of increase or decrease as constants with an `incide …` predicate and a listing function, and a function giving the pena for a case where there is more than one preceito or a vigência gate.
Every exported rule carries `@export`, `@desc` on its inputs, `@ref` and an `@nlg:en` herald.

**Vigência** (PLAN § 10), each date from the amending law's own clause, read on Planalto (§ 7):

| provision | law | from | before it |
| --- | --- | --- | --- |
| Cap. II-B, arts. 337-E–337-P | Lei 14.133/2021 (inserted) | 1.4.2021 | the article does not apply (law's answer) |
| art. 338-A | Lei 15.280/2025 (inserted) | 8.12.2025 | does not apply |
| art. 339, caput | Lei 14.110/2020 (re-worded) | 21.12.2020 | the crime REFUSES (earlier wording not in the source) |
| arts. 342 (caput, §§ 1º–2º) and 343 | Lei 10.268/2001 (re-worded) | 29.8.2001 | every rule REFUSES |
| art. 342, pena | Lei 12.850/2013 (re-worded) | 19.9.2013 (45 days, LC 95/1998 art. 8º § 1º) | the pena REFUSES; the crime is decided |
| art. 344, parágrafo único | Lei 14.245/2021 (added) | 23.11.2021 | the increase does not apply |
| art. 349-A | Lei 12.012/2009 (inserted) | 7.8.2009 | does not apply |
| art. 350 | revoked by Lei 13.869/2019 | 3.1.2020 (120 days) | REFUSES (its text is not in the source); after, no crime |
| Cap. IV, arts. 359-A–359-H | Lei 10.028/2000 (inserted) | 20.10.2000 | does not apply |

The rest is the 1940 text (its fines' amounts cancelled by Lei 7.209/1984, art. 2º) and answers for any date.
Each gate is asserted directly on the first day and the day before (PLAN trap T5).

**Not encoded, deliberately:**

- The wordings before the re-writings above (not in the source; named refusals).
- Art. 327 (who is a funcionário público) is g6a's: since integration (2026-09-30, ruling F-g6a-23) art. 351, § 4º calls g6a's owner rule `funcionário público para os efeitos penais (art. 327)` (fork F-g6b-14). Art. 327, § 2º's increase reaches none of my chapters (F-g6b-01).
- The procurement and public-finance laws the Code's blanks point to (Lei 14.133/2021's cases of dispensa, the limits "estabelecido em lei ou em resolução do Senado", "despesa total com pessoal"): their answers are inputs.
- Ação penal: only art. 345 states one; elsewhere art. 100 (g1c's) governs and nothing is written.
- Insignificância: inapplicable in Título XI (Súmula 599 STJ, M-sweep-c-15, fork F-sweep-c-10, created by g6a); no g6b offence takes the finding.

## 2. Modules

| module | articles | tests | asserts |
| --- | --- | --- | --- |
| `cp-g6b-comum.l4` | none: the attempt over cp-dominio's `Execução do crime` (art. 14 II's facts), `Processo ou procedimento`, `Pessoa que funciona no processo` | `cp-g6b-comum-testes.l4` | 20 |
| `cp-g6b-licitacoes.l4` | 337-E–337-P | `cp-g6b-licitacoes-testes.l4` | 99 |
| `cp-g6b-justica-reingresso-a-coacao.l4` | 338–344 | `…-testes.l4` | 116 |
| `cp-g6b-justica-exercicio-arbitrario-a-desobediencia.l4` | 345–359 | `…-testes.l4` | 118 |
| `cp-g6b-financas-publicas.l4` | 359-A–359-H | `…-testes.l4` | 74 |

Positive control: 43 single mutations over the four article modules (8, 10, 14 and 11), each run in a scratch copy with the verdicts counted from the tool's output and the total checked to account for every `#ASSERT`; every one made at least one test fail.

## 3. The forks, in prose

24 entries in `registers/parts/g6b.forks.json`. One is settled by an authority, one is open, the rest were resolved by g6b on argument; three are executable interpretation fields.

| id | question | taken |
| --- | --- | --- |
| F-sweep-c-13 | Is art. 337-F formal? | **settled**: yes (Súmula 645 STJ, 2021, on art. 90 of Lei 8.666/1993, whose conduct and intent 337-F restates; M-sweep-c-21) |
| F-g6b-01 | Does art. 327 § 2º's increase reach Caps. II-B, III, IV? | no: "neste Capítulo" is Cap. I |
| F-g6b-02 | 337-E "fora das hipóteses previstas em lei" | the judge's finding on the procurement law (delegated) |
| F-g6b-03 | 337-L "em prejuízo da Administração": result or aim? | result (material); Súmula 645's formal reading is arguable via the heading "Fraude em licitação" |
| F-g6b-04 | 337-P's 2% floor above art. 49's largest fine | **open**: the combined check refuses; a double bind in the text |
| F-g6b-05 | "violência" in 337-K, 345 p.ú., 358 | against the person |
| F-g6b-06 | which offences take an attempt | where the execution can be stopped short; not the "tentar" offences, pure omissions, 337-G, 354, 351 § 4º |
| F-g6b-07 | 339 § 2º's contravenção against a caput that names only crime, infraction, ato ímprobo | § 2º extends the crime (privileged form) |
| F-g6b-08 | does 342 § 2º's retraction reach art. 343? | no |
| F-g6b-09 | are the prosecution's investigations (PIC, inquérito civil) "processo administrativo" (342, 344, 347)? | no: art. 339 (2020) names them separately |
| F-g6b-10 | "as penas" (plural) and the fine (342 § 1º, 343 p.ú., 347 p.ú., 357 p.ú.) | the increase reaches the fine; nothing here computes dias-multa |
| F-g6b-11 | 348 § 2º "cônjuge" and the companheiro | as written: not exempt (the other reading is live) |
| F-g6b-12 | 348: is "reclusão ou detenção" "cominada pena de reclusão"? | yes |
| F-g6b-13 | 351 § 1º "a mão armada" | any weapon, an object used as one included |
| F-g6b-14 | 351 § 4º "funcionário" | art. 327 caput and § 1º, by g6a's owner rule since integration |
| F-g6b-15 | 352 "o preso", without 351's "legalmente" | as written: legality not required |
| F-g6b-16 | 354: how many make a motim? | two or more |
| F-g6b-17 | 358: do the means qualify both figures? | only the second (the semicolon) |
| F-g6b-18 | 359-C "dois últimos quadrimestres do último ano do mandato" | **interpretation field**, TYPICALLY 1 May–31 Dec of the last financial year within the term; the other: the eight months ending on the term's last day |
| F-g6b-19 | 359-C's contrapartida clause | **interpretation field**, TYPICALLY: cash for the carried-over part takes the obligation out (the other reading leaves the clause idle) |
| F-g6b-20 | 359-G "cento e oitenta dias anteriores ao final do mandato" | **interpretation field**, TYPICALLY the 180 days ending on the last day, included |
| F-g6b-21 | 359-C, 359-G: whose term? | the fact supplier's (delegated) |
| F-g6b-22 | 337-O's heading "por projetista" | adds no element; the three contracting contexts do the confining |
| F-g6b-23 | 351: can the fugitive be the agent? | no: art. 351 is another's escape; the prisoner's own is art. 352's when violent (the other reading would punish a peaceful escape more than a violent one) |

Where I looked for ambiguity: every preceito's words against its neighbours' (the retraction, family-exemption and "legalmente" clauses differ between neighbours and are encoded as each is worded), every threshold word ("exceda", "ultrapassa", "superior", "igual ou superior", "mais de uma"), every list of persons or proceedings, every count of time.

## 4. Sweep entries acted on (sweep-c)

| entry | what g6b did |
| --- | --- |
| M-sweep-c-21 (Súmula 645, interpretive) | fork **F-sweep-c-13** created under the reserved id, settled, entry in `settled_by.external_modification`; cross-ref on F-g6b-03 |
| M-sweep-c-15 (Súmula 599, interpretive) | no insignificância input on any g6b offence; cited in every module header; fork F-sweep-c-10 is g6a's (cross-referenced, not duplicated) |
| M-sweep-c-24 (jurisdiction súmulas, no effect; Súmula 165 on falso testemunho) | cited at arts. 338–344's header; changes no element or penalty |
| S-sweep-c-04 (2025–2026 vigências) | 8.12.2025 for art. 338-A (Lei 15.280/2025) |

No binding entry touches arts. 337-E–359-H. Re-read on 2026-09-30: the entries added since (M-sweep-c-28 to -32) concern arts. 337-A, 273, 288, 259 and 253, none of mine.
Fork F-g6a-15 (g6a's: arts. 326 and 335 overlap arts. 337-J, 337-I and 337-K) is cited in the Cap. II-B header; mine are encoded as printed, consistently with its taken reading.

## 5. Proposed shared nouns

- `Execução`: adopted at integration (2026-09-30) as cp-dominio's `Execução do crime`; `cp-g6b-comum.l4` keeps only the attempt predicate over it.
- Nothing is proposed for `cp-dominio.l4` beyond that. `Processo ou procedimento` and `Pessoa que funciona no processo` stay group nouns: no article outside my range lists these kinds of proceeding (a search of the source for them found only "processo" in other senses).

## 6. What `check.sh` prints

`L4=/Users/mengwong/.claude/br-penal-toolchain/l4 ENC/check.sh ENC cp-g6b-`, 2026-10-08, after the four fixes of § 10, exit 0:

```
module                                        errors satisfied  failed refused asserts
cp-g6b-comum-testes.l4                             0        20       0       0      20
cp-g6b-comum.l4                                    0         0       0       0       0
cp-g6b-financas-publicas-testes.l4                 0        74       0       0      74
cp-g6b-financas-publicas.l4                        0         0       0       0       0
cp-g6b-justica-exercicio-arbitrario-a-desobediencia-testes.l4       0       118       0       0     118
cp-g6b-justica-exercicio-arbitrario-a-desobediencia.l4       0         0       0       0       0
cp-g6b-justica-reingresso-a-coacao-testes.l4       0       116       0       0     116
cp-g6b-justica-reingresso-a-coacao.l4              0         0       0       0       0
cp-g6b-licitacoes-testes.l4                        0        99       0       0      99
cp-g6b-licitacoes.l4                               0         0       0       0       0
TOTAL (10 modules)                                 0       427       0       0     427
(a failed assertion also counts as an error; errors minus failed = everything else)
```

On 2026-09-30 the same command printed 411/411 (exercicio 113, reingresso 110, licitações 94); the 16 new assertions are § 10's.

Every module has as many verdicts as `#ASSERT` lines, and none refused. The `#ASSERT REFUSED` lines count as satisfied when the refusal comes with the named message.

## 7. Searches relied on

All fetched from Planalto (`https://www.planalto.gov.br/ccivil_03/…`) on 2026-09-29/30 into the scratch directory `g6b/laws/`, and read at the vigência clause; publication dates from `SOURCE/senado-dadosabertos-527942.xml`.

| law | clause read | DOU | in force |
| --- | --- | --- | --- |
| Lei 10.028/2000 | art. 6º "na data de sua publicação" | 20.10.2000 | 20.10.2000 |
| Lei 10.268/2001 | art. 2º, same | 29.8.2001 | 29.8.2001 |
| Lei 12.012/2009 | art. 3º, same | 7.8.2009 | 7.8.2009 |
| Lei 12.850/2013 | art. 27 "após decorridos 45 (quarenta e cinco) dias de sua publicação oficial"; art. 25 re-wrote art. 342's pena | 5.8.2013 (extra) | 19.9.2013 |
| Lei 13.869/2019 | art. 44 revokes art. 350; art. 45 "após decorridos 120 (cento e vinte) dias" | 5.9.2019 (extra) | 3.1.2020 |
| Lei 14.110/2020 | art. 2º "na data de sua publicação" | 21.12.2020 | 21.12.2020 |
| Lei 14.133/2021 | art. 194, same; art. 193, I revokes Lei 8.666 arts. 89–108 "na data de publicação" | 1.4.2021 (extra) | 1.4.2021 |
| Lei 14.245/2021 | art. 5º, same | 23.11.2021 | 23.11.2021 |
| Lei 15.280/2025 | art. 7º, same (sweep-c's S-sweep-c-04 agrees) | 8.12.2025 | 8.12.2025 |
| LC 95/1998 | art. 8º, § 1º: the day of publication and the last day are counted; in force the next day | — | — |
| Lei 8.666/1993 | arts. 90 and 96, for F-sweep-c-13 and F-g6b-03 | — | revoked |

The two vacatio counts are asserted in the tests: `(YMD 2019 9 5) PLUS 120` is 3.1.2020, and `(YMD 2013 8 5) PLUS 45` was checked to be 19.9.2013 by a probe.

## 8. For the conductor

- **Senado index error**: the Senado record indexes Lei 14.133/2021's insertion as "Art. 377-E" to "Art. 377-P" and omits 337-L (it should be 337-E to 337-P).
- **cp-pena's `o último dia do prazo` is wrong for periods the Code counts in days**: it reads `dias 180` as six calendar months (asserted: from 5.7.2026 it gives 4.1.2027; 180 calendar days end on 31.12.2026). Correct for art. 10's months and years and for dosimetry; a trap for anyone counting a tipo's days with it. Cap. IV counts days by date arithmetic instead.
- **`TYPICALLY` with a user enum constructor** is accepted on a `GIVEN` parameter and rejected on a record field ("must be a literal … could not find a definition"), on the 29 September binary. Phrasebook entry 1.5 says a constructor of your own `ONE OF` type is accepted; that held only for parameters then. The three interpretation fields are therefore parameters of the exported rules.
  Re-probed 2026-10-12: the same construct on a record field (g1b's `cp-g1b-sonda-typically-enum.l4`) checks on `l4-1008` and on a reference-checkout build of 11 October; see `notes/g1b.md` section 8.
  The g6b fields were not rewritten as record fields, and nothing needs it.
- **Art. 327 at art. 351, § 4º**: replaced at integration by g6a's owner rule (ruling F-g6a-23); nothing owed.
- **Roadmap titles corrected** where the mechanical enumeration took a neighbour's line: arts. 337-E–337-O (the amendment note), 343, 346, 349-A (no heading in the source), 359-C, 359-G (a pena line).
- **check.sh's transient double count** (~21:00 on 2026-09-29) was seen and not acted on; the counts above are from the fixed script.
- **No failing assertion**; nothing is expected to fail.
- **Findings about the Code itself**: art. 337-P's floor and art. 49's ceiling cannot both be met for contracts above R$ 135 million at a R$ 1.500 minimum wage (R$ 405 million with art. 60 § 1º's trebling): F-g6b-04. Art. 339 § 2º reduces a penalty for a case its caput does not name: F-g6b-07. Art. 359-C's contrapartida clause is idle on its literal reading: F-g6b-19.

## 9. Open questions for a Brazilian criminal lawyer

1. Art. 337-P against art. 49: which gives way when 2% of the contract exceeds the largest fine? (F-g6b-04)
2. Art. 337-E: do the courts still require, as some did under Lei 8.666's art. 89, a specific intent to harm the treasury and an actual loss? The text has neither. (F-g6b-02, notes)
3. Art. 337-L: is it material ("em prejuízo") or formal like 337-F? Does Súmula 645 reach it? (F-g6b-03)
4. Art. 342: does lying in a prosecutor's investigation (PIC, inquérito civil) fall under "processo ... administrativo"? (F-g6b-09)
5. Art. 348, § 2º: is the companheiro exempt? (F-g6b-11)
6. Art. 348: is a crime punished with "reclusão ou detenção" one "a que é cominada pena de reclusão"? (F-g6b-12)
7. Art. 352: must the imprisonment be lawful, as art. 351 says? (F-g6b-15)
8. Art. 351: a prisoner who instigates a third party to free him — does he take part in the third party's art. 351 (art. 29), or is his own escape, being atypical without violence, beyond it? The record describes only the agent's conduct and does not decide this. (F-g6b-23)
8. Art. 354: how many prisoners make a motim? (F-g6b-16)
9. Art. 359-C: which period is "os dois últimos quadrimestres do último ano do mandato" for a term ending on 5 or 6 January or 31 January? And does enough cash for the carried-over part take the obligation out? (F-g6b-18, F-g6b-19)
10. Art. 359-G: is the term's last day inside "os cento e oitenta dias anteriores ao final do mandato"? (F-g6b-20)
11. Arts. 359-C and 359-G: whose term — the agent's, or the head of the power's? (F-g6b-21)
12. Art. 345, parágrafo único: does violence against a thing make the prosecution public? (F-g6b-05)

## 10. Fixes after the independent test pass (ta-g6, 2026-10-08)

Four record-shape findings, each fixed in the record and tested; no earlier expectation changed.

- **Art. 351 (IT-g6-321).** The record gains `o fugitivo é o próprio agente`. The predicate `de pessoa legalmente presa ou submetida a medida de segurança detentiva, que não o agente (art. 351)` requires another person, and the intentional form, its attempt and § 4º's negligent form all read it (fork F-g6b-23). Tests: the lone escape, consummated and attempted, is not art. 351.
- **Arts. 342, 343 (IT-g6-272, IT-g6-284).** `Pessoa que funciona no processo` gains `parte no processo` and `pessoa sem função no processo`. Art. 342's list was already positive; art. 357's was `WHEN contador THEN FALSE OTHERWISE TRUE`, which would have admitted both new members, so it is now the eight named persons and OTHERWISE FALSE. Tests: a party and a no-role person, under arts. 342, 343 and 357.
- **Art. 344 (IT-g6-289).** `Processo ou procedimento` gains `nenhum processo ou procedimento`, which no article's list names. Tests: art. 344 consummated and attempted, and art. 342, with no proceeding.
- **Art. 337-P (IT-g6-247).** The combined check takes the crime (`Crime cuja multa se fixa`: arts. 337-E–337-O, 337-M as two entries, and `crime de fora do Capítulo II-B`) instead of a `Pena cominada`, reads the pena from it, and refuses a crime outside the chapter. The four existing calls pass `crime do art. 337-E` where they passed `pena do art. 337-E`; their expected values are unchanged.

**Dependant broken:** `cp-ind-g6-justica-exercicio-arbitrario-a-desobediencia.l4` (ta-g6's, not edited) builds the art. 351 record at lines 205–215 without the new field; it needs `` `o fugitivo é o próprio agente` IS FALSE ``.

**Positive controls, not run.** `~/.claude/br-penal-scratch/g6b/mut-fix4.py` copies the modules to scratch, runs a no-mutation baseline per tests module, then seven single mutants: M1 the agent may be the fugitive (expects 3 failed), M2 a party named by art. 342 (2), M3 art. 357 back to OTHERWISE TRUE (2), M4 art. 344 admits no proceeding (2), M5 art. 342 admits no proceeding (1), M6 the chapter test admits any crime (1), M7 the 337-P fix reverted (1). Under M6 the outside-chapter REFUSED test is expected to stay satisfied, because the pena lookup refuses on its own; M7 removes both.
