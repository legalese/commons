# Independent test pass, ta-g2 — arts. 121 to 154-B

**Status (2026-09-30): phase 2 done.** ta-g2's cases (`~/.claude/br-penal-oracle/cases/ta-g2.json`, written 2026-09-29 from the source text alone, before the encoding existed) are converted to assertions against the integrated encoding, run, and every disagreement classified.
The assertions are the twelve files `cp-ind-g2-*.l4` in this directory. Each case is one directive, under a comment `-- IT-g2-NNN: <question>`; a case that could not be expressed keeps its comment and a `NOT EXPRESSIBLE` line, with no directive.
The expected value in every directive is the case's, as written on 2026-09-29. None was changed to match the encoding.

## How the cases were turned into assertions

- Every fact is dated 29.9.2026, the day the source was fetched and after every vigência gate on arts. 121–154-B (the latest the g2 modules use is 10.8.2026), so no case meets a PLAN § 10 refusal. Ages are birth dates set against that day ("60 anos e 5 meses" is born 29.4.1966; "no dia em que completava 60" is born 29.9.1966).
- A pena case is compared on the four things the case states — `espécie`, `mínimo`, `máximo`, `multa` — on the pena the encoding gives for the case's facts (the exported per-case function), or on the `pena do art. N` constant where the case is a bare preceito. `além da pena correspondente à violência` is not asserted: no case states it.
- A fraction case is compared with the encoding's own cause value (`causa de aumento` / `causa de diminuição` with `fixa`, `entre`, `até`), usually together with the `incide …` predicate for the case's facts. The encoding and the cases use the same convention for multipliers: the fraction added, `o dobro` = 1, `o triplo` = 2.
- An ação penal case goes through g1c's `a ação penal do crime (art. 100)` over the action the article declares. Art. 145 returns a list of routes (Súmula 714), and is compared as a list.
- A REFUSE case is `#ASSERT REFUSED` on the expression the encoding offers. The two "até X" floor cases (IT-g2-092, IT-g2-201) are asserted as `menor fração` EQUALS NOTHING instead: that is the encoding's representation of a floor the Code does not state (F-g0-09), so it is the case's answer in the encoding's vocabulary. Where the encoding leaves a power to the judge as a list of options (IT-g2-049, the art. 121 § 5º pardon), the case is asserted as the option being offered and not exercised.
- Homicídio (IT-g2-001–081) and suicídio/aborto (IT-g2-082–123) were converted by two forks of ta-g2 under the same written protocol; the rest by ta-g2 directly. The results of all eight slices were read back and are summarised here.
- A type error anywhere in a file suppresses every verdict in it, and `NOT` on one line reaches to the end of the line (`NOT (x) AND y` is `NOT (x AND y)`): both were met and fixed before the counts below were taken.

## Counts

| | |
| --- | --- |
| cases | 383 |
| expressed (one directive each) | 380 |
| not expressible | 3 |
| agree (assertion satisfied) | 369 |
| disagree | 11 |
| — class E | 1 |
| — class T | 0 |
| — class F | 7 |
| — class S | 3 |
| — class R | 0 |
| exposed (EXPOSURE.md) | 15: 13 agree, 2 disagree |
| of the agreements, input-determined | 91 |

**Input-determined** marks an agreement where the decisive step of the case is the choice of an input that carries the Code's words (`por mais de trinta dias`, `mal injusto e grave`, `de modo intencional e repetitivo`), with only a mapping or a gate between input and answer. Those agreements show the encoding routes the finding correctly; they do not show it reads the threshold the way the case does, because the encoding never sees the threshold.

`check.sh` over the twelve files, verbatim:

```
module                                        errors satisfied  failed refused asserts
cp-ind-g2-aborto.l4                                1        25       1       0      26
cp-ind-g2-constrangimento-ameaca.l4                1        32       1       0      33
cp-ind-g2-correspondencia.l4                       0        13       0       0      13
cp-ind-g2-domicilio.l4                             0        11       0       0      11
cp-ind-g2-homicidio.l4                             4        76       4       0      80
cp-ind-g2-honra.l4                                 1        51       1       1      53
cp-ind-g2-lesao-corporal.l4                        1        38       1       0      39
cp-ind-g2-periclitacao.l4                          0        46       0       0      46
cp-ind-g2-rixa.l4                                  1         4       1       0       5
cp-ind-g2-segredos.l4                              0        28       0       0      28
cp-ind-g2-sequestro-escravidao.l4                  1        29       1       0      30
cp-ind-g2-suicidio.l4                              0        16       0       0      16
TOTAL (12 modules)                                10       369      10       1     380
(a failed assertion also counts as an error; errors minus failed = everything else)
```

The failed and refused counts are the disagreements below: a failing assertion here is a finding, not a defect of the test file.

## Disagreements

Classes: (E) the encoding departs from the text; (T) the case misread the text; (F) a genuine ambiguity, with its fork; (S) stale — a later ruling or sweep finding; (R) a conductor's strict ruling.

| id | articles | case expects | encoding answers | class | evidence |
| --- | --- | --- | --- | --- | --- |
| IT-g2-007 | art. 121, § 1º | FALSE (arguable) | the § 1º reduction is among the case's causes of decrease (obligatory once the findings are made); outer limits reduced | F (F-g2a-02) | cp-g2a-homicidio.l4:800 returns `diminuição do art. 121, § 1º` as a cause; F-g2a-02 taken causaUmaVezFeitosOsAchados vs faculdadeDeReduzir (the case's reading); source: "o juiz pode reduzir a pena de um sexto a um terço" |
| IT-g2-029 | art. 121, § 2º-B, II | TRUE (arguable) | false: the nanny's guarda/cuidado is not read as "autoridade" | F (no fork recorded) | cp-g2a-homicidio.l4:439 reads only `outra relação de autoridade sobre a vítima`; cp-dominio.l4:93 `guarda, cuidado ou vigilância da vítima` is left out. F, no fork recorded |
| IT-g2-045 | art. 121, § 4º | FALSE (arguable) | true: on the 60th birthday the victim is "maior de 60" | F (F-g0-06) EXPOSED | cp-pena `maior de` = completed years ≥ N; F-g0-06 taken completouNAnos vs somenteAposOAniversario (the case's reading) |
| IT-g2-047 | art. 121, § 4º; art. 121, § 2º, IX | TRUE (arguable) | false: § 2º IX excludes the § 4º increase (no double counting); causes EMPTY | F (F-g2a-03) | cp-g2a-homicidio.l4:626 AND NOT qualificado pelo § 2º, IX; F-g2a-03 taken incisoIXAfastaOAumento vs ambosIncidem (the case's reading) |
| IT-g2-123 | art. 128; art. 124; art. 126 | FALSE (arguable) | D and G not punishable: ADPF 54 read-down excludes the fact from arts. 124 and 126 (probe: art. 128 FALSE; elements of 124 and 126 TRUE; `a ADPF 54 exclui o fato do tipo` TRUE; crimes FALSE) | S (F-g2a-22) [M-sweep-b-01] | cp-g2a-aborto.l4 `a ADPF 54 exclui o fato do tipo` (from 12.4.2012), binding entry M-sweep-b-01 |
| IT-g2-126 | art. 129, caput | FALSE | TRUE: `crime de lesão corporal (art. 129)` holds when the one injured is the agent | E | cp-g2a-lesao-corporal.l4:180-190, 214-218 read only that an offence to integrity occurred; nothing compares f's `vítima`'s pessoa with f's agente's pessoa, so "de outrem" (source line 732) is not an element anywhere. No fork records it. |
| IT-g2-213 | art. 137 | REFUSE (arguable) | FALSE: `há rixa` requires three or more participants | F (F-g2a-30) | cp-g2a-rixa.l4, `há rixa` = número de pessoas AT LEAST 3; fork F-g2a-30 takes tresOuMaisContendores (the case's own alternative) over doisBastam |
| IT-g2-263 | art. 145, caput; art. 100 | pública incondicionada (arguable) | REFUSES: 'a ação penal da injúria real (art. 140, § 2º) de cuja violência resulta lesão corporal leve ... não está codificada' | F (F-g2b-06) | cp-g2b-honra.l4:980-985; fork F-g2b-06 (open) records exactly the two readings the case named: art. 100 unconditional vs. Lei 9.099/1995 art. 88 representação |
| IT-g2-265 | art. 145, parágrafo único; art. 141, II | pública condicionada à representação (arguable) | LIST representação, privada (both routes) | S (F-sweep-b-12) [M-sweep-b-21] | cp-g2b-honra.l4:993-994; STF Súmula 714 (legitimidade concorrente), the case's own alternative, settled in F-sweep-b-12 |
| IT-g2-292 | art. 147-A, § 1º, II; art. 121, § 2º-A | TRUE (arguable) | FALSE: from 10.10.2024 § 1º II has no definition to apply (inaplicavelRemissaoMorta) | F (F-sweep-b-24) [M-sweep-b-46] EXPOSED | cp-g2b-constrangimento-ameaca.l4, `contra mulher por razões da condição de sexo feminino (art. 147-A, § 1º, II)`: FALSE for a fact on or after 10.10.2024; F-sweep-b-24 takes the reading the case named as its alternative. EXPOSED (EXPOSURE.md) |
| IT-g2-315 | art. 149, caput | TRUE | FALSE: the caput also requires the judge's finding `violação intensa e persistente, a juízo do juiz`, which the case's facts do not supply | S (F-sweep-b-10) [M-sweep-b-19] | cp-g2b-sequestro-escravidao.l4:386 (caput = um dos modos AND the finding); M-sweep-b-19 / F-sweep-b-10 settled by STF Inq 3412 (2012): not every breach of labour rights counts. The text (source line 974) names only the modes |

**All seven F disagreements are on cases marked arguable, and in six of them the encoding took the reading the case named as its alternative**: IT-g2-007 (F-g2a-02, the § 1º reduction is due once the findings are made), IT-g2-045 (F-g0-06, "maior de 60" from the birthday itself), IT-g2-047 (F-g2a-03, § 2º IX displaces the § 4º age increase), IT-g2-213 (F-g2a-30, a rixa needs three), IT-g2-292 (F-sweep-b-24, § 1º II inert) and IT-g2-029. Each fork records the case's reading among its readings, except IT-g2-029, which has no fork: the encoding reads § 2º-B II's "por qualquer outro título tiver autoridade sobre ela" only from the relation `outra relação de autoridade sobre a vítima`, and never reads the shared vocabulary's `guarda, cuidado ou vigilância da vítima` (cp-dominio), so a nanny who has the child in her care is outside § 2º-B II. Whether she should be is the question the case flagged; g2a should record it as a fork. The seventh, IT-g2-263, is a refusal, not a reading: for injúria real with slight injury the encoding takes neither of F-g2b-06's readings and refuses.

**Of the three S disagreements, two are STF rulings the cases named as their alternatives** — ADPF 54 for IT-g2-123 (binding, M-sweep-b-01) and Súmula 714 for IT-g2-265 (M-sweep-b-21, settled in F-sweep-b-12). **The third the case did not foresee**: for IT-g2-315 the encoding requires, beside one of art. 149's modes, the judge's finding that the breach of labour rights was intense and persistent (STF Inq 3412, M-sweep-b-19, settled in F-sweep-b-10). The text (source line 974) names only the modes; the case read the text.

**IT-g2-126 is the one E.** Art. 129 punishes offending the integrity or health "de outrem" (source line 732); no rule of `cp-g2a-lesao-corporal` compares the victim with the agent, so an agent who cuts their own arm makes out `crime de lesão corporal (art. 129)`. The record has room for the fact (the `Vítima` carries a `Pessoa`), so this is a missing element, not a missing input. No fork records it.

## Not expressible

| id | articles | question | why |
| --- | --- | --- | --- |
| IT-g2-006 | art. 121, § 1º | Incide o art. 121, § 1º? | The question (is a reaction three days later "logo em seguida"?) is itself one input finding of the encoding; nothing is computed from it. |
| IT-g2-242 | art. 141, III | Incide o aumento do art. 141, III, por ter sido o crime cometido "na presença de várias pessoas"? | The encoding takes 'na presença de várias pessoas' as an input circumstance in the Code's words (`Circunstância da ofensa à honra`); no count of those present is compared with anything, so the question whether two people are 'várias' is the input itself. In substance this agrees with the case's REFUSE: the encoding decides no number. |
| IT-g2-335 | art. 150 | O crime foi cometido "durante a noite" (art. 150, § 1º)? | The encoding takes `durante a noite` as one input element of `Elemento da violação de domicílio`; nothing is computed from an hour or from daylight, so whether 18h40 at dusk is night is the input itself. In substance this agrees with the case: the encoding fixes no definition of night. |

## Exposed cases

EXPOSURE.md lists what the encoders saw of the test authors' work. For ta-g2 that is IT-g2-292 by name, and two conventions of ours that bear on specific cases. On these cases an agreement is not evidence; a disagreement still is.

| id | why | result |
| --- | --- | --- |
| IT-g2-044 | the "maior de N" convention at the birthday boundary (EXPOSURE.md) | agree |
| IT-g2-045 | the "maior de N" convention at the birthday boundary (EXPOSURE.md) | disagree (F) |
| IT-g2-088 | the dobro/triplo convention (EXPOSURE.md) | agree |
| IT-g2-091 | the dobro/triplo convention (EXPOSURE.md) | agree |
| IT-g2-093 | the dobro/triplo convention (EXPOSURE.md) | agree |
| IT-g2-111 | the "maior de N" convention at the birthday boundary (EXPOSURE.md) | agree |
| IT-g2-114 | the dobro/triplo convention (EXPOSURE.md) | agree |
| IT-g2-159 | the dobro/triplo convention (EXPOSURE.md) | agree |
| IT-g2-196 | the dobro/triplo convention (EXPOSURE.md) | agree |
| IT-g2-200 | the dobro/triplo convention (EXPOSURE.md) | agree |
| IT-g2-247 | the dobro/triplo convention (EXPOSURE.md) | agree |
| IT-g2-248 | the dobro/triplo convention (EXPOSURE.md) | agree |
| IT-g2-249 | the dobro/triplo convention (EXPOSURE.md) | agree |
| IT-g2-284 | the dobro/triplo convention (EXPOSURE.md) | agree |
| IT-g2-292 | named in EXPOSURE.md | disagree (F) |

## Findings that are not disagreements

- **Art. 123 does not check who the agent is** (found converting IT-g2-102, which agrees). `os elementos do infanticídio estão reunidos` reads the circumstances `a vítima é o próprio filho da agente` and `sob a influência do estado puerperal`, but nothing checks that the agent is a woman or gave birth. A father for whom a fact-finder entered the puerperal circumstance would be convicted of infanticídio rather than homicídio. The case agrees only because its facts give the father no such circumstance.
- **Many agreements are input-determined.** Where the Code's own threshold is carried by an input phrase ("por mais de trinta dias", "logo em seguida", "de modo intencional e repetitivo", "mal injusto e grave", "durante a noite", "na presença de várias pessoas"), the encoding never sees the threshold, and the case that tests one side of it agrees by construction. Three such cases could not be expressed at all (IT-g2-006, IT-g2-242, IT-g2-335). Where the encoding does compute a threshold from a number or a date — days of private imprisonment (art. 148 § 1º III, > 15), participants (arts. 137, 146 § 1º, 147-A § 1º III), every age — both sides were tested and agree, apart from the F-g0-06 birthday.
- **The alínea a / alínea b distinction of art. 121 § 2º VII** (a police officer's relatives by blood only, a judge's by affinity too) lives in two input constructors whose names carry the Code's words (`cp-g2a-comum`); IT-g2-015, 016 and 017 agree, but through the input vocabulary rather than a computed test of the degree or kind of kinship.
- **Art. 147-A § 1º II** (IT-g2-292, exposed) is inert from 10.10.2024 under F-sweep-b-24: stalking a former partner in a context of domestic violence gets no increase. The case read the dangling reference as pointing to art. 121-A § 1º. Both readings are in the register and the sweep (M-sweep-b-46); the choice is a policy one for the conductor, not a defect.
- **Arguable cases that agree** — the encoding took the case's reading: IT-g2-044 ("maior de 60" at 60 years and 5 months), IT-g2-052 (privilege with an objective qualifier), IT-g2-084 (art. 122 is formal), IT-g2-090 ("menor" is under 18, F-g2a-20), IT-g2-111 (14 years and 4 months "é maior de quatorze"), IT-g2-194 (calling the authority does not discharge the duty to help, F-g2a-27), IT-g2-362 (§ 1º's representation reaches § 1º-A), IT-g2-344 (art. 151 caput pena, with the postal question left to F-sweep-b-06).
- **F-g2b-06's register entry says more than the code does.** Its `taken.reading` is `incondicionadaPeloArt100`, while its rationale and `cp-g2b-honra.l4:980–985` refuse for the slight injury, the one case where the two readings differ (IT-g2-263). A reader of the register alone would expect an answer where the encoding gives a refusal.

## Files

- `cp-ind-g2-homicidio.l4` — arts. 121, 121-A, 121-B (IT-g2-001–081)
- `cp-ind-g2-suicidio.l4` — art. 122 (IT-g2-082–097)
- `cp-ind-g2-aborto.l4` — arts. 123–128 (IT-g2-098–123)
- `cp-ind-g2-lesao-corporal.l4` — art. 129 (IT-g2-124–162)
- `cp-ind-g2-periclitacao.l4` — arts. 130–136 (IT-g2-163–208)
- `cp-ind-g2-rixa.l4` — art. 137 (IT-g2-209–213)
- `cp-ind-g2-honra.l4` — arts. 138–145 (IT-g2-214–267)
- `cp-ind-g2-constrangimento-ameaca.l4` — arts. 146–147-C (IT-g2-268–300)
- `cp-ind-g2-sequestro-escravidao.l4` — arts. 148–149-A (IT-g2-301–330)
- `cp-ind-g2-domicilio.l4` — art. 150 (IT-g2-331–342)
- `cp-ind-g2-correspondencia.l4` — arts. 151–152 (IT-g2-343–355)
- `cp-ind-g2-segredos.l4` — arts. 153–154-B (IT-g2-356–383)

Per-case results (verdict, class, evidence) for every one of the 383 cases: `/Users/mengwong/.claude/br-penal-oracle/results/ta-g2/*.json`, one file per slice.
