# Independent test pass — ta-g3, arts. 155 to 212

**Status (2026-09-30):** phase 2 is done.
All 401 cases of `~/.claude/br-penal-oracle/cases/ta-g3.json` were converted.
391 became one directive each, and 10 could not be expressed.
**No finding is of class (E): the encoding departs from the text nowhere in this range.**
There are 7 disagreements, 3 of class (S) and 4 of class (F).
None is of class (T), where my case misread the text, and none of class (R), a conductor's ruling.

The cases were written on 2026-09-29 from the source text alone, before the encoding existed.
Their expected values were not changed in phase 2.

## Files

| module | cases | directives | satisfied | failed | refused | not expressible |
| --- | --- | --- | --- | --- | --- | --- |
| `cp-ind-g3-furto.l4` (arts. 155–156) | 65 | 61 | 58 | 3 | 0 | 4 |
| `cp-ind-g3-roubo.l4` (art. 157) | 30 | 30 | 30 | 0 | 0 | 0 |
| `cp-ind-g3-extorsao.l4` (arts. 158–160) | 35 | 35 | 34 | 1 | 0 | 0 |
| `cp-ind-g3-usurpacao.l4` (arts. 161–162) | 15 | 15 | 15 | 0 | 0 | 0 |
| `cp-ind-g3-dano.l4` (arts. 163–167) | 27 | 27 | 27 | 0 | 0 | 0 |
| `cp-ind-g3-apropriacao-indebita.l4` (arts. 168–170) | 30 | 28 | 28 | 0 | 0 | 2 |
| `cp-ind-g3-estelionato.l4` (art. 171) | 28 | 28 | 26 | 2 | 0 | 0 |
| `cp-ind-g3-outras-fraudes.l4` (arts. 171-A–179) | 49 | 48 | 48 | 0 | 0 | 1 |
| `cp-ind-g3-receptacao.l4` (arts. 180–180-A) | 24 | 24 | 24 | 0 | 0 | 0 |
| `cp-ind-g3-disposicoes-gerais.l4` (arts. 181–183-A) | 19 | 19 | 18 | 0 | 1 | 0 |
| `cp-ind-g3-propriedade-imaterial.l4` (arts. 184, 186) | 17 | 16 | 16 | 0 | 0 | 1 |
| `cp-ind-g3-organizacao-do-trabalho.l4` (arts. 197–207) | 43 | 43 | 43 | 0 | 0 | 0 |
| `cp-ind-g3-sentimento-religioso-e-mortos.l4` (arts. 208–212) | 19 | 17 | 17 | 0 | 0 | 2 |
| **total** | **401** | **391** | **384** | **6** | **1** | **10** |

`cp-ind-g3-comum.l4` holds no directive.
It has the date every case is set on, 28.9.2026, which falls after Lei nº 15.517/2026 (DOU 23.9.2026), the last amending law in the range.
It also has `a pena confere com`, which compares a `Pena cominada` on species, minimum, maximum and multa only.
No vigência gate fired, so no (R) or vigência (S) outcome could arise.

Each case's directive sits directly below a line `-- IT-g3-NNN: <the case's question>`.
Comments in the fact sections that name a case read `-- fatos de IT-g3-NNN: …`, so each `-- IT-g3-NNN:` line appears exactly once across the files (checked: 401 anchors, 401 distinct ids).
The per-module counts above are from `check.sh` runs made while the files were written.
A combined run is recorded under **Verification** below.

## Disagreements

| id | articles | my expectation | the encoding's answer | class | evidence |
| --- | --- | --- | --- | --- | --- |
| IT-g3-009 | 155 § 1º with § 4º I | TRUE: the night-rest increase also applies to furto qualificado (arguable; alternative named Tema 1087) | FALSE | S | STJ Tema 1087, M-sweep-b-28, fork F-sweep-b-19 (settled): `incide o aumento do art. 155, § 1º` requires no qualified form (`cp-g3-furto.l4`, the `null (as formas qualificadas presentes f)` limb) |
| IT-g3-017 | 155 § 2º with § 4º II (abuso de confiança) | TRUE: the privilege is available (arguable; alternative named Súmula 511) | FALSE | S | Súmula 511 STJ, M-sweep-b-27, fork F-sweep-b-18 (settled); fork F-g0-25 classes abuso de confiança as subjective (`a forma admite o privilégio`) |
| IT-g3-034 | 155 § 4º-C II | REFUSE: the Code does not define "idoso" (arguable; alternative the Estatuto's 60) | TRUE for a victim of 62 | F | F-g0-08, reading `sessentaOuMais`, unsettled: `cp-pena.l4` `idoso` is 60 completed years or more, read off art. 183 III |
| IT-g3-102 | 158 § 4º | TRUE: the triple applies to a member of any organização criminosa, as the text says (arguable) | FALSE: only an ultraviolent organisation, paramilitary group or militia | F | F-sweep-b-22, reading `lidoComoOsDemais`, unsettled (`incide o aumento do art. 158, § 4º`, `cp-g3-extorsao.l4`). My reading is the fork's `literalQualquerOrganizacaoCriminosa`. M-sweep-b-43 finds the missing "ultraviolenta" in Lei 15.358's own text, not in the compilation |
| IT-g3-214 | 171 § 2º VI | FALSE: in the Code's text, paying before the denúncia does not bar the action (arguable; alternative named Súmula 554) | TRUE | S | Súmula 554 STF read a contrario, M-sweep-b-22, fork F-sweep-b-13 (`o pagamento do cheque obsta a ação penal (art. 171, § 2º, VI; Súmula 554 STF)`, `cp-g3-estelionato.l4`) |
| IT-g3-223 | 171 § 4º | REFUSE: "idoso" is undefined in the Code (arguable) | TRUE for a victim of 65 | F | F-g0-08 as for IT-g3-034; `incide o aumento do art. 171, § 4º` reads `idoso ou vulnerável (art. 155, § 4º-C, II)` |
| IT-g3-310 | 182 I, 181 I, 100 | ação penal pública incondicionada: a divorced ex-spouse is in neither art. 181 nor art. 182 (arguable) | REFUSE: "se o art. 182, I, alcança … o divorciado não está decidido nesta codificação (fork F-sweep-b-23)" | F | F-sweep-b-23 is open, and the encoding declines (`cp-g3-disposicoes-gerais.l4`, `o alcance do art. 182, I, depois do Tema 1053`). The summary of sweep entry M-sweep-b-45 (STF Tema 1053) itself says the divorced spouse is named by neither article, which is my answer |

Two of these call for a decision:

- **IT-g3-310.** The encoding refuses even though the evidence its own sweep gathered answers the question. Settling F-sweep-b-23 on the text ("desquitado ou judicialmente separado" does not name the divorced) turns the refusal into an answer.
- **IT-g3-102.** The encoding narrows a harsher provision to match its siblings. The narrowing favours the defendant, and M-sweep-b-43 shows the gap was enacted, not introduced in the compilation. The fork is open and needs a ruling.

The (S) rows need no change: in each, my case recorded the text's answer and named the ruling that the encoding followed.

## Not expressible

In 8 of the 10, the encoding agrees with my case in substance: it leaves the question to the judge, or to whoever supplies the facts, and has no rule to assert against.

| id | articles | expected | why no directive |
| --- | --- | --- | --- |
| IT-g3-008 | 155 § 1º | REFUSE ("repouso noturno" at 22h30) | `durante o repouso noturno` is an input circumstance, read per STJ Tema 1144; no rule decides it from the hour |
| IT-g3-012 | 155 § 2º | REFUSE (which of the three options) | `as opções do juiz pelo art. 155, § 2º` returns all three and none is chosen (PLAN § 2.4) |
| IT-g3-014 | 155 § 2º | REFUSE ("pequeno valor" at R$ 900) | `pequeno valor da coisa, reconhecido pelo juiz` is an input finding (F-g0-14) |
| IT-g3-015 | 155 § 2º | FALSE (the text does not oblige the judge) | whether "pode" is a faculdade or a direito subjetivo is fork F-g0-27, left open in a comment; no rule answers it |
| IT-g3-186 | 168-A § 3º I | REFUSE (must the judge drop the penalty) | the § 3º options are returned and none is chosen |
| IT-g3-202 | 169 p.ú. I | FALSE (treasure on the finder's own land) | cannot be stated: how the thing came to the agent is one required value whose only treasure member is `tesouro achado em prédio alheio`, so the missing element has no way to be recorded |
| IT-g3-241 | 176 p.ú. | REFUSE (must the judge waive the penalty) | the power is returned as an option; nothing decides its exercise |
| IT-g3-329 | 184 § 4º, caput | REFUSE (does a private whole copy violate the caput) | the violation under Lei 9.610 is an input finding (F-g3b-01, F-g3b-03) |
| IT-g3-393 | 212 | FALSE (ashes scattered respectfully) | the act is recorded by its verb (`Conduta contra o respeito aos mortos`), and there is no verb for a respectful act |
| IT-g3-398 | 210 | FALSE (authorised restoration of a tomb) | as IT-g3-393 |

IT-g3-202, IT-g3-393 and IT-g3-398 are true gaps.
In each, the record has no way to state the fact my case describes.
The rule is not wrong on the facts it can receive.

## Exposure (EXPOSURE.md)

These cases, or the conventions they rest on, were visible to the encoders in the conductor's log, as `~/.claude/br-penal-oracle/EXPOSURE.md` records.
They are marked **EXPOSED**: every one agrees with the encoding, and that agreement is not evidence.

| id | what was exposed | outcome |
| --- | --- | --- |
| IT-g3-004 | furto 1–6 | satisfied, EXPOSED |
| IT-g3-006 | repouso noturno "de metade" | satisfied, EXPOSED |
| IT-g3-069 | roubo 6–10 | satisfied, EXPOSED |
| IT-g3-086 | latrocínio 24–30 | satisfied, EXPOSED |
| IT-g3-088 | 157 § 4º as reclusão 18–30 (the worked example of the doubling notation) | satisfied, EXPOSED |
| IT-g3-112 | "maior de N" as N years lived (convention) | satisfied, EXPOSED |
| IT-g3-224 | estelionato's ação penal is pública incondicionada | satisfied, EXPOSED |
| IT-g3-281 | receptação 2–6 | satisfied, EXPOSED |
| IT-g3-287 | art. 180 § 3º's multa "alternativa ou cumulativa" (also PLAN § 2.2.1) | satisfied, EXPOSED |
| IT-g3-291, IT-g3-292 | art. 180 § 5º revoked | satisfied, EXPOSED |

Correction to my phase-1 reply: it cited IT-g3-269 for receptação 2–6.
That number came from a listing made before the cases were renumbered.
The case is IT-g3-281; IT-g3-269 is art. 178.

The encoders also had PLAN § 2.2.1, shape 6a: art. 159 has no multa.
So agreement on IT-g3-106, 107, 115 and 116 was reachable legitimately.

## Where agreement proves less than it looks

- **Elements folded into a single option.** Several conducts are recorded as one checkbox or enum member that already contains the element my case removes.
  - The cases: 161 § 1º I, where "águas alheias" is part of the conduct (IT-g3-144); the negatives for 171 § 2º (IT-g3-209, 216, 271–275); and 177 §§ 1º III and 2º (IT-g3-245, 267).
  - For these, the negative case can only show that a conduct left unrecorded gives FALSE. The rule never reads the missing element separately.
- **The deciding point is an input flag.** Several arguable cases agree only because of this: "logo depois" (IT-g3-071), the necessary restriction (IT-g3-100), "facilitando a libertação" (IT-g3-119), "indevida" (IT-g3-093, 094), "prejuízo considerável" (IT-g3-156).
  - My facts set the flag, so these confirm the wiring, not a reading.
- **Arguable cases where the encoding took my reading under its own fork:**

  | case | fork |
  | --- | --- |
  | IT-g3-087 | F-g3-06 |
  | IT-g3-113 | F-g3-14 |
  | IT-g3-135 | F-g3-16 |
  | IT-g3-192 | F-g3-21 |
  | IT-g3-401 | F-g3b-21 |

  IT-g3-112 (F-g0-06) belongs here too, but it is EXPOSED.
- **Art. 201 (IT-g3-371) agrees because it is encoded as written.** Its reception under the right to strike is fork F-g3b-10, still open.
- **Art. 175 § 2º.** On a caput conviction, which is detenção, the encoding offers two of art. 155 § 2º's three options: it leaves out replacing reclusão with detenção. IT-g3-237 asks only whether the privilege applies, so it passes. Leaving out an option that cannot apply to detenção looks right, but it is a reading.

## Verification

- **Planted wrong expectations.** These were run in scratch copies, each expected to produce exactly as many failures as were planted:
  - usurpação: 2 planted, 2 failed;
  - receptação and disposições gerais: 7 planted, 7 failed;
  - propriedade imaterial: 3 planted, 3 failed.
- **Slices with no planted control:** furto, roubo, extorsão, dano, apropriação, estelionato, outras fraudes, trabalho and mortos.
  - Their comparisons are exact equalities: pena records, cause lists, ação penal members.
  - Their negatives pair with positives built from the same fact builders. For example, IT-g3-247 (a liquidante distributes fictitious dividends: not art. 177 § 1º) and IT-g3-277 (a director does the same: made out, satisfied) differ only in the role.
- **Combined run.** `L4=/Users/mengwong/.claude/br-penal-toolchain/l4 ./check.sh . cp-ind-g3-` over all fourteen files, after the fact-section comments were relabelled (a change to comments only): _pending when this file was written; see below._

Re-run with `L4=/Users/mengwong/.claude/br-penal-toolchain/l4 ENC/check.sh ENC cp-ind-g3-`.
On 2026-09-30 the load average was between 100 and 430, from other sessions' mutation runs, and one module took 20 to 80 minutes.
