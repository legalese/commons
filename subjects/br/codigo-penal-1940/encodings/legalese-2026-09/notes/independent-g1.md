# Independent test pass, Parte Geral (arts. 1–120): ta-g1

**Status (2026-09-30): complete.**
The 339 cases in `~/.claude/br-penal-oracle/cases/ta-g1.json` were written from the source alone on 2026-09-29, before the encoding existed.
They were turned into assertions against the finished encoding on 2026-09-30, in the 21 files `cp-ind-g1-*.l4`.
Four subagents of ta-g1 did the conversion, one per case range (001–086, 087–182, 183–270, 271–339).
ta-g1 merged their results and checked that every case id appears exactly once.
It checked that every fork id and sweep entry cited below exists in `registers/fork-register.json` and `registers/external-modifications.json`.
It re-ran the whole set with `check.sh` (TOTAL line below).
It also re-classified one disagreement (IT-g1-099, F → E; see § 3).
On 2026-10-11 the class label of four S rows was re-checked against the sweep register; two moved from S to F (IT-g1-161, 217; see § 9).

Each case is one directive, `#ASSERT` or `#ASSERT REFUSED`, preceded by `-- IT-g1-NNN: <question>`.
It encodes the case's expected value exactly as the case states it.
No expected value was changed to match the encoding.
Where a case gave no date, the subagent chose one and said so in a comment beside the directive; most were chosen after 4.7.2025 so that art. 115's gate (§ 3) does not refuse.

## 1. Counts

| | cases |
| --- | --- |
| cases | 339 |
| expressed (one directive each) | 333 |
| not expressible | 6 |
| agree | 310 |
| disagree | 23 |
| — E, the encoding departs from the text | 1 |
| — T, the case misread the text | 0 |
| — F, a genuine ambiguity, a fork took the other reading | 11 |
| — S, a sweep entry or ruling changed the answer | 4 |
| — R, the conductor's strict vigência ruling (PLAN § 10) | 7 |
| exposed (`~/.claude/br-penal-oracle/EXPOSURE.md`) | 17 (15 agree, 2 disagree) |
| independent agreements (agree, not exposed) | 295 |

These counts are those of 2026-09-30, with the F and S rows as re-labelled on 2026-10-11 (§ 9): 1 + 0 + 11 + 4 + 7 = 23.
After the fix round (§ 8) IT-g1-099 agrees, so the same table reads agree 311, disagree 22, E 0, with F, S and R as above.

`check.sh` over `cp-ind-g1-`, verbatim, as run on 2026-09-30:

```
module                                        errors satisfied  failed refused asserts
TOTAL (21 modules)                                14       310      14       9     333
```

Failed (14): the E (IT-g1-099), nine F (IT-g1-094, 095, 148, 159, 161, 171, 172, 217, 331) and the four S (IT-g1-070, 125, 162, 304).
Refused (9): the seven R, and IT-g1-301 and 302 (F, fork F-g1c-19).
Satisfied (310): the agreements.
There are no errors other than the failed assertions, and every `#ASSERT` has a verdict.

**No T, but two of my cases should have been marked arguable.**
IT-g1-217 (art. 89) read the text literally with no alternative, and Súmula 617 STJ (M-sweep-a-29) reads it the other way.
IT-g1-148's "exatamente 5 anos" needed a calendar date to be asserted, and which date is "exactly" five years is itself a question under art. 10 (F-g1b-17).

## 2. Disagreements

| case | articles | my expectation | the encoding's answer | class | evidence |
| --- | --- | --- | --- | --- | --- |
| IT-g1-070 | art. 25; art. 23, II | REFUSE | FALSE for a decision on or after 1.8.2023 (probed with decision date 2026-09-30); REFUSE for an earlier decision | S | `a situação de legítima defesa (art. 25)`, cp-g1a-ilicitude.l4:193-201, keyed on `a data da ADPF 779` (:172); sweep entry M-sweep-a-01 (binding); fork F-g1a-06 (the date the arm is keyed on) |
| IT-g1-094 | art. 33, § 2º, b; art. 33, § 3º | false | LIST `regime semi-aberto` (semi-aberto admitted to the reincidente at 3 years with favourable circumstances) | F | F-sweep-a-10 took semiabertoAteQuatroAnosSeFavoravel, settled by Súmula 269 STJ (M-sweep-a-23); `o regime inicial mais brando que a pena permite (art. 33, § 2º)`, cp-g1b-privativas-de-liberdade.l4 |
| IT-g1-095 | art. 33; art. 33, § 2º, a; art. 69 | REFUSE | LIST `regime semi-aberto` (answers; does not refuse) | F | F-g1b-01 took detencaoNuncaIniciaFechado (caput governs detenção over § 2º, a); `o regime inicial mais gravoso da espécie (art. 33, caput)` |
| IT-g1-099 | art. 42 | 2 anos e 4 meses | 2 anos, 3 meses e 26 dias (244 days of custody credited as 8.1333 thirty-day months) | E | `a pena a cumprir depois da detração (art. 42)` / `o tempo a computar (art. 42)`, cp-g1b-privativas-de-liberdade.l4:341-351: custody counted in calendar days (F-g1b-04) then converted at 30 days a month. F-g0-03's taken reading covers only fractions of a quantity and its rationale says 'the calendar enters when the term is served'; no fork covers crediting time served. Art. 10: 'pelo calendário comum'. |
| IT-g1-125 | art. 51 | REFUSE | FALSE (the unpaid fine does not bar extinção, inability to pay proven, decision after 22.3.2024) | S | M-sweep-a-03 (ADI 7.032, binding read-down), implemented as `a multa obsta a extinção da punibilidade (art. 51; ADI 7.032)`, cp-g1b-multa.l4 |
| IT-g1-148 | art. 64, I | true | TRUE for 'não prevalece' (the condenação no longer counts on the fifth anniversary, 30.6.2020) | F | F-g1b-17 took inicioDaProvaEArtigoDez: art. 10 counting, the five years end on 29.6.2020, so on 30.6.2020 more than five years have passed; cp-g1b-circunstancias.l4 `a condenação anterior não prevalece pelo decurso de cinco anos (art. 64, I)` |
| IT-g1-159 | art. 67 | reincidência | `nenhuma prepondera: a ponderação é do juiz` (single reincidência vs confissão) | F | F-g1b-18 took motivosPersonalidadeReincidencia with the confession as personality (STJ Tema 585); `a segunda fase (arts. 61 a 67)`, cp-g1b-circunstancias.l4 |
| IT-g1-161 | art. 59 | REFUSE | FALSE (valuing pending inquiries/prosecutions as antecedentes is inadmissible) | F (was S; § 9) | F-sweep-a-03 took condenacoesDefinitivasSemPrazo and demoted processosEmCurso ("Súmula 444 STJ forbids it"); the sweep entry behind it, M-sweep-a-11 (Súmula 444 STJ), is class interpretive and routes to that fork; `a valoração dos antecedentes é admissível`, cp-g1b-aplicacao-da-pena.l4:126 |
| IT-g1-162 | art. 59 | REFUSE | FALSE (for a sentence from 6.5.2024, a sexual crime's victim's prior sexual life may not be weighed) | S (confirmed; § 9) | M-sweep-a-04 (ADPF 1.107, class binding, read-down, no fork routed); `a valoração do comportamento da vítima é admissível (ADPF 1.107)`, cp-g1b-aplicacao-da-pena.l4:159 |
| IT-g1-171 | art. 71 | 2 anos e 4 meses a 3 anos e 4 meses | JUST [2 anos, 4 meses e 24 dias, the same] (a fixed increase of 1/5 for three crimes) | F | F-sweep-a-04 took escalaPorNumeroDeCrimes (Súmula 659 STJ, M-sweep-a-14) as the TYPICALLY default; `o intervalo da pena no concurso (arts. 69 a 71)` |
| IT-g1-172 | art. 71 | 1/6 a 2/3 | `causa de aumento` (fixa 1/5) | F | F-sweep-a-04 (Súmula 659 STJ, M-sweep-a-14); `o aumento do crime continuado (art. 71)` with `a leitura da Súmula 659 STJ` |
| IT-g1-217 | art. 89 | false | true (extinct: no suspension during the período de prova) | F (was S; § 9) | `a pena privativa de liberdade está extinta pelo art. 90`, cp-g1c-livramento-condicional.l4:561; fork F-sweep-a-14 took extintaSemSuspensaoTempestiva and demoted art89ImpedeExtincao, which is the literal reading of art. 89 my case gave; the sweep entry behind it, M-sweep-a-29 (Súmula 617 STJ), is class interpretive and routes to that fork |
| IT-g1-295 | art. 110, § 1º | false | REFUSE: 'a redação do art. 115 anterior à Lei nº 15.160, de 2025 (em vigor em 4.7.2025), não está codificada' | R | `os prazos de prescrição são reduzidos de metade (art. 115)`, cp-g1c-prescricao.l4:297-300; PLAN § 10, conductor's ruling 2026-09-30 |
| IT-g1-296 | art. 110, § 1º; art. 117, IV | true | REFUSE: 'a redação do art. 115 anterior à Lei nº 15.160, de 2025 (em vigor em 4.7.2025), não está codificada' | R | `os prazos de prescrição são reduzidos de metade (art. 115)`, cp-g1c-prescricao.l4:297-300; PLAN § 10, conductor's ruling 2026-09-30 |
| IT-g1-301 | art. 111, V | "2028-04-20" | REFUSE: 'a redação do art. 111, V anterior à Lei nº 14.344, de 2022 (em vigor em 9.7.2022), não está codificada' | F | F-g1c-19 (dataDoFato): `o termo inicial da prescrição (art. 111)`, cp-g1c-prescricao.l4:392-394 |
| IT-g1-302 | art. 111, V; art. 111, I | "2020-08-01" | REFUSE: 'a redação do art. 111, V anterior à Lei nº 14.344, de 2022 (em vigor em 9.7.2022), não está codificada' | F | F-g1c-19 (dataDoFato): `o termo inicial da prescrição (art. 111)`, cp-g1c-prescricao.l4:387-396 |
| IT-g1-304 | art. 112, I | "2021-03-10" | JUST 2022-09-20 (trânsito for both parties) | S (confirmed; § 9) | M-sweep-a-06 (class binding, binding_effect struck; STF Tema 788, ARE 848.107, modulated to trânsito para a acusação after 12.11.2020, no fork routed): `vale o Tema 788 (art. 112, I)`, cp-g1c-prescricao.l4:774-790 |
| IT-g1-314 | art. 115 | 8 anos | REFUSE: 'a redação do art. 115 anterior à Lei nº 15.160, de 2025 (em vigor em 4.7.2025), não está codificada' | R | `os prazos de prescrição são reduzidos de metade (art. 115)`, cp-g1c-prescricao.l4:297-300; PLAN § 10, conductor's ruling 2026-09-30 |
| IT-g1-315 | art. 115 | true | REFUSE: 'a redação do art. 115 anterior à Lei nº 15.160, de 2025 (em vigor em 4.7.2025), não está codificada' | R (exposed) | `os prazos de prescrição são reduzidos de metade (art. 115)`, cp-g1c-prescricao.l4:297-300; PLAN § 10, conductor's ruling 2026-09-30 |
| IT-g1-316 | art. 115 | false | REFUSE: 'a redação do art. 115 anterior à Lei nº 15.160, de 2025 (em vigor em 4.7.2025), não está codificada' | R (exposed) | `os prazos de prescrição são reduzidos de metade (art. 115)`, cp-g1c-prescricao.l4:297-300; PLAN § 10, conductor's ruling 2026-09-30 |
| IT-g1-331 | art. 117, IV | REFUSE | TRUE: the acórdão date is among the interruptions | F | F-sweep-a-19 (acordaoConfirmatorioInterrompe, settled by STF HC 176.473/RR): `as datas de interrupção da pretensão punitiva (art. 117, I a IV)`, cp-g1c-prescricao.l4:641-650 |
| IT-g1-338 | art. 109, IV; art. 111, I; art. 10 | true | REFUSE: 'a redação do art. 115 anterior à Lei nº 15.160, de 2025 (em vigor em 4.7.2025), não está codificada' | R | `os prazos de prescrição são reduzidos de metade (art. 115)`, cp-g1c-prescricao.l4:297-300; PLAN § 10, conductor's ruling 2026-09-30 |
| IT-g1-339 | art. 115; art. 117, I; art. 117, IV; art. 117, § 2º | true | REFUSE: 'a redação do art. 115 anterior à Lei nº 15.160, de 2025 (em vigor em 4.7.2025), não está codificada' | R | `os prazos de prescrição são reduzidos de metade (art. 115)`, cp-g1c-prescricao.l4:297-300; PLAN § 10, conductor's ruling 2026-09-30 |

## 3. What the disagreements say

**The one E: art. 42 credits time served at thirty days a month (IT-g1-099).**
`o tempo a computar (art. 42)` (cp-g1b-privativas-de-liberdade.l4:341) counts days in custody on the calendar (F-g1b-04) and then turns them into months at thirty days each.
Eight calendar months of preventiva, 244 days, are credited as 8 months 4 days, so a 3-year pena leaves 2 years 3 months 26 days instead of 2 years 4 months.
F-g0-03's taken reading covers only "computing a fraction of a penalty", and its own rationale says "the calendar enters when the term is served".
No fork covers the conversion of time served.
The drift is small and changes sign with the months spanned: a period covering February credits less than its calendar months.

**R: no prescription is computable for any crime before 4.7.2025 (IT-g1-295, 296, 314, 315, 316, 338, 339).**
`os prazos de prescrição são reduzidos de metade (art. 115)` (cp-g1c-prescricao.l4:297) refuses on the date of the fact before it looks at age.
Every prescription period passes through it, and the module's comment says so on purpose (fork F-g1c-26).
None of the seven involves violência sexual contra a mulher.
In four of them (295, 296, 338, and 314 on the 21st birthday) the present wording's ages do not engage the halving at all.
The encoding refuses anyway, and says why: the earlier wording, its ages included, is not in the source.
The subagent shifted each case's dates past 4.7.2025, and each then gave my expected answer.
For IT-g1-338 it also ran a control with the denúncia received a day earlier, which came back not prescribed, so art. 10's counting under the gate is right.
The ruling is the conductor's to keep or narrow.
Its cost is that the prescription machinery answers nothing for the crimes that prescription questions are usually about.

**F-g1c-19: art. 111, V's gate fires before its own exception (IT-g1-301, 302).**
For crimes before 9.7.2022 the termo inicial refuses (the earlier wording of inciso V is not in the source).
In IT-g1-302 the ação penal had been proposed before the victim turned 18, so inciso V yields to inciso I, whose wording has not changed since 1984.
Checking "salvo se a esse tempo já houver sido proposta a ação penal" before the gate would answer that case without reading any missing text.
Shifted past 2022, both cases give my expected dates (2030-04-20 for the shifted 301, 2022-08-01 for 302).

**The F and S rows are mostly where my case named the other reading.**
In IT-g1-070, 094, 095, 125, 159, 161, 162, 172, 304 and 331 the encoding took exactly the ruling or reading my case gave as its `alternative`.
The exceptions are:
- IT-g1-171: marked certain, but the same fork as 172 (F-sweep-a-04, Súmula 659 STJ as the TYPICALLY default).
  The encoding gives a fixed 1/5 where the text gives 1/6 to 2/3.
  PLAN § 2.4 says a range stays a range; here a súmula replaces it by default.
- IT-g1-148: the fifth anniversary counted as more than five years under art. 10 (F-g1b-17, the reading favourable to the accused).
- IT-g1-217: see § 1.

## 4. Not expressible

| case | articles | my expectation | why |
| --- | --- | --- | --- |
| IT-g1-122 | art. 49, § 1º | data do fato | The minimum wage is an input number whose NAME says 'vigente ao tempo do fato' (cp-pena.l4:390); no rule chooses a date, so there is nothing to assert. Agrees by the parameter's name only. |
| IT-g1-124 | art. 51 | false | No rule: the encoding has no conversion of an unpaid fine (art. 51's §§ 1º–2º are revoked; cp-g1b-multa.l4 § Art. 51). The absence agrees with the case but cannot be asserted. |
| IT-g1-158 | art. 66 | REFUSE | The case answers REFUSE (the judge's power under art. 66). The encoding takes the judge's use of the power as an input finding (`circunstância relevante, anterior ou posterior ao crime, não prevista expressamente em lei`, cp-g1b-circunstancias.l4 `a atenuante está nos fatos`); no rule decides or refuses, so an assertion would only test the input passing through. |
| IT-g1-240 | art. 97, § 1º | false | The encoding has no predicate for 'the Code fixes a maximum'. It encodes Súmula 527 STJ's ceiling (F-sweep-a-12 tetoNaPenaMaximaCominada), which is the alternative my case named; were it expressible it would be a disagreement of class S (M-sweep-a-27). |
| IT-g1-329 | art. 117, IV | false | `Causa interruptiva (art. 117)` has no constructor for a sentença absolutória, so none can be supplied: not interrupting by construction, nothing to assert. |
| IT-g1-333 | art. 117, VI | REFUSE | The day of the reincidência is supplied with the `reincidência (art. 117, VI)` event (F-g1c-30, fact-supplied); no rule answers it. Substantively this matches my REFUSE (the text leaves the day open). |

IT-g1-240 would be an S disagreement if it could be asserted: the encoding caps the medida de segurança at the maximum pena cominada (Súmula 527 STJ, M-sweep-a-27), the alternative the case named.
IT-g1-333 matches my REFUSE in substance: the day of the reincidência is an input.

## 5. Agreements that are weaker than they look

These agree, but the deciding fact is an input to the encoding, so the assertion shows only that the rule reads the input:
- IT-g1-031, 032: the source of the duty to act (art. 13 § 2º).
- IT-g1-043, 061: the atenuante (art. 65, III, b and c).
- IT-g1-063: the subagent had to state that the excess was intentional, which the case did not.
- IT-g1-200–202: the art. 83 floor goes through the whole rule, since there is no predicate for it alone.
- IT-g1-210: the time rule never reads faltas.
- IT-g1-259: `Perdão do ofendido` has no addressee.
- IT-g1-284, 288, 327, 328: no field for, in turn, reincidência or an agravante before sentence, a hypothetical pena, the offering of the denúncia, and a later desclassificação.

Translated rather than asserted as written:
- IT-g1-096 and IT-g1-130 expected REFUSE, but the encoding returns the judge's options or range (PLAN § 2.4).
  The directives assert the substance of the REFUSE's own reason instead: the regime options, and the pena-base range from the minimum to the maximum cominado.
  Both agree.
- IT-g1-269 agrees only through the encoding's Súmula 497 helper; passing the 3-year aggregate straight to the executória rule gives 8 years.

## 6. Exposed

Per `EXPOSURE.md`, agreement on these is not evidence:
- IT-g1-181, 287, 297 and 319: the four REFUSE expectations on older wordings (arts. 75, 109 VI, 110 § 1º, 115).
- IT-g1-121, 136, 137, 155, 156, 173, 186, 189, 315, 316 and 317: "maior de N", "triplo" as +2, and `from: null`.
- IT-g1-074 and IT-g1-082: the birthday boundary and "até metade".

Fifteen agree.
IT-g1-315 and 316 disagree, as R; a disagreement is still a finding.

## 7. Files

- `cp-ind-g1-a-*.l4` (8 files): IT-g1-001–086, arts. 1–31 and cp-pena's arts. 10, 11, 14.
- `cp-ind-g1-b-*.l4` (6 files, `-casos` holds fixtures only): IT-g1-087–182, arts. 32–76.
- `cp-ind-g1-c-*.l4` (6 files): IT-g1-183–270, arts. 77–108 and 118–120.
- `cp-ind-g1-p-prescricao.l4`: IT-g1-271–339, arts. 109–117.

Per-case results, one object per case with the encoding's answer and the evidence, are in ta-g1's scratchpad as `g1/results-all.json` (session 452e2526).
They are not part of the deposit.

## 8. Re-run after fix round (2026-10-09)

Re-run of `cp-ind-g1-*.l4` (21 modules) with `check.sh` after the F-g1-* fix round, no edits to any cp-ind file.
Every module still typechecks; no fixture needed a new field, so no fixture was changed and no positive control applied.

```
TOTAL (21 modules)                                13       311      13       9     333
```

Before: 310 satisfied, 14 failed, 9 refused. After: 311 satisfied, 13 failed, 9 refused. UNACCOUNTED 0.
The only change is IT-g1-099 (art. 42, the E): it now agrees (g1b art. 42 fix).
The 13 failed are IT-g1-070, 094, 095, 125, 148, 159, 161, 162, 171, 172, 217, 304, 331; the 9 refused are IT-g1-295, 296, 301, 302, 314, 315, 316, 338, 339.
These are the same sets as in § 1 and § 2 (F, S and R classes, unchanged by the fix round; two S rows were re-labelled F on 2026-10-11, § 9).

## 9. Class labels re-checked, 2026-10-11

Four disagreements had been labelled S: IT-g1-161, 162, 217 and 304.
The question was whether S fits each, or whether the honest label is F.
The test applied is the sweep register's own, from `BRIEF.md` item 3 and `sweep-a.external-modifications.json`.
An entry of class `binding` struck, suspended or read down a provision, and the encoder implements it as a rule-version arm or a REFUSE.
An entry of class `interpretive` chooses between readings of the text, and the encoder opens or settles a fork on it.
So S fits where the entry is `binding`, and F fits where the entry is `interpretive` and a recorded fork took the other reading.
Nothing here asserts what any court holds beyond what the register records.

| case | old | new | the register says | the "got" |
| --- | --- | --- | --- | --- |
| IT-g1-161 | S | F | M-sweep-a-11 (Súmula 444 STJ) is `interpretive`, `fork_ids` F-sweep-a-03. The fork (`kind` vagueness, `status` settled) took condenacoesDefinitivasSemPrazo and demoted processosEmCurso with the rationale "Súmula 444 STJ forbids it". | Reproduced. The `#ASSERT REFUSED` fails with "expected a refusal, but the expression produced a value", and `#EVAL` of the same expression gives FALSE. |
| IT-g1-162 | S | S | M-sweep-a-04 (ADPF 1.107, item iii) is `binding`, `binding_effect` read-down, `fork_ids` empty. The encoding keys the arm on the sentence date 6.5.2024 and on Título VI (F-g1b-23, `encoding-placement`, taken tituloSeisEDataDaSentenca), which fixes the scope and the date key, and not the answer for a sentence on or after 6.5.2024. | Reproduced, with the fixture's sentence date in 2025. The `#ASSERT REFUSED` fails the same way and `#EVAL` gives FALSE. |
| IT-g1-217 | S | F | M-sweep-a-29 (Súmula 617 STJ) is `interpretive`, `fork_ids` F-sweep-a-14. The fork (`kind` statutory-wording, `status` settled) took extintaSemSuspensaoTempestiva and demoted art89ImpedeExtincao, whose description is the literal reading of art. 89 that my case gave. | Reproduced. `#ASSERT NOT (…)` fails, and `#EVAL` of the inner expression gives TRUE. |
| IT-g1-304 | S | S | M-sweep-a-06 (Tema 788, ARE 848.107/DF) is `binding`, `binding_effect` struck, `fork_ids` empty. Its disposition note gives the modulation: trânsito para a acusação after 12.11.2020 and a penalty not yet declared extinct by prescription. The case's acusação trânsito is 10.3.2021, so the arm applies. | Reproduced. The assertion fails, and the termo inicial evaluates to `JUST OF (DATE OF 20, 9, 2022)`, the defesa's trânsito. |

**IT-g1-161 and 217 move from S to F.**
In both, the source the encoding follows is an STJ súmula, which the register classes `interpretive`, and the encoder recorded a fork whose demoted reading is the one my case took.
That is the definition of F, and it matches how the file already labels IT-g1-094 (M-sweep-a-23, Súmula 269 STJ, fork F-sweep-a-10) and IT-g1-171 and 172 (M-sweep-a-14, Súmula 659 STJ, fork F-sweep-a-04).
The register agrees with those three labels: M-sweep-a-23 and M-sweep-a-14 are `interpretive` and route to F-sweep-a-10 and F-sweep-a-04.

**A caveat on IT-g1-161, so the label is not read as more than it is.**
F-sweep-a-03 is also settled by M-sweep-a-12 (RE 593.818/SC), whose disposition note says it is "binding on lower courts as a repercussão-geral thesis, but its effect on the text is interpretive: it chooses between two readings of arts. 59 and 64 and strikes nothing".
So the register's own line between S and F is the entry's class, not whether the court that decided is binding.
The fork's rejection of processosEmCurso cites Súmula 444 STJ alone, and that is the source my case's `alternative` named.
I did not check whether any other source in the register bears on pending inquiries and prosecutions as maus antecedentes; M-sweep-a-11 and a-12 are the entries routed to this fork.

**IT-g1-217 is not a T, and the label is F, not E.**
Art. 89 read alone says the judge may not declare the penalty extinct while the liberado's trial is pending, and my case answered false.
Art. 90 says the penalty is extinct if the livramento is not revoked by its end.
The register records both readings as a fork of `kind` statutory-wording, with the literal art. 89 reading as a demoted option, so the text supports it and I did not misread it.
The encoding does not depart from the text either: it takes the reading the fork records and cites its settling entry in the rule's comment (cp-g1c-livramento-condicional.l4:548).
§ 1 stands: the case should have been marked arguable.

**IT-g1-162 and 304 stay S.**
Both entries are `binding` with an empty `fork_ids`: the text was read down (ADPF 1.107) or struck in part (Tema 788), and the encoding implements the register's proposed rule-version arm.
My text-only answer is out of date for any sentence or trânsito after the dates the entries key on.
In IT-g1-304 the case's own facts fall after the date (10.3.2021 against 12.11.2020).
IT-g1-162 states no sentence date; the converting subagent chose a sentence in 2025, after 6.5.2024 (`a data da ADPF 1.107`, cp-g1b-aplicacao-da-pena.l4:140).
With the sentence date changed to 1.1.2023 the same call refuses ("se, antes da ADPF 1.107 (6.5.2024), a sentença por crime sexual podia valorar a vida sexual pregressa … não está codificado"), which matches my REFUSE.
So the disagreement exists only because of the date the converting subagent chose.

**Counts.**
E 1, T 0, F 9 → 11, S 6 → 4, R 7; the total is 23 both before and after (1 + 0 + 11 + 4 + 7).
After the fix round (§ 8) IT-g1-099 agrees, so the live total is 22 (13 failed and 9 refused), with E 0.
No E and no T was found among the four.
The `.l4` files were not changed, and no fork or register entry was edited.
