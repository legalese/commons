# g1b — arts. 32–76: the penalties, their cominação and application, concurso, the limit of art. 75

**Status (2026-09-30): done.** All 45 units of `registers/parts/g1b.roadmap.json` are dispositioned (42 encoded, 3 inert, 0 deferred); `check.sh` prints 0 errors and 388 of 388 assertions satisfied (§ 4); 42 forks.
This file is the reviewer's record and was the resume point through a usage-limit stop on 2026-09-29.

## PROGRESS

- [x] Read BRIEF, PLAN, the skills (SKILL.md, gotchas, drafting-patterns, all eleven source-pattern pages, encoding-a-subject), `cp-dominio.l4`, `cp-pena.l4`, `cp-g3-furto*.l4`, source lines 157–357, sweep-a (all 40 entries) and its proposed forks, and the sweep-b/-c entries that touch arts. 32–76.
- [x] Vigência of every law that re-worded arts. 32–76, read from Planalto's texts of the laws (§ 7).
- [x] `cp-g1b-condenacao.l4` — the nouns of the sentencing (DECLARE only).
- [x] `cp-g1b-circunstancias.l4` — arts. 61–67 (122 assertions).
- [x] `cp-g1b-privativas-de-liberdade.l4` — art. 33 §§ 2º–4º, arts. 34–42 (54).
- [x] `cp-g1b-restritivas-de-direitos.l4` — arts. 44–48 (56).
- [x] `cp-g1b-multa.l4` — arts. 50–52 (23).
- [x] `cp-g1b-cominacao.l4` — arts. 54–57, 58 parágrafo único (24).
- [x] `cp-g1b-aplicacao-da-pena.l4` — arts. 59, 60, 68 (52).
- [x] `cp-g1b-concurso-de-crimes.l4` — arts. 69–76 (57).
- [x] `cp-g1b-casos.l4` — test fixtures shared by the seven tests modules (no rule of the Code, no directive).
- [x] nlg: 385 rendered lines over the seven tests modules; 0 of 274 module rule and constructor names render bare.
- [x] Quotations: every clause quoted from the Code found verbatim in the source; three paraphrased comment quotes corrected.
- [x] Mutation run: 20 single mutations, 20 caught (§ 5).
- [x] Forks: 42 entries, validated (§ 8 for the one deliberate finding).
- [x] Roadmap: validated (`register-validate: ok`).
- Last check.sh (2026-09-30): `TOTAL (16 modules)                                 0       388       0       0     388`

## 1. What g1b encoded, and what it did not

The Parte Geral's Título V, Capítulos I to III: arts. 33 (§§ 2º–4º), 34–42, 44–48, 50–52, 54–57, 58 (parágrafo único), 59–76.
Arts. 32, 43, 49, 53 and the caputs of arts. 33 and 58 are g0's, in `cp-pena.l4`, as is art. 68's third-phase arithmetic, which `cp-g1b-aplicacao-da-pena.l4` uses.

**Judgement stays with the judge.** No rule chooses a quantity.
The pena-base (art. 59, II), the pena provisória (arts. 61–67) and the pena definitiva (art. 68 and its parágrafo único) are each a range; `a dosimetria respeita o art. 68` checks the quantities a sentence records against them.
Art. 59's circumstances are the judge's valuations (favorável, neutra, desfavorável), and the rules check only what a valuation may rest on (Súmulas 241 and 444 STJ, RE 593.818, ADPF 1.107).
Powers (art. 44 § 5º, art. 68 parágrafo único, art. 50's instalments) are returned as options; findings the Code leaves to the court ("motivo fútil", "suficiente", "ineficaz") are inputs.

**Reincidência is computed** (arts. 63–64) from the agent's prior convictions and the date of the new crime; the tests cross-check it against `cp-dominio`'s certified `reincidente` (F-g0-05).

**Which facts the text answers for.** Where a later law re-worded a provision, a rule checks the date that governs it (§ 7):
an added limb simply does not reach an earlier fact (art. 61 II f's violence against women, II h's "mulher grávida", II m; art. 65 I's exception; art. 33 § 4º; art. 47 IV and V);
a replaced wording that is not in the source refuses by name for an earlier fact (art. 61 II h's "velho"; arts. 43–46 before Lei 9.714/1998; art. 75's thirty years before Lei 13.964/2019).
The three binding STF rulings on my articles are dated arms keyed on the day of the decision they govern (ADI 3.150 and ADI 7.032 on art. 51; ADPF 1.107 on art. 59); before each the rule refuses by name.

**Not encoded, deliberately:**
- The Lei de Execução Penal's rules that arts. 33 § 2º ("forma progressiva, segundo o mérito"), 36, 38–40 point to, and the dívida-ativa rules art. 51 borrows: outside the source.
- Arts. 38, 39, 40 are carried as the Code's words (`inert`): rights and a pointer to special legislation, which no rule reads.
- The special regime of crimes hediondos (Lei nº 8.072/1990, art. 2º, § 1º), which the Senado records against art. 33 (§ 8).
- Art. 359-M-A (Lei 15.402/2026), which restricts arts. 69–70 for Título XII Cap. II: g5's; cross-referred at arts. 69–70 (M-sweep-a-08).
- What art. 74 leaves open about the intended crime (F-g1b-31); art. 20 § 3º itself (g1a's; art. 73 cites it).
- Prescription, suspension and parole (arts. 77–120): g1c's. `a pena que regula a prescrição do crime continuado (Súmula 497 STF)` and `a pena considerada para os benefícios (art. 75; Súmula 715 STF)` are exposed for them.

## 2. The forks, in prose

42 entries in `registers/parts/g1b.forks.json`: nine reserved by sweep-a (all settled by the authority the sweep found) and 33 of g1b's own (resolved on argument; some cite authority for one side).
Where g1b looked: every article in the range, each preceito's words against the others (the cross-references that no longer fit: arts. 54, 58 p.ú., 60 § 2º against the 1998 art. 44), every boundary word ("superior a", "igual ou inferior", "depois de", "dentro de"), every undefined class ("crime sexual", "crime contra a administração pública", "o mesmo crime", "preponderantes"), and every place the Code hands the court a judgement.

The reserved forks g1b created: F-sweep-a-01 (Súmula 231: the second phase floored at the minimum), -02 (Súmula 241: the same conviction not twice), -03 (RE 593.818 and Súmula 444: what counts as a record), -04 (Súmula 659: the continued crime's fraction by number of crimes, both readings executable), -05 (Súmula 497, spanning g1c), -08 (Súmula 715, spanning g1c), -09 (Súmulas 718, 719, 440: a harsher regime needs a concrete ground, delegated), -10 (Súmula 269: the reincidente at four years or less), -11 (Súmulas 545 and 630 as revised in 2025: every confession attenuates).
F-sweep-a-06 (Súmula 711; arts. 2, 4, 71) is g1a's to create (art. 2 is the lowest-numbered; message sent). F-sweep-c-08 (art. 61 II f against art. 226 II) is the art. 226 encoder's; F-g1b-12 cross-refers M-sweep-c-13.

The g1b forks most worth a lawyer's time: F-g1b-18 (which circumstances preponderate under art. 67), F-g1b-20 and F-g1b-25 (arts. 54 and 60 § 2º left beside the 1998 art. 44), F-g1b-22 (art. 58 p.ú.'s reference to a paragraph that no longer exists), F-g1b-27 (reclusão over detenção as "a mais grave"), F-g1b-29 (the continued crime's caput not capped at art. 69's sum).

## 2a. The fork registry (the forks file, `registers/parts/g1b.forks.json`, is generated from this and the prose in § 2)

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
| F-g1b-23 | 59; ADPF 1.107 | "crimes sexuais", and sentences before the ruling | Título VI (delegated); before 6.5.2024 refuse |
| F-g1b-24 | 60 § 1º | what is "aumentada até o triplo" | the value of the dia-multa (to 15 minimum wages) |
| F-g1b-25 | 60 § 2º vs 44 § 2º | does art. 60 § 2º still stand beside art. 44 § 2º | both stand as printed |
| F-g1b-26 | 68 p.ú. | "a causa que mais aumente ou diminua" among ranges; may one limit both | larger largest fraction, then larger smallest; yes |
| F-g1b-27 | 70 | "a mais grave das penas cabíveis" | the penalty fixed per crime; reclusão over detenção, then length |
| F-g1b-28 | 71 p.ú. | "observadas as regras ... do art. 75": cap on the penalty imposed? | no: art. 75 limits time served |
| F-g1b-29 | 71 caput | is the caput capped at art. 69's sum (art. 70 p.ú.) | not by the text; analogy in bonam partem arguable |
| F-g1b-30 | 72 | does "concurso de crimes" include the continued crime | yes (text) |
| F-g1b-31 | 74 | the intended crime, where its result did not occur | not answered by art. 74; not encoded here |
| F-g1b-32 | 75 § 2º | base of the new unification | total imposed less time served, then the limit |
| F-g1b-33 | 69, 76 | order of execution within one species | the longer first |

## 3. Proposed shared nouns (PROPOSTO-COMUM)

In `cp-g1b-condenacao.l4`, each marked in place:
- `Natureza da infração anterior` and `Condenação anterior` — g1c's arts. 77, 81, 83, 110 and 117 turn on prior convictions and reincidência, and may not import g1b. Hoist to `cp-dominio.l4`, with `Agente` carrying a list of them; the rules of arts. 63–64 in `cp-g1b-circunstancias.l4` then serve both groups.
- `Espécie aplicada` — the species a sentence applied (reclusão or detenção, never undecided), which any encoder of a sentence reads.

The rest of `cp-g1b-condenacao.l4` (`Crime em julgamento`, `Sentença`, `Circunstâncias judiciais`, the enums of findings and circumstances) is Título V's own.

## 4. What `check.sh` prints for g1b's modules

`L4=/Users/mengwong/.claude/br-penal-toolchain/l4 ENC/check.sh ENC cp-g1b-`, 2026-09-30, exit 0:

```
module                                        errors satisfied  failed refused asserts
cp-g1b-aplicacao-da-pena-testes.l4                 0        52       0       0      52
cp-g1b-aplicacao-da-pena.l4                        0         0       0       0       0
cp-g1b-casos.l4                                    0         0       0       0       0
cp-g1b-circunstancias-testes.l4                    0       122       0       0     122
cp-g1b-circunstancias.l4                           0         0       0       0       0
cp-g1b-cominacao-testes.l4                         0        24       0       0      24
cp-g1b-cominacao.l4                                0         0       0       0       0
cp-g1b-concurso-de-crimes-testes.l4                0        57       0       0      57
cp-g1b-concurso-de-crimes.l4                       0         0       0       0       0
cp-g1b-condenacao.l4                               0         0       0       0       0
cp-g1b-multa-testes.l4                             0        23       0       0      23
cp-g1b-multa.l4                                    0         0       0       0       0
cp-g1b-privativas-de-liberdade-testes.l4           0        54       0       0      54
cp-g1b-privativas-de-liberdade.l4                  0         0       0       0       0
cp-g1b-restritivas-de-direitos-testes.l4           0        56       0       0      56
cp-g1b-restritivas-de-direitos.l4                  0         0       0       0       0
TOTAL (16 modules)                                 0       388       0       0     388
(a failed assertion also counts as an error; errors minus failed = everything else)
```

Each tests module's satisfied count equals its `#ASSERT` count; nothing refused, nothing unaccounted.

## 5. Positive control

Twenty single mutations, each to a copy of the modules, each run against its tests module (scratchpad `g1b/mut/mutate.py`); all twenty caught.
The harness first reported 0 satisfied for every run: it read stdout only, and `l4 run` writes its diagnostics to stderr. It was fixed to read both before any result was trusted.

| mutation | failed | refused |
| --- | --- | --- |
| art. 64 I boundary (GREATER THAN → AT LEAST) | 3 | 0 |
| art. 63 same-day trânsito | 1 | 0 |
| art. 61 II m vigência a day late | 1 | 0 |
| art. 65 I exception made retroactive | 2 | 0 |
| Tema 585 multirreincidência dropped | 1 | 0 |
| art. 33 § 2º a threshold 8 → 9 years | 4 | 0 |
| detenção may start closed | 5 | 0 |
| art. 44 I four → five years | 2 | 0 |
| art. 44 § 4º thirty → twenty days | 2 | 0 |
| art. 50 ten → nine days | 2 | 0 |
| ADI 7.032's date a day late | 0 | 1 |
| art. 58 p.ú. read like the caput | 1 | 0 |
| Súmula 241 check dropped | 2 | 0 |
| art. 68 p.ú. comparator inverted | 5 | 0 |
| art. 70 fraction 1/2 → 2/3 | 3 | 0 |
| Súmula 659 three crimes 1/5 → 1/4 | 2 | 0 |
| art. 75 limit 40 → 30 | 4 | 0 |
| art. 75 vigência a day late | 1 | 1 |
| ADPF 1.107 read-down dropped | 3 | 0 |
| detração not inclusive | 4 | 0 |

The ADI 7.032 mutation showed only as a refused assertion (PLAN § 12, T5); the three ruling-date gates now carry direct assertions that fail loudly.

## 6. Open questions for a Brazilian criminal lawyer

1. Art. 67: which of the listed circumstances "resultam dos motivos determinantes do crime, da personalidade do agente e da reincidência" — are the age (art. 65 I) and the confession preponderant; and where both sides have a preponderant circumstance other than reincidência against confession, does anything direct the judge? (F-g1b-18)
2. Art. 60 § 2º: does it survive beside art. 44 § 2º, so that a penalty of six months or less for a violent crime may be replaced by a fine? (F-g1b-25)
3. Art. 71 caput: is the continued crime's penalty capped at art. 69's sum, as the parágrafo único's is? (F-g1b-29)
4. Art. 70: is "a mais grave das penas" the reclusão over a longer detenção? (F-g1b-27)
5. Art. 44 II: "reincidente em crime doloso" — both crimes dolosos, or any reincidência with a doloso new crime? (F-g1b-08)
6. Art. 44 I: does "violência" include reducing the victim to impotence by other means? (F-g1b-07)
7. Art. 45 § 1º: the minimum wage of which date? (F-g1b-10)
8. Art. 75 § 2º: is the new unification computed on the total imposed or on the unified penalty? (F-g1b-32)
9. ADPF 1.107: which crimes are "crimes sexuais", and does the reading reach sentences before 6.5.2024? (F-g1b-23)
10. Art. 61 II f: must the agent have taken advantage of the domestic relation, or does its existence suffice? (F-g1b-14)
11. Art. 72: does it reach the continued crime? (F-g1b-30)
12. Art. 64 I: is a crime on the fifth anniversary "após período superior a 5 anos"? (F-g1b-17)

## 7. Sweep entries acted on, and the searches g1b made

| entry | class | what g1b did |
| --- | --- | --- |
| M-sweep-a-02 | binding (ADI 3.150) | arm on art. 51: from 13.12.2018 the Ministério Público has priority standing; before, refuses (`o legitimado prioritário para cobrar a multa (art. 51; ADI 3.150)`) |
| M-sweep-a-03 | binding (ADI 7.032) | arm on art. 51: from 22.3.2024 an unpaid fine imposed with a custodial penalty bars extinction unless inability is proven; before, refuses |
| M-sweep-a-04 | binding (ADPF 1.107) | arm on art. 59: from 6.5.2024 a valuation of the victim's sexual life in a crime against sexual dignity is inadmissible; before, refuses (F-g1b-23) |
| M-sweep-a-08 | binding (Lei 15.402, art. 359-M-A) | cross-referred in comments at arts. 69–70; the general rule is exposed for g5's override |
| M-sweep-a-09 … -12, -14, -15, -20 … -25 | interpretive | reserved forks F-sweep-a-01 to -05, -08 to -11 created and settled |
| M-sweep-a-13, -26 | interpretive (rules of proof) | noted: the encoding takes convictions and dates of birth as inputs |
| M-sweep-a-38 | interpretive (Súmula 493) | no effect on arts. 36 or 44 (an LEP practice) |
| M-sweep-a-39, M-sweep-b-42 | interpretive (Súmula 588) | cited at art. 44 I: subsumed for crimes of the Code |
| M-sweep-a-40 | interpretive (Súmula 443) | cited at art. 68: the ranges leave the reasons to the judge |
| M-sweep-c-09, M-sweep-c-13 | binding / interpretive | cross-referred (art. 359-M-A's stay; art. 61 II f with art. 226 II) |

Searches (2026-09-29, curl of planalto.gov.br and the Senado XML in the source bundle; one WebSearch and one WebFetch):

| what | found |
| --- | --- |
| every norm the Senado records against arts. 32–76 | Leis 7.209/1984, 8.072/1990 (art. 33), 9.268/1996, 9.318/1996, 9.714/1998, 10.741/2003, 10.763/2003, 11.340/2006, 12.550/2011, 13.964/2019, 15.159/2025, 15.160/2025; ADI 3.150, ADI 7.032, ADPF 1.107 |
| Lei 9.714/1998 vigência | art. 2º, on publication, DOU 26.11.1998 |
| Lei 9.318/1996 | re-wrote art. 61 II h as "contra criança, velho, enfermo ou mulher grávida"; art. 2º, on publication, DOU 6.12.1996 |
| Lei 10.741/2003 | art. 110 replaced "velho" with "maior de 60 (sessenta) anos"; art. 118, "decorridos 90 (noventa) dias da sua publicação" (DOU 3.10.2003) → 1.1.2004 |
| Lei 10.763/2003 | added art. 33 § 4º; art. 4º, on publication, DOU 13.11.2003 |
| Lei 11.340/2006 | art. 43 re-wrote art. 61 II f; art. 46, "45 (quarenta e cinco) dias após sua publicação" (DOU 8.8.2006) → 22.9.2006 |
| Lei 12.550/2011 | added art. 47 V; art. 20, on publication, DOU 16.12.2011 |
| Lei 13.964/2019 | art. 20, "após decorridos 30 (trinta) dias de sua publicação oficial" (DOU 24.12.2019) → 23.1.2020 |
| Lei 15.159/2025, Lei 15.160/2025 | on publication, DOU 4.7.2025; 15.160's ementa says it only adds the exception, for both ages |
| Lei 7.209/1984 (Planalto) | the 1984 wordings of arts. 61 and 65 I, read only to establish what the later laws changed; nothing encodes them |
| STJ Tema 585 | thesis quoted by the TJDFT (search results name REsp 1.931.145/SP, 22.6.2022, as the reformulation); not in sweep-a (§ 8) |

Vacatio legis counted as LC 95/1998, art. 8º, § 1º has it (the day of publication and the last day included, in force the next day).

## 8. For the conductor

- **F-sweep-a-04 fails one validator rule on purpose.** `materialisation-implies-mechanism` requires TYPICALLY for an interpretation field; this binary rejects a TYPICALLY whose value is a constructor of an own enum (`notes/cp-g1b-sondas/cp-g1b-sonda-typically-enum.l4`). The fork is materialised (both readings run, as `Leituras do concurso`) with mechanism `encoded` and a named default, `a leitura da Súmula 659 STJ`. Decide whether the schema or the entry changes.
- **Two skill findings for `writing-l4-rules`.** Source-patterns entry 1.5 says a constructor of one's own ONE OF type is accepted as a TYPICALLY value: false on this binary. And a field herald on its own line below a TYPICALLY field attaches to the TYPICALLY value, not to the field (`cp-g1b-sonda-typically-herald.l4`).
- **Possible sweep gaps.** (a) Lei nº 8.072/1990, art. 2º, § 1º (initial closed regime for crimes hediondos), which the Senado records against art. 33 and which STF case law is reported to have struck — not in sweep-a, not verified here, not encoded. (b) STJ Tema 585 (confession against reincidência), used in F-g1b-18 — sweep-a lists it as not fetched. (c) The Código de Trânsito Brasileiro's own licence suspension, which displaces much of art. 57.
- **Forks g1b created for spans.** F-sweep-a-05 and F-sweep-a-08 span g1c's articles (message sent to g1c). F-g1b-12's cross-ref M-sweep-c-13 resolves only against sweep-c.
- **Hoisting** (§ 3): `Condenação anterior`, `Natureza da infração anterior`, `Espécie aplicada`.
- **Roadmap titles.** The generator took arts. 44 and 66's titles from the preceding source line ("VI - limitação …", "e) cometido …"); corrected to say they have no rubric of their own.
- **Defects in the Code's own text**, recorded as forks rather than fixed: art. 58 p.ú.'s reference to "o parágrafo único do art. 44" (F-g1b-22); art. 54's "inferior a 1 (um) ano" left beside the 1998 art. 44 (F-g1b-20); art. 60 § 2º beside art. 44 § 2º (F-g1b-25).
- **`cp-g1b-casos.l4`** is a fixtures module for the tests; no roadmap unit names it.
- **cp-pena's day-period defect in `o último dia do prazo` (found by g6b; warning of 2026-09-30).** Checked every g1b rule that counts a period.
  - Only art. 64, I (five years) and art. 46, § 3º (the penalty, stated in months or years) go through the helper; neither is stated in days.
  - Art. 50's ten days use date arithmetic, now marked `-- DIAS-PRAZO`.
  - Art. 42 and art. 44, § 4º compute Durações, not calendar ends; § 4º's thirty days carry a comment telling whoever counts them on the calendar to count in days.
  - No test expectation came from the helper: art. 46's 365, 366 and 181 hours were counted on the calendar by hand, for periods stated in years and months.
- **Wiring at integration.** Art. 73 should read g1a's `a vítima cujas condições se consideram (art. 20, § 3º)` (cp-g1a-erro.l4), which g1a confirms agrees with g1b's reading. F-sweep-a-05 has a second site at g1c's `a pena que regula a prescrição no crime continuado (Súmula 497 STF)`; g1c dropped its duplicate of that fork. F-sweep-a-06 is g1a's, and art. 71's comment points to it.
