# Independent test pass, Título XI (arts. 312–359-H): ta-g6

**Status (2026-09-30): complete.**
The 385 cases in `~/.claude/br-penal-oracle/cases/ta-g6.json` were written from the source alone on 2026-09-29, before the encoding existed.
They were turned into assertions against the finished encoding on 2026-09-30, in the ten files `cp-ind-g6-*.l4`, with shared fixtures in `cp-ind-g6-casos.l4` (no directives).
Every case id appears exactly once: as a directive preceded by `-- IT-g6-NNN: <question>`, or in the not-expressible list of § 3 (checked by script: 372 directives + 13 not expressible = 385).
Each directive is `#ASSERT` or `#ASSERT REFUSED` and states the case's expected value exactly as the case states it.
No expected value was changed to match the encoding.
Every fork id and sweep entry cited below was checked to exist in `registers/fork-register.json` and `registers/external-modifications.json`.

Where a case's facts left a number open, the fixture chose one that does not decide the case, and says so in a comment beside it.
The main ones are these.
- Undated facts are 1 June 2026, after every law in range.
- Where the tax evaded is not the point, it is R$ 60.000,00, above the R$ 20.000,00 insignificance ceiling the encoding takes as a parameter.
- Seized cigarettes are 5.000 packs.
- The art. 337-A § 2º execution minimum is R$ 20.000,00.
- For § 3º, the printed R$ 1.510,00 is passed where the payroll is below it before any readjustment.

Where the encoding reads a fact my case does not mention, it is set so as to isolate the element the case turns on.
Examples are art. 331's ADPF 496 finding of "menosprezo grave e evidente" (TRUE in both desacato cases) and art. 330's order-to-stop flag.

## 1. Counts

| | cases |
| --- | --- |
| cases | 385 |
| expressed (one directive each) | 372 |
| not expressible | 13 |
| agree | 366 |
| disagree | 6 |
| — E, the encoding departs from the text | 0 |
| — T, the case misread the text | 1 |
| — F, a genuine ambiguity, a fork took another reading | 1 |
| — S, a sweep entry or ruling changed the answer | 3 |
| — R, the conductor's strict ruling on art. 327 § 1º before 16.10.2000 | 1 |
| exposed (`~/.claude/br-penal-oracle/EXPOSURE.md`: IT-g6-090, IT-g6-192) | 2 (2 agree) |
| independent agreements (agree, not exposed) | 364 |

`check.sh` over `cp-ind-g6-`, verbatim.
It was run in the foreground one prefix at a time, because the whole set exceeds one foreground call's ten minutes; the header and each module's row are as printed, and the TOTAL is their sum.

```
module                                        errors satisfied  failed refused asserts
cp-ind-g6-administracao-estrangeira.l4             0        12       0       0      12
cp-ind-g6-casos.l4                                 0         0       0       0       0
cp-ind-g6-corrupcao-passiva-a-sigilo.l4            0        50       0       0      50
cp-ind-g6-descaminho-a-sonegacao.l4                3        38       3       0      41
cp-ind-g6-financas-publicas.l4                     1        32       1       0      33
cp-ind-g6-funcionario-publico.l4                   0        12       0       1      13
cp-ind-g6-justica-exercicio-arbitrario-a-desobediencia.l4       0        59       0       0      59
cp-ind-g6-justica-reingresso-a-coacao.l4           1        39       1       0      40
cp-ind-g6-licitacoes.l4                            0        41       0       0      41
cp-ind-g6-peculato-a-concussao.l4                  0        56       0       0      56
cp-ind-g6-usurpacao-a-corrupcao-ativa.l4           0        27       0       0      27
(sum of the eleven rows)                           5       366       5       1     372
```

- Failed (5): the three S (IT-g6-154, 178, 182), the T (IT-g6-259) and the F (IT-g6-380, an `#ASSERT REFUSED` that got a value).
- Refused (1): the R (IT-g6-008).
- Satisfied (366): the agreements.

There are no errors other than the failed assertions, and every `#ASSERT` has a verdict.
The set can fail in both directions: three `#ASSERT REFUSED` directives are satisfied (IT-g6-065, 192, 275), one is failed (IT-g6-380), and four plain assertions fail.

**Every failure was read, not just counted.**
`l4` prints only "assertion failed", so a probe module (deleted afterwards) evaluated the pieces of each failing case.
It returned 14 values, each of which is quoted in the evidence column below.

## 2. Disagreements

| case | articles | my expectation | the encoding's answer | class | evidence |
| --- | --- | --- | --- | --- | --- |
| IT-g6-008 | art. 327, § 1º; art. 1º | false (the 2000 wording's contracted-company limb does not reach a 1999 fact) | REFUSE ("a redação do art. 327, § 1º, anterior à Lei nº 9.983, de 2000 … não está codificada") | R | `o art. 327, § 1º, na redação da Lei nº 9.983, de 2000, rege o fato`, cp-g6a-funcionario-publico.l4:138, refusing through :131 before 16.10.2000; conductor's ruling, fork F-g6a-23. My case said the equiparação does not reach the fact; the ruling declines to say, because the earlier wording (Lei nº 6.799/1980's paraestatal limb) is not in the source. |
| IT-g6-154 | art. 334, caput | true (the text sets no minimum) | FALSE: probe: elements TRUE, `insignificância do descaminho (STJ, Tema 157)` TRUE at the R$ 20.000,00 ceiling, crime FALSE; with the ceiling at 0 the crime is TRUE | S | M-sweep-c-16 (STJ Tema 157 as revised), fork F-sweep-c-10 (taken sumula599ComExcecoes); cp-g6a-descaminho-a-sonegacao.l4:148 and :159. My case was arguable naming exactly this alternative. |
| IT-g6-178 | art. 337-A, caput | true (the text describes the crime by conduct and reduction) | FALSE while the credit is not definitively constituted: probe: elements TRUE; crime FALSE unconstituted, TRUE constituted | S | M-sweep-c-23 (SV 24 extended to art. 337-A), fork F-sweep-c-15 (taken exigeConstituicaoDefinitiva); cp-g6a-descaminho-a-sonegacao.l4:677. The sweep itself calls the linking source a prosecutors' statement, not a court: resolved, not settled. My case was arguable naming this alternative. |
| IT-g6-182 | art. 337-A, § 1º | false (within the Code, payment after the ação fiscal extinguishes nothing) | TRUE, extinguished: probe: § 1º FALSE, Lei nº 10.684/2003 art. 9º § 2º TRUE, overall TRUE | S | M-sweep-c-28 (binding, "added"); cp-g6a-descaminho-a-sonegacao.l4:801 and :810. My case was arguable naming this alternative. |
| IT-g6-259 | art. 339, caput | false (no investigation was opened) | TRUE: probe: consummated FALSE, attempted (art. 14, II) TRUE | T | `denunciação caluniosa tentada (art. 339; art. 14, II)`, cp-g6b-justica-reingresso-a-coacao.l4:322. My case's facts, entered faithfully, are an attempt: Olga did all she meant to do, and the police's refusal stopped the consummation from outside her will. My reasoning ("the offence requires that an investigation be opened") is true of the consummated crime only, and my question asked about the crime without that restriction. The encoding is right. |
| IT-g6-380 | art. 359-G | REFUSE (4.7.2024 is the day the two ways of counting the 180 days disagree on) | FALSE under the taken reading; TRUE under the other: probe, with each reading passed | F | fork F-g6b-20, reading `terminamNoUltimoDia` (TYPICALLY), cp-g6b-financas-publicas.l4:520 and :541. The encoding found the same two readings my case named (5.7–31.12 vs 4.7–30.12) and took the first; my case expected the fork to refuse. Both neighbouring cases agree: 3.7 FALSE and 5.7 TRUE under both readings (IT-g6-379, 378). |

## 3. Not expressible (13)

None was forced.
In each, the thing my case asks is an input the encoding takes as given, or a fact its records cannot hold.

| case | articles | why |
| --- | --- | --- |
| IT-g6-013 | art. 327, § 2º; art. 359-D | No rule lists causes of increase for art. 359-D: g6b's offences carry no art. 327 § 2º at all (fork F-g6b-01). This agrees with my case in substance, but there is nothing to assert. |
| IT-g6-015 | art. 327, § 2º; art. 317 | Whether a Governor holds a "função de direção … de órgão da administração direta" is supplied as input (`entidades dos cargos em comissão ou funções de direção ou assessoramento`). Asserting it would test only my own input. |
| IT-g6-023 | art. 312; art. 30 | Art. 312 reads one agent. g1a's art. 30 (`a circunstância se comunica aos demais concorrentes (art. 30)`) takes "elementar do crime" as an input. No rule composes them, so a non-official participant in peculato cannot be charged with it. |
| IT-g6-025 | art. 312, caput | Whether a temporary use of an official car is "desviá-lo" is the conduct the record takes as input (`desviar o bem (art. 312, caput)`). |
| IT-g6-187 | art. 337-A, § 2º | The encoding returns the judge's options (PLAN § 2.4) and has no rule answering whether the judge MUST withhold the penalty, so my REFUSE has nothing to attach to. Agrees in substance: the faculty is left to the judge. |
| IT-g6-242 | art. 337-O, § 1º | § 1º's definition of "condição de contorno" is folded into an input field's gloss; no rule decides it. |
| IT-g6-247 | art. 337-P; art. 333 | `a multa aplicada cabe na pena cominada do Capítulo II-B (arts. 58 e 337-P)` takes any `Pena cominada`; which crimes the 2% floor reaches is left to the caller. |
| IT-g6-251 | art. 338 | "sem prejuízo de nova expulsão" is carried as a STRING (`a ressalva do art. 338`); no rule answers whether a new expulsion is barred. |
| IT-g6-272 | art. 342 | A party giving a depoimento pessoal cannot be entered: `Pessoa que funciona no processo` has no member for a party. |
| IT-g6-284 | art. 343 | The same: the one offered money is the opposing party, which has no member. |
| IT-g6-289 | art. 344 | "No proceeding exists" cannot be entered: `o processo` is a required `Processo ou procedimento`. |
| IT-g6-321 | art. 351 | The record cannot say that the agent is the fugitive himself; `promoveu ou facilitou a fuga` is the very element at issue. |
| IT-g6-345 | art. 357; art. 332 | `a pretexto de influir em` lists `Pessoa que funciona no processo`, which has no member for a delegado de polícia. Whether he is a "funcionário de justiça" is the question, and it is left to the fact supplier. |

## 4. What the agreements are evidence of

364 agreements are independent, since only IT-g6-090 and IT-g6-192 were exposed.
Six of the "most likely to be encoded wrong" cases I named when the cases were written were not exposed, and all agree:

- **IT-g6-034 and 038:** art. 312 § 3º runs to the sentença irrecorrível (a repair while an appeal is pending extinguishes), and it covers only the culpable form.
- **IT-g6-012 and 014:** art. 327 § 2º reaches only Capítulo I, and not an autarquia (fork F-g6a-02).
- **IT-g6-147:** handing over what the official asked for is not art. 333.
- **IT-g6-065 and 275:** the penas of a 2018 concussão and a 2012 falso testemunho refuse by name, because the earlier cominações are not in the source.

Two cases I had marked arguable also agree: IT-g6-309 (companheira not exempt under art. 348 § 2º, fork F-g6b-11) and IT-g6-273 (inquérito civil outside art. 342, fork F-g6b-09).

Many negative cases test an element the encoding reads directly as an input boolean ("sem autorização …", "por indulgência").
Those agreements show that the element is required and that the right field was named, and not much more.

## 5. Observations that are not disagreements

Five of the not-expressible cases mark places where a fact supplier could get a wrong answer with no diagnostic.
None is an E, because no assertion was possible.
They are listed by how silent the wrong answer would be:

1. **Art. 351 (IT-g6-321).** Nothing distinguishes the fugitive from the one who helps him. A supplier who records a lone prisoner's escape as `promoveu ou facilitou a fuga` convicts him under art. 351, which in the text reaches only another's escape (and art. 352 only an escape with violence).
2. **Arts. 342/343 (IT-g6-272, 284).** A party must be entered as one of the listed roles. Any listed role makes a party's lying deposition, or a bribe offered to a party, the crime.
3. **Art. 337-P (IT-g6-247).** The 2% floor rule accepts any crime's pena. Passing art. 333's would apply the floor to corrupção ativa, outside "os crimes previstos neste Capítulo".
4. **Arts. 312 + 30 (IT-g6-023).** There is no path by which a non-official participant is charged with peculato. The encoding can only answer "not peculato" for him.
5. **Art. 344 (IT-g6-289).** A coercion with no proceeding at all must be entered against some proceeding. The element that saves it (`contra … pessoa que … é chamada a intervir no processo`) then has to be set FALSE by hand.

## 6. Re-run after fix round (2026-10-09)

Three of the eleven modules no longer type-checked, because a fixture builder lacked a field the encoders added.
Each got one line, and no expected value was touched.

| module | builder | field supplied | value | why |
| --- | --- | --- | --- | --- |
| `cp-ind-g6-descaminho-a-sonegacao.l4` | `g6 contrabando` | `o agente conhecia a natureza da mercadoria proibida (art. 334-A, § 1º, IV e V)` | TRUE | the cases are silent; knowing keeps their original facts |
| `cp-ind-g6-licitacoes.l4` | `g6 inidônea` | `o agente sabia que a empresa ou o profissional fora declarado inidôneo` | TRUE | the cases are silent; knowing keeps their original facts |
| `cp-ind-g6-justica-exercicio-arbitrario-a-desobediencia.l4` | `g6 fuga` | `o fugitivo é o próprio agente` | FALSE | every expressed case is about someone who helps another escape (the lone-fugitive case, IT-g6-321, was never expressible) |

The builders' signatures are unchanged, so no call site moved.
The new `Pessoa que funciona no processo` and `Processo ou procedimento` members and the art. 337-P signature change broke nothing in the expressed files.

Check line, `check.sh . cp-ind-g6-` (errors / satisfied / failed / refused / asserts):

| module | before the fixtures | after |
| --- | --- | --- |
| descaminho-a-sonegacao | 1 / 0 / 0 / 0 / 41, UNACCOUNTED 41 | 3 / 38 / 3 / 0 / 41 |
| licitacoes | 1 / 0 / 0 / 0 / 41, UNACCOUNTED 41 | 0 / 41 / 0 / 0 / 41 |
| justica-exercicio-arbitrario-a-desobediencia | 1 / 0 / 0 / 0 / 59, UNACCOUNTED 59 | 0 / 59 / 0 / 0 / 59 |
| the other eight | unchanged | unchanged |
| TOTAL | 5 / 228 / 2 / 1 / 372 | 5 / 366 / 5 / 1 / 372, UNACCOUNTED 0 |

Agreeing: 228 of 372 before (three modules not evaluating), 366 of 372 after.
The after row is the same as § 1: the encoding's changes did not move any previously agreeing case.
The six disagreements stand as recorded in § 2 (IT-g6-008, 154, 178, 182, 259, 380); they were not re-probed by id, only matched by module and count (descaminho 3 failed, financas-publicas 1 failed, reingresso 1 failed, funcionario-publico 1 refused).
No new disagreement appeared.
Exposed cases IT-g6-090 and 192 were not checked by id; the module counts match § 1 exactly, which is the evidence that they still agree.
Not applied: the art. 30 + 312 trap (IT-g6-023) was left for a later pass, as instructed.

Positive control: a scratch copy of `cp-ind-g6-licitacoes.l4` with the new knowledge field set FALSE gave 39 satisfied / 2 failed instead of 41 satisfied, so the field is exercised; the copy was deleted.
