# g1c — arts. 77–120: notes for the reviewer

**Status (2026-09-30): every unit of arts. 77–120 is encoded (44) or inert (1); none deferred.**
This file is written as the work goes; the PROGRESS list is the resume point.

## PROGRESS

- [x] Read BRIEF.md, PLAN.md (whole), the `writing-l4-rules` skill (SKILL.md, gotchas, drafting-patterns, all eleven source-pattern pages), `encoding-a-subject`.
- [x] Read `cp-dominio.l4`, `cp-pena.l4`, `cp-g3-furto.l4`, the first part of `cp-g3-furto-testes.l4`.
- [x] Read source lines 356–590 (arts. 76–120), the vide index, the Senado XML vides for arts. 77–120, sweep-a's entries on my range and its reserved forks.
- [x] `cp-g1c-comum.l4` — group-internal nouns and art.-10 date helpers.
- [x] Cap. IV, arts. 77–82 — `cp-g1c-suspensao-condicional.l4` + tests.
- [x] Cap. V, arts. 83–90 — `cp-g1c-livramento-condicional.l4` + tests.
- [x] Caps. VI–VII, arts. 91–95 — `cp-g1c-efeitos-e-reabilitacao.l4` + tests.
- [x] Título VI, arts. 96–99 — `cp-g1c-medidas-de-seguranca.l4` + tests.
- [x] Título VII, arts. 100–106 — `cp-g1c-acao-penal.l4` + tests.
- [x] Título VIII, arts. 107, 108, 120 — `cp-g1c-extincao-da-punibilidade.l4` + tests.
- [x] Título VIII, arts. 109–119 — `cp-g1c-prescricao.l4` + tests.
- [x] Roadmap part: 44 encoded, 1 inert (art. 85), 0 deferred; validates.
- [x] Forks: 38 entries in `registers/parts/g1c.forks.json`; every quote verbatim in the source; validates. F-sweep-a-05 and -08 span g1b's articles and live in g1b's register (g1b's message, 2026-09-30); g1c cross-refers to both.
- [x] Sweep-a answered the vigência questions (2026-09-29); the conductor asked for the earlier wordings to be recorded, not encoded (§ 8).
- [x] English glosses checked (§ 6).
- [x] Mutation results for prescrição (12/12) and extinção (4/4).
- [x] cp-pena's day-counting defect (conductor, 2026-09-30): the one day-stated period in my range, art. 92, IV's 180 days, now has a day-counted end date tagged `-- DIAS-PRAZO` and its own test (5.7.2026 → 31.12.2026). No other rule of mine sends a day-stated period through `o último dia do prazo`; the prescription suspensions add days by plain date arithmetic.
- [x] Final check.sh (§ 5): `TOTAL (15 modules)                                 0       467       0       0     467`; reply sent to the conductor.
- Last check.sh TOTAL: `TOTAL (15 modules)                                 0       467       0       0     467`

## 1. What is encoded, and what is not

Seven modules and their seven tests modules, all `cp-g1c-*`:

| module | articles | what it answers |
| --- | --- | --- |
| `cp-g1c-comum.l4` | none of its own | `Natureza da infração`, `Condenação`, `Período`; art. 10 helpers (`o dia seguinte ao fim do prazo`, `a data cai no prazo`, `o dia em que a pessoa completa os anos`) |
| `cp-g1c-suspensao-condicional.l4` | 77–82 | which sursis modalities a case meets and their probation ranges; the first-year conditions; revocation (obligatory / facultative / none) and the judge's options; the § 2º extension; extinction |
| `cp-g1c-livramento-condicional.l4` | 83–90 | the fraction per penalty and the time to exceed (art. 84 sums); the first day it is passed; III–IV and the parágrafo único; revocation (86–87), its effects (88), extinction with Súmula 617 |
| `cp-g1c-efeitos-e-reabilitacao.l4` | 91, 91-A, 92–95 | the general effects (91) with ADPF 569's order of destination; equivalent goods (91 § 1º); perda alargada (91-A); the specific effects (92) and which are automatic; rehabilitation: what it reaches, when it may be asked, its requirements, its revocation |
| `cp-g1c-medidas-de-seguranca.l4` | 96–99 | the measures open to the inimputável; the minimum's range; the ceiling of Súmula 527; the dates of the medical examinations; conditional release; art. 98's substitution |
| `cp-g1c-acao-penal.l4` | 100–106 | **`a ação penal do crime (art. 100)`, the exported fallback for every Parte Especial article that states no ação penal**; who brings it, on what condition; the subsidiary private action; successors (§ 4º); the complex crime (101); retraction of the representation (102); decadência (103) with its 2026 paragraph; renúncia (104); the victim's pardon (105–106) |
| `cp-g1c-extincao-da-punibilidade.l4` | 107, 108, 120 | whether a found cause extinguishes punibilidade; what survives an indulto and a perdão judicial (Súmulas 631 and 18); art. 108 as an invariance; art. 120 |
| `cp-g1c-prescricao.l4` | 109–119 | the art. 109 table; the pena em abstrato; the fine (114); the halving (115); the termo inicial (111, 112 with Tema 788); suspensions and interruptions and the count they drive; whether the pretensão punitiva (abstract and by the penalty applied, 110 § 1º) or executória is prescribed on a day, and the last day of the period that ran out; 118; 119 with Súmula 497 |

**Inert:** art. 85 (an instruction to the sentencing court; the conditions are the LEP's), carried as text. Art. 91, § 2º (precautionary measures of the CPP) is carried as text inside the encoded art. 91.

**Not encoded, deliberately:**

- The procedure these articles lean on: the CPP's time for the denúncia (art. 100 § 3º), the order among successors (100 § 4º), silence as acceptance of a pardon, the LEP's conditions of livramento and its art. 141, the Lei Maria da Penha's art. 16 on retracting a representation, the JECrim's civil settlement as renúncia (Lei 9.099, art. 74). Where an article turns on one of those facts it arrives as an input.
- The earlier wordings of re-worded articles (§ 8): each rule that reads one refuses by name for a crime before the re-wording.
- Who is inimputável or semi-imputável (art. 26, g1a), whether art. 44's substitution is available (g1b), whether a crime is against a woman for reasons of her sex (art. 121-A § 1º, g2a), reincidência (arts. 63–64, g1b): each is an input finding here, named after its article, for the conductor to wire at integration.

**Judgement stays with the judge.** Every "poderá" returns the options or the eligibility, never a choice: sursis modalities and the probation range, the first-year conditions, revocation options, the livramento's grant, the perda alargada, the medidas open to the judge. Art. 77, II's weighing, art. 78 § 2º's "inteiramente favoráveis", art. 83's "comprovado" and "constatação", and the medical examinations are findings taken as inputs.

## 2. The forks, in prose

38 entries in `registers/parts/g1c.forks.json`: 30 `F-g1c-NN` and the eight the sweep reserved on arts. 83–117 (F-sweep-a-12 to -19). Eight are settled by an authority (the F-sweep-a ones), two are open (F-g1c-09, -30), the rest resolved on argument. Two more reserved forks bear on my range and are g1b's, because their lowest article is g1b's: F-sweep-a-05 (art. 71 with art. 119; Súmula 497 STF) and F-sweep-a-08 (art. 75 with art. 83; Súmula 715 STF). g1c created F-sweep-a-05 first and withdrew it when g1b reported its own; both are cited at their sites in my modules.

| id | question | taken |
| --- | --- | --- |
| F-g1c-01 | Does art. 77 § 2º keep the caput's incisos I–III? | yes |
| F-g1c-02 | A penalty ≤ 2 years and a convict over 70: caput, § 2º or both? | both returned; the judge chooses |
| F-g1c-03 | Art. 77 § 2º's age: on which date? | the sentence's |
| F-g1c-04 | Art. 81, I: does a conviction to a fine only revoke? | yes, as printed |
| F-g1c-05 | "no curso do prazo": the crime or the conviction becoming final? | the conviction becoming final (also arts. 86–87) |
| F-g1c-06 | Art. 81, II's fine after Lei 9.268/1996 | as printed |
| F-g1c-07 | "está sendo processado": from when? | from the receipt of the charge |
| F-g1c-08 | An obligatory cause not decreed before the period ends: does art. 82 still extinguish? | no |
| F-g1c-09 | Art. 83: not a repeat offender and no good record — which fraction? | **open**: the text answers neither; REFUSE |
| F-g1c-10 | Penalties summed (art. 84) with different fractions | each its own fraction, parts added |
| F-g1c-11 | "nos últimos 12 meses" | a 12-month term from the falta, by art. 10 |
| F-g1c-12 | Art. 86, II "observado o art. 84" | revoke only if the summed penalty is no longer covered, time on livramento counting (art. 88) |
| F-g1c-13 | A misdemeanour punished with prison, in arts. 86–87 | no ground in either |
| F-g1c-14 | Art. 88: never again, even after revocation for an earlier crime? | as printed (LEP art. 141 noted) |
| F-g1c-15 | Art. 91-A's "pena máxima" | with the causes, as art. 109 |
| F-g1c-16 | Art. 92, II's two limbs | independent; the second has no "doloso/reclusão" |
| F-g1c-17 | Art. 92 § 2º, I and inciso I's thresholds | § 2º applies the effect without them |
| F-g1c-18 | Art. 94: "computando-se o período de prova" | the two years run from the probation's first day |
| F-g1c-19 | Which wording governs an earlier fact? | the crime's date: added paragraphs don't apply, re-worded ones refuse |
| F-g1c-20 | Art. 97 "punível com detenção" | the preceito admits detenção; a fine alone does not |
| F-g1c-21 | Art. 98 and art. 97's detenção rule | both measures open |
| F-g1c-22 | Art. 100 § 4º "cônjuge" and the companheiro | as printed |
| F-g1c-23 | Art. 101 when the complex crime's article declares a private action | a public component prevails (Súmula 608 STF's reading) |
| F-g1c-24 | Two acts on the same day (arts. 102, 106 § 2º) | REFUSE: the dates cannot order them |
| F-g1c-25 | Art. 114: the fine cominated or applied | cominated before the final judgment, applied after |
| F-g1c-26 | Art. 115's "sentença" | the first condemnatory decision |
| F-g1c-27 | Art. 111, V: whose age | a victim under 18 at the act |
| F-g1c-28 | Art. 110 § 1º: "a da denúncia ou queixa" | its offering |
| F-g1c-29 | Suspended days (art. 116) | added as days |
| F-g1c-30 | Art. 117, VI: the day of the reincidência | **open**, delegated to the fact supplier |
| F-sweep-a-05 (g1b's) | Crime continuado and prescription | settled, Súmula 497 STF: without the increase — cited at art. 119 |
| F-sweep-a-08 (g1b's) | Art. 75's ceiling and art. 83 | settled, Súmula 715 STF: benefits on the whole penalty — cited at art. 84, and tested |
| F-sweep-a-12 | Is a medida de segurança bounded? | settled, Súmula 527 STJ: by the maximum cominated |
| F-sweep-a-13 | Does a falta grave restart art. 83's count? | settled, Súmula 441 STJ: no |
| F-sweep-a-14 | Art. 89 without a timely suspension | settled, Súmula 617 STJ: extinct |
| F-sweep-a-15 | What an indulto leaves | settled, Súmula 631 STJ: the secondary effects |
| F-sweep-a-16 | The perdão judicial's effects | settled, Súmula 18 STJ: none |
| F-sweep-a-17 | The pronúncia and a later reclassification | settled, Súmula 191 STJ: it interrupts |
| F-sweep-a-18 | Art. 110's +1/3 and the punitive claim | settled, Súmula 220 STJ: executória only |
| F-sweep-a-19 | A confirmatory acórdão (117, IV) | settled, STF HC 176.473: it interrupts |

Where I looked for forks: every article, every clause with "poderá", every date, every cross-reference, and every paragraph a later law added or re-worded.

## 3. Proposed shared nouns (PROPOSTO-COMUM)

In `cp-g1c-comum.l4`, each marked in a comment:

- `Natureza da infração` (crime doloso / crime culposo / contravenção penal) — arts. 63–64 (g1b) and any Parte Especial article that turns on a prior conviction.
- `Condenação` — a conviction as the record certifies it (nature, date of the crime, penalties, date it became final).
- `o dia em que a pessoa completa os anos` — the birthday on which a person completes N years, agreeing with `cp-pena`'s count of age by construction (tested on the day and the day before, 29 February included).

## 4. Sweep entries acted on

| entry | class | what g1c did |
| --- | --- | --- |
| M-sweep-a-05 | binding (ADPF 569, art. 91, II, b) | implemented the arm at `a destinação diversa é admitida (art. 91, II, b; ADPF 569)`, dated 17.5.2024; before it the ruling's reach refuses; `o destinatário do produto ou proveito` gives the order |
| M-sweep-a-06 | binding (Tema 788, art. 112, I) | two arms at `vale o Tema 788 (art. 112, I)` / `o termo inicial da prescrição da pretensão executória (art. 112)`: after 12.11.2020 and not declared extinct, from the trânsito for both parties |
| M-sweep-a-03 | binding (ADI 7.032, art. 51) | noted at arts. 82 and 90: they extinguish the custodial penalty; an unpaid cumulative fine is art. 51's (g1b); cross-ref on F-g1c-08 and F-sweep-a-14 |
| M-sweep-a-02 | binding (ADI 3.150, art. 51) | cross-ref on F-g1c-06 |
| M-sweep-a-15 | interpretive | F-sweep-a-05 (g1b's register), cited at art. 119; `a pena que regula a prescrição no crime continuado (Súmula 497 STF)` |
| M-sweep-a-20 | interpretive | F-sweep-a-08 (g1b's register), cited at art. 84; test: penalties summing fifty years need a third of fifty |
| M-sweep-a-27 | interpretive | F-sweep-a-12, settled |
| M-sweep-a-28 | interpretive | F-sweep-a-13, settled |
| M-sweep-a-29 | interpretive | F-sweep-a-14, settled |
| M-sweep-a-30 | interpretive | F-sweep-a-15, settled |
| M-sweep-a-31 | interpretive | F-sweep-a-16, settled |
| M-sweep-a-32 | interpretive | F-sweep-a-17, settled |
| M-sweep-a-33 | interpretive | F-sweep-a-18, settled |
| M-sweep-a-34 | interpretive | F-sweep-a-19, settled |
| M-sweep-a-17, -35 | no-effect | confirmed by construction: art. 110 § 1º reads only a penalty a sentence fixed |
| M-sweep-a-26 | no-effect | the age is an input (proof by document is a rule of evidence) |
| M-sweep-a-36, -37 | scoped-out by the sweep | noted in the prescrição header |
| M-sweep-a-08 | binding (Lei 15.402, art. 359-M-A) | read; it bears on arts. 69–70 (g1b), not on my range |

V16 (ADPF 569) and V17 are disposed by the sweep; V16 is M-sweep-a-05 above.

## 5. What `check.sh` prints

Last full run (2026-09-29, before the usage stop; unchanged files):

```
TOTAL (15 modules)                                 0       464       0       0     464
```

Final run (2026-09-30), after the art. 92, IV day count was added: see the line under it.

```
TOTAL (15 modules)                                 0       467       0       0     467
```
(exit 0; run in the foreground on 2026-09-30, after the art. 92, IV day count and the Súmula 715 test were added)

Mutation controls, each a single change in a scratch copy, run against that module's tests:

| module | mutations | caught |
| --- | --- | --- |
| suspensão condicional | 6 | 5 (the sixth is equivalent: a judgment on the period's last day extends it to the same day) |
| livramento condicional | 8 | 8 |
| efeitos e reabilitação | 7 | 7 |
| medidas de segurança | 5 | 5 |
| ação penal | 7 | 7 |
| prescrição | 12 | 12 (among them the art. 109 thresholds, Tema 788's date, the day-count of suspensions, the stop at art. 117, V, the § 1º start, the art. 115 age) |
| extinção da punibilidade | 4 | 4 |

One assertion failed on its first run and was a finding about my test, not the code: `P1`'s agent was twenty at a 2010 crime, and art. 115 rightly halved the period. The case now uses an older agent, and the twenty-year-old's case is its own assertion.

## 6. English glosses

`l4 nlg --lang en` on all seven tests modules (464 lines). None of the 183 rule names defined in my modules renders bare. Two constructor-with-fields enums in `cp-g1c-prescricao.l4` had their herald below the one-line `HAS`, where it glossed the field, not the constructor (measured: probe with layouts A/B/C); re-laid with the herald on the line below the constructor and `HAS` indented after it. Record type names (`Caso de decadência`, `Período`, and `cp-pena`'s `Intervalo de duração`) render bare when a record is built inline; the brief asks for glosses on exported rules and fields, not types.

## 7. Vigências used in the gates

| law | vigência | used for | confirmed |
| --- | --- | --- | --- |
| Lei 9.268/1996 | 2.4.1996 (on publication) | art. 92, I; art. 117, V–VI | **no** — publication date from the Senado XML |
| Lei 11.106/2005 | 29.3.2005 | art. 107, VII–VIII revoked | sweep-a: art. 4º, on publication |
| Lei 11.596/2007 | 30.11.2007 | art. 117, IV | sweep-a: art. 3º, on publication |
| Lei 12.234/2010 | 6.5.2010 | arts. 109 VI, 110 § 1º | sweep-a: art. 3º, on publication |
| Lei 12.694/2012 | 23.10.2012 (90-day vacatio) | art. 91, §§ 1º–2º | **no** — vacatio from memory |
| Lei 13.344/2016 | 21.11.2016 (45-day vacatio) | art. 83, V | **no** — vacatio from memory |
| Lei 13.964/2019 | 23.1.2020 | arts. 83 III, 91-A, 116 II–IV | sweep-a: art. 20, 30 days, LC 95 count |
| Lei 14.344/2022 | 9.7.2022 | art. 111, V | sweep-a: art. 34, 45 days, LC 95 count |
| Lei 14.994/2024 | 10.10.2024 | art. 92, II and §§ 1º–2º | sweep-a: art. 10, on publication |
| Lei 15.160/2025 | 4.7.2025 | art. 115 | sweep-a: art. 3º, on publication |
| Lei 15.358/2026 | 25.3.2026 | arts. 91-A § 5º, 92 IV, §§ 3º–4º | sweep-a S-sweep-a-03 |
| Lei 15.438/2026 | 19.6.2026 | art. 103, parágrafo único | sweep-a S-sweep-a-03 |
| Lei 15.487/2026 | 7.8.2026 | art. 92, § 2º | sweep-a S-sweep-a-03 |
| ADPF 569 | 17.5.2024 (judgment) | art. 91, II, b | M-sweep-a-05 |
| Tema 788 | trânsito for the prosecution after 12.11.2020 | art. 112, I | M-sweep-a-06 |

Lei 7.209/1984 itself (the base) is not gated: the encoding answers for facts under the 1984 Parte Geral and later.

## 8. Earlier wordings available for a vintage pass

Recorded at the conductor's request, NOT encoded: each rule that reads a re-worded provision refuses by name for a crime before the re-wording (PLAN § 10). Sweep-a fetched these from Planalto on 2026-09-29; its copies are in `/private/tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/452e2526-ee93-4276-9db4-448804aa5ac6/scratchpad/sweep-a/`. **Caution (sweep-a's):** Planalto's text of Lei 7.209/1984 (`v-l7209.txt`, `l7209.flat`) has scanning artefacts elsewhere (art. 110 caput "regula-se julgado pela pena aplicada"; art. 109, III "se o máxima da pena superior"); it is Planalto's transcription, not the DOU of 13.7.1984.

| article | earlier wording(s), in force | sweep-a's copy |
| --- | --- | --- |
| 83, III | Lei 7.209/1984 ("comprovado comportamento satisfatório …"), to 22.1.2020 | `v-l7209.txt`; current from `g1c-l13964.txt` |
| 83, V | Lei 8.072/1990's inciso, to 20.11.2016 | not fetched |
| 92, I | Lei 7.209/1984, to 1.4.1996 | `v-l7209.txt` (Lei 9.268/1996 not fetched) |
| 92, II | Lei 7.209/1984 ("pátrio poder … contra filho, tutelado ou curatelado"), to 24.9.2018; Lei 13.715/2018, 25.9.2018 to 9.10.2024 | `v-l7209.txt`, `g1c-l13715.txt`, `g1c-l14994.txt` |
| 92, § 1º | Lei 7.209/1984's parágrafo único, to 9.10.2024 | `v-l7209.txt` |
| 92, § 2º | Lei 14.994/2024's caput, 10.10.2024 to 6.8.2026 | `g1c-l14994.txt` |
| 107, VII–VIII | Lei 7.209/1984 (marriage in crimes contra os costumes), to 28.3.2005 | `v-l7209.txt`, `g1c-l11106.txt` |
| 109, caput and VI | Lei 7.209/1984 ("VI - em dois anos …"), to 5.5.2010 | `v-l7209.txt`, `g1c-l12234.txt` |
| 110, §§ 1º–2º | Lei 7.209/1984 (§ 2º allowed a start before the receipt of the charge), to 5.5.2010 | `v-l7209.txt`, `g1c-l12234.txt` |
| 111, V | none before 18.5.2012; Lei 12.650/2012 ("crimes contra a dignidade sexual de crianças e adolescentes"), 18.5.2012 to 8.7.2022 | `g1c-l12650.txt`, `g1c-l14344.txt` |
| 115 | Lei 7.209/1984 (the same rule without the 2025 exception), to 3.7.2025 | `v-l7209.txt`, `L15160.txt` |
| 116, II | Lei 7.209/1984 ("no estrangeiro" — sweep-a: form only), to 22.1.2020 | `v-l7209.txt` |
| 117, IV | Lei 7.209/1984 ("pela sentença condenatória, recorrível"), to 29.11.2007 | `v-l7209.txt`, `g1c-l11596.txt` |

Two places where the encoding already answers an earlier crime by the current words, because sweep-a's copies show the words did not change there — for the conductor to confirm or undo in the vintage pass:

- **art. 115** for a crime before 4.7.2025 where the exception is not engaged: the halving (sweep-a: the only change of substance was the added exception). Where it is engaged, REFUSE.
- **art. 92, II** where the crime is against none of the persons the inciso names and not against a woman for reasons of her sex: FALSE on any date (every earlier wording sweep-a quotes names only children, wards and co-holders).

## 9. Open questions for a Brazilian criminal lawyer

1. Art. 83: which fraction for a convict who is not a repeat offender in an intentional crime but has no good record (F-g1c-09)?
2. Art. 88 with LEP art. 141: may a new livramento follow a revocation for an earlier crime (F-g1c-14)?
3. Art. 97: is outpatient treatment open, by case law, for an act punishable with reclusão (F-g1c-20)?
4. Art. 100 § 4º: does the companheiro take the spouse's place (F-g1c-22)?
5. Art. 101: is Súmula 608 STF's reading (a public component prevails) still the rule after art. 225's rewrite, and is the text I quote from memory exact (F-g1c-23)?
6. Art. 117, VI: does the reincidência interrupt on the day of the new crime or when its conviction becomes final (F-g1c-30)?
7. Art. 115: which decision is "a sentença" when the conviction first comes on appeal (F-g1c-26)?
8. Art. 81, II: is frustrating the fine still a ground after Lei 9.268/1996 (F-g1c-06)?
9. Art. 82: may the sursis be revoked after the period, for an obligatory cause that arose within it (F-g1c-08)?
10. Art. 92, §§ 3º–4º: automatic, or to be declared under § 1º?
11. Art. 110, § 1º: offering or receipt of the denúncia (F-g1c-28)?
12. Art. 116: are suspended days added as days, or the remaining period re-counted by the calendar (F-g1c-29)?

## 10. For the conductor

- **F-sweep-a-05** spans art. 71 (g1b) and arts. 109–119. Your task message told g1c to create it; g1b created it too, as the owner of the lowest article, so g1c withdrew its copy (2026-09-30). Only g1b's is in the registers.
- **Inputs to wire at integration:** art. 26 (g1a) → `inimputável (art. 26, caput)`, the semi-imputável of art. 98; art. 44 (g1b) → `a substituição prevista no art. 44 é indicada ou cabível` (art. 77, III); art. 121-A § 1º (g2a) → the § 2º class of art. 92; arts. 63–64 (g1b) → the reincidência inputs; art. 51 with ADI 7.032 (g1b) → the fine left after arts. 82 and 90.
- **`cp-dominio`'s `Relação do agente com a vítima`** is reused in art. 100 § 4º for what a successor is to the victim; the constructors fit, the type's name does not. A neutral kinship type would be cleaner.
- **Three vigências are unverified** (§ 7): Leis 9.268/1996, 12.694/2012, 13.344/2016.
- **Two answers for earlier facts** go by the current words where sweep-a's copies show no change (§ 8): art. 115 without the exception, art. 92, II outside its persons.
- **Record type names render bare** in `nlg` in every module, `cp-pena`'s included.
- **Exported rules** (all prefix names): `a ação penal do crime (art. 100)`, `a ação penal do crime complexo (art. 101)`, and one or more per chapter; each has `@export`, `@desc` on every input, and `@nlg:en`.
