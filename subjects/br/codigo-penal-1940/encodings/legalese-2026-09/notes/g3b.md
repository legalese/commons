# g3b — arts. 184–212: notes for the reviewer

**Status (2026-09-29): done. Every article in scope encoded (18) or revoked and out of scope (11); 331 of 331 assertions satisfied; 24 of 24 mutations caught.**
Parte Especial Títulos III (propriedade imaterial), IV (organização do trabalho) and V (sentimento religioso e respeito aos mortos).

## PROGRESS

- [x] Read BRIEF.md, PLAN.md, the `writing-l4-rules` skill (SKILL.md, gotchas, drafting-patterns, all eleven source-pattern pages), `encoding-a-subject`, `cp-dominio.l4`, `cp-pena.l4`, `cp-g3-furto.l4` and its tests.
- [x] Read arts. 184–212 in `SOURCE/codigo-penal-1940.txt` (lines 1404–1518) and the Senado metadata rows for them.
- [x] Read sweep-b (entries, searches, dispositions, proposed forks). No reserved fork falls in 184–212. Entries on the range: M-sweep-b-37, M-sweep-b-38.
- [x] Fetched from Planalto: the vigência clauses of Leis 10.695/2003, 9.777/1998 and 8.683/1993; Lei 9.610/1998 arts. 1º, 46 and 115; Lei 9.609/1998 art. 12; LC 95/1998 art. 8º; CF arts. 9º, 109 VI, 227 § 1º II; Lei 7.783/1989 arts. 11, 14, 15.
- [x] `cp-g3b-comum.l4` (the stage of execution; helpers).
- [x] Título III: `cp-g3b-propriedade-imaterial.l4` + tests.
- [x] Título IV: `cp-g3b-organizacao-do-trabalho.l4` + tests.
- [x] Título V: `cp-g3b-sentimento-religioso-e-mortos.l4` + tests.
- [x] Roadmap: 18 encoded, 11 out-of-scope, 0 deferred; validates.
- [x] Forks: 24 entries (F-g3b-01 to -24); validate (my entries clean).
- [x] English glosses: every rule of the four modules renders through its herald (§ 5).
- [x] Every quotation of the Code checked verbatim against the source (§ 5).
- [x] Mutation run (positive control): 24 single mutations, each caught by at least one failing assertion (§ 5).
- [x] Final `check.sh`: 0 errors, 331 satisfied, 0 failed, 0 refused, 331 asserts; exit 0 (§ 5).
- [x] Report sent to team-lead (2026-09-29).
- [x] 2026-10-08: added `ato lícito` to `Conduta contra o respeito aos mortos` so a lawful act on a grave, corpse or ashes can be recorded (F-g3b-25); six tests; check.sh 337 of 337.

- [x] 2026-10-08 (s-g3b2): art. 184 § 2º, first limb, now reads a knowledge finding (F-g3b-26); eight tests added; check.sh 345 of 345; positive control: removing the requirement fails 5 of the 98 assertions of the module. Changes, old -> new: (a) `Fato de violação de direito autoral` gains `o agente sabia que o original ou cópia fora reproduzido com violação de direito` (BOOLEAN, @nlg:en); (b) `violação de direito autoral qualificada do art. 184, § 2º`: the first limb was verbs AND `reproduzido com violação`, now also AND `o agente conhecia a violação na origem da cópia` (the finding OR the agent's own reproduction, `reprodução total ou parcial`); the rental limb is unchanged; (c) tests: `Achado` gains `ciente da pirataria`, the eight pirated-copy fixtures carry it, six new cases and eight new `#ASSERT`s (no existing `#ASSERT` changed). Checked and left alone: caput, § 1º, § 3º (the agent's own violation, reproduction or offering), the rental limb (see the fork), art. 186.

**Checkpoint (SAVESCUM, 2026-09-29).** Done: every unit of arts. 184–212 (18 encoded, 11 out-of-scope, 0 deferred; roadmap part validates). Half-done: nothing. Next: nothing in scope; await the conductor (F-g3b-10 open for a lawyer or the sweep). Last `check.sh` TOTAL, verbatim:
`TOTAL (7 modules)                                  0       331       0       0     331`

**On `notes/conductor.md`.** g3b read it at the start, before the conductor withdrew it as a private log. Nothing in it concerns arts. 184–212 beyond the count of an independent tester's cases, and no reading, fork or test here depends on it: every reading was made from the source and recorded as a fork.

## 1. What g3b encoded, and what it did not

Four modules (122, 523, 1,109 and 519 lines; PLAN § 1 asks for under about 1,500) and three test modules:

| module | articles | test module | `#ASSERT`s |
| --- | --- | --- | --- |
| `cp-g3b-comum.l4` | none: the art. 14 split, the heavier pena, the causes that apply | (exercised by the three below) | — |
| `cp-g3b-propriedade-imaterial.l4` | 184 (caput, §§ 1º–4º), 186 (I–IV); stubs for 185 and 187–196 | `cp-g3b-propriedade-imaterial-testes.l4` | 90 |
| `cp-g3b-organizacao-do-trabalho.l4` | 197 (I, II), 198, 199, 200 (and p.u.), 201, 202, 203 (caput, § 1º I–II, § 2º), 204, 205, 206, 207 (caput, §§ 1º–2º) | `cp-g3b-organizacao-do-trabalho-testes.l4` | 165 |
| `cp-g3b-sentimento-religioso-e-mortos.l4` | 208 (three figures, p.u.), 209 (and p.u.), 210, 211, 212 | `cp-g3b-sentimento-religioso-e-mortos-testes.l4` | 76 |

For every punishing provision: the case record, the predicate that its elements are made out (consummated and attempted, art. 14, except art. 205 — habitual, no attempt), the pena cominada as a `Pena cominada` constant compared in a test with the preceito's words, the causes of increase as constants plus `incide …` predicates (arts. 203 § 2º, 207 § 2º, 208 p.u., 209 p.u.), a function giving the pena for a case, and the limits once the causes and any attempt are applied. The only ação penal the range states is art. 186's, encoded per form.

**Temporal scope.** Checked against the Senado metadata and the amending laws' own vigência clauses:

| article | wording | in force | what refuses before |
| --- | --- | --- | --- |
| 184, 186 | Lei nº 10.695/2003 (definitions and penalties) | 1.8.2003 (30 days from DOU 2.7.2003, counted by LC 95/1998 art. 8º § 1º; F-g3b-20) | everything: crime, pena, limits, ação penal |
| 203, 207 | Lei nº 9.777/1998 (penalties; §§ 1º–2º added) | 30.12.1998 (on publication) | the pena, causes and limits; the capita's 1940 definitions answer for any date; §§ 1º–2º are simply not law before (the law's own answer) |
| 206 | Lei nº 8.683/1993 (whole article) | 16.7.1993 (on publication) | everything |
| 197–202, 204, 205, 208–212 | 1940; the fines' printed amounts cancelled by Lei nº 7.209/1984 art. 2º (M-sweep-b-07), none printed in the compiled text | — | nothing: a `Pena cominada` carries no amount |

**Not encoded, deliberately:**

- Arts. 185 and 187–196: revoked (Lei nº 10.695/2003; Lei nº 9.279/1996). Carried as labelled inert stubs so the gap reads as a revocation (phrasebook 9.1); `out-of-scope` in the roadmap, with a note pointing at the stub.
- Lei nº 9.610/1998 (copyright) and the labour legislation behind arts. 203 and 204: arts. 184, 203 and 204 are normas penais em branco, and what they point to is taken as a finding the fact supplier makes under that law (F-g3b-01, -11, -17).
- Computer programs: Lei nº 9.609/1998, art. 12 answers for them by speciality; every art. 184 rule refuses by name for a program (F-g3b-02).
- The earlier wordings of arts. 184, 186, 203, 207 (penalty) and 206: not in the source; refused by name.
- Competence (CF art. 109, VI: "os crimes contra a organização do trabalho") and concurso de crimes (arts. 69–71, where one set of facts meets two articles, e.g. 210 and 211): procedural or g1b's.

## 2. The forks, in prose

24 entries in `registers/parts/g3b.forks.json`. None settled by an authority; one open (F-g3b-10); the rest resolved by g3b on argument. No sweep-b reserved id falls in arts. 184–212 (checked against `sweep-b.forks-proposed.json` by provision), so none is created.

| id | question | taken | divergence witness |
| --- | --- | --- | --- |
| F-g3b-01 | What completes "direitos de autor e os que lhe são conexos" (and V3, Lei 5.988/1973)? | Lei 9.610/1998, as a delegated finding; Lei 5.988/1973 revoked by 9.610 art. 115 | none |
| F-g3b-02 | Does art. 184 reach computer programs? | no: Lei 9.609/1998 art. 12 by speciality; refuses by name | `a pirataria de programa de computador` |
| F-g3b-03 | Does § 4º take the private copy out of the caput too? | no, only §§ 1º–3º, as it says | `a cópia privada única de obra inteira` |
| F-g3b-04 | § 2º: does "sem a expressa autorização" close both limbs? | only the rental limb | `a venda de cópia pirata autorizada pelo titular` |
| F-g3b-05 | Art. 186: III against I and IV | III prevails (otherwise it has no case of its own) | `a violação simples contra autarquia` |
| F-g3b-06 | "violência" alone | against the person; art. 200 says "contra coisa" when it means it | `o culto perturbado com violência contra coisa` |
| F-g3b-07 | Art. 200: what "coletivo" qualifies | "abandono" only (gender agreement); the count includes the agent if an employee | `o locaute, com violência contra coisa` |
| F-g3b-08 | Does art. 200 p.u. reach art. 201? | yes (same words; favours the accused) | `a greve de dois no transporte` |
| F-g3b-09 | Art. 200 "praticando violência": whose? | the participant who practises it | none (only the agent's means are recorded) |
| F-g3b-10 | **Art. 201 and the right to strike** | **OPEN**; encoded as written | `a greve de três no transporte` |
| F-g3b-11 | Art. 203 "direito assegurado pela legislação do trabalho" | a delegated finding under labour law | none |
| F-g3b-12 | Art. 203 § 1º II "coação" | violence against the person or a serious threat | `o desligamento impedido com ameaça simples` |
| F-g3b-13 | "deficiência física ou mental" | not sensory (CF art. 227 § 1º II, in 1998, listed "física, sensorial ou mental") | `contra a trabalhadora cega` |
| F-g3b-14 | § 2º with several victims | any victim in the class | `contra Ana e Bruno, antes dos dezoito dele` |
| F-g3b-15 | "trabalhadores" (arts. 206, 207) | two or more | `o recrutamento enganoso de uma só` |
| F-g3b-16 | Art. 207 § 1º "não assegurar condições do seu retorno" | a third mode of the recruiter's conduct | none |
| F-g3b-17 | Art. 204 "obrigação legal relativa à nacionalização do trabalho" | a delegated finding | none |
| F-g3b-18 | Art. 205 "Exercer atividade" | habitual; one act is not the crime; no attempt | `o médico suspenso que atende uma vez` |
| F-g3b-19 | Arts. 211 and 212: parts and ashes | each reaches only what it names | `as cinzas ocultadas`, `a parte do cadáver vilipendiada` |
| F-g3b-20 | Vigência of Lei 10.695/2003 | 1.8.2003 (LC 95/1998 art. 8º § 1º) | 31.7.2003 / 1.8.2003 |
| F-g3b-21 | Is a stillborn child's body a "cadáver"? | yes (in the member's herald) | none |
| F-g3b-22 | Art. 208 "escarnecer de alguém" | a particular person | none |
| F-g3b-23 | "aliciar" and "recrutar" (arts. 206, 207) | distinct: otherwise § 1º of art. 207 is idle | `o recrutamento sem aliciamento para outro estado` |
| F-g3b-24 | Arts. 197–199: consummated when the victim gives in, or when the means are used? | when the victim gives in (the stage herald says so) | `a não exercer o ofício, tentado` |

## 3. Proposed shared nouns (PROPOSTO-COMUM)

- **`Etapa da execução`** (`cp-g3b-comum.l4`): one enumeration for how far an execution went — consummated, interrupted by circumstances outside the agent's will, abandoned by the agent (art. 15), not begun — with two helpers that feed `cp-pena.l4`'s art. 14 rules. Every group splits its offences by art. 14; most offences have no specific consummating fact the way art. 155 has "posse de fato" (STJ Tema 934), and three separate booleans let a case be both consummated and never begun.
- Not proposed, but for the conductor: `a mais grave de duas penas cominadas` and `as causas que incidem` in `cp-g3b-comum.l4` duplicate helpers local to `cp-g3-furto.l4`; both belong in `cp-pena.l4` if hoisted.
- Considered and kept local: `Condição do trabalhador (arts. 203 e 207)` — "indígena" and the nature of a disability, which only arts. 203 § 2º and 207 § 2º read. The shared `pessoa com deficiência` does not say which nature, which F-g3b-13 needs.

## 4. Sweep entries acted on

| entry | class | what g3b did |
| --- | --- | --- |
| M-sweep-b-37 | interpretive (Súmula 502 STJ) | comment at art. 184 § 2º; test `a exposição à venda de DVDs piratas` asserts § 2º, the crime, and § 1º's pena; cross-ref on F-g3b-01 and F-g3b-04 |
| M-sweep-b-38 | interpretive (Súmula 574 STJ) | no effect (a rule of proof; the encoding takes proved facts); noted in the module header; cross-ref on F-g3b-01 |
| M-sweep-b-07 | binding (Lei 7.209/1984 art. 2º) | checked: no preceito in arts. 184–212 prints a réis amount in the compiled text; cited in the Título IV and V headers as why their 1940 penalties answer for any date |

Read and not bearing on the range: every other sweep-b entry (all name articles 121–183). V3 (Lei 5.988/1973), which no sweep examined: answered in F-g3b-01 (the law was revoked by Lei 9.610/1998, art. 115, except its art. 17 §§ 1º–2º; art. 184's words are Lei 9.610 art. 1º's; Lei 9.610 is the fact supplier's, delegated-to-fact).

## 5. What `check.sh` prints, and the checks it does not make

`L4=/Users/mengwong/.claude/br-penal-toolchain/l4 ./check.sh . cp-g3b-`, from the encoding directory, 2026-09-29:

```
module                                        errors satisfied  failed refused asserts
cp-g3b-comum.l4                                    0         0       0       0       0
cp-g3b-organizacao-do-trabalho-testes.l4           0       165       0       0     165
cp-g3b-organizacao-do-trabalho.l4                  0         0       0       0       0
cp-g3b-propriedade-imaterial-testes.l4             0        90       0       0      90
cp-g3b-propriedade-imaterial.l4                    0         0       0       0       0
cp-g3b-sentimento-religioso-e-mortos-testes.l4       0        76       0       0      76
cp-g3b-sentimento-religioso-e-mortos.l4            0         0       0       0       0
TOTAL (7 modules)                                  0       331       0       0     331
(a failed assertion also counts as an error; errors minus failed = everything else)
```

Exit status 0. The `#ASSERT` lines number 90, 165 and 76, so every assertion produced a verdict and every verdict was "satisfied".

**A positive control.** Every assertion passed on its first run, which is exactly when a test suite cannot be trusted until it has been seen to fail. Twenty-four single mutations were made, one at a time, to copies of the modules (a scratch directory, never the encoding), each a plausible misreading of the text or a slip of a number; each made at least one assertion fail:

| mutation | failed |
| --- | --- |
| art. 184 § 1º without "sem autorização expressa" | 1 |
| § 4º applied to the caput too (F-g3b-03's other reading) | 3 |
| art. 186 III not consulted first (F-g3b-05) | 6 |
| Lei 10.695/2003 in force a day late (1 failed, 2 refused: the gate's own assertion is what fails loudly, PLAN T5) | 1 |
| § 2º "sem autorização" on both limbs (F-g3b-04) | 1 |
| a computer program not refused (F-g3b-02) | 4 |
| arts. 197–199 accepting a plain threat | 2 |
| art. 197 II minimum of one month instead of three | 2 |
| art. 200 p.u. with two employees | 3 |
| "coletivo" required of a suspension too (F-g3b-07; applied by hand, the script's anchor missed it) | 2 |
| arts. 203/207 § 2º including sensory disability (F-g3b-13) | 1 |
| art. 203 § 2º up to one half instead of one third | 3 |
| Lei 9.777/1998 in force a day late (3 failed, 1 refused) | 3 |
| one worker as "trabalhadores" (F-g3b-15) | 3 |
| art. 207 § 1º's return clause not negated | 2 |
| art. 205 satisfied by one act (F-g3b-18) | 1 |
| art. 203 caput accepting a serious threat | 2 |
| arts. 208/209 p.u. counting violence against a thing (F-g3b-06) | 3 |
| art. 211 reaching the ashes (F-g3b-19) | 1 |
| art. 212 reaching a part (F-g3b-19) | 1 |
| art. 208's mockery without publicity | 1 |
| art. 211's attempt ignoring a consummated act | 2 |
| art. 212 as reclusão | 1 |
| an abandoned execution (art. 15) counted as an attempt, in `cp-g3b-comum.l4` | 1 in each of the three test modules |

Cross-checks:

- **English.** `L4_BIN nlg --lang en` on the three test modules renders 90, 165 and 76 lines. The only bare names are test case values, the test-local keyword-first mixfix `a pena de …` (bare by PLAN § 8.2, expected) and `EMPTY`; no rule of the four modules renders bare.
- **Quotations.** Every quotation of the Code in the seven files, split at deliberate "..." elisions, was looked up in the source with whitespace collapsed, and with and without the amendment notes ("(Redação dada …)", "(Incluído …)") that sit between paragraphs: 296 pieces, 0 not found. The first pass found one quotation of art. 14 that ran its incisos I and II together over the rubric "Tentativa" between them; it is now two quotations. Quotations of other laws (Lei 10.695 art. 5º, Lei 9.610 arts. 1º, 46 II, Lei 9.609 art. 12, the "entra em vigor" clauses, CF art. 109 VI) were checked against the texts fetched from Planalto.
- **Linter.** No warning in any module (one AND/OR-at-one-column warning in art. 202's rule was fixed by restructuring).

## 6. Open questions for a Brazilian criminal lawyer

1. Is art. 201 still operative against a strike exercised within Lei nº 7.783/1989 in a public work or a service of collective interest, or was it not received by CF art. 9º? Has the STF or STJ said so? (F-g3b-10)
2. Does "violência" in arts. 208 and 209, parágrafo único, include violence against things (a broken altar, a broken coffin)? And in arts. 197–199, 203 and 204? (F-g3b-06)
3. Is a blind or deaf worker "portadora de deficiência física" for arts. 203 § 2º and 207 § 2º? (F-g3b-13)
4. Does art. 205 require habitual practice, or is one act of the barred activity enough? (F-g3b-18)
5. Does art. 211 reach the ashes, and art. 212 a part of a corpse? (F-g3b-19)
6. Arts. 206 and 207: is one worker enough for "trabalhadores"? (F-g3b-15)
7. Art. 186: does inciso III (a public offended party) prevail over I and IV? (F-g3b-05)
8. Art. 184 § 4º: is a single private copy of a whole work, without profit, still the caput's crime? (F-g3b-03)
9. Do the labour legislation's rules on the nationalisation of labour survive the 1988 Constitution, so that art. 204 still has an object? (F-g3b-17)
10. Arts. 197–199: consummated when the victim gives in, or when the violence or serious threat is used? (F-g3b-24)

## 7. Searches relied on

All 2026-09-29, by `curl` from Planalto (`www.planalto.gov.br/ccivil_03/...`), decoded as cp1252; copies in the g3b scratch directory, not in the encoding.

| what | found |
| --- | --- |
| Lei nº 10.695/2003 (`leis/2003/l10.695.htm`) | art. 5º: "Esta Lei entra em vigor 30 (trinta) dias após a sua publicação."; DOU 2.7.2003 |
| Lei nº 9.777/1998 (`leis/l9777.htm`) | re-wrote only the Pena lines of arts. 203 and 207 and added their §§ 1º–2º (and art. 132 p.u.); art. 2º in force on publication; DOU 30.12.1998 |
| Lei nº 8.683/1993 (`leis/1989_1994/l8683.htm`) | re-wrote art. 206 whole; art. 2º in force on publication; DOU 16.7.1993 |
| Lei nº 9.610/1998 (`leis/l9610.htm`) | art. 1º ("os direitos de autor e os que lhes são conexos"); art. 46 II (the private copy of "pequenos trechos"); art. 115 (revokes Lei 5.988/1973 except art. 17 §§ 1º–2º) |
| Lei nº 9.609/1998 (`leis/l9609.htm`) | art. 12: "Violar direitos de autor de programa de computador: Pena - Detenção de seis meses a dois anos ou multa." |
| LC nº 95/1998 (`leis/lcp/lcp95.htm`) | art. 8º § 1º (counting a vacatio), incl. by LC 107/2001 |
| CF (`constituicao/constituicao.htm`) | art. 9º (right to strike); art. 109 VI; art. 227 § 1º II in its 1988 wording ("física, sensorial ou mental") |
| Lei nº 7.783/1989 (`leis/l7783.htm`) | arts. 11, 14, 15 |

Not searched: case law of the STF or STJ on any of the forks (no fork is settled by an authority); the CLT's text.

## 8. For the conductor

- **F-g3b-10 is open** and the question it raises (arts. 200–201 and the right to strike) was not examined by sweep-b. Worth a relay to sweep-b if it is still running.
- **Lei nº 9.609/1998** (software) displaces art. 184 for computer programs; the encoding refuses by name there. Not examined by the sweep.
- **Module paths** in the roadmap and forks use the l4-ide symlink form, `jl4/examples/legal/br-codigo-penal/encodings/legalese-2026-09/…`, as g0's do.
- **Names** that other groups might also declare: `Etapa da execução` (PROPOSTO-COMUM, § 3). Constructor names chosen to avoid the shared modules' (`consumada` is spelled `execução consumada`).
- Art. 197 has no preceito outside its incisos; for facts in neither inciso its pena function refuses by name ("os fatos não estão em nenhum inciso do art. 197, que não tem outra pena") rather than hand back inciso I's pena. Every other pena function in the range returns its article's one preceito for any case, as `cp-g3-furto.l4` does.

## 9. Change of 2026-10-08: recording a lawful act against the dead (F-g3b-25)

An independent test pass found that the record could not state an act that is none of the criminal verbs: an authorised restoration of a tomb had to be recorded as `violar`, and ashes scattered respectfully as `vilipendiar`.

| old | new |
| --- | --- |
| `Conduta contra o respeito aos mortos` ended at `vilipendiar` | one more constructor, `` `ato lícito` ``, glossed in English; arts. 209 to 212 each ask for their own verbs, so no rule changed and none makes out a crime for it |
| header comment "The verbs of arts. 209 to 212, in their order." | adds that `ato lícito` is for an act that is none of them, citing F-g3b-25 |
| tests: 76 assertions | 82: six `NOT crime` assertions (`a sepultura restaurada com autorização`, `a urna recolocada com autorização` under art. 210; `o cadáver exumado com autorização`, `o cadáver cremado com autorização` under art. 211; `as cinzas espalhadas com respeito`, `o cadáver tratado com respeito` under art. 212); the existing criminal cases per article are untouched |
| `g3b.forks.json`: 24 entries | 25: F-g3b-25 (delegated to the fact supplier): is an authorised act outside the verb, or inside it with only unlawfulness excluded (art. 23, III)? Taken: outside, as a recorded fact |

Positive control: in a scratch copy where arts. 210 to 212 accept `ato lícito` as their verb, the six new assertions fail (and so do the existing criminal cases, 34 failure lines in all, because that mutation also removed their verbs).
`check.sh` TOTAL after the change: `TOTAL (7 modules) 0 337 0 0 337`.
