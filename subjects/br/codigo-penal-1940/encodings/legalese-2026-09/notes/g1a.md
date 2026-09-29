# g1a — Parte Geral, Títulos I–IV (arts. 1–31): notes for the reviewer

**Status (2026-09-29): all 31 roadmap units encoded; forks file written and validated; final check.sh in § 5.**

## PROGRESS

- [x] Read BRIEF.md, PLAN.md, the writing-l4-rules skill (SKILL.md, gotchas, drafting-patterns, all eleven source-pattern pages), encoding-a-subject.
- [x] Read cp-dominio.l4, cp-pena.l4, cp-g3-furto.l4 and its tests.
- [x] Read source lines 19–156 (arts. 1–31), sweep-a entries and proposed forks naming arts. 1–31, and the sweep-b/c entries that mention them.
- [x] Probe: `RULES EFFECTIVE DATE` works pinned (`EVAL UNDER RULES EFFECTIVE AT`), but unpinned it needs a document `TIMEZONE` and then reads the wall clock. Not used; ADPF 779's arm takes an explicit decision date instead (fork F-g1a-06).
- [x] Título I (arts. 1–9, 12): `cp-g1a-aplicacao.l4` + `cp-g1a-aplicacao-testes.l4`. 95/95. Mutations 10/10 (+1 rewritten) caught.
- [x] Título II, arts. 13, 15–19: `cp-g1a-crime.l4` + `cp-g1a-crime-testes.l4`. 59/59. Mutations 12/12 caught.
- [x] Título II, arts. 23–25 (ADPF 779 arm): `cp-g1a-ilicitude.l4` + `cp-g1a-ilicitude-testes.l4`. 37/37. Mutations 12/12 caught.
- [x] Título II, arts. 20–22: `cp-g1a-erro.l4` + `cp-g1a-erro-testes.l4`. 28/28. Mutations 9/9 caught.
- [x] Título III (arts. 26–28): `cp-g1a-imputabilidade.l4` + `cp-g1a-imputabilidade-testes.l4`. 26/26. Mutations 8/8 caught after one test was added (§ 5).
- [x] Título IV (arts. 29–31): `cp-g1a-concurso.l4` + `cp-g1a-concurso-testes.l4`. 31/31. Mutations 9/9 caught.
- [x] Roadmap: 31 encoded, 0 inert, 0 out-of-scope, 0 deferred; `register-validate.mjs encoding-roadmap` ok.
- [x] Forks: `registers/parts/g1a.forks.json`, 25 entries; validator: no finding in this file (§ 2).
- [x] nlg --lang en on every tests module: no rule renders as a bare name.
- [x] Every quotation in a comment checked verbatim against the source, split at dispositivos: 179 pieces, 2 misquotes found and fixed.

## 1. What is encoded, and what is not

Six modules, one per run of related articles (the Parte Geral's Títulos I–IV have no chapters), each with its tests module:

| module | articles | exported entry points |
| --- | --- | --- |
| `cp-g1a-aplicacao.l4` | 1–9, 12 | `a lei que rege o fato (arts. 1º a 4º)`, `a redação alcança o fato (arts. 2º e 4º)`, `a extraterritorialidade (art. 7º)`, `a lei brasileira se aplica ao crime (arts. 5º a 7º)`, `o efeito da pena cumprida no estrangeiro (art. 8º)`, `a sentença estrangeira pode ser homologada (art. 9º)` |
| `cp-g1a-crime.l4` | 13, 15–19 | `a imputação do resultado (art. 13)`, `o desfecho da execução (arts. 14, 15 e 17)`, `as causas de diminuição cabíveis (art. 16)`, `o fato é punível quanto ao elemento subjetivo (art. 18, parágrafo único)`, `o agente responde pelo resultado que agrava especialmente a pena (art. 19)` |
| `cp-g1a-ilicitude.l4` | 23–25 | `o efeito das excludentes de ilicitude (art. 23)`, `não há crime (art. 23)`, `as causas de diminuição cabíveis (art. 24, § 2º)` |
| `cp-g1a-erro.l4` | 20–22 | `o efeito do erro (art. 20)`, `a vítima cujas condições se consideram (art. 20, § 3º)`, `o efeito do erro sobre a ilicitude (art. 21)`, `as causas de diminuição cabíveis (art. 21)`, `só é punível o autor da coação ou da ordem (art. 22)` |
| `cp-g1a-imputabilidade.l4` | 26–28 | `a imputabilidade do agente (arts. 26 a 28)`, `o agente é isento de pena por inimputabilidade (arts. 26 a 28)`, `as causas de diminuição cabíveis (arts. 26 e 28)` |
| `cp-g1a-concurso.l4` | 29–31 | `a pena cominada ao concorrente (art. 29)`, `as causas do concorrente (art. 29, §§ 1º e 2º)`, `a circunstância se comunica aos demais concorrentes (art. 30)`, `o ajuste, a determinação ou instigação e o auxílio não são puníveis (art. 31)` |

Arts. 10, 11 and 14 are g0's, in `cp-pena.l4`; `cp-g1a-crime.l4` calls art. 14's rules.

Every article is re-enacted text of Lei nº 7.209/1984 except art. 25's parágrafo único (Lei nº 13.964/2019). No vigência gate is needed anywhere: the one recent paragraph demands the caput's requisites, so it makes no fact worse (fork F-g1a-10). The only dated arm is ADPF 779's.

**Not encoded, deliberately:**

- The reading of arts. 23, II and 25 before ADPF 779 (1.8.2023), for the "legítima defesa da honra" thesis only: `a situação de legítima defesa (art. 25)` refuses by name for a decision before that date where the thesis is invoked.
- How far a different penalty served abroad attenuates (art. 8º): the judge's; the rule refuses by name. The deduction of a fine, which is money, not time.
- Which court homologates a foreign sentence (art. 9º): procedure (the STJ since EC 45/2004).
- What the special legislation does with minors (art. 27), and the medidas de segurança that follow art. 26 (arts. 96–98, g1c's).
- The judge's choices inside a range, and the comparison of whole laws under art. 2º, parágrafo único: inputs or listed options, never computed.

**How the judge's decisions appear.** Findings the Code leaves to the fact-finder are record fields in the Code's own words (`o erro deriva de culpa`, `agressão atual ou iminente`, `participação de menor importância, segundo o juiz`). Discretions ("pode", "poderá") are returned as causes that are `cabível`, never applied (fork F-g1a-13). Outcomes that the Code names are total enums whose members carry the article (`isento de pena (art. 20, § 1º)`, `rege a lei posterior mais favorável (art. 2º, parágrafo único)`).

### For the Parte Especial encoders, at integration

PLAN § 1 lets no group import another's module today, so these are for the conductor to wire:

- `a redação alcança o fato (arts. 2º e 4º)`: every penalty rule gated on a recent re-wording. cp-g3-furto's gate is its first half; the second half (a milder new wording reaches earlier facts) matters wherever a 2025–2026 law LOWERED a penalty. M-sweep-c-11 (art. 217-A § 4º-A) is the kind of case it answers.
- `o desfecho da execução (arts. 14, 15 e 17)`: every offence that admits an attempt. It adds art. 15 (desistance) and art. 17 (impossible crime, Súmulas 145 STF and 567 STJ) to art. 14.
- `o resultado é imputável ao agente (art. 13)` and `o agente responde pelo resultado que agrava especialmente a pena (art. 19)`: result crimes and forms qualified by result.
- `não há crime (art. 23)`: every offence; it takes the date of the decision (ADPF 779).
- `a vítima cujas condições se consideram (art. 20, § 3º)`: before reading a quality of the victim. g1b's arts. 73–74 send the aberratio ictus to it.
- `o agente é isento de pena por inimputabilidade (arts. 26 a 28)` and `as causas de diminuição cabíveis (arts. 26 e 28)`.
- `a circunstância se comunica aos demais concorrentes (art. 30)`: arts. 312 (funcionário público) and 181 (kinship), among others.

## 2. The forks, in prose

25 entries in `registers/parts/g1a.forks.json`: two carry the ids sweep-a reserved; 23 are `F-g1a-NN`. Four are settled by an authority, one is open, twenty are resolved on argument (of which seven are delegated to the fact-finder's finding).

| id | question | taken | status |
| --- | --- | --- | --- |
| F-sweep-a-06 | the law of a crime permanente or continuado when the law changes (arts. 2, 4, 71) | the law in force at the cessation, even if harsher | **settled**, STF Súmula 711 (M-sweep-a-16) |
| F-sweep-a-07 | art. 17 and the police: flagrante preparado, surveillance | prepared flagrante is impossible crime; surveillance alone is not | **settled**, STF Súmula 145 (M-sweep-a-18), with STJ Súmula 567 (M-sweep-a-19, M-sweep-b-33) |
| F-g1a-01 | art. 2: does an intermediate law (in force only between fact and decision) count | yes, any later law | resolved |
| F-g1a-02 | art. 2, p.ú.: may favourable parts of two laws be combined | no, whole laws only | **settled**, STJ Súmula 501 (not in the sweep; read in a secondary compilation) |
| F-g1a-03 | art. 3 against the constitutional lex mitior | art. 3 as printed; the other reading arguable | resolved |
| F-g1a-04 | art. 5, § 1º: "espaço aéreo correspondente" | the airspace over the high seas | resolved |
| F-g1a-05 | art. 8: "idênticas" | the same kind among art. 32's three | resolved |
| F-g1a-06 | which date ADPF 779's arm is keyed on | the date of the decision; before it, the thesis refuses | resolved |
| F-g1a-07 | art. 15: voluntary, or spontaneous | voluntary suffices (art. 65, III, b says "espontânea" where it means it) | resolved, delegated |
| F-g1a-08 | art. 16: "até o recebimento" | the day of receipt is in time | resolved |
| F-g1a-09 | art. 16: partial reparation | a whole reparation only | resolved, delegated |
| F-g1a-10 | art. 25, p.ú.: new case or declaratory | declaratory (it demands the caput's requisites) | resolved |
| F-g1a-11 | art. 24: "que não provocou por sua vontade" and negligent provocation | the Code's words, the fact-finder decides | resolved, delegated |
| F-g1a-12 | art. 23, p.ú.: an excess with neither dolo nor culpa | not punished | resolved |
| F-g1a-13 | "pode"/"poderá" in arts. 21, 24 § 2º, 26 p.ú., 28 § 2º, 29 § 1º: power or right | recorded, not built in: the causes are listed as available | **open** |
| F-g1a-14 | art. 20, § 1º: a culpable putative justification where there is no culposo form | not punishable (read with the caput) | resolved |
| F-g1a-15 | art. 22: "superior hierárquico" | public hierarchy | resolved, delegated |
| F-g1a-16 | art. 26: a disturbance that took all capacity; an illness that took some | the text's pairing; the first goes to the p.ú. | resolved |
| F-g1a-17 | art. 31: does a crime the executor abandoned "chegar a ser tentado" | no: "tentado" is art. 14, II's word | resolved |
| F-g1a-18 | art. 29, § 1º: participant only, or co-author too | participant (the judge's finding) | resolved, delegated |
| F-g1a-19 | art. 29, § 2º: which crime is "menos grave" | by pena cominada, as F-g0-18 | resolved |
| F-g1a-20 | art. 30: must the participant know the elementary circumstance | art. 30 as printed; ignorance is art. 20's error | resolved (extensionally equivalent) |
| F-g1a-21 | art. 16: which violence bars it | violence or grave threat used against a person as the means | resolved |
| F-g1a-22 | art. 24: "perigo atual" and an imminent danger | the Code's word; the fact-finder decides | resolved, delegated |
| F-g1a-23 | art. 7: nationality at what time | at the time of the crime | resolved, delegated |

Where I looked for ambiguity: every article's words against its neighbours' (arts. 24 and 25 on "atual"; art. 15 against art. 65, III, b; art. 22 against art. 65, III, c; art. 31 against art. 14, II; art. 20's caput against its § 1º), every threshold and every date, and every place the Code hands something to the judge.

**Validation.** Wrapped in a register envelope, `register-validate.mjs fork-register` against a merge of sweep-a and sweep-b as peer: 19 rules checked, no finding in this file. The findings it prints are the peers' reserved ids that other encoders own (F-sweep-a-01–05, 08–19; F-sweep-b-*); F-sweep-a-06 and -07 resolve. `M-sweep-b-33` (a cross-ref in F-sweep-a-07) resolves only with sweep-b as peer.

## 3. Sweep entries acted on

| entry | class | what g1a did |
| --- | --- | --- |
| M-sweep-a-01 | binding, read-down (ADPF 779) | **implemented** the rule-version arm "arts. 23, II, e 25 lidos conforme ADPF 779 (2023-08-01)" as `a situação de legítima defesa (art. 25)` in `cp-g1a-ilicitude.l4`, citing the entry in its header and `@ref`s; it reaches art. 20, § 1º through `cp-g1a-erro.l4`. Fork F-g1a-06 on the date axis. |
| M-sweep-a-16 | interpretive (Súmula 711 STF) | created **F-sweep-a-06**, settled; `o dia que fixa a lei aplicável (art. 4º; Súmula 711 STF)` |
| M-sweep-a-18 | interpretive (Súmula 145 STF) | created **F-sweep-a-07**, settled; third limb of `crime impossível (art. 17)` |
| M-sweep-a-19 | interpretive (Súmula 567 STJ) | cross-ref in F-sweep-a-07; the surveillance field is deliberately not read, and a test says so |
| M-sweep-b-33 | interpretive, subsumed (Súmula 567 at art. 155) | cross-ref in F-sweep-a-07 |
| M-sweep-a-37 | interpretive, scoped out (Súmula 338 STJ) | noted at art. 27; the ECA is outside the encoding |

Read and left for their owners: M-sweep-a-07 (Lei 7.209 art. 2º, the Parte Especial's fines), M-sweep-a-08 and M-sweep-c-09 (arts. 69–70, g1b and Título XII), M-sweep-b-24 (Súmula 582, roubo's consummation, g3), M-sweep-c-11 (art. 217-A's lex mitior question, g4a; `a redação alcança o fato (arts. 2º e 4º)` is the rule it needs). Sweep-a's search log says no 2025–2026 law touched arts. 1–120; the source agrees for arts. 1–31 (every line but art. 25 p.ú. is "Redação dada pela Lei nº 7.209").

## 4. Proposed shared nouns (PROPOSTO-COMUM)

Marked in the modules; the conductor decides whether to hoist them into `cp-dominio.l4`:

- `Execução do crime`, with `Até onde chegou a execução` and `Por que a execução iniciada não se consumou` (`cp-g1a-crime.l4`): every offence that admits an attempt. **g5 declared its own `Estágio da execução` for the same purpose** (seen in the first 40 lines of `cp-g5-comum.l4`, which I printed by accident while listing the directory — I read nothing else of it and used nothing from it). Keep one.
- `Conduta e resultado` (art. 13) and `Elemento subjetivo` (art. 18) (`cp-g1a-crime.l4`).
- `Situação justificante` and its parts (`cp-g1a-ilicitude.l4`).
- `O agente ao tempo da ação ou da omissão` (`cp-g1a-imputabilidade.l4`).

Nouns used only in this range stay local: `Lei penal no tempo`, `Fato no tempo`, `Veículo`, `Lugar`, `Lugar do crime`, `Crime cometido no estrangeiro`, `Pena cumprida no estrangeiro`, `Pedido de homologação de sentença estrangeira`, `Erro do agente`, `Consciência da ilicitude`, `Coação ou ordem`, `Concorrente`, `Circunstância ou condição`. Nationality is a field of `Crime cometido no estrangeiro`, not of the shared `Agente`.

A duplicate to reconcile: `a primeira pena é menos grave que a segunda` (art. 29, § 2º) restates F-g0-18's measure of the heavier pena, which lives in g3's `cp-g3-furto.l4` (`a mais grave das penas`) and again, per g5's header, in `cp-g5-comum.l4`.

## 5. What check.sh prints

`L4=/Users/mengwong/.claude/br-penal-toolchain/l4 ./check.sh . cp-g1a-`, run from the encoding directory, 2026-09-29, after the last edit to any g1a module (exit status 0):

```
module                                        errors satisfied  failed refused asserts
cp-g1a-aplicacao-testes.l4                         0        95       0       0      95
cp-g1a-aplicacao.l4                                0         0       0       0       0
cp-g1a-concurso-testes.l4                          0        31       0       0      31
cp-g1a-concurso.l4                                 0         0       0       0       0
cp-g1a-crime-testes.l4                             0        59       0       0      59
cp-g1a-crime.l4                                    0         0       0       0       0
cp-g1a-erro-testes.l4                              0        28       0       0      28
cp-g1a-erro.l4                                     0         0       0       0       0
cp-g1a-ilicitude-testes.l4                         0        37       0       0      37
cp-g1a-ilicitude.l4                                0         0       0       0       0
cp-g1a-imputabilidade-testes.l4                    0        26       0       0      26
cp-g1a-imputabilidade.l4                           0         0       0       0       0
TOTAL (12 modules)                                 0       276       0       0     276
(a failed assertion also counts as an error; errors minus failed = everything else)
```

Every tests module's `#ASSERT` count equals its satisfied count; nothing refused, nothing unaccounted.

**Mutations** (positive controls, one at a time on scratch copies, harness in the session scratchpad; each run's unmutated baseline row reproduces the module's satisfied count, so the harness observes the run — its first version read stdout only and reported 0 for everything, including the baseline):

| module | mutations | caught |
| --- | --- | --- |
| aplicacao | 11 (vigência first day, art. 3's exception, Súmula 711, § 2º's private-only, § 2º d), § 3º b), art. 8 deduction, art. 9 request, lex mitior filter, intermediate law) | 11 |
| crime | 12 (§ 1º, § 2º "podia", omission relevance, surveillance counted, Súmula 145 dropped, art. 16 grave threat, art. 16 receipt day, art. 16 fraction, dolo eventual, art. 18 p.ú., art. 19 causation, desistance arm) | 12 |
| ilicitude | 12 (ADPF arm dropped — caught as 3 refused, which check.sh now fails on —, ADPF date strict, pre-ADPF refusal, art. 24 § 1º, provocation, § 2º, moderation, "atual", p.ú. unbound, excess modality swapped, "estrito", excess without situation) | 12 |
| erro | 9 | 9 |
| imputabilidade | 8 | 7, then 8: "completa" in art. 28, § 1º was not caught until a test for an incomplete accidental intoxication with no capacity left was added |
| concurso | 9 (§ 1º finding, § 1º fraction, § 2º foreseeability, § 2º fraction up to double, § 2º less-grave check, art. 30 elementar, art. 31 desistance counted as tentado, art. 31 express provision, art. 31 extended to executors) | 9 |

## 6. Open questions for a Brazilian criminal lawyer

1. "Pode"/"poderá" in arts. 21, 24 § 2º, 26 p.ú., 28 § 2º and 29 § 1º: once the requirements are met, must the judge reduce? Is the answer the same for all five? (F-g1a-13)
2. ADPF 779: does the reading-down bind from the merits acórdão (1.8.2023) or from the medida cautelar? Does it apply to decisions after it on facts before it? (F-g1a-06)
3. Art. 20, § 1º: where the putative justification comes from an avoidable error and the crime has no culposo form, is the agent unpunished (teoria limitada) or punished for the doloso crime with art. 21's reduction? (F-g1a-14)
4. Art. 26: a disturbance of mental health that is not an illness but took all capacity — caput or parágrafo único? (F-g1a-16)
5. Art. 31: does the executor's voluntary desistance leave the instigator and the helper unpunished? (F-g1a-17)
6. Art. 29, § 1º: can a co-author have a "participação de menor importância"? (F-g1a-18)
7. Art. 16: does a whole reparation remain required, and does art. 16 reach negligent crimes with a violent result? (F-g1a-09, F-g1a-21)
8. Art. 3º: is the ultra-activity of temporary laws compatible with CF art. 5º, XL? Has the STF said so? (F-g1a-03)
9. Art. 24: does "por sua vontade" bar a danger caused by negligence, and does "perigo atual" include an imminent one? (F-g1a-11, F-g1a-22)

## 7. For the conductor

- **Traps met, beyond PLAN § 12.**
  - A constructor that carries fields (`X HAS f IS A T`) takes a herald only if the name stands alone on its line, the herald below it, and `HAS` on the NEXT line; a herald below a `X HAS f …` line goes to the field, and the constructor renders bare, with no diagnostic. Probe in the session scratchpad (`g1a/sonda-construtor-nlg.l4`).
  - A constructor and a function may share one name and type-check (resolved by type); `nlg` then renders the constructor with the function's herald. Silent; renamed mine.
  - PLAN's T1 bit twice in test helpers (`em`, `a` as both keyword segment and parameter), and a helper whose head was also the name of a constant failed with "multiple definitions for `__EQUALS__`" at every use.
- **Roadmap titles.** The mechanical titles in `g1a.roadmap.json` are shifted for three units: art. 14 is titled "Relevância da omissão" (art. 13 § 2º's heading), art. 18 "Crime impossível" (art. 17's), art. 29 "DO CONCURSO DE PESSOAS" (the Título's). Left as generated; the conductor owns them.
- **An authority the sweep did not list:** STJ Súmula 501 (combination of laws), which settles F-g1a-02. sweep-a may want it as an interpretive entry.
- **Rules that take a date the shared records lack.** Art. 23's rules take `a data da decisão` (ADPF 779); art. 2º's take `a data da apreciação`. Neither is a fact of the case, so neither is a field.
- **cp-g5-comum.l4.** I printed its first 40 lines by accident (§ 4). Nothing from it is used.
